### func onConfigurationUpdate(AbilityConfiguration)

```cangjie
public open func onConfigurationUpdate(newConfig: AbilityConfiguration): Unit
```

**功能：** 当系统配置更新时调用。仅当前formExtensionAbility存活时更新配置才会触发此生命周期。需要注意：formExtensionAbility创建后10秒内无操作将会被清理。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newConfig|[AbilityConfiguration](../AbilityKit/cj-apis-ability.md#class-abilityconfiguration)|是|-|表示需要更新的配置信息。|

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*
import kit.UIKit.AppLog

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onConfigurationUpdate(newConfig: AbilityConfiguration) {
        AppLog.info(ExampleFormExtensionAbility onConfigurationUpdate ${newConfig.language}, ${newConfig.colorMode}")
    }
}
```

### func onFormEvent(String, String)

```cangjie
public open func onFormEvent(formId: String, message: String): Unit
```

**功能：** 卡片提供方接收处理卡片事件的通知接口。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|formId|String|是|-|请求触发事件的卡片标识。|
|message|String|是|-|事件消息。|

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*
import kit.UIKit.AppLog

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onFormEvent(formId: String, message: String): Unit {
        AppLog.info("ExampleFormExtensionAbility onFormEvent ${formId}, ${message}")
    }
}
```

### func onRemoveForm(String)

```cangjie
public open func onRemoveForm(formId: String): Unit
```

**功能：** 卡片提供方接收销毁卡片的通知接口。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|formId|String|是|-|请求销毁的卡片标识。|

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*
import kit.UIKit.AppLog

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onRemoveForm(formId: String): Unit {
        AppLog.info("ExampleFormExtensionAbility onRemoveForm: ${formId}")
    }
}
```

### func onStop()

```cangjie
public open func onStop(): Unit
```

**功能：** 当卡片提供方的卡片进程退出时，触发该回调。

**系统能力：** SystemCapability.Ability.Form

**起始版本：** 20

**示例：**

<!-- compile -->

```cangjie
import ohos.form.form_extension_ability
import kit.FormKit.*
import kit.UIKit.AppLog

let FORM_EXT_ABILITY_REGISTER_RESULT = FormExtensionAbility.registerCreator("ExampleFormExtensionAbility",
    {=> ExampleFormExtensionAbility()})

class ExampleFormExtensionAbility <: FormExtensionAbility {
    public override func onStop() {
        AppLog.info("ExampleFormExtensionAbility onStop")
    }
}
```