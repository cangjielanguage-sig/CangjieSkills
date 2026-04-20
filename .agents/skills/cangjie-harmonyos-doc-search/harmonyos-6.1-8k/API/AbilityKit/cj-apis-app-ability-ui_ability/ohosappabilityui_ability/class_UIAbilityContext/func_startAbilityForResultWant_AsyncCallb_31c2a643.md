### func startAbilityForResult(Want, AsyncCallback\<AbilityResult>)

```cangjie
public func startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): Unit
```

**功能：** 启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。仅支持在主线程调用。

UIAbility被启动后，有如下情况：

- 在正常情况下，可以通过调用[terminateSelfWithResult](#func-terminateselfwithresultabilityresult)接口销毁自身，并将结果返回给调用方。

- 在异常情况下，如杀死UIAbility，会将异常结果返回给调用方，异常结果中resultCode为-1。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](./cj-apis-app-ability-want.md#class-want)|是|-|启动Ability的必要信息。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<[AbilityResult](./cj-apis-ability-ability_result.md#class-abilityresult)>|是|-| 执行结果回调函数。|

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
  | 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
  | 16000019 | No matching ability is found. |
  | 16000050 | Internal error. |
  | 16000053 | The ability is not on the top of the UI. |
  | 16000055 | Installation-free timed out. |
  | 16000071 | App clone is not supported. |
  | 16000072 | App clone or multi-instance is not supported. |
  | 16000073 | The app clone index is invalid. |
  | 16000076 | The app instance key is invalid. |
  | 16000077 | The number of app instances reaches the limit. |
  | 16000078 | The multi-instance is not supported. |
  | 16000079 | The APP_INSTANCE_KEY cannot be specified. |
  | 16000080 | Creating a new instance is not supported. |
  | 16200001 | The caller has been released. |

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*
import kit.ArkUI.WindowStage
import ohos.business_exception.BusinessException

class MyUIAbility20 <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
            this.context.startAbilityForResult(
                Want(bundleName: "com.example.cangjieinsight", abilityName: "testAbility"),
                {err: ?BusinessException, data: ?AbilityResult => })
    }
}
```