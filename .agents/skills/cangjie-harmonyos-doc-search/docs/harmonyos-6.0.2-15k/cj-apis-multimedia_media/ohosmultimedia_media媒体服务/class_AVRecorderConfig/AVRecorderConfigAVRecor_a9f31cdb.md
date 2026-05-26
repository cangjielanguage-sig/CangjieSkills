### AVRecorderConfig(AVRecorderProfile, String, ?AudioSourceType, ?VideoSourceType, ?FileGenerationMode, ?AVMetadata, ?Int32)

```cangjie
public AVRecorderConfig(
    public var profile: AVRecorderProfile,
    public var url: String,
    public var audioSourceType!: ?AudioSourceType = None,
    public var videoSourceType!: ?VideoSourceType = None,
    public var fileGenerationMode!: ?FileGenerationMode = None,
    public var metadata!: ?AVMetadata = None,
    public var maxDuration!: ?Int32 = None
)
```

**功能：** 构造AVRecorderConfig实例。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|profile|[AVRecorderProfile](#class-avrecorderprofile)|是|-|录制的profile，必要参数。|
|url|String|是|-|录制输出URL：fd://xx (fd number)，必要参数。|
|audioSourceType|?[AudioSourceType](#enum-audiosourcetype)|否|None| **命名参数。** 选择录制的音频源类型。选择音频录制时必填。|
|videoSourceType|?[VideoSourceType](#enum-videosourcetype)|否|None| **命名参数。** 选择录制的视频源类型。选择视频录制时必填。|
|fileGenerationMode|?[FileGenerationMode](#enum-filegenerationmode)|否|None| **命名参数。** 创建媒体文件的模式，配合[on(AVRECORDER_PHOTO_ASSET_AVAILABLE)](#func-onavrecordercallbacktype-callback1argumentphotoasset)监听使用。|
|metadata|?[AVMetadata](#class-avmetadata)|否|None| **命名参数。** 设置元数据信息。|
|maxDuration|?Int32|否|None| **命名参数。** 设置录制的最大时长，单位为秒，有效值取值范围[1, 2^31-1]，无效输入会重置为最大值。|