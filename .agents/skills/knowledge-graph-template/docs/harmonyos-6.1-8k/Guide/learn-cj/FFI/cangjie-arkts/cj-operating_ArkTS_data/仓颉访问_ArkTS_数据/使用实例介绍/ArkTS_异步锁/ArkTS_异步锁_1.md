### ArkTS 异步锁

为了解决多并发实例间的数据竞争问题， ArkTS 语言基础库引入了异步锁能力。为了开发者的开发效率， AsyncLock 对象支持跨并发实例引用传递，具体可参考[异步锁](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/arkts-utils/arkts-async-lock-introduction.md)。本节重点介绍异步锁结合 sendable 对象的场景。

仓颉侧实现：

<!--compile-->
```cangjie
// 定义包名，该包名需要和 cjpm.toml 的 package name 保持一致
package ohos_app_cangjie_entry

internal import ohos.ark_interop.JSModule
internal import ohos.ark_interop.JSContext
internal import ohos.ark_interop.JSCallInfo
internal import ohos.ark_interop.JSValue

func testAsync(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 创建 PromiseCapability
    let promise = context.promiseCapability()
    spawn {
        // 使用新线程来执行运算密集的任务
        // 回到 ArkTS 线程
        context.postJSTask {
            // 向 ArkTS 返回结果
            promise.resolve(context.string("abcdedf").toJSValue())
        }
    }
    // 返回 Promise
    promise.toJSValue()
}

func readName(context: JSContext, callInfo: JSCallInfo): JSValue {
    let some = callInfo[0].asObject()
    some["lock"].asObject().callMethod("lockAsync", context.function { context, callInfo =>
        return some["name"]
    }.toJSValue())
}

let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports =>
        exports["testAsync"] = runtime.function(testAsync).toJSValue()
        exports["readName"] = runtime.function(readName).toJSValue()
}
```

在 Index.d.ts 文件中，提供互操作的接口声明：

```typescript
// libohos_app_cangjie_entry.so对应的Index.d.ts
export declare function testAsync(): Promise<boolean>;
export declare function readName(data: Some): Promise<string>;

interface Some {}
```

在 entry->src->main->ets 中创建一个文件 workerTest.ets，主线程代码如下：

```typescript
// workerTest.ets
import hilog from '@ohos.hilog';
import worker, {MessageEvents} from '@ohos.worker';
import {ArkTSUtils} from "@kit.ArkTS";

// 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
import { readName } from "libohos_app_cangjie_entry.so";

// 定义 Sendable 类
@Sendable
export class Some {
  name: string = "safd";
  type: string = "";
  result: boolean = false;
  lock: ArkTSUtils.locks.AsyncLock;

  constructor() {
    this.lock = new ArkTSUtils.locks.AsyncLock();
  }

  getName(): Promise<string> {
    return this.lock.lockAsync(() => {
      return this.name;
    });
  }

  setName(value: string): Promise<void> {
    return this.lock.lockAsync(() => {
      this.name = value;
    });
  }
}
// 程序入口
export async function startTestWorker() {
  hilog.info(0, "test", "worker test begin");
  // 创建 worker
  const thread = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
  // 创建并初始化事件回调表
  const eventHandlers = new Map<string, (msg: MessageEvents) => void>();
  eventHandlers.set("close", (evt) => {
    thread.terminate();
  });
  eventHandlers.set("result", async (evt) => {
    let result = evt.data.value as boolean;
    const name = await a.getName();
    hilog.info(0, "worker", `result is ${result}, name is ${name}`);
  });
  // 监听 worker 消息
  thread.onmessage = (evt) => {
    let type = evt.data.type as string;
    if (eventHandlers.has(type)) {
      eventHandlers.get(type)!(evt);
    } else {
      hilog.error(0, "worker", "unknown message type: %{public}s", type);
    }
  };
  // 创建 Sendable 对象
  let a = new Some();
  // 调用仓颉接口
  hilog.info(0, "test", `name: ${await readName(a)}`);
  // 向 worker 发送消息 "begin"
  a.type = "begin";
  thread.postMessageWithSharedSendable(a);
}
```

在 entry->src->main->ets 中创建一个 workers 文件夹，在 workers 中创建 Workers.ets 文件，代码如下：

```typescript
// Workers.ets
import {ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker} from '@kit.ArkTS';
import hilog from '@ohos.hilog';