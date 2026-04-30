### class ScrollAnimationOptions

```cangjie
public class ScrollAnimationOptions {
    public var duration: Float64
    public var curve: Curve
    public var canOverScroll: Bool
    public init(
        duration!: Float64 = 1000.0,
        curve!: Curve = Curve.Ease,
        canOverScroll!: Bool = false
    )
}
```

**功能：** 自定义滚动动效的参数选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var canOverScroll

```cangjie
public var canOverScroll: Bool
```

**功能：** 设置滚动是否可越界。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var curve

```cangjie
public var curve: Curve
```

**功能：** 设置滚动曲线。

**类型：** [Curve](./cj-common-types.md#enum-curve)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var duration

```cangjie
public var duration: Float64
```

**功能：** 设置滚动时长。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float64, Curve, Bool)

```cangjie
public init(
    duration!: Float64 = 1000.0,
    curve!: Curve = Curve.Ease,
    canOverScroll!: Bool = false
)
```

**功能：** 构造一个ScrollAnimationOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Float64|否|1000.0| **命名参数。** 设置滚动时长。设置为小于0的值时，按默认值显示。|
|curve|[Curve](./cj-common-types.md#enum-curve)|否|Curve.Ease| **命名参数。** 设置滚动曲线。|
|canOverScroll|Bool|否|false| **命名参数。** 设置滚动是否可越界。<br>**说明：**<br>仅在设置为true，且组件的edgeEffect设置为EdgeEffect.Spring时，滚动能够越界，并在越界时启动回弹动画。|