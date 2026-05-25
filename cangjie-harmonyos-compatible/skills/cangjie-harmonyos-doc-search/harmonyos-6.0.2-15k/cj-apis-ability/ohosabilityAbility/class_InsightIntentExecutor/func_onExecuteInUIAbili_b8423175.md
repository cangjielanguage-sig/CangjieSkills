### func onExecuteInUIAbilityForegroundMode(String, String, WindowStage)

```cangjie
public open func onExecuteInUIAbilityForegroundMode(name: String, param: String, pageLoader: WindowStage): ExecuteResult
```

**功能：** 当意图调用是将UIAbility在前台显示时，触发该回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|意图调用名称。|
|param|String|是|-|意图调用参数。|
|pageLoader|[WindowStage](../../arkui-cj/cj-apis-window.md#class-windowstage)|是|-|页面加载器。|

**返回值：**

|类型|说明|
|:----|:----|
|[ExecuteResult](#class-executeresult)|意图调用执行结果。|

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
        windowStage.loadContent("EntryView2")
        return ExecuteResult(22, result: ##"{"message":"cangjieinsighttest"}"##, uris: ["test1", "test2"], flags: 22)
    }
}
```