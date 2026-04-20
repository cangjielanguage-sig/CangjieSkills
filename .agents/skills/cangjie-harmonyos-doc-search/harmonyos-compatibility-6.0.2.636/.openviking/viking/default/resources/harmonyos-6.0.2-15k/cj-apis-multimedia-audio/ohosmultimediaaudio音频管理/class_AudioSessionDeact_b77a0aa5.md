## class AudioSessionDeactivatedEvent

```cangjie
public class AudioSessionDeactivatedEvent {
    public let reason: AudioSessionDeactivatedReason
    public init(reason: AudioSessionDeactivatedReason)
}
```

**功能：** 音频会话已停用事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

### let reason

```cangjie
public let reason: AudioSessionDeactivatedReason
```

**功能：** 音频会话停用原因。

**类型：** [AudioSessionDeactivatedReason](#enum-audiosessiondeactivatedreason)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

### init(AudioSessionDeactivatedReason)

```cangjie
public init(reason: AudioSessionDeactivatedReason)
```

**功能：** AudioSessionDeactivatedEvent构造函数。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|reason|[AudioSessionDeactivatedReason](#enum-audiosessiondeactivatedreason)|是|-|音频会话停用原因。|