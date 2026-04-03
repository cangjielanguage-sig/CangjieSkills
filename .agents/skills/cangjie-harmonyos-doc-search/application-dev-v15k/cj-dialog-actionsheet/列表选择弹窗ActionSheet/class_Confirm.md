## class Confirm

```cangjie
public class Confirm {
    public Confirm(
        public var value: String,
        public var action: () -> Unit,
        public var enabled!: Bool = true,
        public var defaultFocus!: Bool = false,
        public var style!: DialogButtonStyle = DialogButtonStyle.DEFAULT
    )
}
```

**功能：** 确认Button的使能状态、默认焦点、按钮风格、文本内容和点击回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var action

```cangjie
public var action:() -> Unit
```

**功能：** Button选中时的回调。

**类型：** ()->Unit

**读写能力：** 可读写

**起始版本：** 19

### var defaultFocus

```cangjie
public var defaultFocus: Bool = false
```

**功能：** 设置Button是否是默认焦点。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var enabled

```cangjie
public var enabled: Bool = true
```

**功能：** 点击Button是否响应。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var style

```cangjie
public var style: DialogButtonStyle = DialogButtonStyle.DEFAULT
```

**功能：** 设置Button的风格样式。

**类型：** [DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle)

**读写能力：** 可读写

**起始版本：** 19

### var value

```cangjie
public var value: String
```

**功能：** Button文本内容。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Confirm(String, () -> Unit, Bool, Bool, DialogButtonStyle)

```cangjie
public Confirm(
    public var value: String,
    public var action: () -> Unit,
    public var enabled!: Bool = true,
    public var defaultFocus!: Bool = false,
    public var style!: DialogButtonStyle = DialogButtonStyle.HIGHLIGHT
) {}
```

**功能：** 按钮参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数:**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | String | 是 | \- | Button文本内容。 |
| action | () -> Unit | 是 | \- | Button选中时的回调。 |
| enabled | Bool | 否 | true | **命名参数。**  点击Button是否响应，true表示Button可以响应，false表示Button不可以响应 |
| defaultFocus | Bool | 否 | false | **命名参数。**  设置Button是否是默认焦点，true表示Button是默认焦点，false表示Button不是默认焦点。 |
| style | [DialogButtonStyle](./cj-common-types.md#enum-dialogbuttonstyle) | 否 | DialogButtonStyle.DEFAULT | **命名参数。**  设置Button的风格样式。 |