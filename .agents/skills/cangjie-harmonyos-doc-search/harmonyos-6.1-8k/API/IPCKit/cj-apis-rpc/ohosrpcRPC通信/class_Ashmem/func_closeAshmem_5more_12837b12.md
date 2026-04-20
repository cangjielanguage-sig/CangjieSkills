### func closeAshmem()

```cangjie
public func closeAshmem(): Unit
```

**功能：** 关闭这个Ashmem。

> **说明：**
>
> 关闭Ashmem对象前需要先解除地址映射。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ashmem = Ashmem.create("ashmem", 1024*1024)
    ashmem.closeAshmem()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getAshmemSize()

```cangjie
public func getAshmemSize(): Int32
```

**功能：** 获取Ashmem对象的内存大小。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回Ashmem对象的内存大小。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ashmem = Ashmem.create("ashmem", 1024*1024)
    let result = ashmem.getAshmemSize()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func mapReadWriteAshmem()

```cangjie
public func mapReadWriteAshmem(): Unit
```

**功能：** 在此进程虚拟地址空间上创建可读写的共享文件映射。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900001 | Failed to call mmap. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ashmem = Ashmem.create("ashmem", 1024*1024)
    ashmem.mapReadWriteAshmem()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func mapReadonlyAshmem()

```cangjie
public func mapReadonlyAshmem(): Unit
```

**功能：** 在此进程虚拟地址空间上创建只读的共享文件映射。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900001 | Failed to call mmap. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ashmem = Ashmem.create("ashmem", 1024*1024)
    ashmem.mapReadonlyAshmem()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func mapTypedAshmem(UInt32)

```cangjie
public func mapTypedAshmem(mapType: UInt32): Unit
```

**功能：** 在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mapType|UInt32|是|-|指定映射的内存区域的保护等级。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900001 | Failed to call mmap. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ashmem = Ashmem.create("ashmem", 1024*1024)
    ashmem.mapTypedAshmem(Ashmem.PROT_READ | Ashmem.PROT_WRITE)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```