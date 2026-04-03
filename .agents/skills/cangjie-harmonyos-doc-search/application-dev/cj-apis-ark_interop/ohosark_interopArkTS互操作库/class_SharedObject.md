## class SharedObject

```cangjie
public open class SharedObject {
    public init()
}
```

**功能：** 可以被 ArkTS 引用的仓颉对象的基类。

**起始版本：** 22

**示例：**

<!--compile-->
```cangjie
// 创建一个类继承 SharedObject
class MyObject <: SharedObject {
    let name: String = "MyObject"
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 实例化一个 MyObject 对象
    let data = MyObject()
    // 从 data 创建一个 JSExternal 对象
    let external = context.external(data)
    // 创建一个 JSObject 对象
    let object = context.object()
    // 绑定 external 到 object
    object.attachCJObject(external)
    // 创建一个对外可见函数，在这个函数中，通过object访问对象属性
    object["name"] = context.function { context, callInfo =>
        // 获取 this 对象
        let object = callInfo.thisArg.asObject()
        // 从 object 中获取绑定的 MyObject 实例
        let external = object.getAttachInfo().getOrThrow()
        // 把 data.name 转换为 JSString
        let name = context.string(external.cast<MyObject>().getOrThrow().name)
        return name.toJSValue()
    }.toJSValue()
    return object.toJSValue()
}
```

### prop nativeId

```cangjie
public prop nativeId: Int64
```

**功能：** 对象唯一标识。

**起始版本：** 22

**类型：** Int64

**读写能力：** 只读

### init()

```cangjie
public init()
```

**功能：** 创建一个 SharedObject 对象。

**起始版本：** 22