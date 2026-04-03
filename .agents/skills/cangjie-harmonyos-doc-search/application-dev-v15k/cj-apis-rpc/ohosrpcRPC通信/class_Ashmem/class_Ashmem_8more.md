## class Ashmem

```cangjie
public class Ashmem {
    public static const PROT_EXEC: UInt32 = 4
    public static const PROT_NONE: UInt32 = 0
    public static const PROT_READ: UInt32 = 1
    public static const PROT_WRITE: UInt32 = 2
}
```

**功能：** 提供与匿名共享内存对象相关的方法，包括创建、关闭、映射和取消映射Ashmem、从Ashmem读取数据和写入数据、获取Ashmem大小、设置Ashmem保护。

共享内存只适用与本设备内跨进程通信。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### static const PROT_EXEC

```cangjie
public static const PROT_EXEC: UInt32 = 4
```

**功能：** 映射的内存可执行。

**类型：** UInt32

**起始版本：** 19

### static const PROT_NONE

```cangjie
public static const PROT_NONE: UInt32 = 0
```

**功能：** 映射的内存不可访问。

**类型：** UInt32

**起始版本：** 19

### static const PROT_READ

```cangjie
public static const PROT_READ: UInt32 = 1
```

**功能：** 映射的内存可读。

**类型：** UInt32

**起始版本：** 19

### static const PROT_WRITE

```cangjie
public static const PROT_WRITE: UInt32 = 2
```

**功能：** 映射的内存可写。

**类型：** UInt32

**起始版本：** 19

### static func create(String, Int32)

```cangjie
public static func create(name: String, size: Int32): Ashmem
```

**功能：** 静态方法，通过复制现有Ashmem对象的文件描述符（fd）来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|名称，用于查询Ashmem信息。|
|size|Int32|是|-|Ashmem的大小，以字节为单位。|

**返回值：**

|类型|说明|
|:----|:----|
|[Ashmem](#class-ashmem)|返回创建的Ashmem对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The passed parameter is not an Ahmem object;<br>3.3.The ashmem instance for obtaining packaging is empty.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024 * 1024)
```

### static func create(Ashmem)

```cangjie
public static func create(ashmem: Ashmem): Ashmem
```

**功能：** 静态方法，通过复制现有Ashmem对象的文件描述符（fd）来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ashmem|[Ashmem](#class-ashmem)|是|-|已存在的Ashmem对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[Ashmem](#class-ashmem)|返回创建的Ashmem对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes:<br>1.The number of parameters is incorrect;<br>2.The passed parameter is not an Ahmem object;<br>3.3.The ashmem instance for obtaining packaging is empty.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024 * 1024) //static func create(String, Int32)
let ashmem2 = Ashmem.create(ashmem) //static func create(Ashmem)
```

### func closeAshmem()

```cangjie
public func closeAshmem(): Unit
```

**功能：** 关闭这个Ashmem。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

let ashmem = Ashmem.create("ashmem", 1024*1024)
ashmem.closeAshmem()
```