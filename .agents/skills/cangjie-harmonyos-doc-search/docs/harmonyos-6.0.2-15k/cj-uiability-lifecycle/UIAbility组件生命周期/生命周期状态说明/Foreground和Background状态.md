### Foreground和Background状态

Foreground和Background状态分别在[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例切换至前台和切换至后台时触发，对应于[onForeground()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onforeground)回调和[onBackground()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onbackground)回调。

`onForeground()`回调，在UIAbility的UI可见之前，如UIAbility切换至前台时触发。可以在`onForeground()`回调中申请系统需要的资源，或者重新申请在`onBackground()`中释放的资源。

`onBackground()`回调，在UIAbility的UI完全不可见之后，如UIAbility切换至后台时候触发。可以在`onBackground()`回调中释放UI不可见时无用的资源，或者在此回调中执行较为耗时的操作，例如状态保存等。

例如应用在使用过程中需要使用用户定位时，假设应用已获得用户的定位权限授权。在UI显示之前，可以在`onForeground()`回调中开启定位功能，从而获取到当前的位置信息。

当应用切换到后台状态，可以在`onBackground()`回调中停止定位功能，以节省系统的资源消耗。

```cangjie
import kit.AbilityKit.UIAbility

class MainAbility <: UIAbility {
    // ...

    public override func onForeground(): Unit {
        // 申请系统需要的资源，或者重新申请在onBackground()中释放的资源
    }

    public override func onBackground(): Unit {
        // 释放UI不可见时无用的资源，或者在此回调中执行较为耗时的操作
        // 例如状态保存等
    }
}
```

当应用的UIAbility实例已创建，且UIAbility配置为[singleton](cj-uiability-launch-type.md#singleton启动模式)启动模式时，再次调用[startAbility()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitywant)方法启动该UIAbility实例时，只会进入该UIAbility的[onNewWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onnewwantwant-launchparam)回调，不会进入其[onCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-oncreatewant-launchparam)和[onWindowStageCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onwindowstagecreatewindowstage)生命周期回调。应用可以在该回调中更新要加载的资源和数据等，用于后续的UI展示。

```cangjie
import kit.AbilityKit.{UIAbility, Want, LaunchParam}

class MainAbility <: UIAbility {
    // ...
    public override func onNewWant(want: Want, launchParam: LaunchParam): Unit {
        // 更新资源、数据
    }
}
```