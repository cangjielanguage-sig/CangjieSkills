## enum MediaError

```cangjie
public enum MediaError <: Equatable<MediaError> & ToString {
    | NETWORK_ERROR
    | FORMAT_ERROR
    | DECODE_ERROR
    | ...
}
```

**功能：** 播放器的错误类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<MediaError>
- ToString

### DECODE_ERROR

```cangjie
DECODE_ERROR
```

**功能：** 解码错误。

**起始版本：** 19

### FORMAT_ERROR

```cangjie
FORMAT_ERROR
```

**功能：** 媒体格式错误。

**起始版本：** 19

### NETWORK_ERROR

```cangjie
NETWORK_ERROR
```

**功能：** 网络错误。

**起始版本：** 19

### func !=(MediaError)

```cangjie
public operator func !=(other: MediaError): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MediaError](#enum-mediaerror)|是|-|待比较的播放器错误类型枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等返回true，否则返回false。|

### func ==(MediaError)

```cangjie
public operator func ==(other: MediaError): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MediaError](#enum-mediaerror)|是|-|待比较的播放器错误类型枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取播放器错误类型枚举值的字符串表示。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|播放器错误类型枚举值的字符串表示。|

## enum MediaPlaybackState

```cangjie
public enum MediaPlaybackState <: Equatable<MediaPlaybackState> & ToString {
    | NONE
    | PLAYING
    | PAUSED
    | STOPPED
    | ...
}
```

**功能：** 当前网页的播控状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<MediaPlaybackState>
- ToString

### NONE

```cangjie
NONE
```

**功能：** 表示页面无音视频启播。

**起始版本：** 19

### PAUSED

```cangjie
PAUSED
```

**功能：** 表示页面音视频暂停。

**起始版本：** 19

### PLAYING

```cangjie
PLAYING
```

**功能：** 表示页面音视频播放中。

**起始版本：** 19

### STOPPED

```cangjie
STOPPED
```

**功能：** 表示页面音视频停止。

**起始版本：** 19

### func !=(MediaPlaybackState)

```cangjie
public operator func !=(other: MediaPlaybackState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MediaPlaybackState](#enum-mediaplaybackstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(MediaPlaybackState)

```cangjie
public operator func ==(other: MediaPlaybackState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MediaPlaybackState](#enum-mediaplaybackstate)|是|-|待比较的另一个枚举值。|

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