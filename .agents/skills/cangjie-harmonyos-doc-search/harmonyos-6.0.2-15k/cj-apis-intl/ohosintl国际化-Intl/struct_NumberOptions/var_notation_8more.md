### var notation

```cangjie
public var notation: String = "standard"
```

**功能：** 数字的格式化规格，取值包括："standard", "scientific", "engineering", "compact"。默认值为standard。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var numberingSystem

```cangjie
public var numberingSystem: String = ""
```

**功能：** 数字系统，取值包括："adlm", "ahom", "arab", "arabext", "bali", "beng", "bhks", "brah", "cakm", "cham", "deva", "diak", "fullwide", "gong", "gonm", "gujr", "guru", "hanidec", "hmng", "hmnp", "java", "kali", "khmr", "knda", "lana", "lanatham", "laoo", "latn", "lepc", "limb", "mathbold", "mathdbl", "mathmono", "mathsanb", "mathsans", "mlym", "modi", "mong", "mroo", "mtei", "mymr", "mymrshan", "mymrtlng", "newa", "nkoo", "olck", "orya", "osma", "rohg", "saur", "segment", "shrd", "sind", "sinh", "sora", "sund", "takr", "talu", "tamldec", "telu", "thai", "tibt", "tirh", "vaii", "wara", "wcho"。numberingSystem属性默认值为locale的默认数字系统。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var signDisplay

```cangjie
public var signDisplay: String = "auto"
```

**功能：** 数字符号的显示格式，取值包括："auto", "never", "always", "expectZero"。默认值为auto。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var style

```cangjie
public var style: String = "decimal"
```

**功能：** 数字的显示格式，取值包括："decimal", "currency", "percent", "unit"。默认值为decimal。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var unit

```cangjie
public var unit: String = ""
```

**功能：** 单位名称，如："meter", "inch", "hectare"等。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var unitDispaly

```cangjie
public var unitDispaly: String = "short"
```

**功能：** 单位的显示格式，取值包括："long", "short", "narrow"。默认值为short。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var unitUsage

```cangjie
public var unitUsage: String = "default"
```

**功能：** 单位的使用场景，取值包括："default", "area-land-agricult", "area-land-commercl", "area-land-residntl", "length-person", "length-person-small", "length-rainfall", "length-road", "length-road-small", "length-snowfall", "length-vehicle", "length-visiblty", "length-visiblty-small", "length-person-informal", "length-person-small-informal", "length-road-informal", "speed-road-travel", "speed-wind", "temperature-person", "temperature-weather", "volume-vehicle-fuel", "elapsed-time-second", "size-file-byte", "size-shortfile-byte"。默认值为default。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var useGrouping

```cangjie
public var useGrouping: Bool = false
```

**功能：** 是否分组显示。useGrouping属性默认值为false。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19