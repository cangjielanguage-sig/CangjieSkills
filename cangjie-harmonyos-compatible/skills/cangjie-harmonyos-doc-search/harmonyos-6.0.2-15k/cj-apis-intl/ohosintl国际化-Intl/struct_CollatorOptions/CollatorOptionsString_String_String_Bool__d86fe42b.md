### CollatorOptions(String, String, String, Bool, String, Bool, String)

```cangjie
public CollatorOptions(
    public var localeMatcher!: String = "best fit",
    public var usage!: String = "sort",
    public var sensitivity!: String = "variant",
    public var ignorePunctuation!: Bool = false,
    public var collation!: String = "default",
    public var numeric!: Bool = false,
    public var caseFirst!: String = "false"
)
```

**功能：** 构建排序对象时可设置的配置项。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|localeMatcher|String|否|"best fit"| **命名参数。** locale匹配算法，取值范围："best fit", "lookup"。|
|usage|String|否|"sort"| **命名参数。** 比较的用途。|
|sensitivity|String|否|"variant"| **命名参数。** 表示字符串中的哪些差异会导致非零结果值，取值范围："base", "accent", "case", "variant"。|
|ignorePunctuation|Bool|否|false| **命名参数。** 表示是否忽略标点符号，取值范围：true，false。|
|collation|String|否|"default"| **命名参数。** 排序规则，取值范围："big5han", "compat", "dict", "direct", "ducet", "eor", "gb2312", "phonebk", "phonetic", "pinyin", "reformed", "searchjl", "stroke", "trad", "unihan", "zhuyin"。|
|numeric|Bool|否|false| **命名参数。** 是否使用数字排序，取值范围：true，false。|
|caseFirst|String|否|"false"| **命名参数。** 表示大写、小写的排序顺序，取值范围："upper", "lower", "false"。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import std.sort.*

// 创建排序对象
let options = CollatorOptions(localeMatcher: "lookup", usage: "sort",sensitivity: "case")
let collator = Collator("zh-CN", options: options)

// 区分大小写排序
let array = ["app", "App", "Apple", "ANIMAL", "animal", "apple", "APPLE"]
array.sortBy(stable: true){a: String, b: String =>
if(collator.compare(a, b) < 0) {
    return Ordering.LT
}
if(collator.compare(a, b) > 0) {
    return Ordering.GT
}
return Ordering.EQ}
// animal ANIMAL app App apple Apple APPLE

// 中文拼音排序
let array = ["苹果", "梨", "香蕉", "石榴", "甘蔗", "葡萄", "橘子"]
array.sortBy(stable: true){a: String, b: String =>
if(collator.compare(a, b) < 0) {
    return Ordering.LT
}
if(collator.compare(a, b) > 0) {
    return Ordering.GT
}
return Ordering.EQ}
// 甘蔗,橘子,梨,苹果,葡萄,石榴,香蕉

// 按笔画排序
let options = CollatorOptions(localeMatcher: "lookup", usage: "sort", collation: "stroke")
let collator = Collator("zh-CN", options: options)
let array = ["苹果", "梨", "香蕉", "石榴", "甘蔗", "葡萄", "橘子"]
array.sortBy(stable: true){a: String, b: String =>
if(collator.compare(a, b) < 0) {
    return Ordering.LT
}
if(collator.compare(a, b) > 0) {
    return Ordering.GT
}
return Ordering.EQ}
// 甘蔗,石榴,苹果,香蕉,梨,葡萄,橘子
```