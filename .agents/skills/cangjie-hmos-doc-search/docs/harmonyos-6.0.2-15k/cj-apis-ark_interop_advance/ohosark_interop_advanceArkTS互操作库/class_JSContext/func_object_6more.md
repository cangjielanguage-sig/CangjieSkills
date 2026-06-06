### func object()

```cangjie
public func object(): JSObject
```

**功能：** 创建一个空的 ArkTS object 引用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSObject](#class-jsobject)|ArkTS object 引用。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.object()
    return result.toJSValue()
}
```

### func postJSTask(() -> Unit)

```cangjie
public func postJSTask(callback: ()->Unit): Unit
```

**功能：** 多线程工具：创建在 ArkTS 线程执行的任务。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|在 ArkTS 执行的任务|

**示例：**

```cangjie
func createObject(context: JSContext, callback: (JSObject) -> Unit): Unit {
    if (context.isInBindThread()) {
        callback(context.object())
    } else {
        context.postJSTask {
            callback(context.object())
        }
    }
}
```

### func promiseCapability()

```cangjie
public func promiseCapability(): JSPromiseCapability
```

**功能：** 创建一个 ArkTS Promise。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSPromiseCapability](#class-jspromisecapability)|ArkTS promise 的 native 引用。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.promiseCapability()
    return result.toJSValue()
}
```

### func requireAppNativeModule(String, String) <sub>(deprecated)</sub>

```cangjie
public func requireAppNativeModule(moduleName: String, modulePath: String): JSValue
```

**功能：** 加载ArkTS原生app的指定模块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**废弃版本：** 16

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|要求加载的模块名。|
|modulePath|String|是|-|模块加载路径。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|模块返回值，一般是一个对象，如果加载出错将会返回 undefined。|

### func requireJSModule(String) <sub>(deprecated)</sub>

```cangjie
public func requireJSModule(moduleName: String): JSValue
```

**功能：** 加载指定的ArkTS模块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**废弃版本：** 16

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|要求加载的模块名。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|模块返回值，一般是一个对象，如果加载出错将会返回 undefined。|

### func requireSystemNativeModule(String, ?String)

```cangjie
public func requireSystemNativeModule(moduleName: String, prefix!: ?String = None): JSValue
```

**功能：** 加载系统内置的 ArkTS napi 模块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|ArkTS napi 模块的注册名称|
|prefix|?String|否|None| **命名参数。** ArkTS napi 模块的归档目录，在 /system/lib64/module 下可省，在子目录下是子目录名称|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|模块返回值，一般是一个对象，如果加载出错将会返回 undefined|

**示例：**

```cangjie
func doSth(context: JSContext): Unit {
    let hilog = context.requireSystemNativeModule("hilog")
    let pushService = context.requireSystemNativeModule("core.push.pushService", prefix: "hms")
}
```