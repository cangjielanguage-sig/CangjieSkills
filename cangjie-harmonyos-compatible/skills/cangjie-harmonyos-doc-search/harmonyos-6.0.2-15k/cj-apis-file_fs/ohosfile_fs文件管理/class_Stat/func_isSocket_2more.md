### func isSocket()

```cangjie
public func isSocket(): Bool
```

**功能：** 用于判断文件是否是套接字。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是套接字。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let isSocket = FileFs.stat(filePath).isSocket()
```

### func isSymbolicLink()

```cangjie
public func isSymbolicLink(): Bool
```

**功能：** 用于判断文件是否是符号链接。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是符号链接。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let isSymbolicLink = FileFs.stat(filePath).isSymbolicLink()
```