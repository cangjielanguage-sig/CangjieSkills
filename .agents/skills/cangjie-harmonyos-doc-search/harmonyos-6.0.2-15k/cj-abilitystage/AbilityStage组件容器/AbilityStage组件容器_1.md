# AbilityStage组件容器

[AbilityStage](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilitystage)是一个[Module](../cj-start/basic-knowledge/application-package-overview.md#应用的多module设计机制)级别的组件容器，应用的[HAP](../cj-start/basic-knowledge/hap-package.md)在首次加载时会创建一个AbilityStage实例，可以对该Module进行初始化等操作。

AbilityStage与Module一一对应，即一个Module拥有一个AbilityStage。

DevEco Studio默认工程中已自动生成AbilityStage。如需手动新建一个AbilityStage文件，具体步骤如下。

1. 在工程Module对应的cangjie目录下，右键选择“New &gt; Cangjie File”，新建一个文件并命名为MyAbilityStage.cj。

2. 打开MyAbilityStage.cj文件，导入AbilityStage的依赖包，自定义类继承AbilityStage并加上需要的生命周期回调，示例中增加了一个[onCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-oncreate)生命周期回调。

    ```cangjie
    import kit.AbilityKit.{AbilityStage, Want}

    class MyAbilityStage <: AbilityStage {
        public override func onCreate(): Unit {
            // 应用HAP首次加载时触发，可以在此执行该Module的初始化操作（例如资源预加载、线程创建等）
        }

        public override func onAcceptWant(want: Want): String {
            // 仅specified模式下触发
            return "MyAbilityStage"
        }
    }
    ```

3. 同时，需要完成注册。

    ```cangjie
    import ohos.ability.AbilityStage

    let ENTRY_STAGE_REGISTER_RESULT = AbilityStage.registerCreator("entry", {=> MyAbilityStage()})
    ```

4. 在[module.json5配置文件](../cj-start/basic-knowledge/module-configuration-file.md)中，通过配置 `srcEntry` 参数来指定模块对应的代码路径，以作为HAP加载的入口。

    ```json
    {
      "module": {
        "name": "entry",
        "type": "entry",
        "srcEntry": "ohos_app_cangjie_entry.MyAbilityStage",
        // ...
      }
    }
    ```

[AbilityStage](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilitystage)拥有[onCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-oncreate)生命周期回调和[onAcceptWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onacceptwantwant)、[onConfigurationUpdate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onconfigurationupdateabilityconfiguration)、[onMemoryLevel()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onmemorylevelmemorylevel)事件回调。

- onCreate()生命周期回调：在开始加载对应Module的第一个[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例之前会先创建AbilityStage，并在AbilityStage创建完成之后执行其onCreate()生命周期回调。AbilityStage模块提供在Module加载的时候，通知开发者，可以在此进行该Module的初始化（如资源预加载，线程创建等）能力。

- onAcceptWant()事件回调：UIAbility[指定实例模式（specified）](cj-uiability-launch-type.md#specified启动模式)启动时候触发的事件回调，具体使用请参见[Ability启动模式综述](cj-uiability-launch-type.md)。

- onConfigurationUpdate()事件回调：当系统全局配置发生变更时触发的事件，系统语言、深浅色等，配置项目前均定义在[AbilityConfiguration](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilityconfiguration)结构体中。

- onMemoryLevel()事件回调：当系统调整内存时触发的事件。