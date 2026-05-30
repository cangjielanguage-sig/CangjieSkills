## enum AudioRendererCallbackType

```cangjie
public enum AudioRendererCallbackType <: Equatable<AudioRendererCallbackType> & Hashable & ToString {
    | AR_AUDIO_INTERRUPT
    | AR_MARK_PEACH
    | AR_PERIOD_REACH
    | AR_STATE_CHANGE
    | AR_OUTPUT_DEVICE_CHANGE
    | AR_OUTPUT_DEVICE_CHANGE_WITH_INFO
    | AR_WRITE_DATA
    | ...
}
```

**功能：** [AudioRenderer](#class-audiorenderer)的callback类型。

**系统能力：** 详见各枚举值

**起始版本：** 19

**父类型：**

- Equatable\<[AudioRendererCallbackType](#enum-audiorenderercallbacktype)>
- Hashable
- ToString

### AR_AUDIO_INTERRUPT

```cangjie
AR_AUDIO_INTERRUPT
```

**功能：** 音频中断事件。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

### AR_MARK_PEACH

```cangjie
AR_MARK_PEACH
```

**功能：** 到达标记事件。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### AR_OUTPUT_DEVICE_CHANGE

```cangjie
AR_OUTPUT_DEVICE_CHANGE
```

**功能：** 音频输出设备变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### AR_OUTPUT_DEVICE_CHANGE_WITH_INFO

```cangjie
AR_OUTPUT_DEVICE_CHANGE_WITH_INFO
```

**功能：** 音频流输出设备变化及原因事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### AR_PERIOD_REACH

```cangjie
AR_PERIOD_REACH
```

**功能：** 到达标记事件。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### AR_STATE_CHANGE

```cangjie
AR_STATE_CHANGE
```

**功能：** 状态变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### AR_WRITE_DATA

```cangjie
AR_WRITE_DATA
```

**功能：** 音频数据写入回调事件。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### func !=(AudioRendererCallbackType)

```cangjie
public operator func !=(other: AudioRendererCallbackType): Bool
```

**功能：** 对回调事件类型进行判不等。

**系统能力：** 详见各枚举值

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioRendererCallbackType](#enum-audiorenderercallbacktype)|是|-|相比较的回调事件类型。 |

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型不同返回true，否则返回false。|

### func ==(AudioRendererCallbackType)

```cangjie
public operator func ==(other: AudioRendererCallbackType): Bool
```

**功能：** 对回调事件类型进行判等。

**系统能力：** 详见各枚举值

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioRendererCallbackType](#enum-audiorenderercallbacktype)|是|-|相比较的回调事件类型。|

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