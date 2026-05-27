### NumberOptions(String, String, String, String, String, String, String, String, String, String, String, String, String, Bool, Int64, Int64, Int64, Int64, Int64)

```cangjie
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
```

**功能：** 构建创建数字格式化对象时可设置的配置项的对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**