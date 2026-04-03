## class AppEventPackageHolder

```cangjie
public class AppEventPackageHolder {
    public init(watcherName: String)
}
```

**功能：** 订阅数据持有者类，用于对订阅事件进行处理。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### init(String)

```cangjie
public init(watcherName: String)
```

**功能：** 类构造函数，用于创建订阅数据持有者实例。先通过[addWatcher](#static-func-addwatcherwatcher)添加事件观察者，再通过观察者名称关联到应用内已添加的观察者对象。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|watcherName|String|是|-|已通过[addWatcher](#static-func-addwatcherwatcher)添加的事件观察者名称。若未通过addWatcher添加，则默认无数据。|

**异常：**

- BusinessException：对应错误码如下表，详见[应用事件打点错误码](./cj-errorcode-hiappevent.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 11105001 | Parameter error. |

### func setSize(Int32)

```cangjie
public func setSize(size: Int32): Unit
```

**功能：** 设置每次取出的应用事件包的数据大小阈值。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int32|是|-|数据大小阈值，单位为byte。取值范围[0, 2^31-1]，超出范围会抛异常。|

**异常：**

- BusinessException：对应错误码如下表，详见[应用事件打点错误码](./cj-errorcode-hiappevent.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 11104001 | Invalid size value. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    // 添加数据观察者“Watcher1”，订阅监听系统事件
    HiAppEvent.addWatcher(Watcher(
        "Watcher1",
        appEventFilters: [ AppEventFilter("button")]
    ))

    let holder = AppEventPackageHolder("watcher2")
    holder.setSize(100)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func takeNext()

```cangjie
public func takeNext(): Option<AppEventPackage>
```

**功能：** 获取订阅事件。

系统根据setSize设置的数据大小阈值或setRow设置的条数来取出订阅事件数据，默认取1条订阅事件。当订阅事件数据全部被取出时返回None。

当setRow和setSize同时调用时仅setRow生效。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Option\<[AppEventPackage](#class-appeventpackage)>|取出的事件包对象，订阅事件数据被全部取出后会返回None。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    let holder = AppEventPackageHolder("watcher3")
    if (let Some(v) <- holder.takeNext()) {
        let eventPkg = v
        Hilog.info(0, "AppLogCj", "HiAppEvent packageId=${eventPkg.packageId}", "")
        Hilog.info(0, "AppLogCj", "HiAppEvent row=${eventPkg.row}", "")
        Hilog.info(0, "AppLogCj", "HiAppEvent size=${eventPkg.size}", "")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```