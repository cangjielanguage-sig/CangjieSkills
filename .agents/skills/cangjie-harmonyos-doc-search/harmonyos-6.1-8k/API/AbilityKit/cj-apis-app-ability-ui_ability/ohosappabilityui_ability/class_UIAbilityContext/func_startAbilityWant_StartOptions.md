### func startAbility(Want, ?StartOptions)

```cangjie
public func startAbility(want: Want, options!: ?StartOptions = None): Unit
```

**功能：** 启动一个UIAbility。仅支持在主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](./cj-apis-app-ability-want.md#class-want)|是|-|启动UIAbility的必要信息。|
|options|?[StartOptions](./cj-apis-app-ability-start_options.md#class-startoptions)|否|None|**命名参数。** 启动UIAbility所携带的参数。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码说明文档](../cj-errorcode-universal.md)和[元能力子系统错误码](./cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | The application does not have permission to call the interface. |
  | 801 | Capability not support. |
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
  | 16000067 | The StartOptions check failed. |
  | 16000068 | The ability is already running. |
  | 16000071 | App clone is not supported. |
  | 16000072 | App clone or multi-instance is not supported. |
  | 16000073 | The app clone index is invalid. |
  | 16000076 | The app instance key is invalid. |
  | 16000077 | The number of app instances reaches the limit. |
  | 16000078 | The multi-instance is not supported. |
  | 16000079 | The APP_INSTANCE_KEY cannot be specified. |
  | 16000080 | Creating a new instance is not supported. |
  | 16200001 | The caller has been released. |
  | 16300003 | The target application is not the current application. |

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*
import kit.ArkUI.WindowStage

class MyUIAbility19 <: UIAbility {
    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
            this.context.startAbility(Want(bundleName: "com.example.cangjieinsight", abilityName: "testAbility"))
    }
}
```