## class FormExtensionAbility

```cangjie
public open class FormExtensionAbility {}
```

**功能：** 卡片扩展类。包含卡片提供方接收创建卡片、修改可见性等的通知接口。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

### prop context

```cangjie
public prop context: FormExtensionContext
```

**功能：** 获取FormExtensionAbility的上下文环境。

**类型：** [FormExtensionContext](#class-formextensioncontext)

**读写能力：** 只读

**起始版本：** 20

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onAddForm(want: Want): FormBindingData {
        let context = this.context
        return FormBindingData("")
    }
}
```

### static func registerCreator(String, () -> FormExtensionAbility)

```cangjie
public static func registerCreator(name: String, creator: () -> FormExtensionAbility): Unit
```

**功能：** 注册[FormExtensionAbility](#class-formextensionability)的对应的creator。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|注册FormExtensionAbility的名称。|
|creator|()->[FormExtensionAbility](#class-formextensionability)|是|-|注册FormExtensionAbility的对应的 creator。|

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onAddForm(want: Want): FormBindingData {
        return FormBindingData("")
    }
}
```

### func onAcquireFormState(Want)

```cangjie
public open func onAcquireFormState(want: Want): FormState
```

**功能：** 卡片提供方接收查询卡片状态通知接口，默认返回卡片初始状态(该方法可以选择性重写)。

**系统能力：**  SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](../AbilityKit/cj-apis-ability.md#class-want)|是|-|want表示获取卡片状态的描述。描述包括Bundle名称、能力名称、模块名称、卡片名和卡片维度。|

**返回值：**

|类型|说明|
|:----|:----|
|[FormState](cj-apis-form-form-info.md#enum-formstate)|返回卡片状态枚举。|

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onAcquireFormState(want: Want): FormState {
        return FormState.Default
    }
}
```