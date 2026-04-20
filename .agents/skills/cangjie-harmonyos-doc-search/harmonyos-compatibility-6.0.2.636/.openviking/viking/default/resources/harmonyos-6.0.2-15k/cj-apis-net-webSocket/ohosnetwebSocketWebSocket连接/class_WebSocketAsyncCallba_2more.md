## class WebSocketAsyncCallback

```cangjie
open public class WebSocketAsyncCallback<T> <: Callback2Argument<Option<AsyncError>,Option<T>> {
    public WebSocketAsyncCallback(let f:(Option <AsyncError>, Option <T> ) -> Unit)
}
```

**功能：** 打开事件的callback类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**父类型：**

- [Callback2Argument\<Option\<AsyncError>, Option\<T>>](../BasicServicesKit/cj-apis-base.md#class-callback2argument)

### WebSocketAsyncCallback((Option\<AsyncError>, Option\<T>) -> Unit)

```cangjie
public WebSocketAsyncCallback(let f:(Option <AsyncError>, Option <T> ) -> Unit)
```

**功能：** 构造一个WebSocketAsyncCallback对象。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|f|(Option\<[AsyncError](../BasicServicesKit/cj-apis-base.md#class-asyncerror)>, Option\<T>) -> Unit|是|-|回调方法。|

### func invoke(Option\<AsyncError>, Option\<T>)

```cangjie
public open func invoke(arg1: Option <AsyncError>, arg2: Option <T>)
```

**功能：** 执行入参回调方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|Option\<[AsyncError](../BasicServicesKit/cj-apis-base.md#class-asyncerror)>|是|-|回调失败，AsyncError返回值。|
|arg2|Option\<T>|是|-|回调成功，返回T类型。|

## class WebSocketClientCert

```cangjie
public class WebSocketClientCert {
    public WebSocketClientCert(
        public let certPath : String,
        public let keyPath : String,
        public let keyPassword !: ?String = None
    )
}
```

**功能：** 客户端证书类型。

**起始版本：** 19

### let certPath

```cangjie
public let certPath: String
```

**功能：** 证书路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let keyPassword

```cangjie
public let keyPassword: ?String = None
```

**功能：** 证书秘钥的密码。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let keyPath

```cangjie
public let keyPath: String
```

**功能：** 证书秘钥的路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### WebSocketClientCert(String, String, ?String)

```cangjie
public WebSocketClientCert(
    public let certPath : String,
    public let keyPath : String,
    public let keyPassword !: ?String = None
)
```

**功能：** WebSocketClientCert构造函数。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|certPath|String|是|-|证书路径。|
|keyPath|String|是|-|证书秘钥的路径。|
|keyPassword|?String|否|None| **命名参数。** 证书秘钥的密码。|