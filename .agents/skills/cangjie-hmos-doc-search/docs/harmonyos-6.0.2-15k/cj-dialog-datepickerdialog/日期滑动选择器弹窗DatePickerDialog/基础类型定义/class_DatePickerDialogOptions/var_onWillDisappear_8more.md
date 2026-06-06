#### var onWillDisappear

```cangjie
public var onWillDisappear: ?() -> Unit
```

**功能：** 弹窗退出动效前的事件回调。

> **说明：**
>
> - 正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。
> - 快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。

**类型：** ?()->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var selected

```cangjie
public var selected: ?DateTime
```

**功能：** 选中日期。

**类型：** ?DateTime

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var selectedTextStyle

```cangjie
public var selectedTextStyle: ?PickerTextStyle
```

**功能：** 设置选中项的文本颜色、字号、字体粗细。初始值：PickerTextStyle(0xff007dff, MyFont(size: 20.fp, weight: FontWeight.Medium))。

**类型：** ?[PickerTextStyle](./cj-button-picker-datepicker.md#class-pickertextstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var shadow

```cangjie
public var shadow: ?ShadowOptions
```

**功能：** 设置弹窗背板的阴影。当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。

**类型：** ?[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var showTime

```cangjie
public var showTime: Bool = false
```

**功能：** 是否展示时间项，true表示显示时间，false表示不显示时间。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var start

```cangjie
public var start: ?DateTime
```

**功能：** 起始日期。

**类型：** ?DateTime

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var textStyle

```cangjie
public var textStyle: ?PickerTextStyle
```

**功能：** 设置所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。初始值：PickerTextStyle(0xff182431, MyFont(size: 16.fp, weight: FontWeight.Regular))。

**类型：** ?[PickerTextStyle](./cj-button-picker-datepicker.md#class-pickertextstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var useMilitaryTime

```cangjie
public var useMilitaryTime: Bool = false
```

**功能：** 展示时间是否为24小时制，true表示显示24小时制，false表示显示12小时制。初始值：false。

> **说明：**
>
> 当展示时间为12小时制时，上下午与小时无联动关系。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19