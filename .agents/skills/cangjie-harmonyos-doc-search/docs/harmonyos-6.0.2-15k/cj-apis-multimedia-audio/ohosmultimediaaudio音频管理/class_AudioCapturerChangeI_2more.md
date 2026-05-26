## class AudioCapturerChangeInfo

```cangjie
public class AudioCapturerChangeInfo {}
```

**功能：** 描述音频采集器更改信息。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### prop capturerInfo

```cangjie
public prop capturerInfo: AudioCapturerInfo
```

**功能：** 音频采集器信息。

**类型：** [AudioCapturerInfo](#class-audiocapturerinfo)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### prop deviceDescriptors

```cangjie
public prop deviceDescriptors: AudioDeviceDescriptors
```

**功能：** 音频设备描述。

**类型：** [AudioDeviceDescriptors](#type-audiodevicedescriptors)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### prop muted

```cangjie
public prop muted: ?Bool
```

**功能：** 音频采集器静音状态。true表示音频采集器为静音状态，false表示音频采集器为非静音状态。

**类型：** ?Bool

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### prop streamId

```cangjie
public prop streamId: Int32
```

**功能：** 音频流唯一id。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

## class AudioCapturerInfo

```cangjie
public class AudioCapturerInfo {
    public AudioCapturerInfo(source: SourceType, capturerFlags: Int32)
}
```

**功能：** 描述音频采集器信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop capturerFlags

```cangjie
public mut prop capturerFlags: Int32
```

**功能：** 音频采集器标志。0代表音频采集器。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop source

```cangjie
public mut prop source: SourceType
```

**功能：** 音源类型。

**类型：** [SourceType](#enum-sourcetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### AudioCapturerInfo(SourceType, Int32)

```cangjie
public AudioCapturerInfo(source: SourceType, capturerFlags: Int32)
```

**功能：** 创建[AudioCapturerInfo](#class-audiocapturerinfo)实例。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[SourceType](#enum-sourcetype)|是|-|音源类型。|
|capturerFlags|Int32|是|-|音频采集器标志。0代表音频采集器。|