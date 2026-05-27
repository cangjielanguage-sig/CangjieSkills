## func isDistributedEnabled()

```cangjie
public func isDistributedEnabled(): Bool
```

**功能：** 查询设备是否支持分布式通知。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回设备是否支持分布式通知的结果（true：支持，false：不支持）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br> 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types.<br>3.Parameter verification failed.|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|
  |1600010|Distributed operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

try {
    let result = isDistributedEnabled()
    AppLog.info("test isDistributedEnabled success. isDistributedEnabled: ${result}")
} catch (e: Exception) {
    AppLog.info("call isDistributedEnabled fail because ${e}")
}
```

## func isNotificationEnabled()

```cangjie
public func isNotificationEnabled(): Bool
```

**功能：** 获取通知使能状态。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回获取通知使能状态的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

try {
    let result = isNotificationEnabled()
    AppLog.info("isNotificationEnabled result is ${result}")
} catch (e: Exception) {
    AppLog.info("call isNotificationEnabled fail because ${e}")
}
```

## func isSupportTemplate(String)

```cangjie
public func isSupportTemplate(templateName: String): Bool
```

**功能：** 查询模板是否存在。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|templateName|String|是|-|模板名称。当前仅支持"downloadTemplate"。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|模板是否存在的结果（true：存在，false：不存在）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br> 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types.<br>3.Parameter verification failed.|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

try {
    let templateName = "downloadTemplate"
    let supported = isSupportTemplate(templateName)
    AppLog.info("isSupportTemplate is ${supported}")
} catch (e: Exception) {
    AppLog.info("call isSupportTemplate fail because ${e}")
}
```