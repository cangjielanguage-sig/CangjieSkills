### func changeSelection(String, Int32, Int32)

```cangjie
public func changeSelection(text: String, start: Int32, end: Int32): Unit
```

**功能：** 当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|整个输入文本。|
|start|Int32|是|-|所选文本的起始位置。|
|end|Int32|是|-|所选文本的结束位置。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |12800003|input method client error.|
  |12800008|input method manager service error.|
  |12800009|input method client is detached.|

- IllegalStateException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |unknown code|未知的错误码。|联系仓颉团队处理。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let controller = getController()
controller.changeSelection("text", 0, 5)
```

### func detach()

```cangjie
public func detach(): Unit
```

**功能：** 自绘控件解除与输入法的绑定。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12800003|input method client error.|
  |12800008|input method manager service error.|

- IllegalStateException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |unknown code|未知的错误码。|联系仓颉团队处理。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let controller = getController()
controller.detach()
```

### func hideSoftKeyboard()

```cangjie
public func hideSoftKeyboard(): Unit
```

**功能：** 隐藏输入法软键盘。

> **说明：**
>
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT_IME_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|permissions check fails.|
  |12800003|input method client error.|
  |12800008|input method manager service error.|

- IllegalStateException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |unknown code|未知的错误码。|联系仓颉团队处理。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let controller = getController()
controller.hideSoftKeyboard()
```