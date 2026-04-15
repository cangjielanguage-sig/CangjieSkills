## class JSExternal

```cangjie
public class JSExternal <: JSHeapObject {}
```

**功能：** 一个可传递到ArkTS侧的仓颉对象引用。可以获取绑定的仓颉对象。

JSExternal的目标是传递一个仓颉对象的强引用到ArkTS运行时，配合其他用户自定义的互操作接口可以访问这个仓颉对象。

**起始版本：** 22

**父类型：**

- [JSHeapObject](#class-jsheapobject)

### func cast\<T>() where T <: SharedObject

```cangjie
public func cast<T>(): Option<T> where T <: SharedObject
```

**功能：** 获取绑定的 SharedObject 对象并转换为 T 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Option\<T>|绑定的仓颉对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
class Data <: SharedObject {
    func doSth() {}
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let external = callInfo[0].asExternal()

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[SharedObject](#class-sharedobject)|绑定的仓颉对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
class Data <: SharedObject {
    func doSth() {}
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let external = callInfo[0].asExternal()

    let sharedObject = external.getData()
    if (let Some(data) <- (sharedObject as Data)) {
         data.doSth()
     }

    context.undefined().toJSValue()
}
```