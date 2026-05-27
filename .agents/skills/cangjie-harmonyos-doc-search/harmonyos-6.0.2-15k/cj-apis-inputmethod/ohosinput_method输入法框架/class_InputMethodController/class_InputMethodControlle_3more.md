## class InputMethodController

```cangjie
public class InputMethodController {}
```

**功能：** 下列API示例中都需使用[getController](#func-getcontroller)获取到InputMethodController实例，再通过实例调用对应方法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### func attach(Bool, TextConfig)

```cangjie
public func attach(showKeyboard: Bool, textConfig: TextConfig): Unit
```

**功能：** 自绘控件绑定输入法。

> **说明：**
>
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|showKeyboard|Bool|是|-|绑定输入法成功后，是否拉起输入法键盘。<br>- true表示拉起。<br>- false表示不拉起。|
|textConfig|[TextConfig](#class-textconfig)|是|-|编辑框的配置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
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
let textConfig = TextConfig(inputAttribute: InputAttribute(TextInputType.TEXT, EnterKeyType.NONE))
controller.attach(true, textConfig)
```

### func attach(Bool, TextConfig, RequestKeyboardReason)

```cangjie
public func attach(showKeyboard: Bool, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Unit
```

**功能：** 自绘控件绑定输入法。

> **说明：**
>
> 需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|showKeyboard|Bool|是|-|绑定输入法成功后，是否拉起输入法键盘。<br>- true表示拉起。<br>- false表示不拉起。|
|textConfig|[TextConfig](#class-textconfig)|是|-|编辑框的配置信息。|
|requestKeyboardReason|[RequestKeyboardReason](#enum-requestkeyboardreason)|是|-|请求键盘输入原因。|

**异常：**

- BusinessException：对应错误码如下表，详见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

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
let textConfig = TextConfig(inputAttribute: InputAttribute(TextInputType.TEXT, EnterKeyType.NONE))
controller.attach(true, textConfig, RequestKeyboardReason.Touch)
```