func f3() {
    // 观察者可以在实时回调函数onReceive中处理订阅事件
    var condition = TriggerCondition(row: 1, size: 100)
    let watcher = Watcher(
        "watcher",
        triggerCondition: condition,
        onTrigger: {
            row, size, holder => Hilog.info(0, "AppLogCj", "HiAppEvent onTrigger: curRow=${row}, curSize=${size}", "")
        },
        onReceive: {
            domain, AppEventGroups =>
                Hilog.info(0, "AppLogCj", "domain =${domain}")
                let groupSize = AppEventGroups.size
                for (i in 0..groupSize) {
                    Hilog.info(0, "AppLogCj", "name =${AppEventGroups[i].name}", "")
                    let appInfosize = AppEventGroups[i]
                        .appEventInfos
                        .size
                    for (j in 0..appInfosize) {
                        Hilog.info(0, "AppLogCj", "appEventInfo name=${AppEventGroups[i].appEventInfos[j].name}", "")
                        Hilog.info(0, "AppLogCj", "appEventInfo domain=${AppEventGroups[i].appEventInfos[j].domain}", "")
                        let paSize = AppEventGroups[i]
                            .appEventInfos[j]
                            .params
                            .size
                        for ((k, v) in AppEventGroups[i]
                                .appEventInfos[j]
                                .params) {
                            Hilog.info(0x0000, "HiAppEnvent", "key=${k}", "")
                            Hilog.info(0x0000, "HiAppEnvent", "value=${v.toString()}", "")
                        }
                    }
                }
        }
    )
    HiAppEvent.addWatcher(watcher)
}

func test() {
    f1()
    f2()
    f3()
}
```