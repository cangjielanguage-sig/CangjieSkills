## class AVRecorder

```cangjie
public class AVRecorder {}
```

**功能：** 音视频录制管理类，用于音视频媒体录制。在调用AVRecorder的方法前，需要先通过[createAVRecorder()](#func-createavrecorder)构建一个AVRecorder实例。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### prop state

```cangjie
public prop state: AVRecorderState
```

**功能：** 音视频录制的状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** [AVRecorderState](#enum-avrecorderstate)

**读写能力：** 只读

**起始版本：** 19

### func getAVRecorderConfig()

```cangjie
public func getAVRecorderConfig(): AVRecorderConfig
```

**功能：** 获取实时的配置参数。

只能在[prepare()](#func-prepare)接口调用后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVRecorderConfig](#class-avrecorderconfig)|实时配置的参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operate not permit.|
  |5400103|IO error.|
  |5400105|Service died.|

### func getAudioCapturerMaxAmplitude()

```cangjie
public func getAudioCapturerMaxAmplitude(): Int32
```

**功能：** 获取当前音频最大振幅参数。

在[prepare()](#func-prepare)成功触发后，才能调用此方法。在[stop()](#func-stop)成功触发后，调用此方法会报错。

调用接口时，获取到的返回值是上一次获取最大振幅的时刻到当前这段区间内的音频最大振幅。即，如果在1s的时刻获取了一次最大振幅，在2s时再获取到的最大振幅时1-2s这个区间里面的最大值。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前音频最大振幅。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|
  |5400105|Service died.|

### func getAvailableEncoder()

```cangjie
public func getAvailableEncoder(): Array<EncoderInfo>
```

**功能：** 获取可用的编码器参数。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[EncoderInfo](#class-encoderinfo)>|编码器参数的数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*

let avRecorder = createAVRecorder()
let encoderInfos = avRecorder.getAvailableEncoder()
```