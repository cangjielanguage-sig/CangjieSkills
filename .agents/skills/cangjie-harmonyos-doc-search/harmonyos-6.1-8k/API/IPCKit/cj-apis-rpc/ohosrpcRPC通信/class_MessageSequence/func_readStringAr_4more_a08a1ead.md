### func readStringArray()

```cangjie
public func readStringArray(): Array<String>
```

**功能：** 从MessageSequence实例读取字符串数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回字符串数组。|

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
    data.readStringArray()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readUInt16Array()

```cangjie
public func readUInt16Array(): Array<UInt16>
```

**功能：** 从MessageSequence实例中读取Array\<UInt16>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt16>|返回Array\<UInt16>类型数据（以字节为单位）。|

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
    data.readUInt16Array()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readUInt32Array()

```cangjie
public func readUInt32Array(): Array<UInt32>
```

**功能：** 从MessageSequence实例中读取Array\<UInt32>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt32>|返回Array\<UInt32>类型数据（以字节为单位）|

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
    data.readUInt32Array()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readUInt64Array()

```cangjie
public func readUInt64Array(): Array<UInt64>
```

**功能：** 从MessageSequence实例中读取Array\<UInt64>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt64>|返回Array\<UInt64>类型数据（以字节为单位）。|

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
    data.readUInt64Array()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```