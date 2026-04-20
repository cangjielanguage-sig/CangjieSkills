### func startAbilityByCall(Want)

```cangjie
public func startAbilityByCall(want: Want): Caller
```

**功能：** 跨设备场景下，启动指定Ability至前台或后台，同时获取其Caller通信接口，调用方可使用Caller与被启动的Ability进行通信。仅支持在主线程调用。 该接口不支持拉起启动模式为specified模式的UIAbility。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](#class-want)|是|-|传入需要启动的Ability的信息，包含abilityName、moduleName、bundleName、deviceId、parameters(可选)，parameters缺省或为空表示后台启动Ability。|

**返回值：**

|类型|说明|
|:----|:----|
|[Caller](#class-caller)|获取要通讯的caller对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|The application does not have permission to call the interface.|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.|
  |16000001|The specified ability does not exist.|
  |16000002|Incorrect ability type.|
  |16000004|Failed to start the invisible ability.|
  |16000006|Cross-user operations are not allowed.|
  |16000008|The crowdtesting application expires.|
  |16000011|The context does not exist.|
  |16000012|The application is controlled.|
  |16000013|The application is controlled by EDM.|
  |16000018|Redirection to a third-party application is not allowed in API version 11 or later.|
  |16000050|Internal error.|
  |16000071|App clone is not supported.|
  |16000072|App clone or multi-instance is not supported.|
  |16000073|The app clone index is invalid.|
  |16000076|The APP_INSTANCE_KEY is invalid.|
  |16000077|The number of app instances reaches the limit.|
  |16000078|The multi-instance is not supported.|
  |16000079|The APP_INSTANCE_KEY cannot be specified.|
  |16000080|Creating a new instance is not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let want = Want(bundleName: "com.example.myservice", moduleName: 'entry', abilityName: "EntryAbility",
    parameters: ##"{"ohos.aafwk.param.callAbilityToForeground":true}"##) // parameters是一个json格式的字符串
let caller = uiAbilityContext.startAbilityByCall(want)
```