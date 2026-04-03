## class AudioCapturerOptions

```cangjie
public class AudioCapturerOptions {
    public AudioCapturerOptions(captureInfo: AudioCapturerInfo, streamInfo: AudioStreamInfo)
}
```

**功能：** 音频采集器选项信息。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### prop capturerInfo

```cangjie
public mut prop capturerInfo: AudioCapturerInfo
```

**功能：** 表示音频流信息。

**类型：** [AudioCapturerInfo](#class-audiocapturerinfo)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### prop streamInfo

```cangjie
public mut prop streamInfo: AudioStreamInfo
```

**功能：** 表示采集器信息。

**类型：** [AudioStreamInfo](#class-audiostreaminfo)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### AudioCapturerOptions(AudioCapturerInfo, AudioStreamInfo)

```cangjie
public AudioCapturerOptions(captureInfo: AudioCapturerInfo, streamInfo: AudioStreamInfo)
```

**功能：** 创建[AudioCapturerOptions](#class-audiocaptureroptions)实例。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|captureInfo|[AudioCapturerInfo](#class-audiocapturerinfo)|是|-|表示音频流信息。|
|streamInfo|[AudioStreamInfo](#class-audiostreaminfo)|是|-|表示采集器信息。|