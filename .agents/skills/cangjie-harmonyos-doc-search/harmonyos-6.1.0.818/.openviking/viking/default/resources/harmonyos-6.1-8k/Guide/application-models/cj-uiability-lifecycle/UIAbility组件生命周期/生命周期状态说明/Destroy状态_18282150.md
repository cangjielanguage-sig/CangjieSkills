### Destroy状态

Destroy状态在[UIAbility](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)实例销毁时触发。可以在onDestroy()回调中进行系统资源的释放、数据的保存等操作。

例如，调用[terminateSelf()](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#func-terminateself)方法停止当前UIAbility实例，执行onDestroy()回调，并完成UIAbility实例的销毁。

<!--RP1-->
再比如，用户使用最近任务列表关闭该UIAbility实例，执行onDestroy()回调，并完成UIAbility实例的销毁。

> **说明：**
>
> 当在开发者模式下调试某个应用时，如果用户从最近任务列表移除了该调试应用的一个任务，则该调试应用的进程会被强制销毁。

<!--RP1End-->

<!-- compile -->

```cangjie
import kit.AbilityKit.UIAbility

class MainAbility <: UIAbility {
    // ...

    public override func onDestroy(): Unit {
        // 系统资源的释放、数据的保存等
    }
}
```