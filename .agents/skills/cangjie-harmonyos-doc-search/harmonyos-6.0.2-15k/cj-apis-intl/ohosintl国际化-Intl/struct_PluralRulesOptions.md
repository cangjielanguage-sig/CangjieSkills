## struct PluralRulesOptions

```cangjie
public struct PluralRulesOptions {
    public PluralRulesOptions(
        public var localeMatcher!: String = "best fit",
        public var ptype!: String = "cardinal",
        public var minimumIntegerDigits!: Int64 = 1,
        public var minimumFractionDigits!: Int64 = 0,
        public var maximumFractionDigits!: Int64 = 3,
        public var minimumSignificantDigits!: Int64 = 1,
        public var maximumSignificantDigits!: Int64 = 21
    )
}
```

**功能：** 创建单复数对象时可设置的配置项。PluralRulesOptions的属性为可选。

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

### var maximumFractionDigits

```cangjie
public var maximumFractionDigits: Int64 = 3
```

**功能：** 表示要使用的最大分数位数，取值范围：1~21。maximumFractionDigits属性默认值为3。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var maximumSignificantDigits

```cangjie
public var maximumSignificantDigits: Int64 = 21
```

**功能：** 表示要使用的最大有效位数，取值范围：1~21。maximumSignificantDigits属性默认值为21。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var minimumFractionDigits

```cangjie
public var minimumFractionDigits: Int64 = 0
```

**功能：** 表示要使用的最小分数位数，取值范围：0~20。minimumFractionDigits属性默认值为0。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var minimumIntegerDigits

```cangjie
public var minimumIntegerDigits: Int64 = 1
```

**功能：** 表示要使用的最小整数位数，取值范围：1~21。minimumIntegerDigits属性默认值为1。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var minimumSignificantDigits

```cangjie
public var minimumSignificantDigits: Int64 = 1
```

**功能：** 表示要使用的最低有效位数，取值范围：1~21。minimumSignificantDigits属性默认值为1。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var ptype

```cangjie
public var ptype: String = "cardinal"
```

**功能：** 排序的类型，取值包括："cardinal", "ordinal"，默认值为cardinal。cardinal：基数词，ordinal：序数词。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### PluralRulesOptions(String, String, Int64, Int64, Int64, Int64, Int64)

```cangjie
public PluralRulesOptions(
    public var localeMatcher!: String = "best fit",
    public var ptype!: String = "cardinal",
    public var minimumIntegerDigits!: Int64 = 1,
    public var minimumFractionDigits!: Int64 = 0,
    public var maximumFractionDigits!: Int64 = 3,
    public var minimumSignificantDigits!: Int64 = 1,
    public var maximumSignificantDigits!: Int64 = 21
)
```

**功能：** 构建创建单复数对象时可设置的配置项的对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|localeMatcher|String|否|"best fit"| **命名参数。** locale匹配算法，取值包括："best fit", "lookup"。|
|ptype|String|否|"cardinal"| **命名参数。** 排序的类型，取值包括："cardinal", "ordinal"，默认值为cardinal。cardinal：基数词，ordinal：序数词。|
|minimumIntegerDigits|Int64|否|1| **命名参数。** 表示要使用的最小整数位数，取值范围：1~21。|
|minimumFractionDigits|Int64|否|0| **命名参数。** 表示要使用的最小分数位数，取值范围：0~20。|
|maximumFractionDigits|Int64|否|3| **命名参数。** 表示要使用的最大分数位数，取值范围：1~21。|
|minimumSignificantDigits|Int64|否|1| **命名参数。** 表示要使用的最低有效位数，取值范围：1~21。|
|maximumSignificantDigits|Int64|否|21| **命名参数。** 表示要使用的最大有效位数，取值范围：1~21。|