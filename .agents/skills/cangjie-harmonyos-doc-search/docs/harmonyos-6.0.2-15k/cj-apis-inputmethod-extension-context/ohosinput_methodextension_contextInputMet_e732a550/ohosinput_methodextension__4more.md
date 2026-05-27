# ohos.input_method.extension_context（InputMethodExtensionContext）

InputMethodExtensionContext模块是InputMethodExtensionAbility的上下文环境，继承于ExtensionContext，提供InputMethodExtensionAbility具有的能力和接口，包括启动、停止、绑定、解绑Ability。

## 导入模块

```cangjie
import kit.IMEKit.*
```

## 使用说明

在使用[InputMethodExtensionContext](#class-inputmethodextensioncontext)的功能前，需要通过[InputMethodExtensionAbility](./cj-apis-inputmethod-extension-ability.md#class-inputmethodextensionability)子类的[context](./cj-apis-inputmethod-extension-ability.md#prop-context)属性获取。实现[InputMethodExtensionAbility](./cj-apis-inputmethod-extension-ability.md#class-inputmethodextensionability)子类的方式请参见[InputMethodExtensionAbility使用说明](./cj-apis-inputmethod-extension-ability.md#使用说明)。

## class InputMethodExtensionContext

```cangjie
public class InputMethodExtensionContext <: ExtensionContext
```

**功能：** InputMethodExtensionContext是[InputMethodExtensionAbility](./cj-apis-inputmethod-extension-ability.md#class-inputmethodextensionability)的上下文环境，继承自[ExtensionContext](../AbilityKit/cj-apis-ability.md#class-extensioncontext)。InputMethodExtensionContext提供[InputMethodExtensionAbility](./cj-apis-inputmethod-extension-ability.md#class-inputmethodextensionability)具有的接口和能力。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**父类型：**

- [ExtensionContext](../AbilityKit/cj-apis-ability.md#class-extensioncontext)

### func destroy()

```cangjie
public func destroy(): Unit
```

**功能：** 销毁输入法应用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**示例：**

<!-- compile -->

```cangjie
import kit.IMEKit.{InputMethodExtensionAbility, InputMethodExtensionContext}
import kit.AbilityKit.Want
import ohos.base.BusinessException

let InputMethod_ABILITY_REGISTER_RESULT = InputMethodExtensionAbility.registerCreator("ExampleAbility") {
    ExampleAbility()
}

class ExampleAbility <: InputMethodExtensionAbility {
    public func onCreate(want: Want): Unit {
        AppLog.info("ExampleAbility oncreate success")
    }

    public func onDestroy(): Unit {
        AppLog.info("ExampleAbility onDestroy success")
        this.context.destroy()
    }
}
```