### class LabelStyle

```cangjie
public class LabelStyle {
    public let overflow: TextOverflow
    public let maxLines: Int32
    public let minFontSize: Length
    public let maxFontSize: Length
    public let heightAdaptivePolicy: TextHeightAdaptivePolicy
    public let font: Fonts
    public let unselectedColor: UInt32
    public let selectedColor: UInt32
    public LabelStyle(
        overflow!: TextOverflow = TextOverflow.Ellipsis,
        maxLines!: Int32 = 1,
        minFontSize!: Length = 0.0.fp,
        maxFontSize!: Length = 0.0.fp,
        heightAdaptivePolicy!: TextHeightAdaptivePolicy = TextHeightAdaptivePolicy.MAX_LINES_FIRST,
        font!: Fonts = Fonts(),
        unselectedColor!: ResourceColor = 0x99182431,
        selectedColor!: ResourceColor = 0xFF007DFF
    )
}
```

**功能：** label文本和字体的样式对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let font

```cangjie
public let font: Fonts
```

**功能：** 设置Label文本字体样式。

**类型：** [Fonts](cj-common-types.md#class-fonts)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let heightAdaptivePolicy

```cangjie
public let heightAdaptivePolicy: TextHeightAdaptivePolicy
```

**功能：** 设置Label文本自适应高度的方式。

**类型：** [TextHeightAdaptivePolicy](cj-common-types.md#enum-textheightadaptivepolicy)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let maxFontSize

```cangjie
public let maxFontSize: Length
```

**功能：** 设置Label文本最大显示字号（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let maxLines

```cangjie
public let maxLines: Int32
```

**功能：** 设置Label文本的最大行数。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let minFontSize

```cangjie
public let minFontSize: Length
```

**功能：** 设置Label文本最小显示字号（不支持百分比设置）。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let overflow

```cangjie
public let overflow: TextOverflow
```

**功能：** 设置Label文本超长时的显示方式。默认值是省略号截断。

**类型：** [TextOverflow](cj-common-types.md#enum-textoverflow)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let selectedColor

```cangjie
public let selectedColor: UInt32
```

**功能：** 设置Label文本字体选中时的颜色。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let unselectedColor

```cangjie
public let unselectedColor: UInt32
```

**功能：** 设置Label文本字体未选中时的颜色。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19