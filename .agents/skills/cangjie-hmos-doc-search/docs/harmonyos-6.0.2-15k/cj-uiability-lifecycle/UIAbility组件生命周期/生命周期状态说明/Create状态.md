### Create状态

Create状态为在应用加载过程中，[UIAbility](../../../cj-apis-ability/.overview.md)实例创建完成时触发，系统会调用[onCreate()](../../../cj-apis-ability/.overview.md)回调。可以在该回调中进行页面初始化操作，例如变量定义资源加载等，用于后续的UI展示。

```cangjie
internal import kit.AbilityKit.UIAbility
internal import kit.AbilityKit.Want

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        // 页面初始化
    }
    // ...
}
```

> **说明：**
>
> [Want](../../../cj-apis-ability/.overview.md)是对象间信息传递的载体，可以用于应用组件间的信息传递。Want的详细介绍请参见[信息传递载体Want](cj-want-overview.md)。