## class EncoderInfo

```cangjie
public class EncoderInfo {
    public let mimeType: String
    public let `type`: String
    public let bitRate: Range
    public let frameRate: ?Range
    public let width: ?Range
    public let height: ?Range
    public let channels: ?Range
    public let sampleRate: ?Array<Int32>
}
```

**功能：** 编码器和规格参数。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### let \`type\`

```cangjie
public let `type`: String
```

**功能：** 编码器类型，audio表示音频编码器，video表示视频编码器。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let bitRate

```cangjie
public let bitRate: Range
```

**功能：** 比特率，包含该编码器的最大和最小值。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** [Range](#class-range)

**读写能力：** 只读

**起始版本：** 19

### let channels

```cangjie
public let channels: ?Range
```

**功能：** 音频采集声道数，包含声道数的最大和最小值，仅音频编码器拥有。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** ?[Range](#class-range)

**读写能力：** 只读

**起始版本：** 19

### let frameRate

```cangjie
public let frameRate: ?Range
```

**功能：** 视频帧率，包含帧率的最大和最小值，仅视频编码器拥有。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** ?[Range](#class-range)

**读写能力：** 只读

**起始版本：** 19

### let height

```cangjie
public let height: ?Range
```

**功能：** 视频帧的高度，包含高度的最大和最小值，仅视频编码器拥有。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** ?[Range](#class-range)

**读写能力：** 只读

**起始版本：** 19

### let mimeType

```cangjie
public let mimeType: String
```

**功能：** 编码器MIME类型名称。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let sampleRate

```cangjie
public let sampleRate: ?Array<Int32>
```

**功能：** 音频采样率，包含所有可以使用的音频采样率值，仅音频编码器拥有。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** ?Array\<Int32>

**读写能力：** 只读

**起始版本：** 19

### let width

```cangjie
public let width: ?Range
```

**功能：** 视频帧的宽度，包含宽度的最大和最小值，仅视频编码器拥有。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** ?[Range](#class-range)

**读写能力：** 只读

**起始版本：** 19