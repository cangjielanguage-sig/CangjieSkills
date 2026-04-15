### func isFile()

```cangjie
public func isFile(): Bool
```

**功能：** 用于判断文件是否是普通文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是普通文件。true：是普通文件；false：不是普通文件。|

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"  // 请替换正确的文件路径，获取文件路径参考本文使用说明
    let isFile = FileIo.stat(filePath).isFile()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isSocket()

```cangjie
public func isSocket(): Bool
```

**功能：** 判断文件是否是套接字。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是套接字。true：是套接字；false：不是套接字。|

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"  // 请替换正确的文件路径，获取文件路径参考本文使用说明
    let isSocket = FileIo.stat(filePath).isSocket()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isSymbolicLink()

```cangjie
public func isSymbolicLink(): Bool
```

**功能：** 判断文件是否为符号链接。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是符号链接。true：是符号链接；false：不是符号链接。|

**示例：**

<!-- compile only -->
<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let filePath = pathDir + "/test.txt"  // 请替换正确的文件路径，获取文件路径参考本文使用说明
    let isSymbolicLink = FileIo.stat(filePath).isSymbolicLink()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```