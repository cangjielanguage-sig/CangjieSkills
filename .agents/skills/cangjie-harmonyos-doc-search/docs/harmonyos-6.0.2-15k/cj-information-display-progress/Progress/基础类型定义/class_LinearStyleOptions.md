### class LinearStyleOptions

```cangjie
public class LinearStyleOptions {
    public var strokeWidth: Length
    public var strokeRadius: Length
    public var enableSmoothEffect: Bool
    public var enableScanEffect: Bool
    public init(strokeWidth!: Length = 4.vp, strokeRadius!: Length = 2.vp, enableSmoothEffect!: Bool = true,
        enableScanEffect!: Bool = false)
    public init(strokeWidth!: Length = 4.vp, enableSmoothEffect!: Bool = true, enableScanEffect!: Bool = false)
}
```

**功能：** Linear的样式参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var enableScanEffect

```cangjie
public var enableScanEffect: Bool
```

**功能：** 扫光效果的开关。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var enableSmoothEffect

```cangjie
public var enableSmoothEffect: Bool
```

**功能：** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var strokeRadius

```cangjie
public var strokeRadius: Length
```

**功能：** 设置线性进度条圆角半径。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var strokeWidth

```cangjie
public var strokeWidth: Length
```

**功能：** 设置进度条宽度（不支持百分比设置）。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Length, Length, Bool, Bool)

```cangjie
public init(strokeWidth!: Length = 4.vp, strokeRadius!: Length, enableSmoothEffect!: Bool = true,
    enableScanEffect!: Bool = false)
```

**功能：** 构造一个LinearStyleOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](./cj-common-types.md#interface-length)|否|4.vp| **命名参数。** 设置进度条宽度（不支持百分比设置）。|
|strokeRadius|[Length](./cj-common-types.md#interface-length)|是|\-| **命名参数。** 设置线性进度条圆角半径。<br/>取值范围[0, strokeWidth / 2]。<br/>初始值：strokeWidth / 2。|
|enableSmoothEffect|Bool|否|true| **命名参数。** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。|
|enableScanEffect|Bool|否|false| **命名参数。** 扫光效果的开关。|

#### init(Length, Bool, Bool)

```cangjie
public init(strokeWidth!: Length = 4.vp, enableSmoothEffect!: Bool = true, enableScanEffect!: Bool = false)
```

**功能：** 构造一个LinearStyleOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](./cj-common-types.md#interface-length)|否|4.vp| **命名参数。** 设置进度条宽度（不支持百分比设置）。|
|enableSmoothEffect|Bool|否|true| **命名参数。** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。|
|enableScanEffect|Bool|否|false| **命名参数。** 扫光效果的开关。|