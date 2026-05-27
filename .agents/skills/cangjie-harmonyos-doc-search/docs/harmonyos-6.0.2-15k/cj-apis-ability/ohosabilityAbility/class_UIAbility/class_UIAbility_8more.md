## class UIAbility

```cangjie
public open class UIAbility <: BaseAbility {}
```

**功能：** UIAbility是包含UI界面的应用组件，继承自BaseAbility，提供组件创建、销毁、前后台切换等生命周期回调，同时也具备组件协同的能力。组件协同主要提供如下常用功能：

- [Caller](#class-caller)：由[startAbilityByCall](#func-startabilitybycallwant)接口返回，CallerAbility(调用者)可使用Caller与CalleeAbility(被调用者)进行通信。

- [Callee](#class-callee)：UIAbility的内部对象，CalleeAbility(被调用者)可以通过Callee与Caller进行通信。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**父类型：**

- [BaseAbility](#class-baseability)

### prop callee

```cangjie
public prop callee: Callee
```

**功能：** UIAbility内部对象，通用组件服务端注册和解除客户端caller通知送信的callback接口。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [Callee](#class-callee)

**读写能力：** 只读

**起始版本：** 19

### prop context

```cangjie
public prop context: UIAbilityContext
```

**功能：** 上下文。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [UIAbilityContext](#class-uiabilitycontext)

**读写能力：** 只读

**起始版本：** 12

### prop lastRequestWant

```cangjie
public prop lastRequestWant: Want
```

**功能：** UIAbility最后请求时的参数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [Want](#class-want)

**读写能力：** 只读

**起始版本：** 12

### prop launchWant

```cangjie
public prop launchWant: Want
```

**功能：** UIAbility启动时的参数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [Want](#class-want)

**读写能力：** 只读

**起始版本：** 12

### func onBackPressed()

```cangjie
public open func onBackPressed(): Bool
```

**功能：** UIAbility生命周期回调，当UIAbility侧滑返回时触发，根据返回值决定是否销毁UIAbility。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示UIAbility将会被移到后台不销毁，返回false表示UIAbility将正常销毁。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onBackPressed(): Bool {
        AppLog.info("onBackPressed called")
        return true
    }
}
```

### func onBackground()

```cangjie
public open func onBackground(): Unit
```

**功能：** UIAbility生命周期回调，当应用从前台转到后台时触发。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onBackground(): Unit {
        AppLog.info("onBackground called")
    }
}
```

### func onContinue(String)

```cangjie
public open func onContinue(wantParams: String): OnContinueResult
```

**功能：** 当UIAbility准备迁移时触发，保存数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|wantParams|String|是|[want](#class-want)相关参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[OnContinueResult](#enum-oncontinueresult)|接续的结果。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

class MainAbility <: UIAbility {
    public override func onContinue(wantParams: String): OnContinueResult {
        AppLog.info("MainAbility onContinue.")
        return OnContinueResult.AGREE
    }
}
```