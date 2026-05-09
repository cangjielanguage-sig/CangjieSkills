### func writeFloat(Float32)

```cangjie
public func writeFloat(val: Float32): Unit
```

**功能：** 将单精度浮点值写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|Float32|是|-|要写入的单精度浮点值。|

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
    data.writeFloat(1.2)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeFloatArray(Array\<Float32>)

```cangjie
public func writeFloatArray(floatArray: Array<Float32>): Unit
```

**功能：** 将单精度浮点数组写入MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|floatArray|Array\<Float32>|是|-|要写入的单精度浮点数组。|

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
    data.writeFloatArray([1.1])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeInt(Int32)

```cangjie
public func writeInt(val: Int32): Unit
```

**功能：** 将整数值写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|Int32|是|-|要写入的整数值。|

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
    data.writeInt(10)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func writeIntArray(Array\<Int32>)

```cangjie
public func writeIntArray(intArray: Array<Int32>): Unit
```

**功能：** 将整数数组写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|intArray|Array\<Int32>|是|-|要写入的整数数组。|

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
    data.writeIntArray([1])
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```