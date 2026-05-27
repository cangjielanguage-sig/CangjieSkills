## class OfflineResourceMap

```cangjie
public class OfflineResourceMap {
    public OfflineResourceMap(
        var urlList: Array<String>,
        var resource: Array<UInt8>,
        var responseHeaders: Array<WebHeader>,
        var _type: OfflineResourceType
    )
}
```

**功能：** 本地离线资源配置对象，用于配置将被[injectOfflineResources](#func-injectofflineresourcesarrayofflineresourcemap)接口注入到内存缓存的本地离线资源的相关信息，内核会根据此信息生成资源缓存，并据此控制缓存的有效期。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### OfflineResourceMap(Array\<String>, Array\<UInt8>, Array\<WebHeader>, OfflineResourceType)

```cangjie
public OfflineResourceMap(
    var urlList: Array<String>,
    var responseHeaders: Array<WebHeader>,
    var _type: OfflineResourceType
)
```

**功能：** OfflineResourceMap主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|urlList|Array\<String>|是|-|本地离线资源对应的网络地址列表，列表的第一项将作为资源的源(Origin), 如果仅提供一个网络地址，则使用该地址作为这个资源的源。url仅支持http或https协议，长度不超过2048。|
|resource|Array\<UInt8>|是|-|本地离线资源的内容。|
|responseHeaders|Array\<[WebHeader](#class-webheader)>|是|-|资源对应的HTTP响应头。|
|_type|[OfflineResourceType](#enum-offlineresourcetype)|是|-|资源的类型，目前仅支持Javascript、图片和CSS类型的资源。|

## class RectEvent

```cangjie
public class RectEvent {
    public RectEvent (
        public let x: Float64,
        public let y: Float64,
        public let width: Float64,
        public let height: Float64
    )
}
```

**功能：** 矩形定义。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### let height

```cangjie
public let height: Float64
```

**功能：** 矩形的高度。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### let width

```cangjie
public let width: Float64
```

**功能：** 矩形的宽度。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### let x

```cangjie
public let x: Float64
```

**功能：** 矩形区域左上角x坐标。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### let y

```cangjie
public let y: Float64
```

**功能：** 矩形区域左上角y坐标。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### RectEvent(Float64, Float64, Float64, Float64)

```cangjie
public RectEvent (
    public let x: Float64,
    public let y: Float64,
    public let width: Float64,
    public let height: Float64
)
```

**功能：** 构造RectEvent对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|矩形区域左上角x坐标。|
|y|Float64|是|-|矩形区域左上角y坐标。|
|width|Float64|是|-|矩形的宽度。|
|height|Float64|是|-|矩形的高度。|