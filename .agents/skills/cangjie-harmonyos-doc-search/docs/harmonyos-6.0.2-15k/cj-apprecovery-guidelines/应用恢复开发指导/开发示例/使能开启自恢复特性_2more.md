### 使能开启自恢复特性

开发者需要在应用模块初始化时使能appRecovery功能。下面为示例的AbilityStage。

```cangjie
import kit.AbilityKit.*

class MyAbilityStage <: AbilityStage {
    public override func onCreate(): Unit {
        AppLog.info("[Demo] MyAbilityStage onCreate")
        enableAppRecovery(
            restart: RestartFlag.ALWAYS_RESTART,
            saveOccasion: SaveOccasionFlag.SAVE_WHEN_ERROR,
            saveMode: SaveModeFlag.SAVE_WITH_FILE
        )
    }
}
```

### 配置支持恢复的Ability

Ability的配置清单一般的名字为module.json5。

```json
{
    "abilities": [
    {
        "name": "EntryAbility",
        "recoverable": true,
    }]
}
```