### AbilityMonitor(String, String, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit)

```cangjie
public AbilityMonitor(
    public var abilityName: String,
    public var moduleName!: String = "",
    public var onAbilityCreate!: ?(UIAbility) -> Unit = None,
    public var onAbilityForeground!: ?(UIAbility) -> Unit = None,
    public var onAbilityBackground!: ?(UIAbility) -> Unit = None,
    public var onAbilityDestroy!: ?(UIAbility) -> Unit = None,
    public var onWindowStageCreate!: ?(UIAbility) -> Unit = None,
    public var onWindowStageRestore!: ?(UIAbility) -> Unit = None,
    public var onWindowStageDestroy!: ?(UIAbility) -> Unit = None
)
```

**功能：** 构造一个[AbilityMonitor](#class-abilitymonitor)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityName|String|是|-|当前[AbilityMonitor](#class-abilitymonitor)绑定的ability名称。|
|moduleName|String|否|""| **命名参数。** 当前[AbilityMonitor](#class-abilitymonitor)绑定的模块名称。|
|onAbilityCreate|?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit|否|None| **命名参数。** ability被启动初始化时的回调函数。None即不设置该属性，则不能收到该生命周期回调。|
|onAbilityForeground|?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit|否|None| **命名参数。** ability状态变成前台时的回调函数。None即不设置该属性，则不能收到该生命周期回调。|
|onAbilityBackground|?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit|否|None| **命名参数。** ability状态变成后台时的回调函数。None即不设置该属性，则不能收到该生命周期回调。|
|onAbilityDestroy|?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit|否|None| **命名参数。** ability被销毁前的回调函数。None即不设置该属性，则不能收到该生命周期回调。|
|onWindowStageCreate|?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit|否|None| **命名参数。** windowStage被创建时的回调函数。None即不设置该属性，则不能收到该生命周期回调。|
|onWindowStageRestore|?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit|否|None| **命名参数。** windowStage被重载时的回调函数。None即不设置该属性，则不能收到该生命周期回调。|
|onWindowStageDestroy|?([UIAbility](../AbilityKit/cj-apis-ability.md#class-uiability)) -> Unit|否|None| **命名参数。** windowStage销毁前调用的回调函数。None即不设置该属性，则不能收到该生命周期回调。|