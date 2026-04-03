func f3(){
    // 观察者可以在实时回调函数onReceive中处理订阅事件
    var condition = TriggerCondition(row: 1, size: 100)
    let watcher= Watcher("watcher", triggerCondition: condition,
             onTrigger: {row, size, holder =>
                Hilog.info(0, "HiAppEnvent", "HiAppEvent onTrigger: curRow=${row}, curSize=${size}")},
             onReceive: {domain, AppEventGroups =>
                Hilog.info(0, "HiAppEnvent", "domain =${domain}")
                let groupSize = AppEventGroups.size
                for (i in 0..groupSize) {
                    Hilog.info(0, "HiAppEnvent", "name =${AppEventGroups[i].name}")
                    let appInfosize = AppEventGroups[i].appEventInfos.size
                    for (j in 0..appInfosize) {
                        Hilog.info(0, "HiAppEnvent", "appEventInfo name=${AppEventGroups[i].appEventInfos[j].name}")
                        Hilog.info(0, "HiAppEnvent", "appEventInfo domain=${AppEventGroups[i].appEventInfos[j].domain}")
                        Hilog.info(0, "HiAppEnvent", "appEventInfo event=${AppEventGroups[i].appEventInfos[j].event.value}")
                        let paSize = AppEventGroups[i].appEventInfos[j].params.size
                        for (k in 0..paSize) {
                            Hilog.info(0, "HiAppEnvent", "key=${AppEventGroups[i].appEventInfos[j].params[k].key}")
                            let value = AppEventGroups[i].appEventInfos[j].params[k].value.value
                            Hilog.info(0, "HiAppEnvent", "value=${value}")
                        }
                    }
                }
            })
    HiAppEvent.addWatcher(watcher)
}

f1()
f2()
f3()
```