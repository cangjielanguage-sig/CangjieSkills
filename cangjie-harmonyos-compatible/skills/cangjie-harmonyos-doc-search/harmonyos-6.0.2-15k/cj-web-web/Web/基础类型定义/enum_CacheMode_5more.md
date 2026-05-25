### enum CacheMode

```cangjie
public enum CacheMode {
    | Default
    | None
    | Online
    | Only
}
```

**功能：** 设置缓存模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### Default

```cangjie
Default
```

**功能：** 优先使用未过期cache加载资源，无效或无cache时从网络获取。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### None

```cangjie
None
```

**功能：** 优先使用cache(含过期)加载资源，无cache时从网络获取。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### Online

```cangjie
Online
```

**功能：** 强制从网络获取最新资源，不使用任何cache。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### Only

```cangjie
Only
```

**功能：** 仅使用本地cache加载资源。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### enum MessageLevel

```cangjie
public enum MessageLevel {
    | Debug
    | Error
    | Info
    | Log
    | Warn
}
```

**功能：** ConsoleMessage的信息级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### Debug

```cangjie
Debug
```

**功能：** 调试级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### Error

```cangjie
Error
```

**功能：** 错误级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### Info

```cangjie
Info
```

**功能：** 消极级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### Log

```cangjie
Log
```

**功能：** 日志级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### Warn

```cangjie
Warn
```

**功能：** 警告级别。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### enum OverScrollMode

```cangjie
public enum OverScrollMode {
    | NEVER
    | ALWAYS
}
```

**功能：** 设置Web过滚动模式，默认关闭。当过滚动模式开启时，当用户在Web根页面上滑动到边缘时，Web会通过弹性动画弹回界面，根页面上的内部页面不会触发回弹。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### ALWAYS

```cangjie
ALWAYS
```

**功能：** 设置Web的过滚动模式为开启。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### NEVER

```cangjie
NEVER
```

**功能：** 设置Web的过滚动模式为关闭。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### enum WebKeyboardAvoidMode

```cangjie
public enum WebKeyboardAvoidMode {
    | RESIZE_VISUAL
    | RESIZE_CONTENT
    | OVERLAYS_CONTENT
}
```

**功能：** 软键盘避让的模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### OVERLAYS_CONTENT

```cangjie
OVERLAYS_CONTENT
```

**功能：** 不调整任何视口大小，不会触发软键盘避让。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### RESIZE_CONTENT

```cangjie
RESIZE_CONTENT
```

**功能：** 软键盘避让时，同时调整可视视口和布局视口的大小。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### RESIZE_VISUAL

```cangjie
RESIZE_VISUAL
```

**功能：** 软键盘避让时，仅调整可视视口大小，不调整布局视口大小。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### enum WebLayoutMode

```cangjie
public enum WebLayoutMode {
    | NONE
    | FIT_CONTENT
}
```

**功能：** 设置Web布局模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### FIT_CONTENT

```cangjie
FIT_CONTENT
```

**功能：** Web布局跟随系统。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### NONE

```cangjie
NONE
```

**功能：** Web基于页面大小的自适应网页布局。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19