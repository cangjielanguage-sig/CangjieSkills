## enum AVTranscoderCallbackType

```cangjie
public enum AVTranscoderCallbackType <: Equatable<AVTranscoderCallbackType> & Hashable & ToString {
    | ProgressUpdate
    | Complete
    | Error
    | ...
}
```

**功能：** 视频转码回调类型。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**父类型：**

- Equatable\<AVTranscoderCallbackType>
- Hashable
- ToString

### ProgressUpdate

```cangjie
ProgressUpdate
```

**功能：** 转码进度更新事件。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

### Complete

```cangjie
Complete
```

**功能：** 转码完成事件。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

### Error

```cangjie
Error
```

**功能：** 转码错误事件。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

### func !=(AVTranscoderCallbackType)

```cangjie
public operator func !=(other: AVTranscoderCallbackType): Bool
```

**功能：** 对视频转码回调类型的枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVTranscoderCallbackType](#enum-avtranscodercallbacktype)|是|-|视频转码回调类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个视频转码回调类型的枚举值不相等返回true，否则返回false。|

### func ==(AVTranscoderCallbackType)

```cangjie
public operator func ==(other: AVTranscoderCallbackType): Bool
```

**功能：** 对视频转码回调类型的枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVTranscoderCallbackType](#enum-avtranscodercallbacktype)|是|-|视频转码回调类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个视频转码回调类型的枚举值相等返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取视频转码回调类型的哈希值。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Int64|视频转码回调类型的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取视频转码回调的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|视频转码回调类型的字符串表示。|