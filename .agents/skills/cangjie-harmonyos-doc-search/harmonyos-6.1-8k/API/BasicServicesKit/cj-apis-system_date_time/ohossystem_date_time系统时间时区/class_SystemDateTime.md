## class SystemDateTime

```cangjie
public class SystemDateTime {}
```

**功能：** 系统时间、时区功能类。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 22

### static func getTime(Bool)

```cangjie
public static func getTime(isNanoseconds!: Bool = false): Int64
```

**功能：** 获取自Unix纪元以来到当前系统时间所经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isNanoseconds|Bool|否|false| **命名参数。** 返回结果是否为纳秒数。<br>- true：表示返回结果为纳秒数(ns)。 <br>- false：表示返回结果为毫秒数(ms)。<br>默认值为false。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|自Unix纪元以来到当前系统时间所经过的时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let time = SystemDateTime.getTime()
    Hilog.info(0, "cangjie_ohos_test", "Succeeded in getting time : ${time}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func getTimezone()

```cangjie
public static func getTimezone(): String
```

**功能：** 获取系统时区。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回系统时区。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let time = SystemDateTime.getTimezone()
    Hilog.info(0, "cangjie_ohos_test", "Succeeded to getTimezone, getTimezone is ${time} ")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func getUptime(TimeType, Bool)

```cangjie
public static func getUptime(timeType: TimeType, isNanoseconds!: Bool = false): Int64
```

**功能：** 获取自系统启动以来经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeType|[TimeType](#enum-timetype)|是|-|获取时间的类型，仅能为Startup或者Active。|
|isNanoseconds|Bool|否|false| **命名参数。** 返回结果是否为纳秒数。<br/>- true：表示返回结果为纳秒数(ns)。 <br/>- false：表示返回结果为毫秒数(ms)。<br>默认值为false。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|自系统启动以来经过的时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let time = SystemDateTime.getUptime(TimeType.Active)
    Hilog.info(0, "cangjie_ohos_test", "Succeeded to getUptime : ${time}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```