### func onAddForm(Want)

```cangjie
public open func onAddForm(want: Want): FormBindingData
```

**功能：** 卡片提供方接收创建卡片的通知接口。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](../AbilityKit/cj-apis-ability.md#class-want)|是|-|当前卡片相关的Want类型信息，包括卡片ID、卡片名称、卡片样式等。这些卡片信息必须作为持久数据进行管理，以便后续更新和删除卡片。|

**返回值：**

|类型|说明|
|:----|:----|
|[FormBindingData](../FormKit/cj-apis-app-form-formBindingData.md#class-formbindingdata)|formBindingData.FormBindingData对象，卡片要显示的数据。|

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

### func onCastToNormalForm(String)

```cangjie
public open func onCastToNormalForm(formId: String): Unit
```

**功能：** 卡片提供方接收临时卡片转常态卡片的通知接口。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|formId|String|是|-|请求转换为常态的卡片标识。|

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*
import kit.UIKit.AppLog

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onCastToNormalForm(formId: String): Unit {
        AppLog.info("ExampleFormExtensionAbility onCastToNormalForm ${formId}")
    }
}
```

### func onChangeFormVisibility(HashMap\<String,Int32>)

```cangjie
public open func onChangeFormVisibility(newStatus: HashMap<String, Int32>): Unit
```

**功能：** 卡片提供方接收修改可见性的通知接口。该接口仅对系统应用生效，且需要将formVisibleNotify配置为true。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newStatus|HashMap\<String,Int32>|是|-|请求修改的卡片标识和可见状态。|

**示例：**

<!-- compile -->

```cangjie
import std.collection.HashMap
import ohos.form.form_extension_ability
import kit.FormKit.*
import kit.UIKit.AppLog

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onChangeFormVisibility(newStatus: HashMap<String, Int32>): Unit {
        AppLog.info("ExampleFormExtensionAbility onChangeFormVisibility ${newStatus}")
    }
}
```