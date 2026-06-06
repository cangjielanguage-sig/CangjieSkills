### func getCapacity()

```cangjie
public func getCapacity(): UInt32
```

**功能：** 获取当前MessageSequence对象的容量大小。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取的MessageSequence实例的容量大小。以字节为单位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
let result = data.getCapacity()
```

### func getRawDataCapacity()

```cangjie
public func getRawDataCapacity(): UInt32
```

**功能：** 获取MessageSequence可以容纳的最大原始数据量。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回MessageSequence可以容纳的最大原始数据量，即128MB。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
data.getRawDataCapacity()
```

### func getReadPosition()

```cangjie
public func getReadPosition(): UInt32
```

**功能：** 获取MessageSequence的读位置。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回MessageSequence实例中的当前读取位置。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
let pos = data.getReadPosition()
```

### func getReadableBytes()

```cangjie
public func getReadableBytes(): UInt32
```

**功能：** 获取MessageSequence的可读字节空间。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取到的MessageSequence实例的可读字节空间。以字节为单位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
let bytes = data.getReadableBytes()
```

### func getSize()

```cangjie
public func getSize(): UInt32
```

**功能：** 获取当前创建的MessageSequence对象的数据大小。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取的MessageSequence实例的数据大小。以字节为单位。|

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

let data = MessageSequence.create()
let size = data.getSize()
```

### func getWritableBytes()

```cangjie
public func getWritableBytes(): UInt32
```

**功能：** 获取MessageSequence的可写字节空间大小。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|获取到的MessageSequence实例的可写字节空间。以字节为单位。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
let bytes = data.getWritableBytes()
```

### func getWritePosition()

```cangjie
public func getWritePosition(): UInt32
```

**功能：** 获取MessageSequence的写位置。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回MessageSequence实例中的当前写入位置。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let data = MessageSequence.create()
let pos = data.getWritePosition()
```