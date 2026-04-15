## class CodecInfo

```cangjie
public class CodecInfo {
    public var codecType: CodecType
    public var codecBitsPerSample: CodecBitsPerSample
    public var codecChannelMode: CodecChannelMode
    public var codecSampleRate: CodecSampleRate
}
```

**功能：** 编码器信息。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var codecBitsPerSample

```cangjie
public var codecBitsPerSample: CodecBitsPerSample
```

**功能：** 表示每个采样点的位数，初始值为CodecBitsPerSampleNone。

**类型：** [CodecBitsPerSample](#enum-codecbitspersample)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var codecChannelMode

```cangjie
public var codecChannelMode: CodecChannelMode
```

**功能：** 表示编码器的声道模式，初始值为CodecChannelModeNone。

**类型：** [CodecChannelMode](#enum-codecchannelmode)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var codecSampleRate

```cangjie
public var codecSampleRate: CodecSampleRate
```

**功能：** 表示编码器的采样率，初始值为CodecSampleRateNone。

**类型：** [CodecSampleRate](#enum-codecsamplerate)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var codecType

```cangjie
public var codecType: CodecType
```

**功能：** 表示编码器类型，初始值为CodecTypeSbc。

**类型：** [CodecType](#enum-codectype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22