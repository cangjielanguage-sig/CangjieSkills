## class RequestInfo

```cangjie
public class RequestInfo {
    public RequestInfo(
       public var url: String,
       public var method: String,
       public var formData: String
    )
}
```

**功能：** Web组件发送的资源请求信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### var formData

```cangjie
public var formData: String
```

**功能：** 请求的表单数据。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var method

```cangjie
public var method: String
```

**功能：** 请求的方法。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var url

```cangjie
public var url: String
```

**功能：** 请求的链接。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### RequestInfo(String, String, String)

```cangjie
public RequestInfo(
    public var url: String,
    public var method: String,
    public var formData: String
)
```

**功能：** RequestInfo主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|请求的链接。|
|method|String|是|-|请求的方法。|
|formData|String|是|-|请求的表单数据。|

## struct SizeOptions

```cangjie
public struct SizeOptions {
    public SizeOptions(
        public var width!: Length = 0.vp,
        public var height!: Length = 0.vp
    ) {}
}
```

**功能：** 设置宽高尺寸。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### var width

```cangjie
public var width: Length = 0.vp
```

**功能：** 元素宽度。

**类型：** [Length](../../arkui-cj/cj-common-types.md#interface-length)

**读写能力：** 可读写。

**起始版本：** 19

### var height

```cangjie
public var height: Length = 0.vp
```

**功能：** 元素高度。

**类型：** [Length](../../arkui-cj/cj-common-types.md#interface-length)

**读写能力：** 可读写。

**起始版本：** 19

### SizeOptions(Length, Length)

```cangjie
public SizeOptions(public var width!: Length = 0.vp, public var height!: Length = 0.vp)
```

**功能：** SizeOptions主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:----|:----|:----|:----|:----|
|width|[Length](../../arkui-cj/cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 元素宽度。|
|height|[Length](../../arkui-cj/cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 元素高度。|

**起始版本：** 19

## class SnapshotInfo

```cangjie
public class SnapshotInfo {
    public SnapshotInfo(
        public var id!: String = "",
        public var size!: SizeOptions = SizeOptions()
    )
}
```

**功能：** 获取全量绘制结果入参。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### var id

```cangjie
public var id: String = ""
```

**功能：** snapshot的id。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var size

```cangjie
public var size: SizeOptions = SizeOptions()
```

**功能：** web绘制的尺寸，最多支持16000px * 16000px，长度单位支持px、vp、%，需保持不同参数传入长度单位一致，默认单位vp，超过规格时返回最大规格。只写数字时单位为vp。

示例：width:‘100px’, height:‘200px’。或者 width:‘20%’, height’30%'。

**类型：** [SizeOptions](#struct-sizeoptions)

**读写能力：** 可读写

**起始版本：** 19

### SnapshotInfo(String, SizeOptions)

```cangjie
public SnapshotInfo(
    public var id!: String = "",
    public var size!: SizeOptions = SizeOptions()
)
```

**功能：** SnapshotInfo主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|否|""| **命名参数。** snapshot的id。|
|size|[SizeOptions](#struct-sizeoptions)|否|SizeOptions()| **命名参数。** web绘制的尺寸。|