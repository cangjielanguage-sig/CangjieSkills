## enum Sound

```cangjie
public enum Sound <: ToString {
    | VIBRATE_WHILE_RINGING
    | DEFAULT_ALARM_ALERT
    | DTMF_TONE_TYPE_WHILE_DIALING
    | DTMF_TONE_WHILE_DIALING
    | HAPTIC_FEEDBACK_STATUS
    | AFFECTED_MODE_RINGER_STREAMS
    | AFFECTED_MUTE_STREAMS
    | DEFAULT_NOTIFICATION_SOUND
    | DEFAULT_RINGTONE
    | SOUND_EFFECTS_STATUS
    | VIBRATE_STATUS
    | ...
}
```

**功能：** 提供设置声音效果的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### AFFECTED_MODE_RINGER_STREAMS

```cangjie
AFFECTED_MODE_RINGER_STREAMS
```

**功能：** 哪些音频流受振铃模式和请勿打扰(DND)模式更改的影响。希望特定的音频流受到振铃模式和DDN模式变化的影响，请将对应比特位设置为1。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### AFFECTED_MUTE_STREAMS

```cangjie
AFFECTED_MUTE_STREAMS
```

**功能：** 受静音模式影响的音频流。希望特定音频流在静音模式下保持静音，请将相应位设置为1。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEFAULT_ALARM_ALERT

```cangjie
DEFAULT_ALARM_ALERT
```

**功能：** 系统默认告警的存储区域。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEFAULT_NOTIFICATION_SOUND

```cangjie
DEFAULT_NOTIFICATION_SOUND
```

**功能：** 系统默认通知音的存储区域。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEFAULT_RINGTONE

```cangjie
DEFAULT_RINGTONE
```

**功能：** 系统默认铃声的存储区域。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DTMF_TONE_TYPE_WHILE_DIALING

```cangjie
DTMF_TONE_TYPE_WHILE_DIALING
```

**功能：** 拨号时播放的双音多频(DTMF)音的类型。值为0表示常规的短音效，值为1表示长音效。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DTMF_TONE_WHILE_DIALING

```cangjie
DTMF_TONE_WHILE_DIALING
```

**功能：** 拨号时是否播放DTMF音。值为1，表示播放DTMF音；值为0，表示不播放。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### HAPTIC_FEEDBACK_STATUS

```cangjie
HAPTIC_FEEDBACK_STATUS
```

**功能：** 设备是否启用触觉反馈。值为true，表示启用触觉反馈；值为false，表示不启用触觉反馈。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### SOUND_EFFECTS_STATUS

```cangjie
SOUND_EFFECTS_STATUS
```

**功能：** 声音功能是否可用。值为0表示不可用；值为1表示可用。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### VIBRATE_STATUS

```cangjie
VIBRATE_STATUS
```

**功能：** 设备是否为事件振动。该参数在系统内部使用。值为1，表示设备会因事件而振动；值为0，表示设备不因事件振动。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### VIBRATE_WHILE_RINGING

```cangjie
VIBRATE_WHILE_RINGING
```

**功能：** 设备在来电响铃时是否振动。此属性将由电话和设置应用程序使用。 该值是布尔类型，仅影响设备因来电而响铃的情况，不影响任何其他应用程序或场景。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置声音效果的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置声音效果的数据项。 |