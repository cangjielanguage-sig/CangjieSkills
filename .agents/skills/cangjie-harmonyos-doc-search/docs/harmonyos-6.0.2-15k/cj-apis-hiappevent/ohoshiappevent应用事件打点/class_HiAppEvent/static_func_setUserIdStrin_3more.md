### static func setUserId(String, String)

```cangjie
public static func setUserId(name: String, value: String): Unit
```

**功能：** 设置用户ID。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|用户ID的key。只能包含大小写字母、数字、下划线和$，不能以数字开头，长度非空且不超过256个字符。|
|value|String|是|-|用户ID的值。长度不超过256，当值为null或空字符串时，则清除用户ID。|

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

HiAppEvent.setUserId("test_userID_name", "test_userID_value")
```

### static func setUserProperty(String, String)

```cangjie
public static func setUserProperty(name: String, value: String): Unit
```

**功能：** 设置用户属性。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|用户属性的key。只能包含大小写字母、数字、下划线和$，不能以数字开头，长度非空且不超过256个字符。|
|value|String|是|-|用户属性的值。长度不超过1024，当值为null或空字符串时，则清除用户属性。|

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
```

### static func write(AppEventInfo)

```cangjie
public static func write(info: AppEventInfo): Unit
```

**功能：** 应用事件打点方法，将事件写入到当天的事件文件中，可接收[AppEventInfo](#struct-appeventinfo)类型的事件对象。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[AppEventInfo](#struct-appeventinfo)|是|-|应用事件对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[应用事件打点错误码](../../errorcodes/cj-errorcode-hiappevent.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |11100001|Function is disabled.|
  |11101001|Invalid event domain.|
  |11101002|Invalid event name.|
  |11101003|Invalid number of event parameters.|
  |11101004|Invalid string length of the event parameter.|
  |11101005|Invalid event parameter name.|
  |11101006|Invalid array length of the event parameter.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

var params: Array<Parameters> = [Parameters("int_data", INT(100)), Parameters("str_data", STRING("strValue"))]
var appInfo : AppEventInfo = AppEventInfo("test_domain", "test_event", EventType.FAULT, params)
HiAppEvent.write(appInfo)
```