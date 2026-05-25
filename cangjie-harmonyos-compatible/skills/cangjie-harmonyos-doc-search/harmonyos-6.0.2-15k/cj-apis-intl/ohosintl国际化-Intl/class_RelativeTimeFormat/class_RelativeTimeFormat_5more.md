## class RelativeTimeFormat

```cangjie
public class RelativeTimeFormat {
    public init()
    public init(locale: String, options!: ?RelativeTimeFormatInputOptions = None)
    public init(locale: Array<String>, options!: ?RelativeTimeFormatInputOptions = None)
}
```

**功能：** 相对时间格式化。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 创建相对时间格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用系统locale创建RelativeTimeFormat对象
let relativetimefmt = RelativeTimeFormat()
```

### init(String, ?RelativeTimeFormatInputOptions)

```cangjie
public init(locale: String, options!: ?RelativeTimeFormatInputOptions = None)
```

**功能：** 创建相对时间格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|options|?[RelativeTimeFormatInputOptions](#struct-relativetimeformatinputoptions)|否|None| **命名参数。** 创建相对时间格式化对象时可配置的选项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用zh-CN locale创建RelativeTimeFormat对象，localeMatcher设置为lookup，numeric设置为always，style设置为long
let r = RelativeTimeFormatInputOptions(localeMatcher: "lookup", numeric: "always", style: "long")
let relativetimefmt = RelativeTimeFormat("zh-CN", options: r)
```

### init(Array\<String>, ?RelativeTimeFormatInputOptions)

```cangjie
public init(locale: Array<String>, options!: ?RelativeTimeFormatInputOptions = None)
```

**功能：** 创建相对时间格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|Array\<String>|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|options|?[RelativeTimeFormatInputOptions](#struct-relativetimeformatinputoptions)|否|None| **命名参数。** 创建相对时间格式化对象时可配置的选项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用en-GB locale创建RelativeTimeFormat对象
let r = RelativeTimeFormatInputOptions(style: "short")
let relativetimefmt = RelativeTimeFormat(["en-GB"], options: r)
```

### func format(Float64, String)

```cangjie
public func format(value: Float64, unit: String): String
```

**功能：** 依据locale和格式化选项，对value和unit进行格式化。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|相对时间格式化的数值。|
|unit|String|是|-|相对时间格式化的单位，取值包括："year", "quarter", "month", "week", "day", "hour", "minute", "second"。|

**返回值：**

|类型|说明|
|:----|:----|
|String|格式化后的相对时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用zh-CN locale创建RelativeTimeFormat对象
let relativetimefmt = RelativeTimeFormat("zh-CN")
// 计算zh-CN locale中数字3，单位quarter的本地化表示
let formatResult = relativetimefmt.format(3.0, "quarter") // formatResult = "3个季度后"
```