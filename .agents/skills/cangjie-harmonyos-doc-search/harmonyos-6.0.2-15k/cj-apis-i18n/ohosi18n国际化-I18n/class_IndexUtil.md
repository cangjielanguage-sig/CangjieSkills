## class IndexUtil

```cangjie
public class IndexUtil {
    public init(locale: String)
}
```

**功能：** 区域索引对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init(String)

```cangjie
public init(locale: String)
```

**功能：** 构造区域索引对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|

### func addLocale(String)

```cangjie
public func addLocale(locale: String): Unit
```

**功能：** 在当前区域的索引列表中，添加新区域的索引列表，形成复合列表。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let indexUtil = getInstance(locale: "zh-CN")
indexUtil.addLocale("en-US")
```

### func getIndex(String)

```cangjie
public func getIndex(text: String): String
```

**功能：** 获取text对应的索引。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|待计算索引值的输入文本。|

**返回值：**

|类型|说明|
|:----|:----|
|String|输入文本对应的索引值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let indexUtil = getInstance(locale: "zh-CN")
let index = indexUtil.getIndex("hi") // index = "H"
```

### func getIndexList()

```cangjie
public func getIndexList(): Array<String>
```

**功能：** 获取当前区域的索引列表。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回当前区域的索引列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let indexUtil = getInstance(locale: "zh-CN")
let indexList = indexUtil.getIndexList()
// indexList = [ "...", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
//              "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "..." ]
```