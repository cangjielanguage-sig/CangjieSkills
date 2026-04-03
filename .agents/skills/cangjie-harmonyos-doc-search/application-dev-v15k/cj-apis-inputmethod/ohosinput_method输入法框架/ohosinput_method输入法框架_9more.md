# ohos.input_method（输入法框架）

本模块主要面向普通前台应用（备忘录、信息、设置等系统应用与三方应用），提供对输入法（输入法应用）的控制、管理能力，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表等等。

## 导入模块

```cangjie
import kit.IMEKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## 权限列表

ohos.permission.CONNECT_IME_ABILITY

## const MAX_TYPE_NUM

```cangjie
public const MAX_TYPE_NUM: Int32 = 0x7F
```

**功能：** 可支持的最大输入法个数。

**类型：** Int32

**起始版本：** 19

## func getController()

```cangjie
public func getController(): InputMethodController
```

**功能：** 获取客户端实例[InputMethodController](#class-inputmethodcontroller)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[InputMethodController](#class-inputmethodcontroller)|返回当前客户端实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12800006|input method controller error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let inputMethodController = getController()
```

## func getCurrentInputMethod()

```cangjie
public func getCurrentInputMethod(): InputMethodProperty
```

**功能：** 获取当前输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[InputMethodProperty](#class-inputmethodproperty)|返回当前输入法属性对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let currentIme = getCurrentInputMethod()
```

## func getCurrentInputMethodSubtype()

```cangjie
public func getCurrentInputMethodSubtype(): InputMethodSubtype
```

**功能：** 获取当前输入法的子类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[InputMethodSubtype](#class-inputmethodsubtype)|返回当前输入法子类型对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let sub = getCurrentInputMethodSubtype()
```

## func getDefaultInputMethod()

```cangjie
public func getDefaultInputMethod(): InputMethodProperty
```

**功能：** 获取默认输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[InputMethodProperty](#class-inputmethodproperty)|返回默认输入法属性对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |12800008|input method manager service error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IMEKit.*

let defaultIme = getDefaultInputMethod()
```