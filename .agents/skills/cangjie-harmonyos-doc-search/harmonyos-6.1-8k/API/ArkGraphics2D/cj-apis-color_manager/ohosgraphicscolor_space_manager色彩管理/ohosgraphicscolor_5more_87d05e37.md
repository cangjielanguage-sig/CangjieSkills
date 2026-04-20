# ohos.graphics.color_space_manager（色彩管理）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

color_space_manager模块提供管理抽象化色域对象的一些基础能力，包括色域对象的创建与色域基础属性的获取等。

## 导入模块

```cangjie
import kit.ArkGraphics2D.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func create(ColorSpace)

```cangjie
public func create(colorSpaceType: ColorSpace): ColorSpaceManager
```

**功能：** 创建标准色域对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorSpaceType|[ColorSpace](#enum-colorspace)|是|-|标准色域类型枚举值。Unknown与Custom不可用于直接创建色域对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpaceManager](#class-colorspacemanager)|返回当前创建的色域对象实例。|

**异常：**

- BusinessException：对应错误码如下表，详见[色彩管理错误码](./cj-errorcode-colorspace-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 18600001 | The parameter value is abnormal. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkGraphics2D.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let colorSpaceManager = create(ColorSpace.Srgb)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func create(ColorSpacePrimaries, Float32)

```cangjie
public func create(primaries: ColorSpacePrimaries, gamma: Float32): ColorSpaceManager
```

**功能：** 创建用户自定义色域对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|primaries|[ColorSpacePrimaries](#class-colorspaceprimaries)|是|-|色域标准三原色。|
|gamma|Float32|是|-|色域gamma值，取值为大于0的浮点数。|

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpaceManager](#class-colorspacemanager)|返回当前创建的色域对象实例。<br>色域类型定义为[ColorSpace](#enum-colorspace)枚举值`CUSTOM`。|

**异常：**

- BusinessException：对应错误码如下表，详见[色彩管理错误码](./cj-errorcode-colorspace-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 18600001 | The parameter value is abnormal. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkGraphics2D.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let primaries = ColorSpacePrimaries(
        0.1,
        0.1,
        0.2,
        0.2,
        0.3,
        0.3,
        0.4,
        0.4
    )
    let gamma = 2.2f32
    let colorSpaceManager = create(primaries, gamma)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```