### func writeFloat64Array(Array\<Float64>)

```cangjie
public func writeFloat64Array(buf: Array<Float64>): Unit
```

**功能：** 将Array\<Float64>类型数据写入MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buf|Array\<Float64>|是|-|要写入的数据。|

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
data.writeFloat64Array([1.1])
```

### func writeFloatArray(Array\<Float32>)

```cangjie
public func writeFloatArray(floatArray: Array<Float32>): Unit
```

**功能：** 将浮点数组写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|floatArray|Array\<Float32>|是|-|要写入的浮点数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The parameter is an empty array;<br>2.The number of parameters is incorrect;<br>3.The parameter type does not match;<br>4.The element does not exist in the array;<br>5.The type of the element in the array is incorrect.|
  |1900009|Failed to write data to the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.writeFloatArray([1.1])
```

### func writeInt(Int32)

```cangjie
public func writeInt(val: Int32): Unit
```

**功能：** 将整数值写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|Int32|是|-|要写入的整数值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match.|
  |1900009|Failed to write data to the message sequence.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.writeInt(10)
```