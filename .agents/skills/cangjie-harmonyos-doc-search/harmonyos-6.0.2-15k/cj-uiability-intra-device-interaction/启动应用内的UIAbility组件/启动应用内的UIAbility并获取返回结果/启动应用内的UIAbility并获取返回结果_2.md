@Entry
    @Component
    class PageFuncAbilityA {
        func build() {
            Row {
                Column {
                    Button("FuncAbility").onClick {
                        evt =>
                        let context = getFuncAbilityAContext()
                        let parametersMap = HashMap<String, JsonValue>()
                        parametersMap.add("info", JsonString("来自FuncAbility Index页面"))
                        let abilityResult = AbilityResult(
                            RESULT_CODE_A,
                            Want(
                                deviceId: "", // deviceId为空表示本设备
                                bundleName: "com.samples.stagemodelabilitydevelop",
                                abilityName: "FuncAbilityB",
                                moduleName: "entry", // moduleName非必选
                                // 自定义信息
                                parameters: JsonObject(parametersMap).toString()
                            )
                        )
                        try {
                            context.terminateSelfWithResult(abilityResult).get()
                        } catch (e: BusinessException) {
                            AppLog.error("Failed to start terminate self. Code is ${e.code}, message is ${e.message}")
                        }
                    }
                // ...
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

3. FuncAbility停止自身后，EntryAbility通过[startAbilityForResult()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilityforresultwant-asynccallbackabilityresult)方法回调接收被FuncAbility返回的信息，RESULT_CODE需要与前面的数值保持一致。

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