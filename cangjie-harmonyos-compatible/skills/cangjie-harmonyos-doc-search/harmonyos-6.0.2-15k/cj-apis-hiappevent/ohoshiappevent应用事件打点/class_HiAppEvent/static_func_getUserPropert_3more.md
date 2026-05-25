### static func getUserProperty(String)

```cangjie
public static func getUserProperty(name: String): String
```

**功能：** 获取之前通过[setUserProperty](#static-func-setuserpropertystring-string)接口设置的value值。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|用户属性的key。只能包含大小写字母、数字、下划线和$，不能以数字开头，长度不超过256。|

**返回值：**

|类型|说明|
|:----|:----|
|String|用户属性的值。没有查到返回空字符串。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

HiAppEvent.setUserProperty("test_setUserProperty_name", "test_setUserProperty_value")
let propertyName = HiAppEvent.getUserProperty("test_getUserProperty_name")
Hilog.info(0, "HiAppEvent", "HiAppEvent::test_getUserProperty is ${propertyName}.")
```

### static func removeProcessor(Int64)

```cangjie
public static func removeProcessor(id: Int64): Unit
```

**功能：** 删除上报事件的数据处理者。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|上报事件数据处理者ID。值大于0。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

var processor : Processor = Processor("test_processor")
let processorId = HiAppEvent.addProcessor(processor)
HiAppEvent.removeProcessor(processorId)
Hilog.info(0, "HiAppEvent", "HiAppEvent::removeProcessor test over.")
```

### static func removeWatcher(Watcher)

```cangjie
public static func removeWatcher(watcher: Watcher): Unit
```

**功能：** 移除应用事件观察者方法，可用于取消订阅应用事件。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|watcher|[Watcher](#struct-watcher)|是|-|应用事件观察者。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[应用事件打点错误码](../../errorcodes/cj-errorcode-hiappevent.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |11102001|Invalid watcher name.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

// 定义一个应用事件观察者
let watcher= Watcher("watcher1")
// 添加一个应用事件观察者来订阅事件
HiAppEvent.addWatcher(watcher)
// 移除该应用事件观察者以取消订阅事件
HiAppEvent.removeWatcher(watcher)
```