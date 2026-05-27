#### 被动保存和恢复

被动保存和恢复依赖恢复框架底层触发，无需注册监听ErrorObserver callback，只需实现Ability的onSaveState接口数据保存和onCreate接口数据恢复流程即可。

```cangjie
import kit.AbilityKit.*

var abilityWant: Want = Want()

public class EntryAbility <: UIAbility {
    var storage: LocalStorage = LocalStorage()
    public override func onCreate(want: Want, launchParam: LaunchParam) {
        AppLog.info("[Demo] EntryAbility onCreate")
        abilityWant = want
        match (launchParam.launchReason) {
            case LaunchReason.APP_RECOVERY =>
                this.storage = LocalStorage()
                if (want.parameters != "") {
                    let recoveryData = want.parameters
                    this.storage.setOrCreate("myData", recoveryData)
                }
            case _ => AppLog.error("APP_RECOVERY")
        }
    }

    func onSaveState(state: StateType, wantParams: HashMap<String, String>) {
        // Ability has called to save app data
        AppLog.info("[Demo] EntryAbility onSaveState")
        wantParams["myData"] = "my1234567"
        return OnSaveResult.ALL_AGREE
    }
}
```

#### 故障Ability的重启恢复标记

发生故障的Ability再次重新启动时，在调度onCreate生命周期里，参数want的parameters成员会有[ABILITY_RECOVERY_RESTART](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#ability_recovery_restart)标记数据，并且值为true。

```cangjie
import kit.AbilityKit.*

public class EntryAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam) {
        if (want.parameters == "") {
            return
        }
        if (want.parameters.contains("ABILITY_RECOVERY_RESTART: true")) {
            AppLog.info("This ability need to recovery")
        }
    }
}
```