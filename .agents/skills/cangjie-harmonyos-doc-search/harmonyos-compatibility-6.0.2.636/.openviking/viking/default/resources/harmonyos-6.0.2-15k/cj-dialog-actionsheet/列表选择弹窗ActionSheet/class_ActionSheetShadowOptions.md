## class ActionSheetShadowOptions

```cangjie
public class ActionSheetShadowOptions {
    public ActionSheetShadowOptions(
        public var radius: Float64,
        public var shadowType!: ShadowType = ShadowType.COLOR,
        public var color!: Color = Color.BLACK,
        public var offsetX!: Float64 = 0.0,
        public var offsetY!: Float64 = 0.0,
        public var fill!: Bool = false
    )
}
```

**功能：** 列表选择弹窗阴影参数的配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var color

```cangjie
public var color: Color = Color.BLACK
```

**功能：** 阴影的颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**起始版本：** 19

### var fill

```cangjie
public var fill: Bool = false
```

**功能：** 阴影是否内部填充。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var offsetX

```cangjie
public var offsetX: Float64 = 0.0
```

**功能：** 阴影的X轴偏移量。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var offsetY

```cangjie
public var offsetY: Float64 = 0.0
```

**功能：** 阴影的Y轴偏移量。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var radius

```cangjie
public var radius: Float64
```

**功能：** 阴影模糊半径。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var shadowType

```cangjie
public var shadowType: ShadowType = ShadowType.COLOR
```

**功能：** 阴影类型。

**类型：** [ShadowType](./cj-common-types.md#enum-shadowtype)

**读写能力：** 可读写

**起始版本：** 19

### ActionSheetShadowOptions(Float64, ShadowType, Color, Float64, Float64, Bool)

```cangjie
public ActionSheetShadowOptions(
    public var radius: Float64,
    public var shadowType!: ShadowType = ShadowType.COLOR,
    public var color!: Color = Color.BLACK,
    public var offsetX!: Float64 = 0.0,
    public var offsetY!: Float64 = 0.0,
    public var fill!: Bool = false
)
```

**功能：** 构造一个ActionSheetShadowOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数:**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| radius | Float64 | 是 | - | 阴影模糊半径。<br>取值范围: [0, +∞)<br>单位: px<br>**说明:**<br>设置小于0的值时，按值为0处理。<br> |
| shadowType | [ShadowType](./cj-common-types.md#enum-shadowtype) | 否 | ShadowType.COLOR | **命名参数。**  阴影类型。 |
| color | [Color](./cj-common-types.md#class-color) | 否   | Color.BLACK | **命名参数。**  阴影的颜色。 |
| offsetX | Float64 | 否   | 0.0 | **命名参数。**  阴影的X轴偏移量。 <br>单位: px<br> |
| offsetY | Float64 | 否   | 0.0 | **命名参数。**  阴影的Y轴偏移量。<br>单位: px<br>|
| fill | Bool | 否   | false | **命名参数。**  阴影是否内部填充。 |