# ohos.multimedia.media（媒体服务）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

media模块为开发者提供一套简单且易于理解的接口，使得开发者能够方便接入系统并使用系统的媒体资源。

媒体子系统包含了音视频相关媒体业务，目前主要提供获取视频缩略图（[AVImageGenerator](#class-avimagegenerator)）的功能。

## 导入模块

```cangjie
import kit.MediaKit.*
```

## 权限列表

ohos.permission.MICROPHONE

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。
- 获取当前应用沙箱所在路径可通过UIAbilityContext.[filesDir](../AbilityKit/cj-apis-app-ability-ui_ability.md#prop-filesdir)获取。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func createAVImageGenerator()

```cangjie
public func createAVImageGenerator(): AVImageGenerator
```

**功能：** 创建AVImageGenerator实例。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[AVImageGenerator](#class-avimagegenerator)|返回AVImageGenerator实例。|

**异常：**

- BusinessException：对应错误码如下表，详见[Media错误码](./cj-errorcode-multimedia-media.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 5400101 | No memory. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    let generator = createAVImageGenerator()
} catch (e: BusinessException) {
    Hilog.error(0, "AppLogCj", e.message)
}
```