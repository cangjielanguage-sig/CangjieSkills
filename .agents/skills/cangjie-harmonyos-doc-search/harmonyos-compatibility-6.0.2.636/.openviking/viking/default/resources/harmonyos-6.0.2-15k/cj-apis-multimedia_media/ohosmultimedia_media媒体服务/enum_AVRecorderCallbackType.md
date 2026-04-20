## enum AVRecorderCallbackType

```cangjie
public enum AVRecorderCallbackType <: Equatable<AVRecorderCallbackType> & Hashable & ToString {
    | AVRECORDER_ERROR
    | AVRECORDER_STATE_CHANGE
    | AVRECORDER_AUDIO_CAPTURER_CHANGE
    | AVRECORDER_PHOTO_ASSET_AVAILABLE
    | ...
}
```

**功能：** AVRecorder的回调类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**父类型：**

- Equatable\<AVRecorderCallbackType>
- Hashable
- ToString

### AVRECORDER_AUDIO_CAPTURER_CHANGE

```cangjie
AVRECORDER_AUDIO_CAPTURER_CHANGE
```

**功能：** 录音配置变化事件的回调类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AVRECORDER_ERROR

```cangjie
AVRECORDER_ERROR
```

**功能：** AVRecorder的错误事件的回调类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AVRECORDER_PHOTO_ASSET_AVAILABLE

```cangjie
AVRECORDER_PHOTO_ASSET_AVAILABLE
```

**功能：** 媒体资源回调事件类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### AVRECORDER_STATE_CHANGE

```cangjie
AVRECORDER_STATE_CHANGE
```

**功能：** 录制状态机AVRecorderState切换的事件的回调类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### func !=(AVRecorderCallbackType)

```cangjie
public operator func !=(other: AVRecorderCallbackType): Bool
```

**功能：** 对AVRecorder回调类型的枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVRecorderCallbackType](#enum-avrecordercallbacktype)|是|-|AVRecorder的回调类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个AVRecorder回调类型的枚举值不相等返回true，否则返回false。|

### func ==(AVRecorderCallbackType)

```cangjie
public operator func ==(other: AVRecorderCallbackType): Bool
```

**功能：** 对AVRecorder回调类型的枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVRecorderCallbackType](#enum-avrecordercallbacktype)|是|-|AVRecorder的回调类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个AVRecorder回调类型的枚举值相等返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取AVRecorder的回调类型的哈希值。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|AVRecorder的回调类型的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取AVRecorder的回调类型的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|AVRecorder的回调类型的字符串表示。|