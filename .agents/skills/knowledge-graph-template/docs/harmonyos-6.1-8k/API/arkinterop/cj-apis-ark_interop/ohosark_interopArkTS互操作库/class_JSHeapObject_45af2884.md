## class JSHeapObject

```cangjie
abstract sealed class JSHeapObject {}
```

**功能：** 一个 ArkTS 运行时对象的强引用（但不会超过 ArkTS 运行时的生命周期，也不会阻止 ArkTS 运行时的销毁）。可以转换为JSValue。

它是所有安全引用的基类，用户不能创建它只能创建它的子类（隐藏构造函数），它的目标是让引用的 ArkTS 运行时对象持续时间超过这个仓颉对象本身。

**起始版本：** 22

### func toJSValue()

```cangjie
public func toJSValue(): JSValue
```

**功能：** 转换为 JSValue。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let number = context.number(123)
    let jsValue = number.toJSValue()
    return jsValue
}
```