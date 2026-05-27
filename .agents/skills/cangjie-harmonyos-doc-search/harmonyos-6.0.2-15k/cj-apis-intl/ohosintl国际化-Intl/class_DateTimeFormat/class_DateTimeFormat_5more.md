## class DateTimeFormat

```cangjie
public class DateTimeFormat {
    public init()
    public init(locale: String, options!: ?DateTimeOptions = None)
    public init(locale: Array<String>, options!: ?DateTimeOptions = None)
}
```

**功能：** 时间、日期格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 创建时间、日期格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用系统当前locale创建DateTimeFormat对象
let datefmt = DateTimeFormat()
```

### init(String, ?DateTimeOptions)

```cangjie
public init(locale: String, options!: ?DateTimeOptions = None)
```

**功能：** 创建时间、日期格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|String|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。locale可填写组成部分中的一个或多个。|
|options|?[DateTimeOptions](#struct-datetimeoptions)|否|None| **命名参数。** 创建时间、日期格式化对象时可设置的配置项。若所有选项均未设置时，year、month、day三个属性的默认值为numeric。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用en-GB locale创建DateTimeFormat对象，dateStyle设置为full，timeStyle设置为medium
let d1 = DateTimeOptions(dateStyle: "full", timeStyle: "medium")
let datefmt = DateTimeFormat("en-GB", options: d1)
```

### init(Array\<String>, ?DateTimeOptions)

```cangjie
public init(locale: Array<String>, options!: ?DateTimeOptions = None)
```

**功能：** 创建时间、日期格式化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|locale|Array\<String>|是|-|表示区域信息的字符串，由语言、脚本、国家或地区组成。locale可填写组成部分中的一个或多个。|
|options|?[DateTimeOptions](#struct-datetimeoptions)|否|None| **命名参数。** 创建时间、日期格式化对象时可设置的配置项。若所有选项均未设置时，year、month、day三个属性的默认值为numeric。入参非法时，当作无该入参创建对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 使用en-GB locale创建DateTimeFormat对象，dateStyle设置为full，timeStyle设置为medium
let d1 = DateTimeOptions(dateStyle: "full", timeStyle: "medium")
let datefmt = DateTimeFormat(["en-GB"], options: d1)
```

### func format(DateTime)

```cangjie
public func format(date: DateTime): String
```

**功能：** 对时间、日期进行格式化。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|date|DateTime|是|-|时间日期对象。|

**返回值：**

|类型|说明|
|:----|:----|
|String|格式化后的时间、日期字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import std.time.DateTime as d

let date = d.of(year: 2021,month: 12, dayOfMonth: 17, hour: 3, minute: 24)
// 使用en-GB locale创建DateTimeFormat对象
var datefmt = DateTimeFormat("en-GB")
var formattedDate = datefmt.format(date) // formattedDate "17/12/2021"

// 使用en-GB locale创建DateTimeFormat对象，dateStyle设置为full，timeStyle设置为medium
let d1 = DateTimeOptions(dateStyle: "full", timeStyle: "medium")
datefmt = DateTimeFormat("en-GB", options: d1)
formattedDate = datefmt.format(date) // formattedDate "Friday, 17 December 2021, 03:24:00"
```