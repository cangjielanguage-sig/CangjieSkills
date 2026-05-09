### func readUInt8Array()

```cangjie
public func readUInt8Array(): Array<UInt8>
```

**功能：** 从MessageSequence实例中读取Array\<UInt8>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|返回Array\<UInt8>类型数据（以字节为单位）|

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
    data.readUInt8Array()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func reclaim()

```cangjie
public func reclaim(): Unit
```

**功能：** 释放不再使用的MessageSequence对象。

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
    let data = MessageSequence.create()
    data.reclaim()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func rewindRead(UInt32)

```cangjie
public func rewindRead(pos: UInt32): Unit
```

**功能：** 重新偏移读取位置到指定的位置。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pos|UInt32|是|-|开始读取数据的目标位置。|

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
    data.rewindRead(0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func rewindWrite(UInt32)

```cangjie
public func rewindWrite(pos: UInt32): Unit
```

**功能：** 重新偏移写位置到指定的位置。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pos|UInt32|是|-|开始写入数据的目标位置。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900009 | Failed to write data to the message sequence. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    data.rewindWrite(0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```