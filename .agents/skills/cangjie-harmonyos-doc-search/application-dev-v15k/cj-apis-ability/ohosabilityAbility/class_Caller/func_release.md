### func release()

```cangjie
public func release(): Unit
```

**功能：** 主动释放通用组件服务端的通信接口。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16200001|The caller has been released.|
  |16200002|The callee does not exist.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let want = Want(bundleName: "com.example.myservice", moduleName: 'entry',
    abilityName: "EntryAbility", parameters: ##"{"ohos.aafwk.param.callAbilityToForeground":true}"##) // parameters是一个json格式的字符串
let caller = uiAbilityContext.startAbilityByCall(want)
try {
    caller.release()
} catch (e: BusinessException) {
    AppLog.error("Caller release error: ${e.message}.")
}
```