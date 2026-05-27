## class SnapshotResult

```cangjie
public class SnapshotResult {
    public SnapshotResult(
        public var id: ?String,
        public var image: ?PixelMap,
        public var status: ?Bool,
        public var size: ?SizeOptions
    )
}
```

**功能：** 全量绘制回调结果。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### var id

```cangjie
public var id: ?String
```

**功能：** snapshot的id。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var image

```cangjie
public var image: ?PixelMap
```

**功能：** [PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)格式的全量绘制结果。

**类型：** PixelMap

**读写能力：** 可读写

**起始版本：** 19

### var size

```cangjie
public var size: ?SizeOptions
```

**功能：** web绘制的真实尺寸，默认单位vp。

**类型：** [SizeOptions](#struct-sizeoptions)

**读写能力：** 可读写

**起始版本：** 19

### var status

```cangjie
public var status: ?Bool
```

**功能：** snapshot的状态，正常为true，失败为false，获取全量绘制结果失败，返回size的长宽都为0，map为空。

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 19

### SnapshotResult(?String, ?PixelMap, ?Bool, ?SizeOptions)

```cangjie
public SnapshotResult(
    public var id: ?String,
    public var image: ?PixelMap,
    public var status: ?Bool,
    public var size: ?SizeOptions
)
```

**功能：** SnapshotResult主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|?String|是|-|snapshot的id。|
|image|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)格式的全量绘制结果。|
|status|?Bool|是|-|snapshot的状态，正常为true，失败为false，获取全量绘制结果失败，返回size的长宽都为0，map为空。|
|size|[SizeOptions](#struct-sizeoptions)|是|-|web绘制的真实尺寸，默认单位vp。|

## class WebHeader

```cangjie
public class WebHeader {
    public WebHeader(
        public var headerKey: String,
        public var headerValue: String
    )
}
```

**功能：** Web组件返回的请求/响应头对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

### var headerKey

```cangjie
public var headerKey: String
```

**功能：** 请求/响应头的key。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var headerValue

```cangjie
public var headerValue: String
```

**功能：** 请求/响应头的value。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### WebHeader(String, String)

```cangjie
public WebHeader(
    public var headerKey: String,
    public var headerValue: String
)
```

**功能：** WebHeader的主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|headerKey|String|是|-|请求/响应头的key。|
|headerValue|String|是|-|请求/响应头的value。|