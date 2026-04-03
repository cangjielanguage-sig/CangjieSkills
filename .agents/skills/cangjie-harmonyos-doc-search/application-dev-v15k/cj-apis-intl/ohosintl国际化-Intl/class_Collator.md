## class Collator

```cangjie
public class Collator {
    public init()
    public init(locale: String, options!: ?CollatorOptions = None)
    public init(locale: Array<String>, options!: ?CollatorOptions = None)
}
```

**功能：** 排序对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 创建排序对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用系统locale创建Collator对象
let collator = Collator()
```

### init(String, ?CollatorOptions)

```cangjie
public init(locale: String, options!: ?CollatorOptions = None)
```

**功能：** 创建排序对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|options|?[CollatorOptions](#struct-collatoroptions)|否|None| **命名参数。** 创建排序对象时可设置的配置项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let c = CollatorOptions(usage: "sort", ignorePunctuation: true)
let collator = Collator("zh-Hans", options: c)
```

### init(Array\<String>, ?CollatorOptions)

```cangjie
public init(locale: Array<String>, options!: ?CollatorOptions = None)
```

**功能：** 创建排序对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|Array\<String>|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|
|options|?[CollatorOptions](#struct-collatoroptions)|否|None| **命名参数。** 创建排序对象时可设置的配置项。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let c = CollatorOptions(usage: "sort", ignorePunctuation: true)
let collator = Collator(["zh-Hans"], options: c)
```

### func compare(String, String)

```cangjie
public func compare(first: String, second: String): Int32
```

**功能：** 依据配置项设置的排序规则，比较两个字符串。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|first|String|是|-|进行比较第一个字符串。|
|second|String|是|-|进行比较的第二个字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|比较结果。当返回值为负数时，表示first排序在second之前；返回值为0时，表示first与second排序相同；返回值为正数，表示first排序在second之后。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用en-GB locale创建Collator对象
let collator = Collator("en-GB")
// 比较"first"和"second"的先后顺序
let compareResult = collator.compare("first", "second") // compareResult = -1
```

### func resolvedOptions()

```cangjie
public func resolvedOptions(): CollatorOptions
```

**功能：** 获取创建排序对象时设置的配置项。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[CollatorOptions](#struct-collatoroptions)|返回排序对象的属性。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let c = CollatorOptions(usage: "sort", ignorePunctuation: true)
let collator = Collator("zh-Hans", options: c)
// 获取Collator对象的配置项
let options = collator.resolvedOptions()
let usage = options.usage // usage = "sort"
let ignorePunctuation = options.ignorePunctuation // ignorePunctuation = true
```