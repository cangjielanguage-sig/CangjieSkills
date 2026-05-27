## class Hilog

```cangjie
public class Hilog {}
```

**功能：** 日志系统对象，使应用/服务可以按照指定级别、标识和格式字符串输出日志内容。提供DEBUG、INFO、WARN、ERROR、FATAL不同级别的日志打印方法。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 19

### static func debug(UInt32, String, String)

```cangjie
public static func debug(domain: UInt32, tag: String, format: String): Unit
```

**功能：** 打印DEBUG级别的日志。

DEBUG级别的日志在正式发布版本中默认不被打印，只有在调试版本或打开调试开关的情况下才会打印。

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

Hilog.debug(0, "hilog_test", "Debug: Hello world!")
```

### static func error(UInt32, String, String)

```cangjie
public static func error(domain: UInt32, tag: String, format: String): Unit
```

**功能：** 打印ERROR级别的日志。

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

Hilog.error(0, "hilog_test", "Error: Hello world!")
```

### static func fatal(UInt32, String, String)

```cangjie
public static func fatal(domain: UInt32, tag: String, format: String): Unit
```

**功能：** 打印FATAL级别的日志。

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

Hilog.fatal(0, "hilog_test", "Fatal: Hello world!")
```

### static func info(UInt32, String, String)

```cangjie
public static func info(domain: UInt32, tag: String, format: String): Unit
```

**功能：** 打印INFO级别的日志。

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

Hilog.info(0, "hilog_test", "Info: Hello world!")
```