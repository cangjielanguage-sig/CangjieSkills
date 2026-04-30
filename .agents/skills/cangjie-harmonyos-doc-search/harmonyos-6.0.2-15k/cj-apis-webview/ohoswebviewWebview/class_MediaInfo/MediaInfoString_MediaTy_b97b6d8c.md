### MediaInfo(String, MediaType, Array\<MediaSourceInfo>, NativeMediaPlayerSurfaceInfo, Bool, Array\<String>, Bool, String, Preload, HashMap\<String, String>, HashMap\<String, String>)

```cangjie
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
```

**功能：** MediaInfo的主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|embedID|String|是|-|网页中的\<video>或\<audio>的ID。|
|mediaType|[MediaType](#enum-mediatype)|是|-|媒体的类型。|
|mediaSrcList|Array\<[MediaSourceInfo](#class-mediasourceinfo)>|是|-|媒体的源。可能有多个源，应用需要选择一个支持的源来播放。|
|surfaceInfo|[NativeMediaPlayerSurfaceInfo](#class-nativemediaplayersurfaceinfo)|是|-|用于同层渲染的surface信息。|
|controlsShown|Bool|是|-|\<video>或\<audio>中是否有controls属性。|
|controlList|Array\<String>|是|-|\<video>或\<audio>中的controlslist属性的值。|
|muted|Bool|是|-|是否要求静音播放。|
|posterUrl|String|是|-|海报的地址。|
|preload|[Preload](#enum-preload)|是|-|是否需要预加载。|
|headers|HashMap\<String, String>|是|-|播放器请求媒体资源时，需要携带的HTTP头。|
|attributes|HashMap\<String, String>|是|-|\<video>或\<audio>标签中的属性。|