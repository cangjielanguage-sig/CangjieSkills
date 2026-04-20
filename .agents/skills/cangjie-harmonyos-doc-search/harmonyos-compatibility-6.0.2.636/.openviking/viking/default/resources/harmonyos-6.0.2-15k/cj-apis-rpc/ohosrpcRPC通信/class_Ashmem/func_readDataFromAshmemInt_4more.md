### func readDataFromAshmem(Int64, Int64)

```cangjie
public func readDataFromAshmem(size: Int64, offset: Int64): Array<Byte>
```

**功能：** 从此Ashmem对象关联的共享文件中读取数据。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int64|是|-|要读取的数据的大小。|
|offset|Int64|是|-|要读取的数据在此Ashmem对象关联的内存区间的起始位置。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Byte>|返回读取的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match.|
  |1900004|Failed to read data from the shared memory.|

### func setProtectionType(UInt32)

```cangjie
public func setProtectionType(protectionType: UInt32): Unit
```

**功能：** 设置映射内存区域的保护等级。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|protectionType|UInt32|是|-|要设置的保护类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match.|
  |1900002|Failed to call ioctl.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024*1024)
ashmem.setProtectionType(Ashmem.PROT_READ)
```

### func unmapAshmem()

```cangjie
public func unmapAshmem(): Unit
```

**功能：** 删除该Ashmem对象的地址映射。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024*1024)
ashmem.unmapAshmem()
```

### func writeDataToAshmem(Array\<Byte>, Int64, Int64)

```cangjie
public func writeDataToAshmem(buf: Array<Byte>, size: Int64, offset: Int64): Unit
```

**功能：** 将数据写入此Ashmem对象关联的共享文件。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buf|Array\<Byte>|是|-|写入Ashmem对象的数据。|
|size|Int64|是|-|要写入的数据大小。|
|offset|Int64|是|-|要写入的数据在此Ashmem对象关联的内存区间的起始位置。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match; <br/> 3.Failed to obtain arrayBuffer information.|
  |1900003|Failed to write data to the shared memory.|