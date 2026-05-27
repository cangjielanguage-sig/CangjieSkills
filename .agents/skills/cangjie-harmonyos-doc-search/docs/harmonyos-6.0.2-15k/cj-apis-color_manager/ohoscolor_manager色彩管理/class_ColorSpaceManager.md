## class ColorSpaceManager

```cangjie
public class ColorSpaceManager {}
```

**功能：** 当前色域对象实例。

> **说明：**
>
> 先使用[create()](#func-createcolorspace)获取到ColorSpaceManager实例，再通过此实例调用下述对应方法。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

### func getColorSpaceName()

```cangjie
public func getColorSpaceName(): ColorSpace
```

**功能：** 获取色域类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpace](#enum-colorspace)|返回色域类型枚举值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[色彩管理错误码](../../errorcodes/cj-errorcode-colorspace-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |18600001|Parameter value is abnormal.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

let colorSpaceManagerInstance = create(ColorSpace.SRGB)
let colorSpace: ColorSpace = colorSpaceManagerInstance.getColorSpaceName()
```

### func getGamma()

```cangjie
public func getGamma(): Float32
```

**功能：** 获取色域gamma值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Float32|返回色域gamma值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[色彩管理错误码](../../errorcodes/cj-errorcode-colorspace-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |18600001|The parameter value is abnormal.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

let colorSpaceManagerInstance = create(SRGB)
let colorSpace = colorSpaceManagerInstance.getGamma()
```

### func getWhitePoint()

```cangjie
public func getWhitePoint(): Array<Float32>
```

**功能：** 获取色域白点值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|返回色域白点值[x, y]。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[色彩管理错误码](../../errorcodes/cj-errorcode-colorspace-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |18600001|The parameter value is abnormal.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

let colorSpaceManagerInstance = create(SRGB)
let colorSpace = colorSpaceManagerInstance.getWhitePoint()
```