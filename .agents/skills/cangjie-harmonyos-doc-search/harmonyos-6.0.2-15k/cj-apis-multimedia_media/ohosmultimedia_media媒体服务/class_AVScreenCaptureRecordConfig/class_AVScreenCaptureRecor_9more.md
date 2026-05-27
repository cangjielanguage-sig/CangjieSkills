## class AVScreenCaptureRecordConfig

```cangjie
public class AVScreenCaptureRecordConfig {
    public AVScreenCaptureRecordConfig(
        public var fd: Int32,
        public var frameWidth: Int32,
        public var frameHeight: Int32,
        public var videoBitrate!: Int32 = 10000000,
        public var audioSampleRate!: Int32 = 48000,
        public var audioChannelCount!: Int32 = 2,
        public var audioBitrate!: Int32 = 96000,
        public var preset!: AVScreenCaptureRecordPreset = AVScreenCaptureRecordPreset.SCREEN_RECORD_PRESET_H264_AAC_MP4
    )
}
```

**功能：** 录屏参数配置。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### var audioBitrate

```cangjie
public var audioBitrate: Int32 = 96000
```

**功能：** 录屏的音频比特率，内录的系统音和外录的麦克风都是用此比特率，默认96000。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var audioChannelCount

```cangjie
public var audioChannelCount: Int32 = 2
```

**功能：** 录屏的音频通道数，内录的系统音和外录的麦克风都是用此通道数，默认2声道，仅支持设置1或2声道。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var audioSampleRate

```cangjie
public var audioSampleRate: Int32 = 48000
```

**功能：** 录屏的音频采样率，内录的系统音和外录的麦克风都是用此采样率，默认48000，仅支持设置48000或16000。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var fd

```cangjie
public var fd: Int32
```

**功能：** 录制输出的文件fd。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var frameHeight

```cangjie
public var frameHeight: Int32
```

**功能：** 录屏的视频高度，默认屏幕高度，根据不同屏幕默认值不同，单位px。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var frameWidth

```cangjie
public var frameWidth: Int32
```

**功能：** 录屏的视频宽度，默认屏幕宽度，根据不同屏幕默认值不同，单位px。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var preset

```cangjie
public var preset: AVScreenCaptureRecordPreset = AVScreenCaptureRecordPreset.SCREEN_RECORD_PRESET_H264_AAC_MP4
```

**功能：** 录屏使用的编码和封装格式，默认SCREEN_RECORD_PRESET_H264_AAC_MP4格式。

**类型：** [AVScreenCaptureRecordPreset](#enum-avscreencapturerecordpreset)

**读写能力：** 可读写

**起始版本：** 19

### var videoBitrate

```cangjie
public var videoBitrate: Int32 = 10000000
```

**功能：** 录屏的视频比特率，默认10000000。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19