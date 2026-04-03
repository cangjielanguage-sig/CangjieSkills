## struct NumberOptions

```cangjie
public struct NumberOptions {
    public NumberOptions(
        public var locale!: String = "",
        public var currency!: String = "",
        public var currencySign!: String = "standard",
        public var currencyDisplay!: String = "symbol",
        public var unit!: String = "",
        public var unitDispaly!: String = "short",
        public var unitUsage!: String = "default",
        public var signDisplay!: String = "auto",
        public var compactDisplay!: String = "short",
        public var notation!: String = "standard",
        public var localeMather!: String = "best fit",
        public var style!: String = "decimal",
        public var numberingSystem!: String = "",
        public var useGrouping!: Bool = false,
        public var minimumIntegerDigits!: Int64 = 1,
        public var minimumFractionDigits!: Int64 = 0,
        public var maximumFractionDigits!: Int64 = 3,
        public var minimumSignificantDigits!: Int64 = 1,
        public var maximumSignificantDigits!: Int64 = 21
    )
}
```

**功能：** 创建数字格式化对象时可设置的配置项。NumberOptions的属性为可选。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### var compactDisplay

```cangjie
public var compactDisplay: String = "short"
```

**功能：** 紧凑型的显示格式，取值包括："long", "short"。默认值为short。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var currency

```cangjie
public var currency: String = ""
```

**功能：** 货币单位，取值符合ISO-4217标准，如："EUR", "CNY", "USD"等。支持三位数字代码，如："978"，"156"，"840"等。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var currencyDisplay

```cangjie
public var currencyDisplay: String = "symbol"
```

**功能：** 货币的显示方式，取值包括："symbol", "narrowSymbol", "code", "name"。默认值为symbol。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var currencySign

```cangjie
public var currencySign: String = "standard"
```

**功能：** 货币单位的符号显示，取值包括："standard", "accounting"。默认值为standard。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var locale

```cangjie
public var locale: String = ""
```

**功能：** 区域参数， 如："zh-Hans-CN"。locale属性默认值为系统当前Locale。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var localeMather

```cangjie
public var localeMather: String = "best fit"
```

**功能：** 要使用的区域匹配算法，取值包括："lookup", "best fit"。默认值为"best fit"。

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