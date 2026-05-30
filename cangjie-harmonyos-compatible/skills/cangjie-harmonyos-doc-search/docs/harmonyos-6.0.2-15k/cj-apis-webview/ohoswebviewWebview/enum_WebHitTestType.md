## enum WebHitTestType

```cangjie
public enum WebHitTestType <: Equatable<WebHitTestType> & ToString {
    | EditText
    | Email
    | HttpAnchor
    | HttpAnchorImg
    | Img
    | Map
    | Phone
    | Unknown
    | ...
}
```

**功能：** [getHitTest](#func-gethittest)用于指示游标节点。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**父类型：**

- Equatable\<WebHitTestType>
- ToString

### EditText

```cangjie
EditText
```

**功能：** 可编辑的区域。

**起始版本：** 12

### Email

```cangjie
Email
```

**功能：** 电子邮件地址。

**起始版本：** 12

### HttpAnchor

```cangjie
HttpAnchor
```

**功能：** 超链接，其中src为http。

**起始版本：** 12

### HttpAnchorImg

```cangjie
HttpAnchorImg
```

**功能：** 带有超链接的图片，其中src为http+HTML::img。

**起始版本：** 12

### Img

```cangjie
Img
```

**功能：** HTML::img标签。

**起始版本：** 12

### Map

```cangjie
Map
```

**功能：** 地理地址。

**起始版本：** 12

### Phone

```cangjie
Phone
```

**功能：** 电话号码。

**起始版本：** 12

### Unknown

```cangjie
Unknown
```

**功能：** 未知内容。

**起始版本：** 12

### func !=(WebHitTestType)

```cangjie
public operator func !=(other: WebHitTestType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebHitTestType](#enum-webhittesttype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true，否则返回false。|

### func ==(WebHitTestType)

```cangjie
public operator func ==(other: WebHitTestType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebHitTestType](#enum-webhittesttype)|是|-|待比较的另一个枚举值。|

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

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串表示。|