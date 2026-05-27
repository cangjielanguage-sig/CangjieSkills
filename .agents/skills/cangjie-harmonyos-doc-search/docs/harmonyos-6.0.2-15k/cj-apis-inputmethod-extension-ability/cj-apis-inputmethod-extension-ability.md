# ohos.input_method.extension_ability（InputMethodExtensionAbility）

本模块支持开发者自行开发输入法应用，以及管理输入法应用的生命周期。

## 导入模块

```cangjie
import kit.IMEKit.*
```

## 使用说明

在开发输入法应用时，开发者需要定义[InputMethodExtensionAbility](#class-inputmethodextensionability)的子类，依据场景需要实现[onCreate](#func-oncreatewant)和[onDestroy](#func-ondestroy)方法，并使用[registerCreator](#static-func-registercreatorstring----inputmethodextensionability)注册该子类。

如下所示，新建“example_ability.cj”文件：

```cangjie
// example_ability.cj

import kit.IMEKit.{InputMethodExtensionAbility, InputMethodExtensionContext}
import kit.AbilityKit.Want

let InputMethod_ABILITY_REGISTER_RESULT = InputMethodExtensionAbility.registerCreator("ExampleAbility") {
    ExampleAbility()
}

class ExampleAbility <: InputMethodExtensionAbility {
    public func onCreate(want: Want): Unit {
        AppLog.info("ExampleAbility oncreate success")
    }

    public func onDestroy(): Unit {
        AppLog.info("ExampleAbility onDestroy success")
    }
}
```

## class InputMethodExtensionAbility

```cangjie
public open class InputMethodExtensionAbility
```

**功能：** 输入法拓展能力类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

### prop context

```cangjie
public prop context: InputMethodExtensionContext
```

**功能：** 获取InputMethodExtensionAbility的上下文环境。

**类型：** [InputMethodExtensionContext](./cj-apis-inputmethod-extension-context.md#class-inputmethodextensioncontext)

**读写能力：** 只读

**起始版本：** 20

### static func registerCreator(String, () -> InputMethodExtensionAbility)

```cangjie
public static func registerCreator(name: String, creator: () -> InputMethodExtensionAbility): Unit
```

**功能：** 注册[InputMethodExtensionAbility](#class-inputmethodextensionability)的对应的creator。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|注册InputMethodExtensionAbility扩展类型的名称。|
|creator|()->[InputMethodExtensionAbility](#class-inputmethodextensionability)|是|-|注册InputMethodExtensionAbility的对应的 creator。|

**示例：**

<!-- compile -->

```cangjie
// example_ability.cj

import kit.IMEKit.InputMethodExtensionAbility

let InputMethod_ABILITY_REGISTER_RESULT = InputMethodExtensionAbility.registerCreator("ExampleAbility") {
    ExampleAbility()
}
```

## func onCreate(Want)

```cangjie
public open func onCreate(want: Want): Unit
```

**功能：** 拉起输入法应用时触发回调，执行初始化输入法应用操作。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](../AbilityKit/cj-apis-ability.md#class-want)|是|-|当前Extension相关的Want类型信息，包括ability名称、bundle名称等。|

**示例：**

详见本文[使用说明](#使用说明)。

## func onDestroy()

```cangjie
public open func onDestory(): Unit
```

**功能：** 销毁输入法应用时触发回调，执行资源清理等操作。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**示例：**

详见本文[使用说明](#使用说明)。
