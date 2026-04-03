### func defineOwnAccessor(JSKeyable, ?JSLambda, ?JSLambda, Bool, Bool)

```cangjie
public func defineOwnAccessor(key: JSKeyable, getter!:? JSLambda = None, setter!: ?JSLambda = None,
    isEnumerable!: Bool = false,
    isConfigurable!: Bool = false
): Bool
```

**功能：** 为当前对象定义 accessors 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|
|getter|?[JSLambda](#type-jslambda)|否|None| **命名参数。** getter 实现。|
|setter|?[JSLambda](#type-jslambda)|否|None| **命名参数。** setter 实现。|
|isEnumerable|Bool|否|false| **命名参数。** 是否可枚举。|
|isConfigurable|Bool|否|false| **命名参数。** 是否可重新定义。|

**返回值：**

|类型|说明|
|:---|:---|
|Bool|是否成功。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = context.object()
    let getter: JSLambda = {
        context, callInfo => context.number(1.0).toJSValue()
    }
    obj.defineOwnAccessor("a", getter: getter, isConfigurable: false)
    return obj.toJSValue()
}
```

### func defineOwnProperty(JSKeyable, JSValue, Bool, Bool, Bool)

```cangjie
public func defineOwnProperty(key: JSKeyable, setValue: JSValue,
    isWritable!: Bool = true,
    isEnumerable!: Bool = true,
    isConfigurable!: Bool = true
): Bool
```

**功能：** 在当前对象上定义属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|
|setValue|[JSValue](#struct-jsvalue)|是|-|目标值。|
|isWritable|Bool|否|true| **命名参数。** 是否可写。|
|isEnumerable|Bool|否|true| **命名参数。** 是否可枚举。|
|isConfigurable|Bool|否|true| **命名参数。** 是否可重新定义。|

**返回值：**

|类型|说明|
|:---|:---|
|Bool|是否成功。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = context.object()
    obj.defineOwnProperty("a", context.number(1.0).toJSValue(), isWritable: true, isConfigurable: false)
    return obj.toJSValue()
}
```

### func getAttachInfo()

```cangjie
public func getAttachInfo(): ?JSExternal
```

**功能：** 从当前对象上获取绑定的仓颉对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|?[JSExternal](#class-jsexternal)|ArkTS 对仓颉对象的引用或None。|

**示例：**

```cangjie
class Data <: SharedObject {
    func doSth() {}
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = callInfo[0].asObject(context)
    if (let Some(sharedObJ) <- obj.getAttachInfo()) {
        if (let Some(data) <- sharedObJ as Data) {
            data.doSth()
        }
    }
}
```

### func getProperty(JSKeyable)

```cangjie
public func getProperty(key: JSKeyable): JSValue
```

**功能：** 从当前对象获取目标属性值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|获得的值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = callInfo[0].asObject(context)
    let result = obj.getProperty("a")
    return result
}
```