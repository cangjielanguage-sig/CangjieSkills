## class AudioRendererChangeInfo

```cangjie
public class AudioRendererChangeInfo {}
```

**功能：** 描述音频渲染器更改信息。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop deviceDescriptors

```cangjie
public prop deviceDescriptors: AudioDeviceDescriptors
```

**功能：** 音频设备描述。

**类型：** [AudioDeviceDescriptors](#type-audiodevicedescriptors)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop rendererInfo

```cangjie
public prop rendererInfo: AudioRendererInfo
```

**功能：** 音频渲染器信息。

**类型：** [AudioRendererInfo](#class-audiorendererinfo)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop streamId

```cangjie
public prop streamId: Int32
```

**功能：** 音频流唯一id。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

## class AudioRendererInfo

```cangjie
public class AudioRendererInfo {
    public AudioRendererInfo(usage: StreamUsage, rendererFlags: Int32)
}
```

**功能：** 音频渲染器信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop rendererFlags

```cangjie
public mut prop rendererFlags: Int32
```

**功能：** 音频渲染器标志。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop usage

```cangjie
public mut prop usage: StreamUsage
```

**功能：** 音频流使用类型。

**类型：** [StreamUsage](#enum-streamusage)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### AudioRendererInfo(StreamUsage, Int32)

```cangjie
public AudioRendererInfo(usage: StreamUsage, rendererFlags: Int32)
```

**功能：** 构造[AudioRendererInfo](#class-audiorendererinfo)。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|usage|[StreamUsage](#enum-streamusage)|是|-|音频流使用类型。|
|rendererFlags|Int32|是|-|音频渲染器标志。0代表音频渲染器。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

let rendererInfo = AudioRendererInfo(StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
```