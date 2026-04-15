### func terminateSelf()

```cangjie
public func terminateSelf(): Unit
```

**功能：** 销毁UIAbility自身。仅支持在主线程调用。

> **说明：**
>
> 调用该接口后，任务中心的任务默认不会被清理。如需清理，请进行配置。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[元能力子系统错误码](./cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000009 | An ability cannot be started or stopped in Wukong mode. |
  | 16000011 | The context does not exist. |
  | 16000050 | Internal error. |

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*
import kit.ArkUI.WindowStage

class MyUIAbility22 <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
            this.context.terminateSelf()
    }
}
```

### func terminateSelfWithResult(AbilityResult)

```cangjie
public func terminateSelfWithResult(parameter: AbilityResult): Unit
```

**功能：** 销毁UIAbility自身。仅支持在主线程调用。

仅当UIAbility通过[startAbilityForResult](#func-startabilityforresultwant-asynccallbackabilityresult)接口拉起时，调用terminateSelfWithResult接口销毁UIAbility，才会返回结果给调用方。

> **说明：**
>
> 调用该接口后，任务中心的任务默认不会被清理。如需清理，请进行配置。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parameter|[AbilityResult](./cj-apis-ability-ability_result.md#class-abilityresult)|是|-|返回给startAbilityForResult&nbsp;接口调用方的相关信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[元能力子系统错误码](./cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000009 | An ability cannot be started or stopped in Wukong mode. |
  | 16000011 | The context does not exist. |
  | 16000050 | Internal error. |

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*
import kit.ArkUI.WindowStage

class MyUIAbility23 <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
            this.context.terminateSelfWithResult(AbilityResult(0))
    }
}
```