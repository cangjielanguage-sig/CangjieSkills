### static func write(AppEventInfo)

```cangjie
public static func write(info: AppEventInfo): Unit
```

**功能：** 应用事件打点方法，将AppEventInfo类型的事件进行存储。通过此接口写入的事件对象是开发者自定义的对象，为了避免与系统事件产生冲突混淆，不建议写入系统事件（[Event](#class-event)中定义的系统事件名称常量）。此接口写入的事件可通过订阅事件观察者（[addWatcher](#static-func-addwatcherwatcher)）进行订阅。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[AppEventInfo](#class-appeventinfo)|是|-|应用事件对象。其内部定义的事件名称建议避免与[Event](#class-event)中定义的系统事件名称常量产生冲突。|

**异常：**

- BusinessException：对应错误码如下表，详见[应用事件打点错误码](./cj-errorcode-hiappevent.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 11100001 | Function is disabled. Possible caused by the param disable in ConfigOption is true. |
  | 11101001 | Invalid event domain.Possible causes: 1. Contain invalid characters; 2. Length is invalid. |
  | 11101002 | Invalid event name. Possible causes: 1. Contain invalid characters; 2. Length is invalid. |
  | 11101003 | Invalid number of event parameters. Possible caused by the number of parameters is over 32. |
  | 11101004 | Invalid string length of the event parameter. |
  | 11101005 | Invalid event parameter name. Possible causes: 1. Contain invalid characters; 2. Length is invalid. |
  | 11101006 | Invalid array length of a event parameter. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import std.collection.HashMap

try {
    let params = HashMap<String, EventValueType>()
    params.add("cangjie", IntValue(1001))
    params.add("cangjie2", StringValue("1001"))
    var appInfo: AppEventInfo = AppEventInfo("cangjie1", "test_event", EventType.Fault, params)
    HiAppEvent.write(appInfo)
    HiAppEvent.clearData()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```