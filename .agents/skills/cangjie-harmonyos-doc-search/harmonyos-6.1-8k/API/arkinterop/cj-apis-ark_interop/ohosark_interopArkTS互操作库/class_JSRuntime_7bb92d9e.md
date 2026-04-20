## class JSRuntime

```cangjie
public class JSRuntime {
    public init()
}
```

**功能：** 仓颉创建的 ArkTS 运行时。

**起始版本：** 22

> **注意：**
>
> 仓颉应用中只能在主线程上使用 JSRuntime() 创建 ArkTS 运行时。

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getJSRuntimeInstance(): Unit {
    // 创建 JSRuntime 实例
    let runtime = JSRuntime()
    // 获取 JSContext 实例
    let context = runtime.mainContext

    Hilog.info(0, "test", "Got JSRuntime instance")

    let jsValue = context.string("JSRuntime instance obtained").toJSValue()
}
```

### prop mainContext

```cangjie
public prop mainContext: JSContext
```

**功能：** 互操作上下文。

**起始版本：** 22

**类型：** [JSContext](#class-jscontext)

**读写能力：** 只读

### init()

```cangjie
public init()
```

**功能：** 构造函数。

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |

### func getNapiEnv()

```cangjie
public func getNapiEnv(): CPointer<Unit>
```

**功能：** 获取环境指针。

**返回值：**

| 类型       | 说明          |
|:---------|:------------|
| CPointer\<Unit> | napi接口的env。 |

**起始版本：** 22