### func showTextInput(RequestKeyboardReason)

```cangjie
public func showTextInput(requestKeyboardReason: RequestKeyboardReason): Unit
```

**功能：** 进入文本编辑状态。

> **说明：**
>
> 编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|requestKeyboardReason|[RequestKeyboardReason](#enum-requestkeyboardreason)|是|-|请求键盘输入原因。|

**异常：**

- BusinessException：对应错误码如下表，详见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
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
let textConfig = TextConfig(inputAttribute: InputAttribute(TextInputType.TEXT, EnterKeyType.NONE))
controller.attach(false, textConfig)
controller.showTextInput(RequestKeyboardReason.Touch)
```

### func stopInputSession()

```cangjie
public func stopInputSession(): Bool
```

**功能：** 结束输入会话。

> **说明：**
>
> 该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|结束会话成功时，返回true；否则抛出异常。|

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
controller.stopInputSession()
```

### func updateAttribute(InputAttribute)

```cangjie
public func updateAttribute(attribute: InputAttribute): Unit
```

**功能：** 更新编辑框属性信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|attribute|[InputAttribute](#class-inputattribute)|是|-|编辑框属性对象。|

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
let attribute = InputAttribute(TextInputType.TEXT, EnterKeyType.NONE)
controller.updateAttribute(attribute)
```