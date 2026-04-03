## class SystemDateTime

```cangjie
public class SystemDateTime {}
```

**功能：** 系统时间、时区功能类。

**起始版本：** 12

### static func getCurrentTime(Bool)

```cangjie
public static func getCurrentTime(isNano!: Bool = false): Int64
```

**功能：** 获取自Unix纪元以来经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isNano|Bool|否|false| **命名参数。** 返回结果是否为纳秒数。<br>- true：表示返回结果为纳秒数（ns）。 <br>- false：表示返回结果为毫秒数（ms）。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|自Unix纪元以来到当前系统时间所经过的时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let time = SystemDateTime.getCurrentTime()
    AppLog.info("Succeeded in getting currentTime : ${time}")
} catch (e: Exception) {
    AppLog.info("Failed to getCurrentTime: ${e.toString()}")
}
```

### static func getRealActiveTime(Bool)

```cangjie
public static func getRealActiveTime(isNano!: Bool = false): Int64
```

**功能：** 获取自系统启动以来经过的时间，不包括深度睡眠时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isNano|Bool|否|false| **命名参数。** 返回结果是否为纳秒数。<br/>- true：表示返回结果为纳秒数（ns）。<br/>- false：表示返回结果为毫秒数（ms）。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|自系统启动以来经过的时间，不包括深度睡眠时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let time = SystemDateTime.getRealActiveTime()
    AppLog.info("Succeeded in getting real active time : ${time}")
} catch (e: Exception) {
    AppLog.info("Failed to get real active time: ${e.toString()}")
}
```

### static func getRealTime(Bool)

```cangjie
public static func getRealTime(isNano!: Bool = false): Int64
```

**功能：** 获取自系统启动以来经过的时间，包括深度睡眠时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isNano|Bool|否|false| **命名参数。** 返回结果是否为纳秒数。<br/>- true：表示返回结果为纳秒数（ns）。 <br/>- false：表示返回结果为毫秒数（ms）。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|自系统启动以来经过的时间，包括深度睡眠时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let time = SystemDateTime.getRealTime()
    AppLog.info("Succeeded in getting real time : ${time}")
} catch (e: Exception) {
    AppLog.info("Failed to get real time: ${e.toString()}")
}
```

### static func getTime(Bool)

```cangjie
public static func getTime(isNano!: Bool = false): Int64
```

**功能：** 获取自Unix纪元以来经过的时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isNano|Bool|否|false| **命名参数。** 返回结果是否为纳秒数。<br>- true：表示返回结果为纳秒数（ns）。 <br>- false：表示返回结果为毫秒数（ms）。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|自Unix纪元以来经过的时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let time = SystemDateTime.getTime()
    AppLog.info("Succeeded in getting time : ${time}")
} catch (e: Exception) {
    AppLog.info("Failed to get time: ${e.toString()}")
}
```