# AbilityStage组件容器

[AbilityStage](../../cj-apis-ability/.overview.md)是一个[Module](../../application-package-overview/.overview.md)级别的组件容器，应用的[HAP](../../hap-package/.overview.md)在首次加载时会创建一个AbilityStage实例，可以对该Module进行初始化等操作。

AbilityStage与Module一一对应，即一个Module拥有一个AbilityStage。

DevEco Studio默认工程中已自动生成AbilityStage。如需手动新建一个AbilityStage文件，具体步骤如下。

1. 在工程Module对应的cangjie目录下，右键选择“New &gt; Cangjie File”，新建一个文件并命名为MyAbilityStage.cj。

2. 打开MyAbilityStage.cj文件，导入AbilityStage的依赖包，自定义类继承AbilityStage并加上需要的生命周期回调，示例中增加了一个[onCreate()](../../cj-apis-ability/.overview.md)生命周期回调。

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

4. 在[module.json5配置文件](../../module-configuration-file/module-configuration-file.md)中，通过配置 `srcEntry` 参数来指定模块对应的代码路径，以作为HAP加载的入口。

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

[AbilityStage](../../cj-apis-ability/.overview.md)拥有[onCreate()](../../cj-apis-ability/.overview.md)生命周期回调和[onAcceptWant()](../../cj-apis-ability/.overview.md)、[onConfigurationUpdate()](../../cj-apis-ability/.overview.md)、[onMemoryLevel()](../../cj-apis-ability/.overview.md)事件回调。

- onCreate()生命周期回调：在开始加载对应Module的第一个[UIAbility](../../cj-apis-ability/.overview.md)实例之前会先创建AbilityStage，并在AbilityStage创建完成之后执行其onCreate()生命周期回调。AbilityStage模块提供在Module加载的时候，通知开发者，可以在此进行该Module的初始化（如资源预加载，线程创建等）能力。

- onAcceptWant()事件回调：UIAbility[指定实例模式（specified）](cj-uiability-launch-type.md#specified启动模式)启动时候触发的事件回调，具体使用请参见[Ability启动模式综述](cj-uiability-launch-type.md)。

- onConfigurationUpdate()事件回调：当系统全局配置发生变更时触发的事件，系统语言、深浅色等，配置项目前均定义在[AbilityConfiguration](../../cj-apis-ability/.overview.md)结构体中。

- onMemoryLevel()事件回调：当系统调整内存时触发的事件。