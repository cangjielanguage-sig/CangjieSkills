## struct CollatorOptions

```cangjie
public struct CollatorOptions {
    public CollatorOptions(
        public var localeMatcher!: String = "best fit",
        public var usage!: String = "sort",
        public var sensitivity!: String = "variant",
        public var ignorePunctuation!: Bool = false,
        public var collation!: String = "default",
        public var numeric!: Bool = false,
        public var caseFirst!: String = "false"
    )
}
```

**功能：** 排序对象时可设置的配置项。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### var caseFirst

```cangjie
public var caseFirst: String = "false"
```

**功能：** 表示大写、小写的排序顺序，取值范围："upper", "lower", "false"。默认值为"false"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var collation

```cangjie
public var collation: String = "default"
```

**功能：** 排序规则，取值范围："big5han", "compat", "dict", "direct", "ducet", "eor", "gb2312", "phonebk", "phonetic", "pinyin", "reformed", "searchjl", "stroke", "trad", "unihan", "zhuyin"。默认值为default。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var ignorePunctuation

```cangjie
public var ignorePunctuation: Bool = false
```

**功能：** 表示是否忽略标点符号，取值范围：true，false。默认值为false。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var localeMatcher

```cangjie
public var localeMatcher: String = "best fit"
```

**功能：** locale匹配算法，取值范围："best fit", "lookup"。默认值为"best fit"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var numeric

```cangjie
public var numeric: Bool = false
```

**功能：** 是否使用数字排序，取值范围：true，false。默认值为false。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var sensitivity

```cangjie
public var sensitivity: String = "variant"
```

**功能：** 表示字符串中的哪些差异会导致非零结果值，取值范围："base", "accent", "case", "variant"。默认值为"variant"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var usage

```cangjie
public var usage: String = "sort"
```

**功能：** 比较的用途。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

> **说明：**
>
> CollatorOptions中属性的不同取值代表的含义请参见[本地习惯排序](../../../../Dev_Guide/internationalization/cj-i18n-sorting-local.md)。