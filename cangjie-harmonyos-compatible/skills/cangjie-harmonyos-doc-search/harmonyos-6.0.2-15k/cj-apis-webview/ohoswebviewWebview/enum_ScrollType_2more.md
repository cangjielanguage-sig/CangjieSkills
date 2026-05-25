## enum ScrollType

```cangjie
public enum ScrollType {
    | EVENT
    | ...
}
```

**功能：** Scroll滚动类型，用于setScrollable。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

### EVENT

```cangjie
EVENT
```

**功能：** 滚动事件，表示通过触摸屏，触摸板，鼠标滚轮生成的网页滚动。

**起始版本：** 20

## type CreateNativeMediaPlayerCallback

```cangjie
public type CreateNativeMediaPlayerCallback = (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) -> NativeMediaPlayerBridge
```

**功能：** [CreateNativeMediaPlayerCallback](#type-createnativemediaplayercallback)是(handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) -> NativeMediaPlayerBridge类型的别名。

**起始版本：** 19