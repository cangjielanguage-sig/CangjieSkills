## class DeviceChangeAction

```cangjie
public class DeviceChangeAction {}
```

**功能：** 描述设备连接状态变化和设备信息。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop \`type\`

```cangjie
public mut prop `type`: DeviceChangeType
```

**功能：** 设备连接状态变化。

**类型：** [DeviceChangeType](#enum-devicechangetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop deviceDescriptors

```cangjie
public mut prop deviceDescriptors: AudioDeviceDescriptors
```

**功能：** 设备信息。

**类型：** [AudioDeviceDescriptors](#type-audiodevicedescriptors)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

## class InterruptEvent

```cangjie
public class InterruptEvent {}
```

**功能：** 播放中断时，应用接收的中断事件。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop eventType

```cangjie
public mut prop eventType: InterruptType
```

**功能：** 中断事件类型，开始或是结束。

**类型：** [InterruptType](#enum-interrupttype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop forceType

```cangjie
public mut prop forceType: InterruptForceType
```

**功能：** 操作是由系统执行或是由应用程序执行。

**类型：** [InterruptForceType](#enum-interruptforcetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop hintType

```cangjie
public mut prop hintType: InterruptHint
```

**功能：** 中断提示。

**类型：** [InterruptHint](#enum-interrupthint)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

## class MicStateChangeEvent

```cangjie
public class MicStateChangeEvent {}
```

**功能：** 麦克风状态变化时，应用接收的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### prop mute

```cangjie
public mut prop mute: Bool
```

**功能：** 回调返回系统麦克风静音状态，true为静音，false为非静音。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

## class VolumeEvent

```cangjie
public class VolumeEvent {}
```

**功能：** 音量改变时，应用接收的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

### prop updateUi

```cangjie
public mut prop updateUi: Bool
```

**功能：** 在UI中显示音量变化，true为显示，false为不显示。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

### prop volume

```cangjie
public mut prop volume: Int32
```

**功能：** 音量等级，可设置范围通过[getMinVolume](#func-getminvolumeaudiovolumetype)和[getMaxVolume](#func-getmaxvolumeaudiovolumetype)获取。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

### prop volumeType

```cangjie
public mut prop volumeType: AudioVolumeType
```

**功能：** 音量流类型。

**类型：** [AudioVolumeType](#enum-audiovolumetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19