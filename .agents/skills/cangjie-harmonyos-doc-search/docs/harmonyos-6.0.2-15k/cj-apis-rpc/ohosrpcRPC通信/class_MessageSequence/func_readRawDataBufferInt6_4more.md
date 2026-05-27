### func readRawDataBuffer(Int64)

```cangjie
public func readRawDataBuffer(size: Int64): Array<Byte>
```

**功能：** 从MessageSequence读取原始数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int64|是|-|要读取的原始数据的大小。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Byte>|返回原始数据（以字节为单位）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match.|
  |1900010|Failed to read data from the message sequence.|

### func readShort()

```cangjie
public func readShort(): Int16
```

**功能：** 从MessageSequence实例读取短整数值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int16|返回短整数值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1900010|Failed to read data from the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.readShort()
```

### func readShortArray(ArrayList\<Int16>)

```cangjie
public func readShortArray(dataIn: ArrayList<Int16>): Unit
```

**功能：** 从MessageSequence实例中读取短整数数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataIn|ArrayList\<Int16>|是|-|要读取的短整数数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The parameter is an empty array;<br>2.The number of parameters is incorrect;<br>3.The parameter type does not match. |
  |1900010|Failed to read data from the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import std.collection.ArrayList

let data = MessageSequence.create()
let list = ArrayList<Int16>()
data.readShortArray(list)
```

### func readShortArray()

```cangjie
public func readShortArray(): Array<Int16>
```

**功能：** 从MessageSequence实例中读取短整数数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int16>|返回短整数数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1900010|Failed to read data from the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.readShortArray()
```