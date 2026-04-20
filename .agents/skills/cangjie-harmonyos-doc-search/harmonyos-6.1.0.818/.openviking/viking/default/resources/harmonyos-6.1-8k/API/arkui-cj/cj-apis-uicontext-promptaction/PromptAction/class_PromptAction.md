## class PromptAction

```cangjie
public class PromptAction {}
```

**功能：** PromptAction类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func closeCustomDialog(Int32)

```cangjie
public func closeCustomDialog(dialogId: Int32): Unit
```

**功能：** 关闭自定义对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dialogId|Int32|是|-|要关闭的对话框ID，由openCustomDialog返回。|

### func openCustomDialog(CustomDialogOptions, (Int32) -> Unit)

```cangjie
public func openCustomDialog(options: CustomDialogOptions, callBack: (Int32) -> Unit): Unit
```

**功能：** 打开自定义对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[CustomDialogOptions](#class-customdialogoptions)|是|-|自定义对话框选项。|
|callBack|(Int32) -> Unit|是|-|回调函数。|

### func showActionMenu(ActionMenuOptions, ShowActionMenuCallBack)

```cangjie
public func showActionMenu(option: ActionMenuOptions, callback!: ShowActionMenuCallBack = defaultCallback)
```

**功能：** 在给定设置中显示操作菜单。此API使用异步回调返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|option|[ActionMenuOptions](#class-actionmenuoptions)|是|-| 操作菜单选项。|
|callback|[ShowActionMenuCallBack](#type-showactionmenucallback)|否|defaultCallback| **命名参数。** 用于返回操作菜单响应结果的回调。defaultCallback表示{_: Option\<BusinessException>, _: Option\<Int32> =>}|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码|说明|
  |:----|:----|
  |100001|Internal error: failed to allocate memory.|

### func showDialog(ShowDialogOptions, ShowDialogCallBack)

```cangjie
public func showDialog(option: ShowDialogOptions, callback!: ShowDialogCallBack = defaultCallback)
```

**功能：** 在给定设置中显示对话框。此API使用异步回调返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|option|[ShowDialogOptions](#class-showdialogoptions)|是|-| 对话框选项。|
|callback|[ShowDialogCallBack](#type-showdialogcallback)|否|defaultCallback|**命名参数。** 用于返回对话框响应结果的回调。defaultCallback表示{_: Option\<BusinessException>, _: Option\<Int32> =>}|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码|说明|
  |:----|:----|
  |100001|Internal error: failed to allocate memory.|

### func showToast(ShowToastOptions)

```cangjie
public func showToast(option: ShowToastOptions): Unit
```

**功能：** 在给定设置中显示Toast。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|option|[ShowToastOptions](#class-showtoastoptions)|是|-|Toast选项。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  |错误码|说明|
  |:----|:----|
  |100001|Internal error: failed to allocate memory.|