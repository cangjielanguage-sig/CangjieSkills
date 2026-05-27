## class MessageSequence

```cangjie
public class MessageSequence {}
```

**功能：** 在RPC或IPC过程中，发送方可以使用MessageSequence提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageSequence提供的读方法从该对象中读取特定格式的数据。数据格式包括：基础类型及数组、IPC对象、接口描述符和自定义序列化对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### static func closeFileDescriptor(Int32)

```cangjie
public static func closeFileDescriptor(fd: Int32): Unit
```

**功能：** 静态方法，关闭给定的文件描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|要关闭的文件描述符。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import kit.CoreFileKit.*

let filePath = "path/to/file"
let file = FileFs.open(filePath, mode: (OpenMode.CREATE.mode | OpenMode.READ_WRITE.mode))
MessageSequence.closeFileDescriptor(file.fd)
```

### static func create()

```cangjie
public static func create(): MessageSequence
```

**功能：** 静态方法，创建MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[MessageSequence](#class-messagesequence)|返回创建的MessageSequence对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
```

### static func dupFileDescriptor(Int32)

```cangjie
public static func dupFileDescriptor(fd: Int32): Int32
```

**功能：** 静态方法，复制给定的文件描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|表示已存在的文件描述符。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回新的文件描述符。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match.|
  |1900013|Failed to call dup.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import kit.CoreFileKit.*

let filePath = "path/to/file"
let file = FileFs.open(filePath, mode: (OpenMode.CREATE.mode | OpenMode.READ_WRITE.mode))
MessageSequence.dupFileDescriptor(file.fd)
```

### func containFileDescriptors()

```cangjie
public func containFileDescriptors(): Bool
```

**功能：** 检查此MessageSequence对象是否包含文件描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：包含文件描述符，false：不包含文件描述符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.containFileDescriptors()
```