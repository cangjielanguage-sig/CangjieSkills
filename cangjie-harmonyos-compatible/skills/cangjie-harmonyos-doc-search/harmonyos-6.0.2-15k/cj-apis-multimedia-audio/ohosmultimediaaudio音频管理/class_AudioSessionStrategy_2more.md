## class AudioSessionStrategy

```cangjie
public class AudioSessionStrategy {
    public let concurrencyMode: AudioConcurrencyMode
    public init(concurrencyMode: AudioConcurrencyMode)
}
```

**功能：** 音频会话策略。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

### let concurrencyMode

```cangjie
public let concurrencyMode: AudioConcurrencyMode
```

**功能：** 音频并发模式。

**类型：** [AudioConcurrencyMode](#enum-audioconcurrencymode)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

### init(AudioConcurrencyMode)

```cangjie
public init(concurrencyMode: AudioConcurrencyMode)
```

**功能：** AudioSessionStrategy的构造函数。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|concurrencyMode|[AudioConcurrencyMode](#enum-audioconcurrencymode)|是|-|音频并发模式。|

## class AudioStreamDeviceChangeInfo

```cangjie
public class AudioStreamDeviceChangeInfo {}
```

**功能：** 流设备变更时，应用接收的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop changeReason

```cangjie
public mut prop changeReason: AudioStreamDeviceChangeReason
```

**功能：** 流设备变更原因。

**类型：** [AudioStreamDeviceChangeReason](#enum-audiostreamdevicechangereason)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop devices

```cangjie
public mut prop devices: AudioDeviceDescriptors
```

**功能：** 设备信息。

**类型：** [AudioDeviceDescriptors](#type-audiodevicedescriptors)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19