## class UIAbilityContext

```cangjie
public open class UIAbilityContext <: Context {}
```

**功能：** UIAbilityContext是[UIAbility](#class-uiability)组件的上下文。

每个UIAbility组件实例化时，系统都会自动创建对应的UIAbilityContext。开发者可以通过UIAbilityContext获取组件信息AbilityInfo、获取应用信息ApplicationInfo、拉起其他UIAbility、连接系统服务、销毁UIAbility等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**父类型：**

- [Context](./cj-apis-app-ability-ui_ability.md#class-context)

### func isTerminating()

```cangjie
public func isTerminating(): Bool
```

**功能：** 查询UIAbility是否处于消亡中状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示是否处于消亡中状态。true表示处于消亡中状态，false表示不处于消亡中状态。|

**异常：**

- BusinessException：对应错误码如下表，详见[元能力子系统错误码](./cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000011 | The context does not exist. |

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*
import kit.ArkUI.WindowStage

class MyUIAbility17 <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        let isTerminating = this.context.isTerminating()
    }
}
```

### func requestDialogService(Want, AsyncCallback\<RequestResult>)

```cangjie
public func requestDialogService(want: Want, result: AsyncCallback<RequestResult>): Unit
```

**功能：** 启动一个支持模态弹框的ServiceExtensionAbility。ServiceExtensionAbility被启动后，应用弹出模态弹框。仅支持在主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](./cj-apis-app-ability-want.md#class-want)|是|-|启动ServiceExtensionAbility的Want信息。|
|result|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<[RequestResult](./cj-apis-app-ability-dialog_request.md#class-requestresult)>|是|-| 回调函数，当启动一个支持模态弹框的ServiceExtensionAbility成功，err中code为0，data为模态弹框请求结果；否则err会返回对应的错误码和错误信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码说明文档](../cj-errorcode-universal.md)和[元能力子系统错误码](./cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | The application does not have permission to call the interface. |
  | 16000001 | The specified ability does not exist. |
  | 16000002 | Incorrect ability type. |
  | 16000004 | Cannot start an invisible component. |
  | 16000005 | The specified process does not have the permission. |
  | 16000006 | Cross-user operations are not allowed. |
  | 16000008 | The crowdtesting application expires. |
  | 16000009 | An ability cannot be started or stopped in Wukong mode. |
  | 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
  | 16000011 | The context does not exist. |
  | 16000012 | The application is controlled. |
  | 16000013 | The application is controlled by EDM. |
  | 16000050 | Internal error. |
  | 16000053 | The ability is not on the top of the UI. |
  | 16000055 | Installation-free timed out. |
  | 16200001 | The caller has been released. |

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*
import kit.ArkUI.WindowStage
import ohos.business_exception.BusinessException

class MyUIAbility18 <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        this.context.requestDialogService(Want(), {err: ?BusinessException, data: ?RequestResult => })
    }
}
```