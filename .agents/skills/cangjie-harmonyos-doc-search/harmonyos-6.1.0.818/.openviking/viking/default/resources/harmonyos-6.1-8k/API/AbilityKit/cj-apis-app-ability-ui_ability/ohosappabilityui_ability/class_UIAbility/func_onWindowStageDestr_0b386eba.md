### func onWindowStageDestroy()

```cangjie
public open func onWindowStageDestroy(): Unit
```

**功能：** 当WindowStage销毁后，系统触发该回调。该回调用于通知开发者WindowStage对象已被销毁，不能再继续使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility16 <: UIAbility {
    public override func onWindowStageDestroy(): Unit {}
}
```