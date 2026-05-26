### class RichEditorTextStyle

```cangjie
public class RichEditorTextStyle {
    public init(fontColor!: Color = Color.BLACK, fontSize!: Length = 16.vp, fontStyle!: FontStyle = FontStyle.Normal, fontWeight!: FontWeight = FontWeight.Normal, fontFamily!: String = "HarmonyOS Sans", decoration!: TextDecoration = TextDecoration(`type`: TextDecorationType.None, color: Color.BLACK))
}
```

**功能：** 文本样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(ResourceColor, Length, FontStyle, FontWeight, String, TextDecoration)

```cangjie
public init(fontColor!: ResourceColor = Color.BLACK, fontSize!: Length = 16.vp, fontStyle!: FontStyle = FontStyle.Normal, fontWeight!: FontWeight = FontWeight.Normal, fontFamily!: String = DEFAULT_FONT, decoration!: TextDecoration = TextDecoration(`type`: TextDecorationType.None, color: Color.BLACK))
```

**功能：** 创建RichEditorTextStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| fontColor |  [ResourceColor](./cj-common-types.md#interface-resourcecolor) | 否 | Color.Black | **命名参数。**  文本颜色。 |
| fontSize | [Length](cj-common-types.md#interface-length) | 否 | 16.vp | **命名参数。**  字体大小，Length为Int64、Float64类型时，使用fp单位。不支持百分比设置。  |
| fontStyle | [FontStyle](./cj-common-types.md#enum-fontstyle) | 否 | FontStyle.Normal | **命名参数。**  字体样式。  |
| fontWeight | [FontWeight](./cj-common-types.md#enum-fontweight) | 否 | FontWeight.Normal | **命名参数。**  字体粗细。  <br>初始值：FontWeight.Normal。|
| fontFamily | String | 否 | DEFAULT_FONT | **命名参数。**  字体列表。|
| decoration | [TextDecoration](#class-textdecoration) | 否 | TextDecoration(\`type\`: TextDecorationType.None，color: Color.BLACK) | **命名参数。**  文本装饰线样式及其颜色。 |

### class TextDecoration

```cangjie
public class TextDecoration {
    public var `type`: TextDecorationType
    public var color: ResourceColor
    public init(`type`!: TextDecorationType, color!: ResourceColor = Color.BLACK) {
        this.`type` = `type`
        this.color = transAppResourceToResourceColor(color)
    }
}
```

**功能：** 文本装饰样式及颜色类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var \`type\`

```cangjie
public var `type`: TextDecorationType
```

**功能：** 表示装饰线类型。

**类型：** [TextDecorationType](./cj-common-types.md#enum-textdecorationtype)

**读写能力：** 可读写

**起始版本：** 12

#### var color

```cangjie
public var color: TextDecorationType
```

**功能：** 表示装饰颜色。

**类型：** [TextDecorationType](./cj-common-types.md#enum-textdecorationtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(TextDecorationType, Color)

```cangjie
public init(`type`!: TextDecorationType, color!: Color = Color.BLACK)
```

**功能：** 创建TextDecoration类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| \`type\`| [TextDecorationType](./cj-common-types.md#enum-textdecorationtype) | 是 | - | **命名参数。**  装饰线类型。 |
| color | [Color](./cj-common-types.md#class-color) | 否 | Color.BLACK | **命名参数。**  装饰颜色。 |