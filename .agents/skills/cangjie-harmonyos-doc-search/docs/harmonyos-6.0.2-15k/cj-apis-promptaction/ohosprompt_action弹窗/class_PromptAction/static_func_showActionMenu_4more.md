### static func showActionMenu(String, Array\<ButtonInfo>, ShowActionMenuCallBack)

```cangjie
public static func showActionMenu(title!: String = "", buttons!: Array<ButtonInfo>,
    callback!: ShowActionMenuCallBack = defaultCallback)
```

**功能：** 创建并显示操作菜单，菜单响应后异步返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|否|""| **命名参数。** 标题文本。|
|buttons|Array\<[ButtonInfo](#class-buttoninfo)>|是|-| **命名参数。** 菜单中菜单项的数组，结构为：ButtonInfo("button", Color.BLACK)，支持1-6个按钮。按钮数量大于6个时，仅显示前6个按钮，之后的按钮不显示。|
|callback|[ShowActionMenuCallBack](#type-showactionmenucallback)|否|defaultCallback| **命名参数。** 菜单响应结果回调。<br>**说明：**<br>i为选中按钮在buttons数组中的索引。默认值defaultCallback表示{err:Option\<AsyncError\>,i:Option\<Int32\> =>}。|

### static func showActionMenu(ActionMenuOptions, ShowActionMenuCallBack)

```cangjie
public static func showActionMenu(option: ActionMenuOptions, callback!: ShowActionMenuCallBack = defaultCallback)
```

**功能：** 创建并显示操作菜单，菜单响应后异步返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|option|[ActionMenuOptions](#class-actionmenuoptions)|是|-|操作菜单选项。|
|callback|[ShowActionMenuCallBack](#type-showactionmenucallback)|否|defaultCallback| **命名参数。** 菜单响应结果回调。<br>**说明：**<br>i为选中按钮在buttons数组中的索引。默认值defaultCallback表示{err:Option\<AsyncError\>,i:Option\<Int32\> =>}。|

### static func openCustomDialog(CustomDialogOptions, (Int32) -> Unit)

```cangjie
public static func openCustomDialog(options: CustomDialogOptions, callBack: (Int32)->Unit): Unit
```

**功能：** 打开自定义弹窗。

> **说明：**
>
> - 该接口仅支持设置CustomDialogOptions的maskRect，alignment，offset，isModal，showInSubWindow，builder属性，其余属性设置不生效。
> - 暂不支持isModal = true与showInSubWindow = true同时使用。
> - 弹窗宽度在设备竖屏时默认为 所在窗口宽度 - 左右margin（16.vp），最大默认宽度为400.vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[CustomDialogOptions](#class-customdialogoptions)|是|-|自定义弹窗的内容。|
|callBack|(Int32)->Unit|是|-|回调函数，返回供closeCustomDialog使用的对话框id。|

### static func openCustomDialogWithOption(CustomDialogOptions, (Int32) -> Unit)

```cangjie
public static func openCustomDialogWithOption(options: CustomDialogOptions, callBack: (Int32)->Unit): Unit
```

**功能：** 打开自定义弹窗。

> **说明：**
>
> - 暂不支持isModal = true与showInSubWindow = true同时使用。
> - 弹窗宽度在设备竖屏时默认为 所在窗口宽度 - 左右margin（16.vp），最大默认宽度为400.vp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[CustomDialogOptions](#class-customdialogoptions)|是|-|自定义弹窗的内容。|
|callBack|(Int32)->Unit|是|-|回调函数，返回供closeCustomDialog使用的对话框id。|