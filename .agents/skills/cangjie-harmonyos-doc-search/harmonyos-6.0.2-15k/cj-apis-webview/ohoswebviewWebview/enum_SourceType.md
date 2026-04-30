## enum SourceType

```cangjie
public enum SourceType <: Equatable<SourceType> & ToString {
    | URL
    | MSE
    | ...
}
```

**功能：** 表示媒体源的类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<SourceType>
- ToString

### MSE

```cangjie
MSE
```

**功能：** 媒体源的类型是blob。

**起始版本：** 19

### URL

```cangjie
URL
```

**功能：** 媒体源的类型是URL。

**起始版本：** 19

### func !=(SourceType)

```cangjie
public operator func !=(other: SourceType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SourceType](#enum-sourcetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(SourceType)

```cangjie
public operator func ==(other: SourceType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SourceType](#enum-sourcetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|