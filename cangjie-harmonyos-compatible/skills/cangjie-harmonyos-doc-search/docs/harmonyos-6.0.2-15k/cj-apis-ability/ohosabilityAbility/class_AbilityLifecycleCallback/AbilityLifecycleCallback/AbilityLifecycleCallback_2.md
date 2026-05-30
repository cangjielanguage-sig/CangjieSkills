|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onAbilityCreate|([UIAbility](#class-uiability))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在ability创建时触发回调。|
|onWindowStageCreate|([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在windowStage创建时触发回调。|
|onWindowStageActive|([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在windowStage获焦时触发回调。|
|onWindowStageInactive|([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在windowStage失焦时触发回调。|
|onWindowStageDestroy|([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在windowStage销毁时触发回调。|
|onAbilityDestroy|([UIAbility](#class-uiability))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在ability销毁时触发回调。|
|onAbilityForeground|([UIAbility](#class-uiability))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在ability的状态从后台转到前台时触发回调。|
|onAbilityBackground|([UIAbility](#class-uiability))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在ability的状态从前台转到后台时触发回调。|
|onAbilityContinue|([UIAbility](#class-uiability))->Unit|是|-| **命名参数。** 注册监听应用上下文的生命周期后，在ability迁移时触发回调。|
|onAbilityWillCreate|?([UIAbility](#class-uiability))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的[onCreate](#func-oncreate)触发前回调。|
|onWindowStageWillCreate|?([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的[onWindowStageCreate](#func-onwindowstagecreatewindowstage)触发前回调。|
|onWindowStageWillDestroy|?([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的[onWindowStageDestroy](#func-onwindowstagedestroy)触发前回调。|
|onAbilityWillForeground|?([UIAbility](#class-uiability))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的[onForeground](#func-onforeground)触发前回调。|
|onAbilityWillDestroy|?([UIAbility](#class-uiability))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的[onDestroy](#func-ondestroy)触发前回调。|
|onAbilityWillBackground|?([UIAbility](#class-uiability))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的[onBackground](#func-onbackground)触发前回调。|
|onWillNewWant|?([UIAbility](#class-uiability))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的[onNewWant](#func-onnewwantwant-launchparam)触发前回调。|
|onNewWant|?([UIAbility](#class-uiability))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的[onNewWant](#func-onnewwantwant-launchparam)触发后回调。|
|onAbilityWillContinue|?([UIAbility](#class-uiability))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的onContinue触发前回调。|
|onWindowStageWillRestore|?([UIAbility](#class-uiability), [WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage))->Unit|否|None| **命名参数。** 注册监听应用上下文的生命周期后，在Ability的onWindowStageRestore触发前回调。|
|onWindowStageResto