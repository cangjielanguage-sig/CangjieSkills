## enum PlaybackStatus

```cangjie
public enum PlaybackStatus <: Equatable<PlaybackStatus> & ToString {
    | PAUSED
    | PLAYING
    | ...
}
```

**功能：** 用于表示播放器的播放状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<PlaybackStatus>
- ToString

### PAUSED

```cangjie
PAUSED
```

**功能：** 前台不可交互状态，例如从屏幕底部上划，应用进入到多任务界面后的状态。

**起始版本：** 19

### PLAYING

```cangjie
PLAYING
```

**功能：** 表示页面音视频播放中。

**起始版本：** 19

### func !=(PlaybackStatus)

```cangjie
public operator func !=(other: PlaybackStatus): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackStatus](#enum-playbackstatus)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PlaybackStatus)

```cangjie
public operator func ==(other: PlaybackStatus): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackStatus](#enum-playbackstatus)|是|-|另一个枚举值。|

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

## enum Preload

```cangjie
public enum Preload <: Equatable<Preload> & ToString {
    | NONE
    | METADATA
    | AUTO
    | ...
}
```

**功能：** 播放器预加载媒体数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<Preload>
- ToString

### AUTO

```cangjie
AUTO
```

**功能：** 预加载足够多的媒体数据，以保证能流畅地播放。

**起始版本：** 19

### METADATA

```cangjie
METADATA
```

**功能：** 只预加载媒体的元数据。

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 不预加载。

**起始版本：** 19

### func !=(Preload)

```cangjie
public operator func !=(other: Preload): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Preload](#enum-preload)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(Preload)

```cangjie
public operator func ==(other: Preload): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Preload](#enum-preload)|是|-|另一个枚举值。|

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