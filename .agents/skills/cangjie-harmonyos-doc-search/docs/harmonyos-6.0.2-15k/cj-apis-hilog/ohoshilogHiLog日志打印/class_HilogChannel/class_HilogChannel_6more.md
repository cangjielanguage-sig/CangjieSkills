## class HilogChannel

```cangjie
public class HilogChannel {
    public init(ty: UInt32, domain: UInt32, tag: String)
}
```

**功能：** 日志系统对象，使应用/服务可以按照指定级别、标识和格式字符串输出日志内容。提供DEBUG、INFO、WARN、ERROR、FATAL不同级别的日志打印方法。支持指定日志类型、日志所对应的业务领域、指定日志标识构造自定义日志系统对象。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 12

### init(UInt32, UInt32, String)

```cangjie
public init(ty: UInt32, domain: UInt32, tag: String)
```

**功能：** HilogChannel的构造函数。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ty|UInt32|是|-|日志类型。|
|domain|UInt32|是|-|日志对应的领域标识，范围是0x0~0xFFFF。<br/>建议开发者在应用内根据需要自定义划分。|
|tag|String|是|-|指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。|

### func debug\<T>(T) where T <: ToString

```cangjie
public func debug<T>(message: T): Unit where T <: ToString
```

**功能：** 打印DEBUG级别的日志。

DEBUG级别的日志在正式发布版本中默认不被打印，只有在调试版本或打开调试开关的情况下才会打印。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|T|是|-|类型T需实现ToString接口，用于日志的格式化输出。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let testLog = HilogChannel(0, 0xD001200, "CJ-Test")
testLog.debug("Debug: Hello world!")
```

### func error\<T>(T) where T <: ToString

```cangjie
public func error<T>(message: T): Unit where T <: ToString
```

**功能：** 打印ERROR级别的日志。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|T|是|-|类型T需实现ToString接口，用于日志的格式化输出。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let testLog = HilogChannel(0, 0xD001200, "CJ-Test")
testLog.error("Error: Hello world!")
```

### func fatal\<T>(T) where T <: ToString

```cangjie
public func fatal<T>(message: T): Unit where T <: ToString
```

**功能：** 打印FATAL级别的日志。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|T|是|-|类型T需实现ToString接口，用于日志的格式化输出。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let testLog = HilogChannel(0, 0xD001200, "CJ-Test")
testLog.fatal("Fatal: Hello world!")
```

### func info\<T>(T) where T <: ToString

```cangjie
public func info<T>(message: T): Unit where T <: ToString
```

**功能：** 打印INFO级别的日志。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|T|是|-|类型T需实现ToString接口，用于日志的格式化输出。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let testLog = HilogChannel(0, 0xD001200, "CJ-Test")
testLog.info("Info: Hello world!")
```