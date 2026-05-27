### func isLoggable(UInt32)

```cangjie
public func isLoggable(level: UInt32): Bool
```

**功能：** 在打印日志前调用该接口，用于检查指定领域标识、日志标识和级别的日志是否可以打印。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|level|UInt32|是|-|日志级别。|

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

let testLog = HilogChannel(0, 0xD001200, "CJ-Test")
testLog.isLoggable(0)
```

### func warn\<T>(T) where T <: ToString

```cangjie
public func warn<T>(message: T): Unit where T <: ToString
```

**功能：** 打印WARN级别的日志。

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
testLog.warn("Warn: Hello world!")
```