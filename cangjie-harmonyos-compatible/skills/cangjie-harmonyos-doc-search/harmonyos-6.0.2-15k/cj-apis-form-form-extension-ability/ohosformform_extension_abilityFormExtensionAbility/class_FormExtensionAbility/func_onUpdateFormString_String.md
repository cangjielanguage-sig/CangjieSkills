### func onUpdateForm(String, String)

```cangjie
public open func onUpdateForm(formId: String, wantParams: String): Unit
```

**功能：** 卡片提供方接收携带参数的更新卡片的通知接口。获取最新数据后调用formProvider的[updateForm](cj-apis-form-form-provider.md#static-func-updateformstring-formbindingdata)接口刷新卡片数据。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|formId|String|是|-|请求更新的卡片ID。|
|wantParams|String|是|-|更新参数。|

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*
import kit.UIKit.AppLog

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onUpdateForm(formId: String, wantParams: String): Unit {
        AppLog.info("ExampleFormExtensionAbility onUpdateForm ${formId}, ${wantParams}")
    }
}
```