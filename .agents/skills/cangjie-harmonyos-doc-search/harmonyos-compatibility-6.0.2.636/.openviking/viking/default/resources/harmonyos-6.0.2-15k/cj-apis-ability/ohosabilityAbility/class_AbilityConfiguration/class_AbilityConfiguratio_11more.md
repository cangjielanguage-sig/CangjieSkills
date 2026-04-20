## class AbilityConfiguration

```cangjie
public class AbilityConfiguration {
    public AbilityConfiguration (
        public var language: String,
        public var colorMode: ConfigurationColorMode,
        public var direction: ConfigurationDirection,
        public var screenDensity: ConfigurationScreenDensity,
        public var displayId: Int32,
        public var hasPointerDevice: Bool,
        public var fontSizeScale: Float64,
        public var fontWeightScale: Float64,
        public var mcc: String,
        public var mnc: String
    )
}
```

**功能：** 定义环境变化信息的类。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 19

### var colorMode

```cangjie
public var colorMode: ConfigurationColorMode
```

**功能：** 表示深浅色模式，默认为浅色。取值范围：

- COLOR_MODE_NOT_SET：未设置
- COLOR_MODE_LIGHT：浅色模式
- COLOR_MODE_DARK：深色模式

**类型：** [ConfigurationColorMode](#enum-configurationcolormode)

**读写能力：** 可读写

**起始版本：** 19

### var direction

```cangjie
public var direction: ConfigurationDirection
```

**功能：** 表示屏幕方向，取值范围：

- DIRECTION_NOT_SET：未设置
- DIRECTION_HORIZONTAL：水平方向
- DIRECTION_VERTICAL：垂直方向

**类型：** [ConfigurationDirection](#enum-configurationdirection)

**读写能力：** 可读写

**起始版本：** 19

### var displayId

```cangjie
public var displayId: Int32
```

**功能：** 表示应用所在的物理屏幕ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var fontSizeScale

```cangjie
public var fontSizeScale: Float64
```

**功能：** 字体大小缩放比例，取值为非负数，默认值为1。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var fontWeightScale

```cangjie
public var fontWeightScale: Float64
```

**功能：** 字体粗细缩放比例，取值为非负数，默认值为1。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var hasPointerDevice

```cangjie
public var hasPointerDevice: Bool
```

**功能：** 指示指针类型设备是否已连接，如键鼠、触控板等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var language

```cangjie
public var language: String
```

**功能：** 表示应用程序的当前语言，例如“zh"。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var mcc

```cangjie
public var mcc: String
```

**功能：** 移动设备国家代码。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var mnc

```cangjie
public var mnc: String
```

**功能：** 移动设备网络代码。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var screenDensity

```cangjie
public var screenDensity: ConfigurationScreenDensity
```

**功能：** 表示屏幕像素密度，取值范围：

- SCREEN_DENSITY_NOT_SET：未设置
- SCREEN_DENSITY_SDPI：120
- SCREEN_DENSITY_MDPI：160
- SCREEN_DENSITY_LDPI：240
- SCREEN_DENSITY_XLDPI：320
- SCREEN_DENSITY_XXLDPI：480
- SCREEN_DENSITY_XXXLDPI：640

**类型：** [ConfigurationScreenDensity](#enum-configurationscreendensity)

**读写能力：** 可读写

**起始版本：** 19