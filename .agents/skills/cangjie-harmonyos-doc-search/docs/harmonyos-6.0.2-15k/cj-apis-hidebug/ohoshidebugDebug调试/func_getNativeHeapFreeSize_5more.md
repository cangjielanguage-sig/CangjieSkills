## func getNativeHeapFreeSize()

```cangjie
public func getNativeHeapFreeSize(): UInt64
```

**功能：** 获取内存分配器持有的缓存内存大小。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|返回内存分配器持有的缓存内存大小，单位为Byte。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let nativeHeapFreeSize: UInt64 = getNativeHeapFreeSize()
```

## func getNativeHeapSize()

```cangjie
public func getNativeHeapSize(): UInt64
```

**功能：** 获取内存分配器统计的进程持有的堆内存大小（含分配器元数据）。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|内存分配器统计的进程持有的堆内存大小（含分配器元数据），单位为Byte。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let nativeHeapSize: UInt64 = getNativeHeapSize()
```

## func getPrivateDirty()

```cangjie
public func getPrivateDirty(): UInt64
```

**功能：** 获取进程的私有脏内存大小。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|返回进程的私有脏内存大小，单位为kB。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let privateDirty: UInt64 = getPrivateDirty()
```

## func getPss()

```cangjie
public func getPss(): UInt64
```

**功能：** 获取应用进程实际使用的物理内存大小。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|返回应用进程实际使用的物理内存大小，单位为kB。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

let pss: UInt64 = getPss()
```

## func getServiceDump(Int32, Int32, Array\<String>)

```cangjie
public func getServiceDump(serviceid: Int32, fd: Int32, args: Array<String>): Unit
```

**功能：** 获取系统服务信息。

**需要权限：** ohos.permission.DUMP，仅系统应用可申请

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serviceid|Int32|是|-|基于该用户输入的service id获取系统服务信息。|
|fd|Int32|是|-|文件描述符，该接口会往该fd中写入数据。|
|args|Array\<String>|是|-|系统服务的Dump接口所对应的参数列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Hidebug错误码](../../errorcodes/cj-errorcode-hidebug.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|the parameter check failed, Possible causes:1.the parameter type error 2.the args parameter is not String array.|
  |11400101|ServiceId invalid. The system ability does not exist.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*
import ohos.base.AppLog
import kit.CoreFileKit.*

let file = FileFs.open("/data/storage/el1/base/testfile", mode: OpenMode.READ_WRITE.mode | OpenMode.CREATE.mode)
try {
    getServiceDump(10, file.fd, ["allInfo"])
} catch (e: Exception) {
    AppLog.error("${e}")
}
FileFs.close(file)
```