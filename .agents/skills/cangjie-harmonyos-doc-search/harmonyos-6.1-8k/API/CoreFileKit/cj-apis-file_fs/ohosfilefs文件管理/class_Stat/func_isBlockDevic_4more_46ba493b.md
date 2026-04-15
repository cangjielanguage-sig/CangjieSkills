### func isBlockDevice()

```cangjie
public func isBlockDevice(): Bool
```

**功能：** 用于判断文件是否是块特殊文件。一个块特殊文件只能以块为粒度进行访问，且访问的时候带缓存。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是块特殊设备。true：是块特殊设备；false：不是块特殊设备。|

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
    let isBLockDevice = FileIo.stat(filePath).isBlockDevice()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isCharacterDevice()

```cangjie
public func isCharacterDevice(): Bool
```

**功能：** 判断文件是否为字符特殊文件。字符特殊设备支持随机访问，且访问时无缓存。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是字符特殊设备。true：是字符特殊设备；false：不是字符特殊设备。|

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
    let isCharacterDevice = FileIo.stat(filePath).isCharacterDevice()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isDirectory()

```cangjie
public func isDirectory(): Bool
```

**功能：** 判断文件是否为目录。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是目录。true：是目录；false：不是目录。|

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
    let dirPath = pathDir + "/test"
    let isDirectory = FileIo.stat(dirPath).isDirectory()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isFifo()

```cangjie
public func isFifo(): Bool
```

**功能：** 用于判断文件是否是命名管道（有时也称为FIFO）。命名管道通常用于进程间通信。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|表示文件是否是&nbsp;FIFO。true：是FIFO；false：不是FIFO。|

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
    let res = FileIo.stat(filePath).isFifo()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```