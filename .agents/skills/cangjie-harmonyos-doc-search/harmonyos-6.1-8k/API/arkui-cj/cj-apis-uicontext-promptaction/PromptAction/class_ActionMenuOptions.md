## class ActionMenuOptions

```cangjie
public open class ActionMenuOptions {
    public var title: ResourceStr
    public var buttons: Array<ButtonInfo>
    public var showInSubWindow: Bool
    public var isModal: Bool
    public init(
        title!: ResourceStr = '',
        buttons!: Array<ButtonInfo>,
        showInSubWindow!: Bool = false,
        isModal!: Bool = true
    )
}
```

**功能：** 菜单操作选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var buttons

```cangjie
public var buttons: Array<ButtonInfo>
```

**功能：** 对话框中的按钮数组。

**类型：** Array\<[ButtonInfo](#class-buttoninfo)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var isModal

```cangjie
public var isModal: Bool
```

**功能：** 是否为模态对话框。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var showInSubWindow

```cangjie
public var showInSubWindow: Bool
```

**功能：** 是否在子窗口中显示。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var title

```cangjie
public var title: ResourceStr
```

**功能：** 要显示的文本标题。

**类型：** [ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(ResourceStr, Array\<ButtonInfo>, Bool, Bool)

```cangjie
public init(
    title!: ResourceStr = '',
    buttons!: Array<ButtonInfo>,
    showInSubWindow!: Bool = false,
    isModal!: Bool = true
)
```

**功能：** 菜单操作选项构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|''| **命名参数。** 要显示的文本标题。|
|buttons|Array\<[ButtonInfo](#class-buttoninfo)>|是|-| **命名参数。** 按钮数组。|
|showInSubWindow|Bool|否|false| **命名参数。** 是否在子窗口中显示。|
|isModal|Bool|否|true| **命名参数。** 是否为模态对话框。|