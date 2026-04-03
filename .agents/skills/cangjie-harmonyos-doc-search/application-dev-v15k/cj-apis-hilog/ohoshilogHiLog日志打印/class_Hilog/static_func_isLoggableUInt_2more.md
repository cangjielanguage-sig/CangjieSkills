### static func isLoggable(UInt32, String, LogLevel)

```cangjie
public static func isLoggable(domain: UInt32, tag: String, level: LogLevel): Bool
```

**功能：** 在打印日志前调用该接口，用于检查指定领域标识、日志标识和级别的日志是否可以打印。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|UInt32|是|-|日志对应的领域标识，范围是0x0~0xFFFF。<br/>建议开发者在应用内根据需要自定义划分。|
|tag|String|是|-|指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。|
|level|[LogLevel](#enum-loglevel)|是|-|日志级别。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果返回true，则该领域标识、日志标识和级别的日志可以打印，否则不能打印。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

Hilog.isLoggable(0, "hilog_test", LogLevel.DEBUG)
```

### static func warn(UInt32, String, String)

```cangjie
public static func warn(domain: UInt32, tag: String, format: String): Unit
```

**功能：** 打印WARN级别的日志。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|UInt32|是|-|日志对应的领域标识，范围是0x0~0xFFFF。<br/>建议开发者在应用内根据需要自定义划分。|
|tag|String|是|-|指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。|
|format|String|是|-|格式字符串，用于日志的格式化输出。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

Hilog.warn(0, "hilog_test", "Warn: Hello world!")
```