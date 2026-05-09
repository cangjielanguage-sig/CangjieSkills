### func readDataFromAshmem(Int64, Int64)

```cangjie
public func readDataFromAshmem(size: Int64, offset: Int64): Array<Byte>
```

**功能：** 从此Ashmem对象关联的共享文件中读取数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int64|是|-|要读取的数据的大小。|
|offset|Int64|是|-|要读取的数据在此Ashmem对象关联的内存区间的起始位置。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Byte>|返回读取的数据。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900004 | Failed to read data from the shared memory. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ashmem = Ashmem.create("ashmem", 1024*1024)
    ashmem.readDataFromAshmem(1, 0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setProtectionType(UInt32)

```cangjie
public func setProtectionType(protectionType: UInt32): Unit
```

**功能：** 设置映射内存区域的保护等级。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|protectionType|UInt32|是|-|要设置的保护类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900002 | Failed to call ioctl. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ashmem = Ashmem.create("ashmem", 1024*1024)
    ashmem.setProtectionType(Ashmem.PROT_READ)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func unmapAshmem()

```cangjie
public func unmapAshmem(): Unit
```

**功能：** 删除该Ashmem对象的地址映射。

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
    ashmem.unmapAshmem()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeDataToAshmem(Array\<Byte>, Int64, Int64)

```cangjie
public func writeDataToAshmem(buf: Array<Byte>, size: Int64, offset: Int64): Unit
```

**功能：** 将数据写入此Ashmem对象关联的共享文件。

> **说明：**
>
> 对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#func-mapreadwriteashmem)进行映射。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buf|Array\<Byte>|是|-|写入Ashmem对象的数据。|
|size|Int64|是|-|要写入的数据大小。|
|offset|Int64|是|-|要写入的数据在此Ashmem对象关联的内存区间的起始位置。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900003 | Failed to write data to the shared memory. |

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
    ashmem.writeDataToAshmem([1], 1, 0)
    ashmem.unmapAshmem()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```