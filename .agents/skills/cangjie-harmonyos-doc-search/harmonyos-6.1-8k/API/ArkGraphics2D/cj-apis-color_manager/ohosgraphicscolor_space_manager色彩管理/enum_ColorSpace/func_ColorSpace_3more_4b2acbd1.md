### func !=(ColorSpace)

```cangjie
public operator func !=(other: ColorSpace): Bool
```

**功能：** 与另一个 `ColorSpace` 枚举值进行不等比较。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorSpace](#enum-colorspace)|是|-|用于比较的另一个色域类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若不相等返回 `true`，否则返回 `false`。|

### func ==(ColorSpace)

```cangjie
public operator func ==(other: ColorSpace): Bool
```

**功能：** 与另一个 `ColorSpace` 枚举值进行相等比较。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorSpace](#enum-colorspace)|是|-|用于比较的另一个色域类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若相等返回 `true`，否则返回 `false`。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将[ColorSpace](#enum-colorspace)枚举值转换为字符串。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|[ColorSpace](#enum-colorspace)枚举值对应的字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkGraphics2D.*

let value: String = ColorSpace.DisplayP3.toString()
```