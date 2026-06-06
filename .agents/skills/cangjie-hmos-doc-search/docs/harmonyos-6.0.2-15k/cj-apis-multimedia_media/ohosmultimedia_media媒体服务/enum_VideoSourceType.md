## enum VideoSourceType

```cangjie
public enum VideoSourceType <: ToString & Equatable<VideoSourceType> {
    | VIDEO_SOURCE_TYPE_SURFACE_YUV
    | VIDEO_SOURCE_TYPE_SURFACE_ES
    | ...
}
```

**功能：** 表示视频录制中视频源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<VideoSourceType>

### VIDEO_SOURCE_TYPE_SURFACE_ES

```cangjie
VIDEO_SOURCE_TYPE_SURFACE_ES
```

**功能：** 输入surface中携带的是ES data。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### VIDEO_SOURCE_TYPE_SURFACE_YUV

```cangjie
VIDEO_SOURCE_TYPE_SURFACE_YUV
```

**功能：** 输入surface中携带的是raw data。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取视频源类型的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|视频源类型的字符串表示。|

### func !=(VideoSourceType)

```cangjie
public operator override func !=(that: VideoSourceType): Bool
```

**功能：** 对视频源类型进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[VideoSourceType](#enum-videosourcetype)|是|-|视频源类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|视频源类型不等，返回true，否则返回false。|

### func ==(VideoSourceType)

```cangjie
public operator override func ==(that: VideoSourceType): Bool
```

**功能：** 对视频源类型进行判等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[VideoSourceType](#enum-videosourcetype)|是|-|视频源类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|视频源类型相等，返回true，否则返回false。|