### static func getTimezone()

```cangjie
public static func getTimezone(): String
```

**功能：** 获取系统时区。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回系统时区。具体可见[支持的系统时区](#支持的系统时区) 。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let time = SystemDateTime.getTimezone()
    AppLog.info("Succeeded to getTimezone, getTimezone is ${time} ")
} catch (e: Exception) {
    AppLog.info("Failed to getTimezone: ${e.toString()}")
}
```

### static func getUptime(TimeType, Bool)

```cangjie
public static func getUptime(timeType: TimeType, isNano!: Bool = false): Int64
```

**功能：** 获取自系统启动以来经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeType|[TimeType](#enum-timetype)|是|-|获取时间的类型。|
|isNano|Bool|否|false| **命名参数。** 返回结果是否为纳秒数。<br/>- true：表示返回结果为纳秒数（ns）。 <br/>- false：表示返回结果为毫秒数（ms）。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|自系统启动以来经过的时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let time = SystemDateTime.getUptime(TimeType.ACTIVE)
    AppLog.info("Succeeded to getUptime : ${time}")
} catch (e: Exception) {
    AppLog.info("Failed to getUptime: ${e.toString()}")
}
```