### var width

```cangjie
public var width: Option<Length> = Option<Length>.None
```

**功能：** 设置弹窗背板的宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(String, String, String, Bool, () -> Unit, DialogAlignment, Offset, Int32, Rectangle, Bool, Bool, Color, BlurStyle)

```cangjie
public init(
    message: String,
    title!: String = "",
    subtitle!: String = "",
    autoCancel!: Bool = true,
    cancel!: () -> Unit = {=>},
    alignment!: DialogAlignment = DialogAlignment.Default,
    offset!: Offset = Offset(0.vp, 0.vp),
    gridCount!: Int32 = 4,
    maskRect!: Rectangle = Rectangle(x: 0, y: 0, width: 100.percent, height: 100.percent),
    showInSubWindow!: Bool = false,
    isModal!: Bool = true,
    backgroundColor!: Color = Color.TRANSPARENT,
    backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
)
```

**功能：** 定义告警弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| message | String | 是 | \- | 弹窗内容。 |
| title | String | 否 | None | **命名参数。**  弹窗标题。 |
| subtitle | String | 否 | None | **命名参数。**  弹窗副标题。 |
| autoCancel | Bool | 否 | true | **命名参数。**  点击遮障层时是否关闭弹窗。true表示关闭弹窗,false表示不关闭弹窗。 |
| cancel | () -> Unit | 否 | None | **命名参数。**  点击遮障层关闭dialog时的回调。 |
| alignment | [DialogAlignment](./cj-common-types.md#enum-dialogalignment) | 否 | DialogAlignment.Bottom | **命名参数。**  弹窗在竖直方向上的对齐方式。|
| offset | [Offset](./cj-common-types.md#class-offset) | 否 | None | **命名参数。**  弹窗相对alignment所在位置的偏移量。|
| gridCount | Int32 | 否 | 4 | **命名参数。**  弹窗容器宽度所占用栅格数。|
| maskRect | [Rectangle](./cj-common-types.md#class-rectangle) | 否 | Rectangle(x: 0.vp, y: 0.vp, height: 100.percent, width: 100.percent) | **命名参数。**  弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。<br/>**说明：**<br/>showInSubWindow为true时，maskRect不生效。 |
| showInSubWindow | Bool | 否 | false | **命名参数。**  某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。<br/>初始值：false，弹窗显示在应用内，而非独立子窗口。<br/>**说明**：showInSubWindow为true的弹窗无法触发显示另一个showInSubWindow为true的弹窗。 |
| isModal | Bool | 否 | true | **命名参数。**  弹窗是否为模态窗口。模态窗口有蒙层，非模态窗口无蒙层。<br/>初始值：true，此时弹窗有蒙层。 |
| backgroundColor | [Color](./cj-common-types.md#class-color) | 否 | Color.TRANSPARENT | **命名参数。**  弹窗背板颜色。<br/>**说明：** <br/>当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则颜色显示将不符合预期效果。 |
| backgroundBlurStyle | [BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle) | 否 | BlurStyle.COMPONENT_ULTRA_THICK | **命名参数。**  弹窗背板模糊材质。<br/>**说明：** <br/>设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。 |