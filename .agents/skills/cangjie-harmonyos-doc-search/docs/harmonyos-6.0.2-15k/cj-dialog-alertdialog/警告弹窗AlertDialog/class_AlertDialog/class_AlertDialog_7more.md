## class AlertDialog

```cangjie
public class AlertDialog {}
```

**功能：** 构造一个AlertDialog类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func show(AlertDialogParamWithConfirm)

```cangjie
public static func show(alertDialog: AlertDialogParamWithConfirm): Unit
```

**功能：** 定义并弹出警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:--- |:--- |:--- |:--- |:--- |
| alertDialog | [AlertDialogParamWithConfirm](#class-alertdialogparamwithconfirm) | 是 | - | 定义并显示AlertDialog组件。 |

### static func show(AlertDialogParamWithConfirm, ActionSheetShadowOptions)

```cangjie
public static func show(alertDialog: AlertDialogParamWithConfirm, shadow: ActionSheetShadowOptions): Unit
```

**功能：** 定义并弹出警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:--- |:--- |:--- |:--- |:--- |
| alertDialog | [AlertDialogParamWithConfirm](#class-alertdialogparamwithconfirm) | 是 | - | 定义并显示AlertDialog组件。 |
| shadow | [ActionSheetShadowOptions](./cj-dialog-actionsheet.md#class-actionsheetshadowoptions) | 是 | - | 设置弹窗背板的阴影。默认无阴影。 |

### static func show(AlertDialogParamWithConfirm, ShadowStyle)

```cangjie
public static func show(alertDialog: AlertDialogParamWithConfirm, shadow: ShadowStyle): Unit
```

**功能：** 定义并弹出警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:--- |:--- |:--- |:--- |:--- |
| alertDialog | [AlertDialogParamWithButtons](#class-alertdialogparamwithbuttons) | 是 | - | 定义并显示AlertDialog组件。 |
| shadow | [ShadowStyle](./cj-common-types.md#enum-shadowstyle) | 是 | - | 设置弹窗背板的阴影。默认无阴影。 |

### static func show(AlertDialogParamWithButtons)

```cangjie
public static func show(alertDialog: AlertDialogParamWithButtons): Unit
```

**功能：** 定义并弹出警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:--- |:--- |:--- |:--- |:--- |
| alertDialog | [AlertDialogParamWithButtons](#class-alertdialogparamwithbuttons) | 是 | - | 定义并显示AlertDialog组件。 |

### static func show(AlertDialogParamWithButtons, ActionSheetShadowOptions)

```cangjie
public static func show(alertDialog: AlertDialogParamWithButtons, shadow: ActionSheetShadowOptions): Unit
```

**功能：** 定义并弹出警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:--- |:--- |:--- |:--- |:--- |
| alertDialog | [AlertDialogParamWithButtons](#class-alertdialogparamwithbuttons) | 是 | - | 定义并显示AlertDialog组件。 |
| shadow | [ActionSheetShadowOptions](./cj-dialog-actionsheet.md#class-actionsheetshadowoptions) | 是 | - | 设置弹窗背板的阴影。默认无阴影。 |

### static func show(AlertDialogParamWithButtons, ShadowStyle)

```cangjie
public static func show(alertDialog: AlertDialogParamWithButtons, shadow: ShadowStyle): Unit
```

**功能：** 定义并弹出警告弹窗。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 参数名 | 参数类型 | 必填 | 默认值 | 描述 |
|:--- |:--- |:--- |:--- |:--- |
| alertDialog | [AlertDialogParamWithButtons](#class-alertdialogparamwithbuttons) | 是 | - | 定义并显示AlertDialog组件。 |
| shadow | [ShadowStyle](./cj-common-types.md#enum-shadowstyle) | 是 | - | 设置弹窗背板的阴影。默认无阴影。 |