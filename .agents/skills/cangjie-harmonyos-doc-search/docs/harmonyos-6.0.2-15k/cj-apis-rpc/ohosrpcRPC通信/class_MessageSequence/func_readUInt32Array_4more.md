### func readUInt32Array()

```cangjie
public func readUInt32Array(): Array<UInt32>
```

**功能：** 从MessageSequence实例中读取Array\<UInt32>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt32>|读取的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match;<br>3.The obtained value of typeCode is incorrect.|
  |1900010|Failed to read data from the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.readUInt32Array()
```

### func readUInt64Array()

```cangjie
public func readUInt64Array(): Array<UInt64>
```

**功能：** 从MessageSequence实例中读取Array\<UInt64>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt64>|读取的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match;<br>3.The obtained value of typeCode is incorrect.|
  |1900010|Failed to read data from the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.readUInt64Array()
```

### func readUInt8Array()

```cangjie
public func readUInt8Array(): Array<UInt8>
```

**功能：** 从MessageSequence实例中读取Array\<UInt8>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|读取的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match;<br>3.The obtained value of typeCode is incorrect.|
  |1900010|Failed to read data from the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.readUInt8Array()
```

### func reclaim()

```cangjie
public func reclaim(): Unit
```

**功能：** 释放不再使用的MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.reclaim()
```