## class JSCurrentJSContext

```cangjie
public class JSCurrentJSContext {}
```

**功能：** 用于保存单次互操作调用的 [JSContext](#class-jscontext)。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

### static func get()

```cangjie
public static func get()
```

**功能：** 获取单次互操作调用的 [JSContext](#class-jscontext)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

### static func set(?JSContext)

```cangjie
public static func set(input: ?JSContext)
```

**功能：** 设置单次互操作调用的 [JSContext](#class-jscontext)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|input|?[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

### static func unset()

```cangjie
public static func unset()
```

**功能：** 取消设置单次互操作调用的 [JSContext](#class-jscontext)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：**  15

## class JSExternal

```cangjie
public class JSExternal <: JSHeapObject {}
```

**功能：** 一个可传递到ArkTS侧的仓颉对象引用。可以获取绑定的仓颉对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

JSExternal的目标是传递一个仓颉对象的强引用到ArkTS运行时，配合其他用户自定义的互操作接口可以访问这个仓颉对象。

**父类型：**

* [JSHeapObject](#class-jsheapobject)

### func cast\<T>() where T <: SharedObject

```cangjie
public func cast<T>(): Option<T> where T <: SharedObject
```

**功能：** 获取绑定的 SharedObject 对象并转换为 T 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Option\<T>|绑定的仓颉对象。|

**示例：**

```cangjie
class Data <: SharedObject {
    func doSth() {}
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let external = callInfo[0].asExternal(context)

    if (let Some(data) <- external.cast<Data>()) {
        data.doSth()
    }

    context.undefined().toJSValue()
}
```

### func getData()

```cangjie
public func getData(): SharedObject
```

**功能：** 获取绑定的 SharedObject 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[SharedObject](#class-sharedobject)|绑定的仓颉对象。|

**示例：**

```cangjie
class Data <: SharedObject {
    func doSth() {}
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let external = callInfo[0].asExternal(context)

    let sharedObject = external.getData()
    if (let Some(data) <- sharedObject as Data) {
        data.doSth()
    }

    context.undefined().toJSValue()
}
```