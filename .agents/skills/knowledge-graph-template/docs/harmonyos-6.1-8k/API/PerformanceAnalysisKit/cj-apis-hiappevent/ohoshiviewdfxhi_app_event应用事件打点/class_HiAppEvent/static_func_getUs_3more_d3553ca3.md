### static func getUserProperty(String)

```cangjie
public static func getUserProperty(name: String): String
```

**功能：** 获取通过setUserProperty接口设置的value值。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|用户属性的key。只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。|

**返回值：**

|类型|说明|
|:----|:----|
|String|用户属性的值。没有查到返回空字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    HiAppEvent.setUserProperty("test_setUserProperty_name", "test_setUserProperty_value")
    let propertyName = HiAppEvent.getUserProperty("test_getUserProperty_name")
    Hilog.info(0, "AppLogCj", "HiAppEvent::test_getUserProperty is ${propertyName}.")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func removeProcessor(Int64)

```cangjie
public static func removeProcessor(id: Int64): Unit
```

**功能：** 移除上报事件的数据处理者。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|上报事件数据处理者ID。值大于0。由调用[addProcessor](#static-func-addprocessorprocessor)接口返回值所得。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    var processor : Processor = Processor("test_processor")
    let processorId = HiAppEvent.addProcessor(processor)
    HiAppEvent.removeProcessor(processorId)
    Hilog.info(0, "AppLogCj", "HiAppEvent::removeProcessor test over.")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func removeWatcher(Watcher)

```cangjie
public static func removeWatcher(watcher: Watcher): Unit
```

**功能：** 移除事件观察者。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|watcher|[Watcher](#class-watcher)|是|-|事件观察者。|

**异常：**

- BusinessException：对应错误码如下表，详见[应用事件打点错误码](./cj-errorcode-hiappevent.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 11102001 | Invalid watcher name. Possible causes: 1. Contain invalid characters; 2. Length is invalid. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    // 定义一个应用事件观察者
    let watcher= Watcher("watcher1")
    // 添加一个应用事件观察者来订阅事件
    HiAppEvent.addWatcher(watcher)
    // 移除该应用事件观察者以取消订阅事件
    HiAppEvent.removeWatcher(watcher)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```