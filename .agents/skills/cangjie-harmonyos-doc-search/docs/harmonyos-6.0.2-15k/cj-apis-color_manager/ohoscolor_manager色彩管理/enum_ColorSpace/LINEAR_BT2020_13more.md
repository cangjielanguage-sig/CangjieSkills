### LINEAR_BT2020

```cangjie
LINEAR_BT2020
```

**功能：** RGB色域为BT2020类型；转换函数为Linear类型。

**起始版本：** 19

### LINEAR_BT709

```cangjie
LINEAR_BT709
```

**功能：** 与LINEAR_SRGB相同；RGB色域为BT709类型；转换函数为Linear类型。

**起始版本：** 19

### LINEAR_P3

```cangjie
LINEAR_P3
```

**功能：** RGB色域为Display P3类型；转换函数为Linear类型。

**起始版本：** 19

### LINEAR_SRGB

```cangjie
LINEAR_SRGB
```

**功能：** RGB色域为SRGB类型；转换函数为Linear类型。

**起始版本：** 19

### P3_HLG

```cangjie
P3_HLG
```

**功能：** RGB色域为Display P3类型；转换函数为HLG类型；编码范围为Full类型。

**起始版本：** 19

### P3_HLG_LIMIT

```cangjie
P3_HLG_LIMIT
```

**功能：** RGB色域为Display P3类型；转换函数为HLG类型；编码范围为Limit类型。

**起始版本：** 19

### P3_PQ

```cangjie
P3_PQ
```

**功能：** RGB色域为Display P3类型；转换函数为PQ类型；编码范围为Full类型。

**起始版本：** 19

### P3_PQ_LIMIT

```cangjie
P3_PQ_LIMIT
```

**功能：** RGB色域为Display P3类型；转换函数为PQ类型；编码范围为Limit类型。

**起始版本：** 19

### SRGB

```cangjie
SRGB
```

**功能：** RGB色域为SRGB类型；转换函数为SRGB类型；编码范围为Full类型；系统默认色域类型。

**起始版本：** 12

### SRGB_LIMIT

```cangjie
SRGB_LIMIT
```

**功能：** RGB色域为SRGB类型。转换函数为SRGB类型。编码范围为Limit类型。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知的色域类型。

**起始版本：** 12

### static func parse(UInt32)

```cangjie
public static func parse(cs: UInt32): ColorSpace
```

**功能：** 将UInt32类型值转换为[ColorSpace](#enum-colorspace)枚举值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cs|UInt32|是|-|[ColorSpace](#enum-colorspace)枚举值对应的整型数。|

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpace](#enum-colorspace)|[ColorSpace](#enum-colorspace)枚举值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

let value: ColorSpace = ColorSpace.parse(1)
```

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将[ColorSpace](#enum-colorspace)枚举值转换为字符串。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|[ColorSpace](#enum-colorspace)枚举值对应的字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*

let value: String = ColorSpace.DISPLAY_P3.toString()
```