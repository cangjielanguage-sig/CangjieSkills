#### var acceptButtonStyle

```cangjie
public var acceptButtonStyle: ?PickerDialogButtonStyle
```

**功能：** 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

> **说明：**
>
> acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。

**类型：** ?[PickerDialogButtonStyle](#class-pickerdialogbuttonstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var alignment

```cangjie
public var alignment: ?DialogAlignment
```

**功能：** 弹窗在竖直方向上的对齐方式。初始值：DialogAlignment.Default。

**类型：** ?[DialogAlignment](./cj-common-types.md#enum-dialogalignment)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
```

**功能：** 弹窗背板模糊材质。

> **说明：**
>
> 设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

**类型：** [BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var backgroundColor

```cangjie
public var backgroundColor: ResourceColor = Color.TRANSPARENT
```

**功能：** 弹窗背板颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var cancelButtonStyle

```cangjie
public var cancelButtonStyle: ?PickerDialogButtonStyle
```

**功能：** 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

> **说明：**
>
> acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。

**类型：** ?[PickerDialogButtonStyle](#class-pickerdialogbuttonstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var dateTimeOptions

```cangjie
public var dateTimeOptions: ?DateTimeOptions
```

**功能：** 设置时分是否显示前置0，目前只支持设置hour和minute参数。初始值：hour: 24小时制默认为"2-digit"，即有前置0；12小时制默认为"numeric"，即没有前置0。minute: 默认为"2-digit"，即有前置0。

**类型：** ?[DateTimeOptions](./cj-information-display-textclock.md#class-datetimeoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var disappearTextStyle

```cangjie
public var disappearTextStyle: ?PickerTextStyle
```

**功能：** 设置所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。初始值：PickerTextStyle(0xff182431, MyFont(size: 14.fp, weight: FontWeight.Regular))。

**类型：** ?[PickerTextStyle](./cj-button-picker-datepicker.md#class-pickertextstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var end

```cangjie
public var end: ?DateTime
```

**功能：** 结束日期。

**类型：** ?DateTime

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var lunar

```cangjie
public var lunar: Bool = false
```

**功能：** 日期是否显示为农历，true表示显示农历，false表示不显示农历。初始值：false。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19