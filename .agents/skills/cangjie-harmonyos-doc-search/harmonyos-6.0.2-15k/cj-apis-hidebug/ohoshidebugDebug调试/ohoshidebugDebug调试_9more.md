# ohos.hidebug（Debug调试）

使用hidebug，可以获取应用内存的使用情况，包括应用进程的静态堆内存（native heap）信息、应用进程内存占用PSS（Proportional Set Size）信息等。

## 导入模块

```cangjie
import kit.PerformanceAnalysisKit.*
```

## 权限列表

ohos.permission.DUMP

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getAppMemoryLimit()

```cangjie
public func getAppMemoryLimit(): MemoryLimit
```

**功能：** 获取应用程序进程内存限制。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[MemoryLimit](#class-memorylimit)|应用程序进程内存限制。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let appMemoryLimit: MemoryLimit = getAppMemoryLimit()
```

## func getAppNativeMemInfo()

```cangjie
public func getAppNativeMemInfo(): NativeMemInfo
```

**功能：** 获取应用进程内存信息。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[NativeMemInfo](#class-nativememinfo)|应用进程内存信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let nativeMemInfo: NativeMemInfo = getAppNativeMemInfo()
```

## func getAppThreadCpuUsage()

```cangjie
public func getAppThreadCpuUsage(): Array<ThreadCpuUsage>
```

**功能：** 获取应用线程CPU使用情况。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[ThreadCpuUsage](#class-threadcpuusage)>|返回当前应用进程下所有[ThreadCpuUsage](#class-threadcpuusage)数组。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let appThreadCpuUsage: Array<ThreadCpuUsage> = getAppThreadCpuUsage()
```

## func getCpuUsage()

```cangjie
public func getCpuUsage(): Float64
```

**功能：** 获取进程的CPU使用率。

如占用率为50%，则返回0.5。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|获取进程的CPU使用率。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let cpuUsage: Float64 = getCpuUsage()
```

## func getNativeHeapAllocatedSize()

```cangjie
public func getNativeHeapAllocatedSize(): UInt64
```

**功能：** 获取内存分配器统计的进程业务分配的堆内存大小。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|返回内存分配器统计的进程业务分配的堆内存大小，单位为Byte。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let nativeHeapAllocatedSize: UInt64 = getNativeHeapAllocatedSize()
```