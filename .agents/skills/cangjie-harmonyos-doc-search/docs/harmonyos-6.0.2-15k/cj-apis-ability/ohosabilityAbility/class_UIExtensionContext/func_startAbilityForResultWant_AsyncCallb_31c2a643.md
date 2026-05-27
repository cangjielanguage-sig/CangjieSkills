### func startAbilityForResult(Want, AsyncCallback\<AbilityResult>)

```cangjie
public func startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): Unit
```

**功能：** 启动一个Ability。使用callback异步回调。Ability被启动后，有如下情况：

- 正常情况下可通过调用[terminateSelfWithResult](#func-terminateselfwithresultabilityresult)接口使之终止并且返回结果给调用方。
- 异常情况下比如杀死Ability会返回异常信息给调用方, 异常信息中resultCode为-1。

- 如果被启动的Ability模式是单实例模式, 不同应用多次调用该接口启动这个Ability，当这个Ability调用[terminateSelfWithResult](#func-terminateselfwithresultabilityresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](#class-want)|是|-|启动Ability的want信息。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[AbilityResult](#struct-abilityresult)>|是|-|回调函数，返回启动Ability的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  | 201 | The application does not have permission to call the interface. |
  | 401 | Parameter error. |
  | 16000001 | The specified ability does not exist. |
  | 16000002 | Incorrect ability type. |
  | 16000004 | Failed to start the invisible ability. |
  | 16000005 | The specified process does not have the permission. |
  | 16000006 | Cross-user operations are not allowed. |
  | 16000008 | The crowdtesting application expires. |
  | 16000009 | An ability cannot be started or stopped in Wukong mode. |
  | 16000010 | The call with the continuation flag is forbidden. |
  | 16000011 | The context does not exist. |
  | 16000012 | The application is controlled.        |
  | 16000013 | The application is controlled by EDM.       |
  | 16000018 | Redirection to a third-party application is not allowed in API version 11 or later. |
  | 16000019 | No matching ability is found. |
  | 16000050 | Internal error. |
  | 16000053 | The ability is not on the top of the UI. |
  | 16000055 | Installation-free timed out. |
  | 16000069 | The extension cannot start the third party application. |
  | 16000070 | The extension cannot start the service. |
  | 16000071 | App clone is not supported. |
  | 16000072 | App clone or multi-instance is not supported. |
  | 16000073 | The app clone index is invalid. |
  | 16000076 | The APP_INSTANCE_KEY is invalid. |
  | 16000077 | The number of app instances reaches the limit. |
  | 16000078 | The multi-instance is not supported. |
  | 16000079 | The APP_INSTANCE_KEY cannot be specified. |
  | 16000080 | Creating an instance is not supported. |
  | 16000082 | The UIAbility is being started. |
  | 16200001 | The caller has been released. |