# ohos.color_manager（色彩管理）

本模块提供管理抽象化色域对象的一些基础能力，包括色域对象的创建与色域基础属性的获取等。

## 导入模块

```cangjie
import kit.ArkGraphics2D.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func create(ColorSpace)

```cangjie
public func create(colorSpaceName: ColorSpace): ColorSpaceManager
```

**功能：** 创建标准色域对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorSpaceName|[ColorSpace](#enum-colorspace)|是|-|标准色域类型枚举值。UNKNOWN与CUSTOM不可用于直接创建色域对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpaceManager](#class-colorspacemanager)|返回当前创建的色域对象实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

let colorSpaceManager = create(ColorSpace.SRGB)
```

## func create(ColorSpacePrimaries, Float32)

```cangjie
public func create(primaries: ColorSpacePrimaries, gamma: Float32): ColorSpaceManager
```

**功能：** 创建用户自定义色域对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|primaries|[ColorSpacePrimaries](#struct-colorspaceprimaries)|是|-|色域标准三原色。|
|gamma|Float32|是|-|色域gamma值。|

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpaceManager](#class-colorspacemanager)|返回当前创建的色域对象实例。色域类型定义为[ColorSpace.CUSTOM](#custom)。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

let primaries = ColorSpacePrimaries(
    redX: 0.1,
    redY: 0.1,
    greenX: 0.2,
    greenY: 0.2,
    blueX: 0.3,
    blueY: 0.3,
    whitePointX: 0.4,
    whitePointY: 0.4
)
let gamma = 2.2f32
let colorSpaceManager = create(primaries, gamma)
```