## class InsightIntentExecutor

```cangjie
public open class InsightIntentExecutor
```

**功能：** 提供意图调用执行基类，开发者通过意图调用执行基类对接端侧意图框架，实现响应意图调用的业务逻辑。开发者接入意图框架时，在意图配置文件中声明对接的意图名称、意图接入方式等，系统根据用户交互和开发者的意图配置文件进行意图调用，触发相应的意图调用执行回调。

### prop context

```cangjie
public prop context: InsightIntentContext
```

**功能：** 意图调用执行上下文。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [InsightIntentContext](#class-insightintentcontext)

**读写能力：** 只读

**起始版本：** 20

### static func registerCreator(String, () -> InsightIntentExecutor)

```cangjie
public static func registerCreator(name: String, creator: () -> InsightIntentExecutor): Unit
```

**功能：** 注册InsightIntentExecutor的对应的creator。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|注册InsightIntentExecutor对应的名称。|
|creator|()->[InsightIntentExecutor](#class-insightintentexecutor)|是|-|注册InsightIntentExecutor的对应的creator。|

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

### func onExecuteInUIAbilityBackgroundMode(String, String)

```cangjie
public open func onExecuteInUIAbilityBackgroundMode(name: String, param: String): ExecuteResult
```

**功能：** 当意图调用是将UIAbility在后台拉起时，触发该回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|意图调用名称。|
|param|String|是|-|意图调用参数。|

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
    public override func onExecuteInUIAbilityBackgroundMode(name: String, param: String): ExecuteResult {
        AppLog.info("MyInsightIntentExecutor onExecuteInUIAbilityBackgroundMode.")

        return ExecuteResult(234, result: ##"{"message":"cangjieinsighttestback"}"##, uris: ["test1", "test2"],
            flags: 22)
    }
}
```