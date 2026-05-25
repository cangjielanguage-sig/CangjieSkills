## class InputMethodSetting

```cangjie
public class InputMethodSetting {}
```

**功能：** 下列API均需使用[getSetting](#func-getsetting)获取到InputMethodSetting实例后，通过实例调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### func getAllInputMethods()

```cangjie
public func getAllInputMethods(): Array<InputMethodProperty>
```

**功能：** 获取所有输入法应用列表。同步接口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[InputMethodProperty](#class-inputmethodproperty)>|返回所有输入法列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12800001|bundle manager error.|
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

let setting = getSetting()
setting.getAllInputMethods()
```

### func getInputMethods(Bool)

```cangjie
public func getInputMethods(enable: Bool): Array<InputMethodProperty>
```

**功能：** 获取已激活/未激活的输入法应用列表。

> **说明：**
>
> 已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。
> 已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enable|Bool|是|-|true表示返回已激活输入法列表，false表示返回未激活输入法列表。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[InputMethodProperty](#class-inputmethodproperty)>|返回已激活/未激活输入法列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |12800001|bundle manager error.|
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

let setting = getSetting()
setting.getInputMethods(true)
```

### func listCurrentInputMethodSubtype()

```cangjie
public func listCurrentInputMethodSubtype(): Array<InputMethodSubtype>
```

**功能：** 查询当前输入法应用的所有子类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[InputMethodSubtype](#class-inputmethodsubtype)>|返回当前输入法应用的所有子类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12800001|package manager error.|
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

let setting = getSetting()
setting.listCurrentInputMethodSubtype()
```