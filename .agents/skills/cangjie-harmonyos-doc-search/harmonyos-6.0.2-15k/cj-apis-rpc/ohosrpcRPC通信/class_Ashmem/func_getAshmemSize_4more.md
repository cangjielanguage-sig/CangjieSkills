### func getAshmemSize()

```cangjie
public func getAshmemSize(): Int32
```

**功能：** 获取Ashmem对象的内存大小。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回Ashmem对象的内存大小。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024*1024)
ashmem.getAshmemSize()
```

### func mapReadWriteAshmem()

```cangjie
public func mapReadWriteAshmem(): Unit
```

**功能：** 在此进程虚拟地址空间上创建可读写的共享文件映射。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter is not an instance of the Ashmem object.|
  |1900001|Failed to call mmap.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024*1024)
ashmem.mapReadWriteAshmem()
```

### func mapReadonlyAshmem()

```cangjie
public func mapReadonlyAshmem(): Unit
```

**功能：** 在此进程虚拟地址空间上创建只读的共享文件映射。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1900001|Failed to call mmap.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024*1024)
ashmem.mapReadonlyAshmem()
```

### func mapTypedAshmem(UInt32)

```cangjie
public func mapTypedAshmem(mapType: UInt32): Unit
```

**功能：** 在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mapType|UInt32|是|-|指定映射的内存区域的保护等级。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The parameter type does not match;<br>3.The passed mapType exceeds the maximum protection level.|
  |1900001|Failed to call mmap.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024*1024)
ashmem.mapTypedAshmem(Ashmem.PROT_READ | Ashmem.PROT_WRITE)
```