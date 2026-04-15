## class MessageSequence

```cangjie
public class MessageSequence {}
```

**功能：**  在RPC或IPC过程中，发送方可以使用MessageSequence提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageSequence提供的读方法从该对象中读取特定格式的数据。数据格式包括：基础类型及数组、IPC对象、接口描述符和自定义序列化对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

### static func closeFileDescriptor(Int32)

```cangjie
public static func closeFileDescriptor(fd: Int32): Unit
```

**功能：** 静态方法，关闭给定的文件描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|要关闭的文件描述符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let filePath = "path/to/file"
    let file = FileIo.open(filePath, mode: (OpenMode.CREATE | OpenMode.READ_WRITE))
    MessageSequence.closeFileDescriptor(file.fd)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func create()

```cangjie
public static func create(): MessageSequence
```

**功能：** 静态方法，创建MessageSequence对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[MessageSequence](#class-messagesequence)|返回创建的MessageSequence对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func dupFileDescriptor(Int32)

```cangjie
public static func dupFileDescriptor(fd: Int32): Int32
```

**功能：** 静态方法，复制给定的文件描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|表示已存在的文件描述符。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回新的文件描述符。|

**异常：**

- BusinessException：对应错误码如下表，详见[RPC错误码](./cj-errorcode-rpc.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 1900013 | Failed to call dup. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let filePath = "path/to/file"
    let file = FileIo.open(filePath, mode: (OpenMode.CREATE | OpenMode.READ_WRITE))
    let newFd = MessageSequence.dupFileDescriptor(file.fd)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func containFileDescriptors()

```cangjie
public func containFileDescriptors(): Bool
```

**功能：** 检查此MessageSequence对象是否包含文件描述符。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：包含文件描述符，false：不包含文件描述符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data = MessageSequence.create()
    let result = data.containFileDescriptors()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```