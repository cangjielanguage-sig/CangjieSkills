## func getSharedDirty()

```cangjie
public func getSharedDirty(): UInt64
```

**功能：** 获取进程的共享脏内存大小。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|返回进程的共享脏内存大小，单位为kB。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let sharedDirty: UInt64 = getSharedDirty()
```

## func getSystemCpuUsage()

```cangjie
public func getSystemCpuUsage(): Float64
```

**功能：** 获取系统的CPU资源占用情况。

例如，当系统资源CPU占用为50%，将返回0.5。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|系统CPU资源占用情况。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Hidebug CpuUsage错误码](../../errorcodes/cj-errorcode-hidebug-cpuusage.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |11400104|The status of the system CPU usage is abnormal.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let cpuUsage: Float64 = getSystemCpuUsage()
```

## func getSystemMemInfo()

```cangjie
public func getSystemMemInfo(): SystemMemInfo
```

**功能：** 获取系统内存信息。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[SystemMemInfo](#class-systemmeminfo)|系统内存信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let systemMemInfo: SystemMemInfo = getSystemMemInfo()
```

## func getVss()

```cangjie
public func getVss(): UInt64
```

**功能：** 获取应用进程虚拟耗用内存大小。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|返回应用进程虚拟耗用内存大小，单位为kB。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let vss: UInt64 = getVss()
```

## func isDebugState()

```cangjie
public func isDebugState(): Bool
```

**功能：** 获取应用进程被调试状态，如果应用进程的native层处于被调试状态，则返回true，否则返回false。暂不支持仓颉层。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|应用进程被调试状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let debugState: Bool = isDebugState()
```