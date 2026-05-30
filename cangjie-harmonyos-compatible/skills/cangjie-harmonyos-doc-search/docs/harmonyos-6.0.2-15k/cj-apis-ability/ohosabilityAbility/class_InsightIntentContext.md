## class InsightIntentContext

```cangjie
public class InsightIntentContext {}
```

**功能：** 意图调用执行上下文，意图调用执行上下文是意图调用执行基类的属性，为意图调用执行基类提供基础能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

### func startAbility(Want)

```cangjie
public func startAbility(want: Want): Unit
```

**功能：** 提供意图调用执行上下文，意图调用执行上下文是意图调用执行基类的属性，为意图调用执行基类提供基础能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](#class-want)|是|-|启动Ability的want信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  | 16000001 | The specified ability does not exist. |
  | 16000004 | Cannot start an invisible component. |
  | 16000005 | The specified process does not have the permission. |
  | 16000006 | Cross-user operations are not allowed. |
  | 16000008 | The crowdtesting application expires. |
  | 16000009 | An ability cannot be started or stopped in Wukong mode. |
  | 16000011 | The context does not exist.        |
  | 16000012 | The application is controlled.        |
  | 16000013 | The application is controlled by EDM.       |
  | 16000050 | Internal error. |
  | 16000053 | The ability is not on the top of the UI. |
  | 16000055 | Installation-free timed out. |
  | 16000061 | Operation not supported. |
  | 16200001 | The caller has been released. |

**示例：**

<!-- compile -->

```cangjie
import kit.AbilityKit.{InsightIntentExecutor, ExecuteResult, InsightIntentContext, Want}
import ohos.base.{AppLog, BusinessException}

let INTENT_REGISTER_RESULT = InsightIntentExecutor.registerCreator("MyInsightIntentExecutor",
    {=> MyInsightIntentExecutor()})

class MyInsightIntentExecutor <: InsightIntentExecutor {
    public override func onExecuteInUIAbilityForegroundMode(name: String, param: String, windowStage: WindowStage): ExecuteResult {
        AppLog.info("MyInsightIntentExecutor onExecuteInUIAbilityForegroundMode.")
        try {
            this.context.startAbility(Want(bundleName: "com.example.cangjieinsight", abilityName: "testAbility"))
        } catch (e: BusinessException) {
            AppLog.error(" error  ${e.message}")
        }
        windowStage.loadContent("EntryView2")
        return ExecuteResult(22, result: ##"{"message":"cangjieinsighttest"}"##, uris: ["test1", "test2"], flags: 22)
    }
}
```