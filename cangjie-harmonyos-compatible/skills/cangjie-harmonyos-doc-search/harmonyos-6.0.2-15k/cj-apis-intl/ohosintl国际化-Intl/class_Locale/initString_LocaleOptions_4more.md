### init(String, ?LocaleOptions)

```cangjie
public init(locale: String, options!: ?LocaleOptions = None)
```

**功能：** 创建区域对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。locale可填写组成部分中的一个或多个。|
|options|?[LocaleOptions](#struct-localeoptions)|否|None| **命名参数。** 创建区域对象的选项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 创建"zh-CN" Locale对象
let locale = Locale("zh-CN")
let localeID = locale.toString() // localeID = "zh-CN"
```

### func maximize()

```cangjie
public func maximize(): Locale
```

**功能：** 最大化区域信息，可补齐Locale中缺少脚本、国家或地区信息。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Locale](#class-locale)|补充完脚本、国家或地区信息后的区域对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 创建"zh" Locale对象
var locale = Locale("zh")

// 补齐Locale对象的脚本和地区
var maximizedLocale = locale.maximize()
var localeID = maximizedLocale.toString() // localeID = "zh-Hans-CN"

// 创建"en-US" Locale对象
locale = Locale("en-US")

// 补齐Locale对象的脚本
maximizedLocale = locale.maximize()
localeID = maximizedLocale.toString() // localeID = "en-Latn-US"
```

### func minimize()

```cangjie
public func minimize(): Locale
```

**功能：** 最小化区域信息，可删除Locale中的脚本、国家或地区信息。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Locale](#class-locale)|删除完脚本、国家或地区信息后的区域对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 创建"zh-Hans-CN" Locale对象
var locale = Locale("zh-Hans-CN")

// 去除Locale对象的脚本和地区
var minimizedLocale = locale.minimize()
var localeID = minimizedLocale.toString() // localeID = "zh"

// 创建"en-US" Locale对象
locale = Locale("en-US")

// 去除Locale对象的地区
minimizedLocale = locale.minimize()
localeID = minimizedLocale.toString() // localeID = "en"
```

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取区域对象的字符串。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|区域对象的字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 创建"en-GB" Locale对象
let locale = Locale("en-GB")
let localeID = locale.toString() // localeID = "en-GB"
```