### class LinearGradientOption

```cangjie
public class LinearGradientOption {
    public LinearGradientOption (
        public let angle!: Float64 = 180.0,
        public let direction!: GradientDirection = GradientDirection.Bottom,
        public let colors!: Array<(Color, Float64)> = [(Color.TRANSPARENT, 0.0)],
        public let repeating!: Bool = false
    )
}
```

**功能：** 线性渐变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let angle

```cangjie
public let angle: Option<Float64> = 180.0
```

**功能：** 线性渐变的起始角度。

**类型：** Option\<Float64>

**读写能力：** 只读

**起始版本：** 19

#### let direction

```cangjie
public let direction: GradientDirection = GradientDirection.Bottom
```

**功能：** 线性渐变的方向。

**类型：** [GradientDirection](./cj-common-types.md#enum-gradientdirection)

**读写能力：** 只读

**起始版本：** 19

#### let colors

```cangjie
public let colors: Array<(Color, Float64)> = [(Color.TRANSPARENT, 0.0)]
```

**功能：** 指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过。

**类型：** Array\<([Color](./cj-common-types.md#color), Float64)>

**读写能力：** 只读

**起始版本：** 19

#### let repeating

```cangjie
public let repeating: Bool = false
```

**功能：** 是否为渐变的颜色重复着色。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

#### LinearGradientOption(Float64, GradientDirection, Array\<(Color, Float64)>, Bool)

```cangjie
public LinearGradientOption (
    public let angle!: Float64 = 180.0,
    public let direction!: GradientDirection = GradientDirection.Bottom,
    public let colors!: Array<(Color, Float64)> = [(Color.TRANSPARENT, 0.0)],
    public let repeating!: Bool = false
)
```

**功能：** 构造一个线性渐变类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|angle|Float64|否|180.0| **命名参数。** 线性渐变的起始角度。0点方向顺时针旋转为正向角度。|
|direction|[GradientDirection](./cj-common-types.md#enum-gradientdirection)|否|GradientDirection.Bottom| **命名参数。** 线性渐变的方向，设置angle后不生效。|
|colors|Array\<([Color](./cj-common-types.md#color), Float64)>|否|[(Color.TRANSPARENT, 0.0)]| **命名参数。** 指定某百分比位置处的渐变色颜色,设置非法颜色直接跳过。|
|repeating|Bool|否|false| **命名参数。** 为渐变的颜色重复着色。|