### func writeParcelableArray(Array\<Parcelable>)

```cangjie
public func writeParcelableArray(parcelableArray: Array<Parcelable>): Unit
```

**功能：** 将可序列化对象数组写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|parcelableArray|Array\<[Parcelable](#interface-parcelable)>|是|-|要写入的可序列化对象数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The parameter is an empty array;<br>2.The number of parameters is incorrect;<br>3.The parameter type does not match;<br>4.The element does not exist in the array.|
  |1900009|Failed to write data to the message sequence.|

### func writeRawDataBuffer(Array\<Byte>, Int64)

```cangjie
public func writeRawDataBuffer(rawData: Array<Byte>, size: Int64): Unit
```

**功能：** 将原始数据写入MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rawData|Array\<Byte>|是|-|要写入的原始数据。|
|size|Int64|是|-|发送的原始数据大小，以字节为单位。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match; <br/> 3.Failed to obtain arrayBuffer information; <br/> 4.The transferred size cannot be obtained; <br/> 5.The transferred size is less than or equal to 0; <br/> 6.The transferred size is greater than the byte length of ArrayBuffer.|
  |1900009|Failed to write data to the message sequence.|

### func writeShort(Int16)

```cangjie
public func writeShort(val: Int16): Unit
```

**功能：** 将短整数值写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|Int16|是|-|要写入的短整数值。|

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
data.writeShort(8)
```