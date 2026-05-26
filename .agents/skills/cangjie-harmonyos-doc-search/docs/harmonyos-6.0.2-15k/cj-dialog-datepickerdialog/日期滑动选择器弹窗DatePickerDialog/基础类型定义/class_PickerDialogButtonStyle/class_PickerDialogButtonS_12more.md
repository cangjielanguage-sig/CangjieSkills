### class PickerDialogButtonStyle

```cangjie
public class PickerDialogButtonStyle {
    public PickerDialogButtonStyle(
        public let `type`!: ?ButtonType = None,
        public let style!: ?ButtonStyleMode = None,
        public let role!: ?ButtonRole = None,
        public let fontSize!: ?Length = None,
        public let fontColor!: ?ResourceColor = None,
        public let fontWeight!: ?FontWeight = None,
        public let fontStyle!: ?FontStyle = None,
        public let fontFamily!: ?String = None,
        public let backgroundColor!: ?ResourceColor = None,
        public let borderRadius!: ?BorderRadiuses = None,
        public let primary!: ?Bool = None
    )
}
```

**功能：** 确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键等。

**起始版本：** 19

#### let \`type\`

```cangjie
public let `type`: ?ButtonType = None
```

**功能：** 按钮显示样式。

**类型：** ?[ButtonType](./cj-button-picker-button.md#enum-buttontype)

**读写能力：** 只读

**起始版本：** 19

#### let style

```cangjie
public let style: ?ButtonStyleMode = None
```

**功能：** 按钮的样式和重要程度。

**类型：** ?[ButtonStyleMode](./cj-button-picker-button.md#enum-buttonstylemode)

**读写能力：** 只读

**起始版本：** 19

#### let role

```cangjie
public let role: ?ButtonRole = None
```

**功能：** Button组件的角色。

**类型：** ?[ButtonRole](./cj-button-picker-button.md#enum-buttonrole)

**读写能力：** 只读

**起始版本：** 19

#### let fontSize

```cangjie
public let fontSize: ?Length = None
```

**功能：** 文本显示字号。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 只读

**起始版本：** 19

#### let fontColor

```cangjie
public let fontColor: ?ResourceColor = None
```

**功能：** 文本显示颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**起始版本：** 19

#### let fontWeight

```cangjie
public let fontWeight: ?FontWeight = None
```

**功能：** 文本的字体粗细。FontWeight类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。

**类型：** ?[FontWeight](./cj-common-types.md#enum-fontweight)

**读写能力：** 只读

**起始版本：** 19

#### let fontStyle

```cangjie
public let fontStyle: ?FontStyle = None
```

**功能：** 文本的字体样式。

**类型：** ?[FontStyle](./cj-common-types.md#enum-fontstyle)

**读写能力：** 只读

**起始版本：** 19

#### let fontFamily

```cangjie
public let fontFamily: ?String = None
```

**功能：** 文本字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和注册自定义字体。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

#### let backgroundColor

```cangjie
public let backgroundColor: ?ResourceColor = None
```

**功能：** 按钮背景色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**起始版本：** 19

#### let borderRadius

```cangjie
public let borderRadius: ?BorderRadiuses = None
```

**功能：** 圆角半径。

**类型：** ?[BorderRadiuses](./cj-common-types.md#class-borderradiuses)

**读写能力：** 只读

**起始版本：** 19

#### let primary

```cangjie
public let primary: ?Bool = None
```

**功能：** 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。

**类型：** ?Bool

**读写能力：** 只读

**起始版本：** 19