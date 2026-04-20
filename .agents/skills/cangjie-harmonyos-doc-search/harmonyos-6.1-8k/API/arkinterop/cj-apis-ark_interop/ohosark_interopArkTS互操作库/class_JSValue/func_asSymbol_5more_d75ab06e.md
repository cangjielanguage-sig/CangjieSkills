### func asSymbol()

```cangjie
public func asSymbol(): JSSymbol
```

**功能：** 把一个 JSValue 转换为 JSSymbol。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSSymbol](#class-jssymbol)|一个 ArkTS symbol的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asUndefined()

```cangjie
public func asUndefined(): JSUndefined
```

**功能：** 把一个 JSValue 转换为 JSUndefined。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSUndefined](#class-jsundefined)|一个ArkTS undefined。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func bindObject(JSValue)

```cangjie
public func bindObject(external: JSValue): Unit
```

**功能：** 往 ArkTS 对象绑定一个仓颉对象。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|external|[JSValue](#class-jsvalue)|是|-|仓颉对象的 ArkTS 引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
class Data <: SharedObject {
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = callInfo[0]
    let data = Data()
    let external = context.external(data)
    jsObJ.bindObject(external.toJSValue())
    return jsObJ
}
```

>

### func bindObject(SharedObject)

```cangjie
public func bindObject(data: SharedObject): Unit
```

**功能：** 往 ArkTS 对象绑定一个仓颉对象。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[SharedObject](#class-sharedobject)|是|-|仓颉对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
class Data <: SharedObject {
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = callInfo[0]
    let data = Data()
    jsObJ.bindObject(data)
    return jsObJ
}
```

>

### func getBindingObject()

```cangjie
public func getBindingObject(): ?SharedObject
```

**功能：** 获取 ArkTS 对象绑定的仓颉对象。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|?[SharedObject](#class-sharedobject)|绑定的仓颉对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
class Data <: SharedObject {
    func doSth() {}
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = callInfo[0]
    if (let Some(shareData) <- jsObJ.getBindingObject()) {
        if (let Some(data) <- (shareData as Data)) {
            data.doSth()
        }
    }
    return jsObJ
}
```