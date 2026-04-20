## class ActionMenuOptions

```cangjie
public open class ActionMenuOptions {
    public ActionMenuOptions(
        public let title!: String = '',
        public let buttons!: Array<ButtonInfo>,
        public let showInSubWindow!: Bool = false,
        public let isModal!: Bool = true
    )
}
```

**功能：** 操作菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let title

```cangjie
public let title: String = ""
```

**功能：** 表示标题文本。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let buttons

```cangjie
public let buttons: Array<ButtonInfo>
```

**功能：** 表示菜单中菜单项按钮的数组，结构为：ButtonInfo("button", Color.BLACK)，支持1-6个按钮。按钮数量大于6个时，仅显示前6个按钮，之后的按钮不显示。

**类型：** Array\<[ButtonInfo](#class-buttoninfo)>

**读写能力：** 只读

**起始版本：** 19

### let showInSubWindow

```cangjie
public let showInSubWindow: Bool = false
```

**功能：** 表示某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isModal

```cangjie
public let isModal: Bool = true
```

**功能：** 表示弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### ActionMenuOptions(String, Array\<ButtonInfo>, Bool, Bool)

```cangjie
public ActionMenuOptions(
    public let title!: String = '',
    public let buttons!: Array<ButtonInfo>,
    public let showInSubWindow!: Bool = false,
    public let isModal!: Bool = true
)
```

**功能：** 构造一个ActionMenuOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|否|""| **命名参数。** 标题文本。|
|buttons|Array\<[ButtonInfo](#class-buttoninfo)>|是|-| **命名参数。** 菜单中菜单项按钮的数组，结构为：ButtonInfo("button",Color.BLACK)，支持1-6个按钮。按钮数量大于6个时，仅显示前6个按钮，之后的按钮不显示。|
|showInSubWindow|Bool|否|false| **命名参数。** 某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。默认弹窗显示在应用内，而非独立子窗口。<br>**说明：** <br> - showInSubWindow 为 true 的弹窗无法触发显示另一个 showInSubWindow 为 true 的弹窗。|
|isModal|Bool|否|true| **命名参数。** 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。默认弹窗有蒙层。|