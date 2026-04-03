## class ColorSpaceManager

```cangjie
public class ColorSpaceManager {}
```

**功能：** 当前色域对象实例。

下列API示例中都需先使用[create()](#func-createcolorspace)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

### func getColorSpaceType()

```cangjie
public func getColorSpaceType(): ColorSpace
```

**功能：** 获取色域类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpace](#enum-colorspace)|返回色域类型枚举值。|

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
    let colorSpaceManagerInstance = create(ColorSpace.Srgb)
    let colorSpace: ColorSpace = colorSpaceManagerInstance.getColorSpaceType()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getGamma()

```cangjie
public func getGamma(): Float32
```

**功能：** 获取色域gamma值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Float32|返回色域gamma值。|

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
    let colorSpaceManagerInstance = create(ColorSpace.Srgb)
    let colorSpace = colorSpaceManagerInstance.getGamma()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getWhitePoint()

```cangjie
public func getWhitePoint(): Array<Float32>
```

**功能：** 获取色域白点值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|返回色域白点值[x, y]。|

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
    let colorSpaceManagerInstance = create(ColorSpace.Srgb)
    let colorSpace = colorSpaceManagerInstance.getWhitePoint()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```