## enum AudioHapticPlayerCallBackType

```cangjie
public enum AudioHapticPlayerCallBackType <: Equatable<AudioHapticPlayerCallBackType> {
    | AHP_END_OF_STREAM
    | AHP_AUDIO_INTERRRUPT
    | ...
}
```

**功能：** [AudioHapticPlayer](#class-audiohapticplayer)类的on/off函数的回调事件类型。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioHapticPlayerCallBackType](#enum-audiohapticplayercallbacktype)>

### AHP_AUDIO_INTERRRUPT

```cangjie
AHP_AUDIO_INTERRRUPT
```

**功能：** 音频中断事件。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

### AHP_END_OF_STREAM

```cangjie
AHP_END_OF_STREAM
```

**功能：** 流结束事件。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

### func !=(AudioHapticPlayerCallBackType)

```cangjie
public operator func !=(other: AudioHapticPlayerCallBackType): Bool
```

**功能：** 对枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioHapticPlayerCallBackType](#enum-audiohapticplayercallbacktype)|是|-|[AudioHapticPlayer](#class-audiohapticplayer)类的on/off函数的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果AudioHapticPlayer类的on/off函数的回调事件类型相同，返回false，否则返回true。|

### func ==(AudioHapticPlayerCallBackType)

```cangjie
public operator func ==(other: AudioHapticPlayerCallBackType): Bool
```

**功能：** 对枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioHapticPlayerCallBackType](#enum-audiohapticplayercallbacktype)|是|-|[AudioHapticPlayer](#class-audiohapticplayer)类的on/off函数的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果[AudioHapticPlayer](#class-audiohapticplayer)类的on/off函数的回调事件类型相同，返回true，否则返回false。|