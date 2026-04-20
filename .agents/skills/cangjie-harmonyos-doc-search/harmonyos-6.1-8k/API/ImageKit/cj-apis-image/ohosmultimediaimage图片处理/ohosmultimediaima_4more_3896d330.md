# ohos.multimedia.image（图片处理）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

image模块提供图片处理效果，包括通过属性创建PixelMap、读取图像像素数据、读取区域内的图片数据等。

## 导入模块

```cangjie
import kit.ImageKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。
- 运行示例代码时，请先通过 [createImageSource](#func-createimagesourcestring-sourceoptions) 构建正确的图片源，支持从raw数组、Uri、文件描述符等构建图片源。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func createImagePacker()

```cangjie
public func createImagePacker(): ImagePacker
```

**功能：** 创建ImagePacker实例。

> **说明：**
>
> 由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用[release](#func-release-1)方法及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ImagePacker](#class-imagepacker)|返回ImagePacker实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let imagePacker : ImagePacker = createImagePacker()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```