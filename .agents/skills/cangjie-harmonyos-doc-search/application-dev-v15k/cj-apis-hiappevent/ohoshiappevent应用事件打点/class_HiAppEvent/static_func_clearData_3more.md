### static func clearData()

```cangjie
public static func clearData(): Unit
```

**功能：** 应用事件打点数据清理方法，将应用存储在本地的打点数据进行清除。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

var params: Array<Parameters> = [Parameters("cangjie", INT(1001)), Parameters("cangjie2", STRING("1001"))]
var appInfo: AppEventInfo = AppEventInfo("cangjie1", "test_event", EventType.FAULT, params)
HiAppEvent.write(appInfo)
HiAppEvent.clearData()
```

### static func configure(ConfigOption)

```cangjie
public static func configure(config: ConfigOption): Unit
```

**功能：** 应用事件打点配置方法，可用于配置打点开关、目录存储配额大小等功能。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[ConfigOption](#struct-configoption)|是|-|应用事件打点配置项对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[应用事件打点错误码](../../errorcodes/cj-errorcode-hiappevent.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |11103001|Invalid max storage quota value.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

var config : ConfigOption = ConfigOption("100M", disable: true)
HiAppEvent.configure(config)
Hilog.info(0, "HiAppEvent", "HiAppEvent::configure.")
```

### static func getUserId(String)

```cangjie
public static func getUserId(name: String): String
```

**功能：** 获取之前通过[setUserId](#static-func-setuseridstring-string)接口设置的value值。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|用户ID的key。只能包含大小写字母、数字、下划线和$，不能以数字开头，长度不超过256。|

**返回值：**

|类型|说明|
|:----|:----|
|String|用户ID的值。没有查到返回空字符串。|

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

HiAppEvent.setUserId("test_getUserId_name", "test_getUserId_value")
let userIdName = HiAppEvent.getUserId("test_getUserId_name")
Hilog.info(0, "HiAppEvent", "HiAppEvent::test_getUserId is ${userIdName}.")
```