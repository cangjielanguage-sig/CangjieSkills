## class Configuration

```cangjie
public class Configuration <: ToString {
    public var direction: Direction
    public var locale: String
    public var deviceType: DeviceType
    public var screenDensity: ScreenDensity
    public var colorMode: ColorMode
    public var mcc: UInt32
    public var mnc: UInt32
    public init(direction: Direction, locale: String)
    public init(
        direction: Direction,
        locale: String,
        deviceType: DeviceType,
        screenDensity: ScreenDensity,
        colorMode: ColorMode,
        mcc: UInt32,
        mnc: UInt32
    )
}
```

**功能：** 表示当前设备的配置。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**父类型：**

- ToString

### var colorMode

```cangjie
public var colorMode: ColorMode
```

**功能：** 颜色模式。

**类型：** [ColorMode](#enum-colormode)

**读写能力：** 可读写

**起始版本：** 20

### var deviceType

```cangjie
public var deviceType: DeviceType
```

**功能：** 设备类型。

**类型：** [DeviceType](#enum-devicetype)

**读写能力：** 可读写

**起始版本：** 20

### var direction

```cangjie
public var direction: Direction
```

**功能：** 屏幕方向。

**类型：** [Direction](#enum-direction)

**读写能力：** 可读写

**起始版本：** 12

### var locale

```cangjie
public var locale: String
```

**功能：** 语言文字国家地区。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var mcc

```cangjie
public var mcc: UInt32
```

**功能：** 移动国家码。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 20

### var mnc

```cangjie
public var mnc: UInt32
```

**功能：** 移动网络码。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 20

### var screenDensity

```cangjie
public var screenDensity: ScreenDensity
```

**功能：** 屏幕密度。

**类型：** [ScreenDensity](#enum-screendensity)

**读写能力：** 可读写

**起始版本：** 20

### init(Direction, String)

```cangjie
public init(direction: Direction, locale: String)
```

**功能：** 构建当前设备状态的对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|direction|[Direction](#enum-direction)|是|-|屏幕方向。|
|locale|String|是|-|语言文字国家地区。|

### init(Direction, String)

```cangjie
public init(
    direction: Direction,
    locale: String,
    deviceType: DeviceType,
    screenDensity: ScreenDensity,
    colorMode: ColorMode,
    mcc: UInt32,
    mnc: UInt32
)
```

**功能：** 构建当前设备状态的对象。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|direction|[Direction](#enum-direction)|是|-|屏幕方向。|
|locale|String|是|-|语言文字国家地区。|
|deviceType|[DeviceType](#enum-devicetype)|是|-|设备类型。|
|screenDensity|[ScreenDensity](#enum-screendensity)|是|-|颜色模式。|
|colorMode|[ColorMode](#enum-colormode)|是|-|屏幕密度。|
|mcn|UInt32|是|-|移动国家码。|
|mnc|UInt32|是|-|移动网络码。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前[Configuration](#class-configuration)的信息，以字符串表示。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|当前[Configuration](#class-configuration)的信息。|