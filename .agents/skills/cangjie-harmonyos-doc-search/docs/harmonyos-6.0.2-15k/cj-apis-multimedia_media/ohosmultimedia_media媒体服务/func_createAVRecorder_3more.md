## func createAVRecorder()

```cangjie
public func createAVRecorder(): AVRecorder
```

**功能：** 创建音视频录制实例。

> **说明：**
>
> - 可创建的音视频录制实例不能超过2个。
> - 由于设备共用音频通路，一个设备仅能有一个实例进行音频录制。创建第二个实例录制音频时，将会因为音频通路冲突导致创建失败。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVRecorder](#class-avrecorder)|AVRecorder实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|

## func createAVTranscoder()

```cangjie
public func createAVTranscoder(): AVTranscoder
```

**功能：** 创建视频转码实例。

> **说明：**
>
> 可创建的视频转码实例不能超过2个。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[AVTranscoder](#class-avtranscoder)|AVTranscoder实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.BusinessException

try {
    let avTranscoder = createAVTranscoder()
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```

## func createAVScreenCaptureRecorder()

```cangjie
public func createAVScreenCaptureRecorder(): ?AVScreenCaptureRecorder
```

**功能：** 创建屏幕录制实例。重复创建AVScreenCaptureRecorder会抛异常，需要释放之后再创建。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|?[AVScreenCaptureRecorder](#class-avscreencapturerecorder)|返回AVScreenCaptureRecorder实例，失败时返回none。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.BusinessException

try {
    let recorder = createAVScreenCaptureRecorder()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```