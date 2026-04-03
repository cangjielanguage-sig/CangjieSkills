### func layoutMode(WebLayoutMode)

```cangjie
public func layoutMode(mode: WebLayoutMode): This
```

**功能：** 设置Web布局模式。

> **说明：**
>
> 目前只支持两种Web布局模式，分别为Web布局跟随系统（WebLayoutMode.NONE）和Web组件高度基于前端页面高度的自适应网页布局（WebLayoutMode.FIT_CONTENT）。
> Web组件高度基于前端页面自适应布局有如下限制：
>
> - 如果Web组件宽或长度超过7680px，请在Web组件创建的时候指定RenderMode.SYNC_RENDER模式，否则会整个白屏。
> - Web组件创建后不支持动态切换layoutMode模式。
> - Web组件宽高规格：指定RenderMode.SYNC_RENDER模式时，分别不超过50万px；指定RenderMode.ASYNC_RENDER模式时，分别不超过7680px。
> - 频繁更改页面宽高会触发Web组件重新布局，影响体验。
> - 不支持瀑布流网页（下拉到底部加载更多）。
> - 仅支持高度自适应，不支持宽度自适应。
> - 由于高度自适应网页高度，无法通过修改组件高度属性来修改组件高度。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[WebLayoutMode](#enum-weblayoutmode)|是|-|web布局模式，跟随系统或自适应布局。<br> 初始值：WebLayoutMode.NONE。|

### func mediaOptions(Int32, Bool)

```cangjie
public func mediaOptions(resumeInterval!: Int32 = 0, audioExclusive!: Bool = true): This
```

**功能：** Web媒体策略的配置。

> **说明：**
>
> - 同一Web实例中的多个音频均视为同一音频。
> - 该媒体播放策略将同时管控有声视频。
> - 属性参数更新后需重新播放音频方可生效。
> - 建议为所有Web组件设置相同的audioExclusive值。
> - 音视频互相打断在应用内和应用间生效，续播只在应用间生效。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resumeInterval|Int32|否|0| **命名参数。** 被暂停的Web音频能够自动续播的有效期，单位：秒。有效期范围0~60秒，如若超过60秒，按照60s处理，由于近似值原因，该有效期可能存在一秒内的误差。|
|audioExclusive|Bool|否|true| **命名参数。** 应用内多个Web实例的音频是否独占。true表示独占，false表示不独占。|

### func mediaPlayGestureAccess(Bool)

```cangjie
public func mediaPlayGestureAccess(access: Bool): This
```

**功能：** 设置有声视频播放是否需要用户手动点击，静音视频播放不受该接口管控，默认需要。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|access|Bool|是|-|有声视频播放是否需要用户手动点击。true表示设置有声视频播放需要用户手动点击，false表示设置有声视频播放不需要用户手动点击。<br> 初始值：true。|