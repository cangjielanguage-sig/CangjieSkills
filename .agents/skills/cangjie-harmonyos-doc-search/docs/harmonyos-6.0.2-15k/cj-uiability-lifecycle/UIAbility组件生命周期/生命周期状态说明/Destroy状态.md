### Destroy状态

Destroy状态在[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例销毁时触发。可以在onDestroy()回调中进行系统资源的释放、数据的保存等操作。

例如，调用[terminateSelf()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-terminateself)方法停止当前UIAbility实例，执行onDestroy()回调，并完成UIAbility实例的销毁。

再比如，用户使用最近任务列表关闭该UIAbility实例，执行onDestroy()回调，并完成UIAbility实例的销毁。

```cangjie
import kit.AbilityKit.UIAbility

class MainAbility <: UIAbility {
    // ...

    public override func onDestroy(): Unit {
        // 系统资源的释放、数据的保存等
    }
}
```