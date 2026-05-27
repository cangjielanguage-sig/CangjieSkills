### AVScreenCaptureRecordConfig(Int32, Int32, Int32, Int32, Int32, Int32, Int32, AVScreenCaptureRecordPreset)

```cangjie
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
```

**功能：** 录屏参数配置。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|录制输出的文件fd。|
|frameWidth|Int32|是|-|录屏的视频宽度，默认屏幕宽度，根据不同屏幕默认值不同，单位px。|
|frameHeight|Int32|是|-|录屏的视频高度，默认屏幕高度，根据不同屏幕默认值不同，单位px。|
|videoBitrate|Int32|否|10000000| **命名参数。** 录屏的视频比特率，默认10000000。|
|audioSampleRate|Int32|否|48000| **命名参数。** 录屏的音频采样率，内录的系统音和外录的麦克风都是用此采样率，默认48000，仅支持设置48000或16000。|
|audioChannelCount|Int32|否|2| **命名参数。** 录屏的音频通道数，内录的系统音和外录的麦克风都是用此通道数，默认2声道，仅支持设置1或2声道。|
|audioBitrate|Int32|否|96000| **命名参数。** 录屏的音频比特率，内录的系统音和外录的麦克风都是用此比特率，默认96000。|
|preset|[AVScreenCaptureRecordPreset](#enum-avscreencapturerecordpreset)|否|AVScreenCaptureRecordPreset.SCREEN_RECORD_PRESET_H264_AAC_MP4| **命名参数。** 录屏使用的编码和封装格式，默认SCREEN_RECORD_PRESET_H264_AAC_MP4格式。|