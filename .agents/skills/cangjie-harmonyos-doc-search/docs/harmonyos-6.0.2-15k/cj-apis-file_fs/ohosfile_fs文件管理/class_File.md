## class File

```cangjie
public class File {}
```

**功能：** 由open接口打开的File对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### prop fd

```cangjie
public prop fd: Int32
```

**功能：** 打开的文件描述符。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop name

```cangjie
public prop name: String
```

**功能：** 文件名。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** String

**读写能力：** 只读

**起始版本：** 12

### prop path

```cangjie
public prop path: String
```

**功能：** 文件路径。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** String

**读写能力：** 只读

**起始版本：** 12

### func getParent()

```cangjie
public func getParent(): String
```

**功能：** 获取File对象对应文件父目录。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回父目录路径。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath, mode: (READ_WRITE.mode | CREATE.mode))
Applog.info("The parent path is: " + file.getParent())
FileFs.close(file)
```

### func tryLock(Bool)

```cangjie
public func tryLock(exclusive!: Bool = false): Unit
```

**功能：** 文件非阻塞式施加共享锁或独占锁。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|exclusive|Bool|否|false| **命名参数。** 是否施加独占锁，默认false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath, mode:(READ_WRITE.mode | CREATE.mode))
file.tryLock(exclusive: true)
FileFs.close(file)
```

### func unLock()

```cangjie
public func unLock(): Unit
```

**功能：** 以同步方式给文件解锁。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath, mode: (READ_WRITE.mode | CREATE.mode))
file.tryLock(exclusive: true)
file.unLock()
FileFs.close(file)
```