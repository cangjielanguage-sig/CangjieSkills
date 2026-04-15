### static func addWatcher(Watcher)

```cangjie
public static func addWatcher(watcher: Watcher): Option<AppEventPackageHolder>
```

**功能：** 添加事件观察者。可通过事件观察者的回调函数监听事件。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|watcher|[Watcher](#class-watcher)|是|-|事件观察者。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<[AppEventPackageHolder](#class-appeventpackage)>|订阅数据持有者，订阅失败时返回None。|

**异常：**

- BusinessException：对应错误码如下表，详见[应用事件打点错误码](./cj-errorcode-hiappevent.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 11102001 | Invalid watcher name. Possible causes: 1. Contain invalid characters; 2. Length is invalid. |
  | 11102002 | Invalid filtering event domain. Possible causes: 1. Contain invalid characters; 2. Length is invalid. |
  | 11102003 | Invalid row value. Possible caused by the row value is less than zero. |
  | 11102004 | Invalid size value. Possible caused by the size value is less than zero. |
  | 11102005 | Invalid timeout value. Possible caused by the timeout value is less than zero. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*

func f1() {
    // 如果观察者传入了回调的相关参数，则可以选择在自动触发的回调函数中对订阅事件进行处理
    var condition = TriggerCondition(row: 1)
    var appEventFilter = [AppEventFilter("button")]
    var watcher = Watcher(
        "watcher1",
        triggerCondition: condition,
        onTrigger: Some(
            {
                row, size, holder =>
                    Hilog.info(0, "AppLogCj", "HiAppEvent onTrigger: curRow=${row}, curSize=${size}", "")
                    while (let Some(v) <- holder.takeNext()) {
                        let eventPkg = v
                        Hilog.info(0, "AppLogCj", "HiAppEvent packageId=${eventPkg.packageId}", "")
                        Hilog.info(0, "AppLogCj", "HiAppEvent row=${eventPkg.row}", "")
                        Hilog.info(0, "AppLogCj", "HiAppEvent size=${eventPkg.size}", "")
                        for (i in 0..eventPkg
                                .data
                                .size) {
                            Hilog.info(0, "AppLogCj", "HiAppEvent info=${eventPkg.data[i]}", "")
                        }
                    }
            }
        )
    )
    HiAppEvent.addWatcher(watcher)
}

func f2() {
    // 如果观察者未传入回调的相关参数，则可以选择使用返回的holder对象手动去处理订阅事件
    let watcher = Watcher("watcher2")
    let holder = HiAppEvent.addWatcher(watcher)
    if (let Some(v1) <- holder) {
        while (let Some(v2) <- v1.takeNext()) {
            let eventPkg = v2
            Hilog.info(0, "test_hiAppEvent_addWatcher", "HiAppEvent packageId=${eventPkg.packageId}", "")
            Hilog.info(0, "test_hiAppEvent_addWatcher", "HiAppEvent row=${eventPkg.row}", "")
            Hilog.info(0, "test_hiAppEvent_addWatcher", "HiAppEvent size=${eventPkg.size}", "")
            for (i in 0..eventPkg
                    .data
                    .size) {
                Hilog.info(0, "test_hiAppEvent_addWatcher", "HiAppEvent info=${eventPkg.data[i]}", "")
            }
        }
    }
}