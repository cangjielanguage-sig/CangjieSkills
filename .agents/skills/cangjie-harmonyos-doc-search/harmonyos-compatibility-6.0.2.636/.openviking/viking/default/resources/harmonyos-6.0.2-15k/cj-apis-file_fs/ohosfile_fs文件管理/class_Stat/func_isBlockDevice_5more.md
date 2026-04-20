### func isBlockDevice()

```cangjie
public func isBlockDevice(): Bool
```

**功能：** 用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是块特殊设备。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let isBLockDevice = FileFs.stat(filePath).isBlockDevice()
```

### func isCharacterDevice()

```cangjie
public func isCharacterDevice(): Bool
```

**功能：** 用于判断文件是否是字符特殊文件。一个字符特殊设备可进行随机访问，且访问的时候不带缓存。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是字符特殊设备。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let isCharacterDevice = FileFs.stat(filePath).isCharacterDevice()
```

### func isDirectory()

```cangjie
public func isDirectory(): Bool
```

**功能：** 用于判断文件是否是目录。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是目录。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let dirPath = pathDir + "/test"
let isDirectory = FileFs.stat(dirPath).isDirectory()
```

### func isFIFO()

```cangjie
public func isFIFO(): Bool
```

**功能：** 用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是&nbsp;FIFO。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let isFIFO = FileFs.stat(filePath).isFIFO()
```

### func isFile()

```cangjie
public func isFile(): Bool
```

**功能：** 用于判断文件是否是普通文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是普通文件。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let isFile = FileFs.stat(filePath).isFile()
```