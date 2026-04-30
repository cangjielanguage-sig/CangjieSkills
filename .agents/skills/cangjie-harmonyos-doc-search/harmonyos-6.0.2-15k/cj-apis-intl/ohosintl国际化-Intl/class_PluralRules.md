## class PluralRules

```cangjie
public class PluralRules {
    public init()
    public init(locale: String, options!: ?PluralRulesOptions = None)
    public init(locale: Array<String>, options!: ?PluralRulesOptions = None)
}
```

**功能：** 创建单复数对象来计算数字的单复数类别。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 创建单复数对象来计算数字的单复数类别。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用系统locale创建PluralRules对象
let pluralRules = PluralRules()
```

### init(String, ?PluralRulesOptions)

```cangjie
public init(locale: String, options!: ?PluralRulesOptions = None)
```

**功能：** 创建单复数对象来计算数字的单复数类别。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|options|?[PluralRulesOptions](#struct-pluralrulesoptions)|否|None| **命名参数。** 创建单复数对象时设置的配置项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用zh-CN locale创建PluralRules对象，localeMatcher设置为lookup，type设置为cardinal
let p = PluralRulesOptions(localeMatcher: "lookup", ptype: "cardinal")
let pluralRules = PluralRules("zh-CN", options: p)
```

### init(Array\<String>, ?PluralRulesOptions)

```cangjie
public init(locale: Array<String>, options!: ?PluralRulesOptions = None)
```

**功能：** 创建单复数对象来计算数字的单复数类别。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|Array\<String>|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|options|?[PluralRulesOptions](#struct-pluralrulesoptions)|否|None| **命名参数。** 创建单复数对象时设置的配置项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用zh-CN locale创建PluralRules对象，localeMatcher设置为lookup，type设置为cardinal
let p = PluralRulesOptions(localeMatcher: "lookup", ptype: "cardinal")
let pluralRules = PluralRules(["zh-CN"], options: p)
```

### func select(Float64)

```cangjie
public func select(n: Float64): String
```

**功能：** 返回一个字符串表示该数字的单复数类别。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|n|Float64|是|-|待获取单复数类别的数字。|

**返回值：**

|类型|说明|
|:----|:----|
|String|单复数类别，取值包括："zero"，"one"，"two", "few", "many", "others"。不同取值代表的含义请参见[语言单复数规则](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html)。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用zh-Hans locale创建PluralRules对象
let zhPluralRules = PluralRules("zh-Hans")
// 计算zh-Hans locale中数字1对应的单复数类别
var plural = zhPluralRules.select(1.0) // plural = other
// 使用en-US locale创建PluralRules对象
let enPluralRules = PluralRules("en-US")
// 计算en-US locale中数字1对应的单复数类别
plural = enPluralRules.select(1.0) // plural = one
```