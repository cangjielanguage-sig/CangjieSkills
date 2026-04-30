### func readFloat()

```cangjie
public func readFloat(): Float32
```

**功能：** 从MessageSequence实例中读取浮点值。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float32|返回浮点值。|

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
data.readFloat()
```

### func readFloat32Array()

```cangjie
public func readFloat32Array(): Array<Float32>
```

**功能：** 从MessageSequence实例中读取Array\<Float32>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|读取的数据。|

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
data.readFloat32Array()
```

### func readFloat64Array()

```cangjie
public func readFloat64Array(): Array<Float64>
```

**功能：** 从MessageSequence实例中读取Array\<Float64>类型数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float64>|读取的数据。|

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
data.readFloat64Array()
```

### func readFloatArray(ArrayList\<Float32>)

```cangjie
public func readFloatArray(dataIn: ArrayList<Float32>): Unit
```

**功能：** 从MessageSequence实例中读取浮点数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataIn|ArrayList\<Float32>|是|-|要读取的浮点数组。|

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
import std.collection.ArrayList

let data = MessageSequence.create()
let list = ArrayList<Float64>()
data.readFloatArray(list)
```

### func readFloatArray()

```cangjie
public func readFloatArray(): Array<Float32>
```

**功能：** 从MessageSequence实例中读取浮点数组。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|返回浮点数组。|

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
data.readFloatArray()
```