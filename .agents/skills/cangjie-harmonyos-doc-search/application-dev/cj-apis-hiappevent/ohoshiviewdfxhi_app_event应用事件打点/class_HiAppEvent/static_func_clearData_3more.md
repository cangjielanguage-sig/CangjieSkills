### static func clearData()

```cangjie
public static func clearData(): Unit
```

**功能：** 应用事件打点数据清理方法，将当前应用存储在本地的打点数据进行清除。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import std.collection.ArrayList
import std.collection.HashMap
import ohos.business_exception.BusinessException

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

### static func configure(ConfigOption)

```cangjie
public static func configure(config: ConfigOption): Unit
```

**功能：** 应用事件打点配置方法，支持配置打点开关和目录存储配额大小。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[ConfigOption](#class-configoption)|是|-|应用事件打点配置项对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[应用事件打点错误码](./cj-errorcode-hiappevent.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 11103001 | Invalid max storage quota value. Possible caused by incorrectly formatted. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    var config : ConfigOption = ConfigOption(maxStorage: "100M", disable: true)
    HiAppEvent.configure(config)
    Hilog.info(0, "AppLogCj", "HiAppEvent::configure.")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func getUserId(String)

```cangjie
public static func getUserId(name: String): String
```

**功能：** 获取通过setUserId接口设置的value值。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|用户ID的key。只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。|

**返回值：**

|类型|说明|
|:----|:----|
|String|用户ID的值。没有查到返回空字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    HiAppEvent.setUserId("test_getUserId_name", "test_getUserId_value")
    let userIdName = HiAppEvent.getUserId("test_getUserId_name")
    Hilog.info(0, "AppLogCj", "HiAppEvent::test_getUserId is ${userIdName}.")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```