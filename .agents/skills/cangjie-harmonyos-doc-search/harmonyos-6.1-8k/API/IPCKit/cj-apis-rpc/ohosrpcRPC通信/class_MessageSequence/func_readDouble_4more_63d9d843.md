### func readDouble()

```cangjie
public func readDouble(): Float64
```

**功能：** 从MessageSequence实例读取双精度浮点值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Float64|返回双精度浮点值。|

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
    let result = data.readDouble()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readDoubleArray()

```cangjie
public func readDoubleArray(): Array<Float64>
```

**功能：** 从MessageSequence实例读取所有双精度浮点数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float64>|返回双精度浮点数组。|

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
import std.collection.ArrayList
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    data.readDoubleArray()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readException()

```cangjie
public func readException(): Unit
```

**功能：** 从MessageSequence中读取异常。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

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
    data.readException()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readFileDescriptor()

```cangjie
public func readFileDescriptor(): Int32
```

**功能：** 从MessageSequence中读取文件描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回文件描述符。|

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
    let fd = data.readFileDescriptor()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```