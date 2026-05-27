### func bindObject(JSValue)

```cangjie
public func bindObject(external: JSValue): Unit
```

**功能：** 往 ArkTS 对象绑定一个仓颉对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|external|[JSValue](#struct-jsvalue)|是|-|仓颉对象的 ArkTS 引用。|

**示例：**

```cangjie
class Data <: SharedObject {}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = callInfo[0]
    let data = Data()
    let external = context.external(data)
    jsObJ.bindObject(external.toJSValue())
    return jsObJ
}
```

>

### func bindObject(JSContext, JSValue) <sub>(deprecated)</sub>

```cangjie
public func bindObject(_: JSContext, external: JSValue): Unit
```

**功能：** 往 ArkTS 对象绑定一个仓颉对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|external|[JSValue](#struct-jsvalue)|是|-|仓颉对象的 ArkTS 引用。|

### func bindObject(SharedObject)

```cangjie
public func bindObject(data: SharedObject): Unit
```

**功能：** 往 ArkTS 对象绑定一个仓颉对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[SharedObject](#class-sharedobject)|是|-|仓颉对象。|

**示例：**

```cangjie
class Data <: SharedObject {}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = callInfo[0]
    let data = Data()
    jsObJ.bindObject(data)
    return jsObJ
}
```

>

### func bindObject(JSContext, SharedObject) <sub>(deprecated)</sub>

```cangjie
public func bindObject(_: JSContext, data: SharedObject): Unit
```

**功能：** 往 ArkTS 对象绑定一个仓颉对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|data|[SharedObject](#class-sharedobject)|是|-|仓颉对象。|

### func getBindingObject()

```cangjie
public func getBindingObject(): ?SharedObject
```

**功能：** 获取 ArkTS 对象绑定的仓颉对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|?[SharedObject](#class-sharedobject)|绑定的仓颉对象。|

**示例：**

```cangjie
class Data <: SharedObject {
    func doSth() {}
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = callInfo[0]
    if (let Some(shareData) <- jsObJ.getBindingObject()) {
        if (let Some(data) <- shareData as Data) {
            data.doSth()
        }
    }
    return jsObJ
}
```

### func getBindingObject(JSContext) <sub>(deprecated)</sub>

```cangjie
public func getBindingObject(_: JSContext): ?SharedObject
```

**功能：** 获取 ArkTS 对象绑定的仓颉对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|?[SharedObject](#class-sharedobject)|绑定的仓颉对象。|