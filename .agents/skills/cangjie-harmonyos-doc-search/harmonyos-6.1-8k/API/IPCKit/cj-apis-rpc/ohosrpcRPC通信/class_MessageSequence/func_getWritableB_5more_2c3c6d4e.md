### func getWritableBytes()

```cangjie
public func getWritableBytes(): UInt32
```

**功能：** 获取MessageSequence的可写字节空间大小。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取到的MessageSequence实例的可写字节空间。以字节为单位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let bytes = data.getWritableBytes()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getWritePosition()

```cangjie
public func getWritePosition(): UInt32
```

**功能：** 获取MessageSequence的写位置。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回MessageSequence实例中的当前写入位置。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let pos = data.getWritePosition()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readAshmem()

```cangjie
public func readAshmem(): Ashmem
```

**功能：** 从MessageSequence读取匿名共享对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Ashmem](#class-ashmem)|返回匿名共享对象。|

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
    let data = MessageSequence.create()
    let ashMem = data.readAshmem()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readBoolean()

```cangjie
public func readBoolean(): Bool
```

**功能：** 从MessageSequence实例读取布尔值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回读取到的布尔值。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900010 | Failed to read data from the message sequence. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let result = data.readBoolean()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readBooleanArray()

```cangjie
public func readBooleanArray(): Array<Bool>
```

**功能：** 从MessageSequence实例中读取布尔数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Bool>|返回布尔数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900010 | Failed to read data from the message sequence. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    data.readBooleanArray()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```