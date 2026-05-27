### 数据保存和恢复

在使能appRecovery功能后，开发者可以在Ability中采用主动保存状态，主动恢复或者选择被动恢复的方式使用appRecovery功能。
下面为示例的EntryAbility。

#### 导包

```cangjie
import kit.AbilityKit.*
```

#### 主动触发保存和恢复

- 定义和注册[ErrorObserver](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#struct-errorobserver) callback，具体可参见[errorManager](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-errormanager)里的使用方法。

    ```cangjie
    import kit.AbilityKit.*
    import ohos.window.*
    import kit.PerformanceAnalysisKit.*

    var registerId: Int32 = -1
    let callback: ErrorObserver = ErrorObserver(
        {
            errMsg =>
            AppLog.info(errMsg)
            saveAppState()
            restartApp()
        }
    )

    public class EntryAbility <: UIAbility {
        public override func onWindowStageCreate(windowStage: WindowStage) {
            // Main window is created, set main page for this ability
            AppLog.info("[Demo] EntryAbility onWindowStageCreate")
            registerId = ErrorManager.on("error", callback)

            windowStage.loadContent("pages/index")
        }
    }
    ```

- 数据保存

    callback触发appRecovery.saveAppState()调用后，会触发EntryAbility的onSaveState(state, wantParams)函数回调。

    ```cangjie
    import kit.AbilityKit.*

    public class EntryAbility <: UIAbility {
        func onSaveState(state: StateType, wantParams: HashMap<String, String>) {
            // Ability has called to save app data
            AppLog.info("[Demo] EntryAbility onSaveState")
            wantParams["myData"] = "my1234567"
            return OnSaveResult.ALL_AGREE
        }
    }
    ```

- 数据恢复

    callback触发后appRecovery.restartApp()调用后，应用会重启，重启后会走到EntryAbility的onCreate(want, launchParam)函数，保存的数据会在want参数的parameters里。

    ```cangjie
    import kit.AbilityKit.*

    let abilityWant: Want

    public class EntryAbility <: UIAbility {
        var storage: LocalStorage = LocalStorage()

        public override func onCreate(want: Want, launchParam: LaunchParam) {
            AppLog.info("[Demo] EntryAbility onCreate")
            abilityWant = want
            match (launchParam.launchReason) {
                case LaunchReason.APP_RECOVERY =>
                    this.storage = LocalStorage()
                    if (want.parameters!="") {
                        let recoveryData = want.parameters
                        this.storage.setOrCreate("myData", recoveryData)
                    }
                case _ => AppLog.error("APP_RECOVERY")
            }
        }
    }
    ```

- 取消注册ErrorObserver callback

    ```cangjie
    import kit.AbilityKit.*

    var registerId: Int32 = -1

    class EntryAbility <: UIAbility {
        public func onWindowStageDestroy() {
            // Main window is destroyed, release UI related resources
            AppLog.info("[Demo] EntryAbility onWindowStageDestroy")

            ErrorManager.off("error", registerId)
        }
    }
    ```