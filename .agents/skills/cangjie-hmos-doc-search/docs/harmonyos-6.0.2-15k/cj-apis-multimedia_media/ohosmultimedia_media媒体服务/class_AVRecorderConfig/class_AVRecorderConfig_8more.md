## class AVRecorderConfig

```cangjie
public class AVRecorderConfig {
    public AVRecorderConfig(
        public var profile: AVRecorderProfile,
        public var url: String,
        public var audioSourceType!: ?AudioSourceType = None,
        public var videoSourceType!: ?VideoSourceType = None,
        public var fileGenerationMode!: ?FileGenerationMode = None,
        public var metadata!: ?AVMetadata = None,
        public var maxDuration!: ?Int32 = None
    )
}
```

**功能：** 表示音视频录制的参数设置。

通过audioSourceType和videoSourceType区分纯音频录制、纯视频录制或音视频录制。纯音频录制时，仅需要设置audioSourceType；纯视频录制时，仅需要设置videoSourceType；音视频录制时，audioSourceType和videoSourceType均需要设置。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### var audioSourceType

```cangjie
public var audioSourceType: ?AudioSourceType = None
```

**功能：** 选择录制的音频源类型。选择音频录制时必填。

**类型：** ?[AudioSourceType](#enum-audiosourcetype)

**读写能力：** 可读写

**起始版本：** 19

### var fileGenerationMode

```cangjie
public var fileGenerationMode: ?FileGenerationMode = None
```

**功能：** 创建媒体文件的模式，配合[on(AVRECORDER_PHOTO_ASSET_AVAILABLE)](#func-onavplayercallbacktype-onavplayerstatechangehandle)监听使用。

**类型：** ?[FileGenerationMode](#enum-filegenerationmode)

**读写能力：** 可读写

**起始版本：** 19

### var maxDuration

```cangjie
public var maxDuration: ?Int32 = None
```

**功能：** 设置录制的最大时长，单位为秒，有效值取值范围[1, 2^31-1]，无效输入会重置为最大值。录制到达设定时长后，录制会自动停止，并通过stateChange回调录制状态，[AVRecorderState](#enum-avrecorderstate) = STOPPED，[StateChangeReason](#enum-statechangereason) = BACKGROUND。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var metadata

```cangjie
public var metadata: ?AVMetadata = None
```

**功能：** 设置元数据信息。详情见[AVMetadata](#class-avmetadata)。

**类型：** ?[AVMetadata](#class-avmetadata)

**读写能力：** 可读写

**起始版本：** 19

### var profile

```cangjie
public var profile: AVRecorderProfile
```

**功能：** 录制的profile，必要参数。

**类型：** [AVRecorderProfile](#class-avrecorderprofile)

**读写能力：** 可读写

**起始版本：** 19

### var url

```cangjie
public var url: String
```

**功能：** 录制输出URL：fd://xx (fd number) 必要参数。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var videoSourceType

```cangjie
public var videoSourceType: ?VideoSourceType = None
```

**功能：** 选择录制的视频源类型。选择视频录制时必填。

**类型：** ?[VideoSourceType](#enum-videosourcetype)

**读写能力：** 可读写

**起始版本：** 19