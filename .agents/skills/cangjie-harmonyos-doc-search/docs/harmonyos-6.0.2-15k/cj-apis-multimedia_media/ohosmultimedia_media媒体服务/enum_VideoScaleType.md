## enum VideoScaleType

```cangjie
public enum VideoScaleType <: Equatable<VideoScaleType> & ToString {
    | VIDEO_SCALE_TYPE_FIT
    | VIDEO_SCALE_TYPE_FIT_CROP
    | VIDEO_SCALE_TYPE_UNKNOWN
    | ...
}
```

**功能：** 视频缩放模式。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

**父类型：**

- Equatable\<VideoScaleType>
- ToString

### VIDEO_SCALE_TYPE_FIT

```cangjie
VIDEO_SCALE_TYPE_FIT
```

**功能：** 默认比例类型，视频拉伸至与窗口等大。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### VIDEO_SCALE_TYPE_FIT_CROP

```cangjie
VIDEO_SCALE_TYPE_FIT_CROP
```

**功能：** 保持视频宽高比拉伸至填满窗口，内容可能会有裁剪。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### VIDEO_SCALE_TYPE_UNKNOWN

```cangjie
VIDEO_SCALE_TYPE_UNKNOWN
```

**功能：** 表示未知视频缩放模式。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

### func !=(VideoScaleType)

```cangjie
public operator func !=(other: VideoScaleType): Bool
```

**功能：** 判断两个VideoScaleType是否不等。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[VideoScaleType](#enum-videoscaletype)|是|-|另一VideoScaleType。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个VideoScaleType不等返回true，否则返回false。|

### func ==(VideoScaleType)

```cangjie
public operator func ==(other: VideoScaleType): Bool
```

**功能：** 判断两个VideoScaleType是否相等。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[VideoScaleType](#enum-videoscaletype)|是|-|另一VideoScaleType。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个VideoScaleType相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回VideoScaleType的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|VideoScaleType的字符串表示。|