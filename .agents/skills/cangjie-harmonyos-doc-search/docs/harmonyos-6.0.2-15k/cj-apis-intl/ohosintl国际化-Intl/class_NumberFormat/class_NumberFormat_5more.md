## class NumberFormat

```cangjie
public class NumberFormat {
    public init()
    public init(locale: String, options!: ?NumberOptions = None)
    public init(locale: Array<String>, options!: ?NumberOptions = None)
}
```

**功能：** 数字格式化。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 创建数字格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用系统当前locale创建NumberFormat对象
let numfmt = NumberFormat()
```

### init(String, ?NumberOptions)

```cangjie
public init(locale: String, options!: ?NumberOptions = None)
```

**功能：** 创建数字格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|options|?[NumberOptions](#struct-numberoptions)|否|None| **命名参数。** 创建数字格式化对象时可设置的配置项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用en-GB locale创建NumberFormat对象，style设置为decimal，notation设置为scientific
let n = NumberOptions(style: 'decimal', notation: "scientific")
let numfmt = NumberFormat("zh", options: n)
```

### init(Array\<String>, ?NumberOptions)

```cangjie
public init(locale: Array<String>, options!: ?NumberOptions = None)
```

**功能：** 创建数字格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|Array\<String>|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|options|?[NumberOptions](#struct-numberoptions)|否|None| **命名参数。** 创建数字格式化对象时可设置的配置项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用en-GB locale创建NumberFormat对象，style设置为decimal，notation设置为scientific
let n = NumberOptions(style: 'decimal', notation: "scientific")
let numfmt = NumberFormat(["en-GB", "zh"], options: n)
```

### func format(Float64)

```cangjie
public func format(number: Float64): String
```

**功能：** 格式化数字字符串。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|number|Float64|是|-|数字对象。|

**返回值：**

|类型|说明|
|:----|:----|
|String|格式化后的数字字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用["en-GB", "zh"] locale列表创建NumberFormat对象，因为en-GB为合法LocaleID，因此使用en-GB创建NumberFormat对象
let n = NumberOptions(style: "decimal", notation: "scientific")
let numfmt = NumberFormat(["en-GB", "zh"], options: n)
let formattedNumber = numfmt.format(1223.0) // formattedNumber = 1.223E3
```