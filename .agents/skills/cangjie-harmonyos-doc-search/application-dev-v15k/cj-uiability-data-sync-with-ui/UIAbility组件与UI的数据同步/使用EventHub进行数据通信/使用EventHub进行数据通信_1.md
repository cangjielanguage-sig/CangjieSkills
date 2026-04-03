## 使用EventHub进行数据通信

[EventHub](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-eventhub.md)为[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)组件提供了事件机制，使它们能够进行订阅、取消订阅和触发事件等数据通信能力。

在[基类Context](cj-application-context-stage.md)中，提供了EventHub对象，可用于在UIAbility组件实例内通信。使用EventHub实现Ability与UI之间的数据通信需要先获取EventHub对象，本章节将以此为例进行说明。

1. 在Ability中调用[eventHub.on()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-eventhub.md#func-oneventcallback0)方法注册一个自定义事件“event1”，eventHub.on()有如下两种调用方式，使用其中一种即可。

    ```cangjie
    import ohos.base.AppLog
    import kit.ArkUI.WindowStage
    import kit.AbilityKit.{UIAbility, UIAbilityContext, Context, Want, LaunchParam, EventCallBack0, EventCallBack1,
        EventCallBack2}

    var globalContext: ?UIAbilityContext = None

    class EventFunc0 <: EventCallBack0 {
        public override func invoke() {
            AppLog.info("1.")
        }
    }

    class EventFunc1 <: EventCallBack1<String> {
        public override func invoke(argOne: String) {
            AppLog.info("1. ${argOne}")
        }
    }

    class EventFunc2 <: EventCallBack2<String, String> {
        public override func invoke(argOne: String, argTwo: String) {
            AppLog.info("1. ${argOne}, ${argTwo}")
        }
    }

    class MainAbility <: UIAbility {
        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            // 获取eventHub
            let eventhub = this.context.eventhub
            // 执行订阅操作
            eventhub.obtainEvent0("event0").on(EventFunc0())
            let eventFunc1 = EventFunc1()
            eventhub.obtainEvent1<String>("event1").on(eventFunc1)
            let eventFunc2 = EventFunc2()
            eventhub.obtainEvent2<String, String>("event2").on(eventFunc2)
            AppLog.info("Ability onCreate")
        }

        public override func onWindowStageCreate(windowStage: WindowStage): Unit {
            // Main window is created, set main page for this ability
            globalContext = this.context
            windowStage.loadContent("EntryView")
        }
        // ...
    }
    ```

2. 在UI中通过[emit()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-eventhub.md#func-emit)方法触发该事件，在触发事件的同时，根据需要传入参数信息。

    ```cangjie
    import kit.AbilityKit.{UIAbilityContext, Want}
    import ohos.base.{AppLog, BusinessException}

    func getContext(): UIAbilityContext {
        return globalContext.getOrThrow()
    }

    func eventHubFunc(context: UIAbilityContext): Unit {
        // 不带参数触发自定义“event1”事件
        context.eventhub.get0("event0").emit()
        // 带1个参数触发自定义“event1”事件
        context.eventhub.get1<String>("event1").emit("1")
        // 带2个参数触发自定义“event1”事件
        context.eventhub.get2<String, String>("event2").emit("2", "test")
        // 开发者可以根据实际的业务场景设计事件传递的参数
    }

    @Entry
    @Component
    class EntryView {
        func build() {
            Row {
                Column {
                    Text("EventHubFuncA").fontSize(50).fontWeight(FontWeight.Bold).onClick {
                        evt =>
                        let context = getContext()
                        eventHubFunc(context)
                    }
                    Text("EventHubFuncB").fontSize(50).fontWeight(FontWeight.Bold).onClick {
                        evt =>
                        let context = getContext()
                        context.eventhub.get0("event0").off()
                        context.eventhub.get1<String>("event1").off()
                        context.eventhub.get2<String, String>("event2").off()
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

3. 在Ability的注册事件回调中可以得到对应的触发事件结果，运行日志结果如下所示。

    ```json
    [Example].[Entry].[EntryAbility] 1.
    [Example].[Entry].[EntryAbility] 1. 1
    [Example].[Entry].[EntryAbility] 1. 2, test
    ```

4. 在自定义事件“event1”使用完成后，可以根据需要调用[off()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-eventhub.md#func-off)方法取消该事件的订阅。