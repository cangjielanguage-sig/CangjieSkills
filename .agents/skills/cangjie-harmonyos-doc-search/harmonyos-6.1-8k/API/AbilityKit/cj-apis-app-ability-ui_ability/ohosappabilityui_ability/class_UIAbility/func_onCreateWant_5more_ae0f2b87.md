### func onCreate(Want, LaunchParam)

```cangjie
public open func onCreate(want: Want, launchParam: LaunchParam): Unit
```

**功能：** 当UIAbility实例创建完成时，系统会触发该回调，开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。该回调仅会在UIAbility冷启动时触发。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](./cj-apis-app-ability-want.md#class-want)|是|-|当前UIAbility的Want类型信息，包括UIAbility名称、Bundle名称等。|
|launchParam|[LaunchParam](./cj-apis-app-ability-ability_constant.md#class-launchparam)|是|-|创建 ability、上次异常退出的原因信息。|

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility11 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let launchWant = this.launchWant
    }
}
```

### func onDestroy()

```cangjie
public open func onDestroy(): Unit
```

**功能：** 当UIAbility被销毁时，系统触发该回调。开发者可以在该生命周期中执行资源清理、数据保存等相关操作。

> **说明：**
>
> 该回调仅在UIAbility正常退出时触发，当UIAbility异常退出（例如低内存终止进程）时，该回调将不被触发。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility12 <: UIAbility {
    public override func onDestroy(): Unit {}
}
```

### func onForeground()

```cangjie
public open func onForeground(): Unit
```

**功能：** 当应用首次启动到前台或者从后台转入到前台时，系统触发该回调。开发者可在该回调中实现系统所需资源的申请，如应用转到前台时申请定位服务等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility13 <: UIAbility {
    public override func onForeground(): Unit {}
}
```

### func onNewWant(Want, LaunchParam)

```cangjie
public open func onNewWant(want: Want, launchParam: LaunchParam): Unit
```

**功能：** 当已经启动的UIAbility实例再次被拉起时，系统会触发该回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](./cj-apis-app-ability-want.md#class-want)|是|-|调用方再次拉起该UIAbility时传递的数据。|
|launchParam|[LaunchParam](./cj-apis-app-ability-ability_constant.md#class-launchparam)|是|-|UIAbility启动参数，包含启动原因等。|

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility14 <: UIAbility {
    public override func onNewWant(want: Want, launchParam: LaunchParam): Unit {}
}
```

### func onWindowStageCreate(WindowStage)

```cangjie
public open func onWindowStageCreate(windowStage: WindowStage): Unit
```

**功能：** 当[WindowStage](../arkui-cj/cj-apis-window.md)实例创建完成后，系统会触发该回调。开发者可以在该回调中通过WindowStage加载页面。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowStage|WindowStage|是|-|WindowStage实例对象。|

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*
import kit.ArkUI.WindowStage

class MyUIAbility15 <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {}
}
```