## 启动应用内的UIAbility并获取返回结果

在一个EntryAbility启动另外一个FuncAbility时，希望在被启动的FuncAbility完成相关业务后，能将结果返回给调用方。例如在应用中将入口功能和账号登录功能分别设计为两个独立的[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)，在账号登录Ability中完成登录操作后，需要将登录的结果返回给入口Ability。

1. 在EntryAbility中，调用[startAbilityForResult()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilityforresultwant-asynccallbackabilityresult)接口启动FuncAbility，异步回调中的data用于接收FuncAbility停止自身后返回给EntryAbility的信息。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

    ```cangjie
    import kit.UIKit.Button
    import ohos.base.{BusinessException, AppLog, AsyncError}
    import kit.AbilityKit.{Want, UIAbilityContext, AbilityResult}
    import std.collection.HashMap
    import encoding.json.{JsonValue, JsonObject, JsonString}

    const RESULT_CODE: Int32 = 1001
    // 见获取UIAbility的上下文信息章节
    func getContext(): UIAbilityContext {
        return globalContext.getOrThrow()
    }

    var resultCallback = {
        errorCode: Option<AsyncError>, data: Option<AbilityResult> => match (errorCode) {
            case Some(e) => AppLog.info("callback error: errcode is ${e.code}")
            case _ => match (data) {
                case Some(value) => if (value.resultCode == RESULT_CODE) {
                    let infoJSobj = JsonValue.fromStr(value.want.parameters).asObject()
                    let map = infoJSobj.getFields()
                    let info = ((map.get("info") ?? JsonString("")) as JsonString ?? JsonString("")).getValue()
                    AppLog.info("startAbilityForResult get info: ${info}")
                }
                case _ => AppLog.info("callback data is null")
            }
        }
    }

    @Entry
    @Component
    class PageAbilityComponentsInteractive {
        func build() {
            Row {
                Column {
                    Button().onClick {
                        evt =>
                        // context为调用方Ability的AbilityContext
                        let context = getContext()
                        let parametersMap = HashMap<String, JsonValue>()
                        parametersMap.add("info", JsonString("来自EntryAbility PageAbilityComponentsInteractive页面"))
                        let want = Want(
                            deviceId: "", // deviceId为空表示本设备
                            bundleName: "com.samples.stagemodelabilitydevelop",
                            abilityName: "FuncAbilityA",
                            moduleName: "entry", // moduleName非必选
                            // 自定义信息
                            parameters: JsonObject(parametersMap).toString()
                        )
                        try {
                            context.startAbilityForResult(want, resultCallback)
                        } catch (e: BusinessException) {
                            AppLog.error("Failed to start FuncAbility. Code is ${e.code}, message is ${e.message}")
                        }
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

2. 在FuncAbility停止自身时，需要调用[terminateSelfWithResult()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-terminateselfwithresultabilityresult)方法，入参[abilityResult](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#struct-abilityresult)为FuncAbility需要返回给EntryAbility的信息。

    ```cangjie
    import kit.UIKit.Button
    import ohos.base.{BusinessException, AppLog}
    import kit.AbilityKit.{UIAbilityContext, AbilityResult}
    import std.collection.HashMap
    import encoding.json.{JsonValue, JsonObject, JsonString}

    const RESULT_CODE_A: Int32 = 1001

    // 见获取UIAbility的上下文信息章节
    func getFuncAbilityAContext(): UIAbilityContext {
        return globalFuncAbilityAContext.getOrThrow()
    }