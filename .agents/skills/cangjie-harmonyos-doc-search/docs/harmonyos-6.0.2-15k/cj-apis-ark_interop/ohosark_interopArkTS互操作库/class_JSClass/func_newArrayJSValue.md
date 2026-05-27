### func new(Array\<JSValue>)

```cangjie
public func new(args: Array<JSValue>): JSValue
```

**功能：** 通过 ArkTS 类实例化一个新对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|args|Array\<[JSValue](#struct-jsvalue)>|是|-|new 的参数列表。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|实例化出来的新对象。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = {
        context, callInfo =>
        let id = callInfo[0]
        let name = callInfo[1]
        let thisArg = callInfo.thisArg
        thisArg.setProperty(context, "id", id)
        thisArg.setProperty(context, "name", name)
        return thisArg
    }
    let clazz = context.clazz(ctor)
    let id = context.number(1.0)
    let name = context.string("aaa")
    let obj = clazz.new([id.toJSValue(), name.toJSValue()])
    return obj
}
```