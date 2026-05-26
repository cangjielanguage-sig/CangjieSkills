## struct RelativeTimeFormatInputOptions

```cangjie
public struct RelativeTimeFormatInputOptions {
    public RelativeTimeFormatInputOptions(
        public var localeMatcher!: String = "best fit",
        public var numeric!: String = "always",
        public var style!: String = "long"
    )
}
```

**功能：** 创建相对时间格式化对象时可设置的属性选项。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### var localeMatcher

```cangjie
public var localeMatcher: String = "best fit"
```

**功能：** locale匹配算法，取值包括："best fit", "lookup"。默认值为"best fit"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var numeric

```cangjie
public var numeric: String = "always"
```

**功能：** 输出消息的格式，取值包括："always", "auto"。默认值为always。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var style

```cangjie
public var style: String = "long"
```

**功能：** 国际化消息的长度，取值包括："long", "short", "narrow"。默认值为long。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### RelativeTimeFormatInputOptions(String, String, String)

```cangjie
public RelativeTimeFormatInputOptions(
    public var localeMatcher!: String = "best fit",
    public var numeric!: String = "always",
    public var style!: String = "long"
)
```

**功能：** 构建创建相对时间格式化对象时可设置的属性选项的对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|localeMatcher|String|否|"best fit"| **命名参数。** locale匹配算法，取值包括："best fit", "lookup"。|
|numeric|String|否|"always"| **命名参数。** 输出消息的格式，取值包括："always", "auto"。|
|style|String|否|"long"| **命名参数。** 国际化消息的长度，取值包括："long", "short", "narrow"。|

> **说明：**
>
> numeric、style不同参数取值显示的效果，请参见[相对时间格式化选项](../../../../Dev_Guide/internationalization/cj-i18n-time-date.md#相对时间格式化)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// 显示相对时间
let relativeTimeFormat1 = RelativeTimeFormat('en-GB')
let formattedRelativeTime1 = relativeTimeFormat1.format(-1.00, 'day') // formattedRelativeTime1: 1 day ago

// 口语化
let r2 = RelativeTimeFormatInputOptions(numeric: "auto")
let relativeTimeFormat2 = RelativeTimeFormat('en-GB', options: r2)
let formattedRelativeTime2 = relativeTimeFormat2.format(-1.00, 'day') // formattedRelativeTime2: yesterday

// 部分语言支持更为简短的显示风格
let relativeTimeFormat3 = RelativeTimeFormat('fr-FR') // 默认style为long
let formattedRelativeTime3 = relativeTimeFormat3.format(-1.00, 'day') // formattedRelativeTime3: il y a 1 jour
let r4 = RelativeTimeFormatInputOptions(style: "narrow")
let relativeTimeFormat4 = RelativeTimeFormat('fr-FR', options: r4)
let formattedRelativeTime4 = relativeTimeFormat4.format(-1.00, 'day') // formattedRelativeTime4: -1 j

// 自定义区域设置格式的相对时间格式
let r5 = RelativeTimeFormatInputOptions(style: "long")
let relativeTimeFormat5 = RelativeTimeFormat('en-GB', options: r5)
// parts: [{type: 'literal', value: 'in'}, {type: 'integer', value: 1, unit: 'day'}, {type: 'literal', value: 'day'}]
let parts = relativeTimeFormat5.formatToParts(1.00, 'day')

// 获取RelativeTimeFormat对象的格式化选项
let r6 = RelativeTimeFormatInputOptions(numeric: "auto")
let relativeTimeFormat6 = RelativeTimeFormat('en-GB', options: r6)
let options = relativeTimeFormat6.resolvedOptions()
let numeric = options.numeric // numeric: auto
```