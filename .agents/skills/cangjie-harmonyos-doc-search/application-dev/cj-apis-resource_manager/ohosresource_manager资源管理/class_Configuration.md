## class Configuration

```cangjie
public class Configuration {
    public var direction: Direction
    public var locale: String
    public var deviceType: DeviceType
    public var screenDensity: ScreenDensity
    public var colorMode: ColorMode
    public var mcc: UInt32
    public var mnc: UInt32
}
```

**功能：** 表示当前设备的状态。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

### var colorMode

```cangjie
public var colorMode: ColorMode
```

**功能：** 颜色模式。

**类型：** [ColorMode](#enum-colormode)

**读写能力：** 可读写

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

### var deviceType

```cangjie
public var deviceType: DeviceType
```

**功能：** 设备类型。

**类型：** [DeviceType](#enum-devicetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

### var direction

```cangjie
public var direction: Direction
```

**功能：** 屏幕方向。

**类型：** [Direction](#enum-direction)

**读写能力：** 可读写

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

### var locale

```cangjie
public var locale: String
```

**功能：** 语言文字国家地区。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

### var mcc

```cangjie
public var mcc: UInt32
```

**功能：** 移动国家码。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

### var mnc

```cangjie
public var mnc: UInt32
```

**功能：** 移动网络码。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

### var screenDensity

```cangjie
public var screenDensity: ScreenDensity
```

**功能：** 屏幕密度。

**类型：** [ScreenDensity](#enum-screendensity)

**读写能力：** 可读写

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22