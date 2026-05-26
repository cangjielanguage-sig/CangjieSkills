## interface ToJSValue

```cangjie
interface ToJSValue {
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** 可用于实现ToJSValue的接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 19

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉类型数据转换为JSValue。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|