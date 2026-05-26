## enum AudioCapturerCallbackType

```cangjie
public enum AudioCapturerCallbackType <: Equatable<AudioCapturerCallbackType> & Hashable & ToString {
    | AUDIO_CAPTURER_CHANGE
    | AUDIO_INTERRUPT
    | INPUT_DEVICE_CHANGE
    | MARK_REACH
    | PERIOD_REACH
    | READ_DATA
    | STATE_CHANGE
    | ...
}
```

**功能：** [AudioCapturer](#class-audiocapturer)的callback类型。

**系统能力：** 详见各枚举值

**起始版本：** 19

**父类型：**

- Equatable\<[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)>
- Hashable
- ToString

### AUDIO_CAPTURER_CHANGE

```cangjie
AUDIO_CAPTURER_CHANGE
```

**功能：** 录音流配置变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### AUDIO_INTERRUPT

```cangjie
AUDIO_INTERRUPT
```

**功能：** 音频中断事件。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

### INPUT_DEVICE_CHANGE

```cangjie
INPUT_DEVICE_CHANGE
```

**功能：** 音频输入设备变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### MARK_REACH

```cangjie
MARK_REACH
```

**功能：** 标记到达事件。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### PERIOD_REACH

```cangjie
PERIOD_REACH
```

**功能：** 到达标记事件。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### READ_DATA

```cangjie
READ_DATA
```

**功能：** 音频数据读取回调事件。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### STATE_CHANGE

```cangjie
STATE_CHANGE
```

**功能：** 状态变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### func !=(AudioCapturerCallbackType)

```cangjie
public operator func !=(other: AudioCapturerCallbackType): Bool
```

**功能：** 对回调事件类型进行判不等。

**系统能力：** 详见各枚举值

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)|是|-|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型不同返回true，否则返回false。|

### func ==(AudioCapturerCallbackType)

```cangjie
public operator func ==(other: AudioCapturerCallbackType): Bool
```

**功能：** 对回调事件类型进行判等。

**系统能力：** 详见各枚举值

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioCapturerCallbackType](#enum-audiocapturercallbacktype)|是|-|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型相同返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取回调事件类型的哈希值。

**系统能力：** 详见各枚举值

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|回调事件类型的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回回调事件的字符串表示。

**系统能力：** 详见各枚举值

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|事件的字符串表示。|