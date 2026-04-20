# ohos.multimedia_media（媒体服务）

媒体服务模块为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源。

媒体子系统包含了音视频相关媒体业务，提供以下常用功能：

- 音视频播放（[AVPlayer](#class-avplayer)）

- 音视频录制（[AVRecorder](#class-avrecorder)）

- 获取音视频元数据（[AVMetadataExtractor](#class-avmetadataextractor)）

- 获取视频缩略图（[AVImageGenerator](#class-avimagegenerator)）

## 导入模块

```cangjie
import kit.MediaKit.*
```

## 权限列表

ohos.permission.MICROPHONE

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createAVImageGenerator()

```cangjie
public func createAVImageGenerator(): AVImageGenerator
```

**功能：** 创建AVImageGenerator实例。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVImageGenerator](#class-avimagegenerator)|视频缩略图获取类。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

try {
    let generator = createAVImageGenerator()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

## func createAVMetadataExtractor()

```cangjie
public func createAVMetadataExtractor(): AVMetadataExtractor
```

**功能：** 创建AVMetadataExtractor实例。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVMetadataExtractor](#class-avmetadataextractor)|元数据获取类。|

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
    let extractor = createAVMetadataExtractor()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

## func createAVPlayer()

```cangjie
public func createAVPlayer(): AVPlayer
```

**功能：** 创建音视频播放器实例。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVPlayer](#class-avplayer)|音视频播放器实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

try {
    let player = createAVPlayer()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```