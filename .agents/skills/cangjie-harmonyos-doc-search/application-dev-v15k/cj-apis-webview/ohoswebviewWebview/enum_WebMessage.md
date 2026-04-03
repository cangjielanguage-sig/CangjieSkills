## enum WebMessage

```cangjie
public enum WebMessage <: Equatable<WebMessage> & ToString {
    | STRING(String)
    | ARRAY_BUFFER(Array<UInt8>)
    | ...
}
```

**功能：** 用于描述[WebMessagePort](#class-webmessageport)所支持的数据类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<WebMessage>
- ToString

### ARRAY_BUFFER(Array\<UInt8>)

```cangjie
ARRAY_BUFFER(Array<UInt8>)
```

**功能：** 二进制类型数据。

**起始版本：** 19

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 字符串类型数据。

**起始版本：** 19

### func !=(WebMessage)

```cangjie
public operator func !=(other: WebMessage): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebMessage](#enum-webmessage)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true，否则返回false。|

### func ==(WebMessage)

```cangjie
public operator func ==(other: WebMessage): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebMessage](#enum-webmessage)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串表示。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串表示。|