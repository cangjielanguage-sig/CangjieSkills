// 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
import { readName, testAsync } from "libohos_app_cangjie_entry.so";

import {Some} from "../workerTest";

// 获取 worker 线程环境
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
// 监听主线程消息
workerPort.onmessage = (evt) => {
  let some = evt.data as Some;
  if (some.type == "begin") {
    beginTask(some);
  }
}

async function beginTask(some: Some) {
  // 在 worker 线程修改对象属性
  await some.setName("modified");
  some.type = "modify";
  hilog.info(0, "worker", `worker name: ${await readName(some)}`);
  // 调用仓颉函数
  testAsync().then(data => {
    hilog.info(0, "worker", `resolved: ${data}`);
    workerPort.postMessage({"type": "result", value: data});
  }).catch((err: Error) => {
    hilog.error(0, "worker", `caught error: ${err.message}`);
    workerPort.postMessage({"type": "result", value: false});
  });
}
```

在 ArkTS 侧启动 Worker：

```typescript
// 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
import { startTestWorker } from "../workerTest"

// 启动 Worker
startTestWorker();
```