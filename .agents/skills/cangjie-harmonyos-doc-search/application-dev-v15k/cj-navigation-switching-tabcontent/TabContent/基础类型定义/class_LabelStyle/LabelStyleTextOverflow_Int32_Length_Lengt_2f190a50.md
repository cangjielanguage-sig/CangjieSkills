#### LabelStyle(TextOverflow, Int32, Length, Length, TextHeightAdaptivePolicy, Fonts, ResourceColor, ResourceColor)

```cangjie
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
```

**功能：** 构造一个LabelStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|overflow|[TextOverflow](cj-common-types.md#enum-textoverflow)|否|TextOverflow.Ellipsis| **命名参数。** 设置Label文本超长时的显示方式。|
|maxLines|Int32|否|1| **命名参数。** 设置Label文本的最大行数。如果指定此参数，则文本最多不会超过指定的行。如果有多余的文本，可以通过textOverflow来指定截断方式。<br> 取值范围：[1, +∞)。|
|minFontSize|[Length](cj-common-types.md#interface-length)|否|0.0.fp| **命名参数。** 设置Label文本最小显示字号（不支持百分比设置）。需配合maxFontSize以及maxLines或布局大小限制使用。自适应文本大小生效后，font.size不生效。<br> 取值范围：(0, +∞)。|
|maxFontSize|[Length](cj-common-types.md#interface-length)|否|0.0.fp| **命名参数。** 设置Label文本最大显示字号（不支持百分比设置）。需配合minFontSize以及maxLines或布局大小限制使用。自适应文本大小生效后，font.size不生效。<br> 取值范围：[minFontSize, +∞)。|
|heightAdaptivePolicy|[TextHeightAdaptivePolicy](cj-common-types.md#enum-textheightadaptivepolicy)|否|TextHeightAdaptivePolicy.MAX_LINES_FIRST| **命名参数。** 设置Label文本自适应高度的方式。|
|font|[Fonts](cj-common-types.md#class-fonts)|否|Fonts()| **命名参数。** 设置Label文本字体样式。当页签为子页签时，默认值是字体大小16.0fp、字体类型'HarmonyOS Sans'，字体风格正常，选中时字重中等，未选中时字重正常。当页签为底部页签时，默认值是字体大小10.0fp、字体类型'HarmonyOS Sans'，字体风格正常，字重中等。|
|unselectedColor|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|0x99182431| **命名参数。** 设置Label文本字体未选中时的颜色。|
|selectedColor|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|0xFF007DFF| **命名参数。** 设置Label文本字体选中时的颜色。|