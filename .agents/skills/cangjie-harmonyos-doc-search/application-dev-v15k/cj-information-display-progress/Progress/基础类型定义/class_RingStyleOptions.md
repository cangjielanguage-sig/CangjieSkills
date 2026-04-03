### class RingStyleOptions

```cangjie
public class RingStyleOptions {
    public var strokeWidth: Length
    public var shadow: Bool
    public var status: ProgressStatus
    public var enableSmoothEffect: Bool
    public var enableScanEffect: Bool
    public init(strokeWidth!: Length = 4.vp, shadow!: Bool = false,
        status!: ProgressStatus = ProgressStatus.PROGRESSING, enableSmoothEffect!: Bool = true,
        enableScanEffect!: Bool = false)
}
```

**功能：** Ring的样式参数。

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

#### var shadow

```cangjie
public var shadow: Bool
```

**功能：** 进度条阴影开关。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var status

```cangjie
public var status: ProgressStatus
```

**功能：** 进度条状态，当设置为LOADING时会开启检查更新动效，此时设置进度值不生效。当从LOADING设置为PROGRESSING，检查更新动效会执行到终点再停止。

**类型：** [ProgressStatus](#enum-progressstatus)

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

#### init(Length, Bool, ProgressStatus, Bool, Bool)

```cangjie
public init(strokeWidth!: Length = 4.vp, shadow!: Bool = false,
    status!: ProgressStatus = ProgressStatus.PROGRESSING, enableSmoothEffect!: Bool = true,
    enableScanEffect!: Bool = false)
```

**功能：** 创建一个RingStyleOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](./cj-common-types.md#interface-length)|否|4.vp| **命名参数。** 设置进度条宽度（不支持百分比设置），宽度大于等于半径时，默认修改宽度至半径值的二分之一。|
|shadow|Bool|否|false| **命名参数。** 进度条阴影开关。|
|status|[ProgressStatus](#enum-progressstatus)|否|ProgressStatus.PROGRESSING| **命名参数。** 进度条状态，当设置为LOADING时会开启检查更新动效，此时设置进度值不生效。当从LOADING设置为PROGRESSING，检查更新动效会执行到终点再停止。|
|enableSmoothEffect|Bool|否|true| **命名参数。** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。|
|enableScanEffect|Bool|否|false| **命名参数。** 扫光效果的开关。|