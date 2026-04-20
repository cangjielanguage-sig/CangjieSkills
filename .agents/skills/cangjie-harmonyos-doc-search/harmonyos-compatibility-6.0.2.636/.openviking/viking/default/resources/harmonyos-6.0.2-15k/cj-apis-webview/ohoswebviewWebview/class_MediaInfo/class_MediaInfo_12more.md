## class MediaInfo

```cangjie
public class MediaInfo {
    public MediaInfo(
        public let embedID: String,
        public let mediaType: MediaType,
        public let mediaSrcList: Array<MediaSourceInfo>,
        public let surfaceInfo: NativeMediaPlayerSurfaceInfo,
        public let controlsShown: Bool,
        public let controlList: Array<String>,
        public let muted: Bool,
        public let posterUrl: String,
        public let preload: Preload,
        public let headers: HashMap<String, String>,
        public let attributes: HashMap<String, String>
    )
}
```

**功能：** [CreateNativeMediaPlayerCallback](#type-createnativemediaplayercallback)回调函数的一个参数。

包含了网页中媒体的信息。应用可以根据这些信息来创建接管网页媒体播放的播放器。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### let attributes

```cangjie
public let attributes: HashMap<String, String>
```

**功能：** `<video>`或`<audio>`标签中的属性。

**类型：** HashMap\<String, String>

**读写能力：** 只读

**起始版本：** 19

### let controlList

```cangjie
public let controlList: Array<String>
```

**功能：** `<video>` 或`<audio>`中的`controlslist`属性的值。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### let controlsShown

```cangjie
public let controlsShown: Bool
```

**功能：** `<video>`或`<audio>`中是否有`controls`属性。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let embedID

```cangjie
public let embedID: String
```

**功能：** 网页中的`<video>`或`<audio>`的ID。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let headers

```cangjie
public let headers: HashMap<String, String>
```

**功能：** 播放器请求媒体资源时，需要携带的 HTTP 头。

**类型：** HashMap\<String, String>

**读写能力：** 只读

**起始版本：** 19

### let mediaSrcList

```cangjie
public let mediaSrcList: Array<MediaSourceInfo>
```

**功能：** 媒体的源。可能有多个源，应用需要选择一个支持的源来播放。

**类型：** Array\<[MediaSourceInfo](#class-mediasourceinfo)>

**读写能力：** 只读

**起始版本：** 19

### let mediaType

```cangjie
public let mediaType: MediaType
```

**功能：** 媒体的类型。

**类型：** [MediaType](#enum-mediatype)

**读写能力：** 只读

**起始版本：** 19

### let muted

```cangjie
public let muted: Bool
```

**功能：** 是否要求静音播放。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let posterUrl

```cangjie
public let posterUrl: String
```

**功能：** 海报的地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let preload

```cangjie
public let preload: Preload
```

**功能：** 是否需要预加载。

**类型：** [Preload](#enum-preload)

**读写能力：** 只读

**起始版本：** 19

### let surfaceInfo

```cangjie
public let surfaceInfo: NativeMediaPlayerSurfaceInfo
```

**功能：** 用于同层渲染的surface信息。

**类型：** [NativeMediaPlayerSurfaceInfo](#class-nativemediaplayersurfaceinfo)

**读写能力：** 只读

**起始版本：** 19