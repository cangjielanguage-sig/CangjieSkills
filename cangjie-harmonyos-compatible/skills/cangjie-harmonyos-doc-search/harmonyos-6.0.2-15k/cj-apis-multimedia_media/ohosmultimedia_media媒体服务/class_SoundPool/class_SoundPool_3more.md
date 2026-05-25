## class SoundPool

```cangjie
public class SoundPool {}
```

**功能：** 音频池提供了系统声音的加载、播放、音量设置、循环设置、停止播放、资源卸载等功能, 在调用SoundPool的接口前，需要先通过[createSoundPool](#func-createsoundpoolint32-audiorendererinfo)创建实例。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

### func load(String)

```cangjie
public func load(uri: String): Int32
```

**功能：** 加载音频资源。获取资源ID，入参可手动传入资源信息或通过读取应用内置资源自动获取。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|音频文件的加载路径描述，一般以"fd://"开头的文件描述。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回资源的id，有效值大于0。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|
  |5400103|I/O error.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.CoreFileKit.*
import kit.AudioKit.*

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)

if (let Some(v) <- soundpool) {
    let file = FileFs.open("/data/storage/el2/base/support_fast_01.mp3", mode: READ_ONLY.mode)
    var uri: String = ""
    uri = "fd://" + file
        .fd
        .toString()
    let soundId = v.load(uri)
}
```

### func load(Int32, Int64, Int64)

```cangjie
public func load(fd: Int32, offset: Int64, length: Int64): Int32
```

**功能：** 加载音频资源。入参可手动传入资源信息或通过读取应用内置资源自动获取。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|资源句柄，通过过[resourceManager.getRawFd](../LocalizationKit/cj-apis-resource_manager.md#func-getrawfdstring)获取。|
|offset|Int64|是|-|资源偏移量，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。|
|length|Int64|是|-|资源长度，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回资源ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|
  |5400103|I/O error.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.AudioKit.*

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)

if (let Some(v) <- soundpool) {
    let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
    let resMgr = abilityContext.resourceManager
    let rawfd = resMgr.getRawFd("01.mp3")
    let id1 = v.load(rawfd.fd, rawfd.offset, rawfd.length)
}
```