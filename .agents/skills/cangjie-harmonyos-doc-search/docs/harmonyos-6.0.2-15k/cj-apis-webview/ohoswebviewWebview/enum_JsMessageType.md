## enum JsMessageType

```cangjie
public enum JsMessageType <: Equatable<JsMessageType> & ToString {
    | NOTSUPPORT
    | STRING
    | NUMBER
    | BOOLEAN
    | ARRAY_BUFFER
    | ARRAY
    | ...
}
```

**功能：** [runJavaScirptExt](#func-runjavascriptextarrayuint8-asynccallbackjsmessageext)脚本执行后返回的结果的类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<JsMessageType>
- ToString

### ARRAY

```cangjie
ARRAY
```

**功能：** 数组类型。

**起始版本：** 19

### ARRAY_BUFFER

```cangjie
ARRAY_BUFFER
```

**功能：** 原始二进制数据缓冲区。

**起始版本：** 19

### BOOLEAN

```cangjie
BOOLEAN
```

**功能：** 布尔类型。

**起始版本：** 19

### NOTSUPPORT

```cangjie
NOTSUPPORT
```

**功能：** 用于描述[webMessagePort](#class-webmessageport)所支持的数据类型。

**起始版本：** 19

### NUMBER

```cangjie
NUMBER
```

**功能：** 数值类型。

**起始版本：** 19

### STRING

```cangjie
STRING
```

**功能：** 字符串类型。

**起始版本：** 19

### func !=(JsMessageType)

```cangjie
public operator func !=(other: JsMessageType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[JsMessageType](#enum-jsmessagetype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true，否则返回false。|

### func ==(JsMessageType)

```cangjie
public operator func ==(other: JsMessageType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[JsMessageType](#enum-jsmessagetype)|是|-|待比较的另一个枚举值。|

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