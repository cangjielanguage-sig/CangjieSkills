## specified启动模式

specified启动模式为指定实例模式，针对一些特殊场景使用（例如文档应用中每次新建文档希望都能新建一个文档实例，重复打开一个已保存的文档希望打开的都是同一个文档实例）。

**图3** 指定实例启动模式原理

![uiability-launch-type3-principle](figures/uiability-launch-type3-principle.png)

假设应用有两个[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例，即EntryAbility和SpecifiedAbility。EntryAbility以specified模式启动SpecifiedAbility。基本原理如下：

1. EntryAbility调用[startAbility()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitywant)方法，并在[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)的parameters字段中设置唯一的Key值，用于标识SpecifiedAbility。
2. 系统在拉起SpecifiedAbility之前，会先进入对应的[AbilityStage](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilitystage)的[onAcceptWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onacceptwantwant)生命周期回调，获取用于标识目标UIAbility的Key值。
3. 系统会根据获取的Key值来匹配UIAbility。
    - 如果匹配到对应的UIAbility，则会启动该UIAbility实例，并进入[onNewWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onnewwantwant-launchparam)生命周期回调。
    - 如果无法匹配对应的Ability，则会创建一个新的Ability实例，并进入该Ability实例的[onCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-oncreatewant-launchparam)生命周期回调和[onWindowStageCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onwindowstagecreatewindowstage)生命周期回调。

**图4** 指定实例模式演示效果

<img src="./figures/uiability-launch-type3.gif" style="zoom:90%">

1. 在SpecifiedAbility中，需要将[module.json5配置文件](../cj-start/basic-knowledge/module-configuration-file.md)的`launchType`字段配置为`specified`。

   ```json
   {
     "module": {
       // ...
       "abilities": [
         {
           "launchType": "specified",
           // ...
         }
       ]
     }
   }
   ```

2. 在EntryAbility中，调用[startAbility()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitywant)方法时，可以在[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)参数中传入了自定义参数`instanceKey`作为唯一标识符，以此来区分不同的Ability实例。示例中`instanceKey`的value值设置为字符串'KEY'。示例中的context的获取方式见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

    ```cangjie
    // 在启动指定实例模式的UIAbility时，给每一个UIAbility实例配置一个独立的Key标识
    // 例如在文档使用场景中，可以用文档路径作为Key标识
    import kit.UIKit.Button
    import ohos.base.{BusinessException, AppLog}
    import kit.AbilityKit.{Want, UIAbilityContext}
    import std.collection.HashMap

    // 见获取UIAbility的上下文信息章节
    func getContext(): UIAbilityContext {
        return globalContext.getOrThrow()
    }

    func getInstance(): String {
        return 'KEY'
    }