## class PromptAction

```cangjie
public class PromptAction {}
```

**功能：** 创建弹窗和响应弹窗动作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func showToast(String, Int32, String, ToastShowMode)

```cangjie
public static func showToast(message!: String, duration!: Int32 = 1500, bottom!: String = "80vp", showMode!: ToastShowMode = ToastShowMode.Default): Unit
```

**功能：** 创建并显式文本提示框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|String|是|-| **命名参数。** 显示的文本信息。|
|duration|Int32|否|1500| **命名参数。** 单位ms，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。|
|bottom|String|否|"80vp"| **命名参数。** 设置弹窗底部边框距离导航条的高度，ToastShowMode.TopMost模式下，软键盘拉起时，如果bottom值过小，toast要被软键盘遮挡时，会自动避让至距离软键盘80.vp处。ToastShowMode.Default模式下，软键盘拉起时，会上移软键盘的高度。<br>**说明：**<br>当底部没有导航条时，bottom为设置弹窗底部边框距离窗口底部的高度。<br>设置对齐方式alignment后，bottom不生效。|
|showMode|[ToastShowMode](#enum-toastshowmode)|否|ToastShowMode.Default| **命名参数。** 设置弹窗是否显示在应用之上。默认显示在应用内。|

### static func showToast(ShowToastOptions)

```cangjie
public static func showToast(option: ShowToastOptions): Unit
```

**功能：** 创建并显式文本提示框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|option|[ShowToastOptions](#class-showtoastoptions)|是|-|文本提示框的选项。|

### static func showDialog(String, String, Array\<ButtonInfo>, ShowDialogCallBack)

```cangjie
public static func showDialog(title!: String = "", message!: String = "", buttons!: Array<ButtonInfo>,
    callback!: ShowDialogCallBack = defaultCallback)
```

**功能：** 创建并显示对话框，对话框响应结果异步返回。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|否|""| **命名参数。** 标题文本。|
|message|String|否|""| **命名参数。** 内容文本。|
|buttons|Array\<[ButtonInfo](#class-buttoninfo)>|是|-| **命名参数。** 对话框中按钮的数组，结构为：ButtonInfo("button", Color.BLACK)，支持大于1个按钮。|
|callback|[ShowDialogCallBack](#type-showdialogcallback)|否|defaultCallback| **命名参数。** 对话框响应结果回调。<br>**说明：**<br>i为选中按钮在buttons数组中的索引。默认值defaultCallback表示{err:Option\<AsyncError\>,i:Option\<Int32\> =>}。|

### static func showDialog(ShowDialogOptions, ShowDialogCallBack)

```cangjie
public static func showDialog(option: ShowDialogOptions, callback!: ShowDialogCallBack = defaultCallback)
```

**功能：** 创建并显示对话框，对话框响应结果异步返回。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|option|[ShowDialogOptions](#class-showdialogoptions)|是|-|页面显示对话框信息描述。|
|callback|[ShowDialogCallBack](#type-showdialogcallback)|否|defaultCallback| **命名参数。** 对话框响应结果回调。<br>**说明：**<br>i为选中按钮在buttons数组中的索引。默认值defaultCallback表示{err:Option\<AsyncError\>,i:Option\<Int32\> =>}。|