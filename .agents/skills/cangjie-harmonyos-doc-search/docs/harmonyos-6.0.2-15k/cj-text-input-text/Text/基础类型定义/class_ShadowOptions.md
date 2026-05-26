### class ShadowOptions

```cangjie
public class ShadowOptions {
    public var radius: Float64
    public var shadowType: ShadowType
    public var offsetX: Float64
    public var offsetY: Float64
    public var color: UInt32
    public var fill: Bool
    public init(radius!: Float64, shadowType!: ShadowType = ShadowType.COLOR, color!: ResourceColor = Color.BLACK, offsetX!: Float64 = 0.0, offsetY!: Float64 = 0.0, fill!: Bool = false)
}
```

**功能：** 阴影属性集合，用于设置阴影的模糊半径、阴影的颜色、X轴和Y轴的偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var radius

```cangjie
public var radius: Float64
```

**功能：** 表示阴影模糊半径。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var shadowType

```cangjie
public var shadowType: ShadowType
```

**功能：** 表示阴影类型。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var offsetX

```cangjie
public var offsetX: Float64
```

**功能：** 表示阴影的 X 轴偏移量。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var offsetY

```cangjie
public var offsetY: Float64
```

**功能：** 表示阴影的 Y 轴偏移量。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var color

```cangjie
public var color: UInt32
```

**功能：** 表示阴影的颜色。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var fill

```cangjie
public var fill: Bool
```

**功能：** 表示阴影是否内部填充。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float64, ShadowType, Float64, Float64, Color, Bool)

```cangjie
public init(radius!: Float64, shadowType!: ShadowType = ShadowType.COLOR, color!: ResourceColor = Color.BLACK, offsetX!: Float64 = 0.0, offsetY!: Float64 = 0.0, fill!: Bool = false)
```

**功能：** 创建ShadowOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 参数名      | 参数类型    | 必填     | 默认值     | 描述         |
| :-------   | :---------- | :------- | :-------- | :----------|
| radius  | Float64 | 是 | - | **命名参数。**  阴影模糊半径。<br/> 取值范围：[0, +∞)。<br/>单位：px。<br/>设置小于0的值时，按值为0处理。如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md)进行转换。|
| shadowType  | [ShadowType](./cj-text-input-span.md#enum-shadowtype) | 否 | ShadowType.COLOR | **命名参数。**  阴影类型。|
| offsetX  | Float64 | 否 | 0.0 | **命名参数。**  阴影的 X 轴偏移量。<br/>单位：px。<br/>如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md)进行转换。|
| offsetY  | Float64 | 否 | 0.0 | **命名参数。**  阴影的 Y 轴偏移量。<br/>单位：px。<br/>如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md)进行转换。|
| color  | [Color](./cj-common-types.md#color) | 否 | 黑色 | **命名参数。**  阴影的颜色。|
| fill  | Bool | 否 | false | **命名参数。**  阴影是否内部填充。textShadow中该字段不生效。|