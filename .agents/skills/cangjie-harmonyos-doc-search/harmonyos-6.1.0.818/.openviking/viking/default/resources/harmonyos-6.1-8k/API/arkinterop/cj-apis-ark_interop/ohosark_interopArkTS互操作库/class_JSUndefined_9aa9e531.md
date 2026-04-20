## class JSUndefined

```cangjie
public class JSUndefined {}
```

**功能：** ArkTS null。

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

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let undefined = context.undefined()
    let jsValue = undefined.toJSValue()
    return jsValue
}
```