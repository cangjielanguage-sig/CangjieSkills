## class UIAbility

```cangjie
public open class UIAbility <: Ability {}
```

**功能：** 表示包含UI界面的应用组件，提供组件创建、销毁、前后台切换等生命周期回调，同时也具备后台通信能力。

- Caller：由startAbilityByCall接口返回，CallerAbility(调用者)可使用Caller与CalleeAbility(被调用者)进行通信。

- Callee：UIAbility的内部对象，CalleeAbility(被调用者)可以通过Callee与Caller进行通信。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**父类型：**

- [Ability](#class-ability)

### prop context

```cangjie
public mut prop context: UIAbilityContext
```

**功能：** 提供UIAbility运行所需的上下文环境。

**类型：** [UIAbilityContext](#class-uiabilitycontext)

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility7 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let context = this.context
    }
}
```

### prop lastRequestWant

```cangjie
public mut prop lastRequestWant: Want
```

**功能：** 最近一次拉起UIAbility请求的Want参数。

当UIAbility被首次创建并拉起时，取值为[onCreate](#func-oncreatewant-launchparam)接收到的Want参数。

当UIAbility被再次拉起时，取值为[onNewWant](#func-onnewwantwant-launchparam)最近一次接收到的Want参数。

**类型：** [Want](./cj-apis-app-ability-want.md#class-want)

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility8 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let lastRequestWant = this.lastRequestWant
    }
}
```

### prop launchWant

```cangjie
public mut prop launchWant: Want
```

**功能：** UIAbility冷启动时接收到的Want参数，取值为[onCreate](#func-oncreatewant-launchparam)接收到的Want参数。

**类型：** [Want](./cj-apis-app-ability-want.md#class-want)

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility9 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let launchWant = this.launchWant
    }
}
```

### func onBackground()

```cangjie
public open func onBackground(): Unit
```

**功能：** 当应用从前台转入到后台时，系统触发该回调。开发者可在该回调中实现UI不可见时的资源释放操作，如停止定位功能等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility10 <: UIAbility {
    public override func onBackground() {
        let launchWant = this.launchWant
    }
}
```