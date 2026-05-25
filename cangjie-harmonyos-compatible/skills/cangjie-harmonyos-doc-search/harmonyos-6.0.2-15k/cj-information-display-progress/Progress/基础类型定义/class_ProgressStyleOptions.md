### class ProgressStyleOptions

```cangjie
public class ProgressStyleOptions {
    public var strokeWidth: Length
    public var scaleCount: Int32
    public var scaleWidth: Length
    public var enableSmoothEffect: Bool
    public init(strokeWidth!: Length = 4.vp, scaleCount!: Int32 = 120, scaleWidth!: Length = 2.vp,
        enableSmoothEffect!: Bool = true)
}
```

**功能：** 各类型进度条的基本样式。

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

#### var scaleCount

```cangjie
public var scaleCount: Int32
```

**功能：** 设置环形进度条总刻度数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var scaleWidth

```cangjie
public var scaleWidth: Length
```

**功能：** 设置环形进度条刻度粗细（不支持百分比设置），刻度粗细大于进度条宽度时，为系统默认粗细。

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

#### init(Length, Int32, Length, Bool)

```cangjie
public init(strokeWidth!: Length = 4.vp, scaleCount!: Int32 = 120, scaleWidth!: Length = 2.vp,
    enableSmoothEffect!: Bool = true)
```

**功能：** 构建一个ProgressStyleOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](./cj-common-types.md#interface-length)|否|4.vp| **命名参数。** 设置进度条宽度（不支持百分比设置）。|
|scaleCount|Int32|否|120| **命名参数。** 设置环形进度条总刻度数。|
|scaleWidth|[Length](./cj-common-types.md#interface-length)|否|2.vp| **命名参数。** 设置环形进度条刻度粗细（不支持百分比设置），刻度粗细大于进度条宽度时，为系统默认粗细。|
|enableSmoothEffect|Bool|否|true| **命名参数。** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。|