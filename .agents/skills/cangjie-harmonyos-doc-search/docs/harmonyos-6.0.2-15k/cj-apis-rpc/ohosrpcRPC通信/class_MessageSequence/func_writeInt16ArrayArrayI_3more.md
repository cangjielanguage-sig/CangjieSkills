### func writeInt16Array(Array\<Int16>)

```cangjie
public func writeInt16Array(buf: Array<Int16>): Unit
```

**功能：** 将Array\<Int16>类型数据写入MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buf|Array\<Int16>|是|-|要写入的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The parameter is an empty array;<br>2.The number of parameters is incorrect;<br>3.The parameter type does not match;<br>4.The obtained value of typeCode is incorrect;<br>5.Failed to obtain arrayBuffer information.|
  |1900009|Failed to write data to the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.writeInt16Array([1])
```

### func writeInt32Array(Array\<Int32>)

```cangjie
public func writeInt32Array(buf: Array<Int32>): Unit
```

**功能：** 将Array\<Int32>类型数据写入MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buf|Array\<Int32>|是|-|要写入的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The parameter is an empty array;<br>2.The number of parameters is incorrect;<br>3.The parameter type does not match;<br>4.The obtained value of typeCode is incorrect;<br>5.Failed to obtain arrayBuffer information.|
  |1900009|Failed to write data to the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.writeInt32Array([1])
```

### func writeInt64Array(Array\<Int64>)

```cangjie
public func writeInt64Array(buf: Array<Int64>): Unit
```

**功能：** 将Array\<Int64>类型数据写入MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buf|Array\<Int64>|是|-|要写入的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The parameter is an empty array;<br>2.The number of parameters is incorrect;<br>3.The parameter type does not match;<br>4.The obtained value of typeCode is incorrect;<br>5.Failed to obtain arrayBuffer information.|
  |1900009|Failed to write data to the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.writeInt64Array([1])
```