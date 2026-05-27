### func writeShortArray(Array\<Int16>)

```cangjie
public func writeShortArray(shortArray: Array<Int16>): Unit
```

**功能：** 将短整数数组写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shortArray|Array\<Int16>|是|-|要写入的短整数数组。|

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
data.writeShortArray([1])
```

### func writeString(String)

```cangjie
public func writeString(val: String): Unit
```

**功能：** 将字符串值写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|String|是|-|要写入的字符串值，其长度应小于40960字节。|

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
data.writeString('abc')
```

### func writeStringArray(Array\<String>)

```cangjie
public func writeStringArray(stringArray: Array<String>): Unit
```

**功能：** 将字符串数组写入MessageSequence实例。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|stringArray|Array\<String>|是|-|要写入的字符串数组，数组单个元素的长度应小于40960字节。|

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
data.writeStringArray(["abc", "def"])
```