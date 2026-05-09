### func writeBooleanArray(Array\<Bool>)

```cangjie
public func writeBooleanArray(booleanArray: Array<Bool>): Unit
```

**功能：** 将布尔数组写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|booleanArray|Array\<Bool>|是|-|要写入的布尔数组。|

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
    data.writeBooleanArray([false, true, false])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeByte(Int8)

```cangjie
public func writeByte(val: Int8): Unit
```

**功能：** 将字节值写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|Int8|是|-|要写入的字节值。|

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
    data.writeByte(2)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeByteArray(Array\<Int8>)

```cangjie
public func writeByteArray(byteArray: Array<Int8>): Unit
```

**功能：** 将字节数组写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|byteArray|Array\<Int8>|是|-|要写入的字节数组。|

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
    data.writeByteArray([1])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeChar(UInt8)

```cangjie
public func writeChar(val: UInt8): Unit
```

**功能：** 将单个字符值写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|UInt8|是|-|要写入的单个字符值。|

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
    data.writeChar(97)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```