## 开发示例

在对应用文件开始访问前，开发者需要[获取应用文件路径](../application-models/cj-application-context-stage.md#获取应用文件路径)。以从AbilityContext获取HAP级别的文件路径为例进行说明，AbilityContext的获取方式请参见[获取UIAbility的上下文信息](../application-models/cj-uiability-usage.md#获取uiability的上下文信息)。

下面介绍几种常用操作示例。

### 新建并读写一个文件

以下示例代码演示了如何新建一个文件并对其读写。

```cangjie
// xxx.cj
import kit.CoreFileKit.*
import kit.AbilityKit.*
import ohos.base.*

// 见获取UIAbility的上下文信息章节
let context = getContext()
// 获取应用文件路径
let filesDir = context.filesDirectory

func createFile(): Unit {
    // 文件不存在时创建并打开文件，文件存在时打开文件
    let file = FileFs.open(filesDir + '/test.txt', mode: OpenMode.READ_WRITE.mode | OpenMode.CREATE.mode)
    // 写入一段内容至文件
    let writeLen = FileFs.write(file.fd, "Try to write str.")
    AppLog.info("The length of str is: ${writeLen}")
    let bufSize = 4096
    var readSize = 0
    // 创建一个大小为1024字节的Array<Byte>对象，用于存储从文件中读取的数据
    let array = Array<Byte>(1024, repeat: 0)
    // 设置读取的偏移量和长度
    let readOptions = ReadOptions(
        offset: readSize,
        length: UIntNative(bufSize)
    )
    // 读取文件内容到ArrayBuffer对象中，并返回实际读取的字节数
    let readLen = FileFs.read(file.fd, array, options: readOptions)
    AppLog.info("the content of file: ${String.fromUtf8(array[..readLen])}")
    // 关闭文件
    FileFs.close(file)
}
```

### 读取文件内容并写入到另一个文件

以下示例代码演示了如何从一个文件读写内容到另一个文件。

```cangjie
// xxx.cj
import kit.CoreFileKit.*
import kit.AbilityKit.*
import ohos.base.*

// 见获取UIAbility的上下文信息章节
let context = getContext()
// 获取应用文件路径
let filesDir = context.filesDirectory

func readWriteFile() {
    // 打开文件
    let srcFile = FileFs.open(filesDir + '/test.txt', mode: OpenMode.READ_WRITE.mode | OpenMode.CREATE.mode)
    let destFile = FileFs.open(filesDir + '/destFile.txt', mode: OpenMode.READ_WRITE.mode | OpenMode.CREATE.mode)
    // 读取源文件内容并写入至目的文件
    let bufSize = 4096
    var readSize = 0
    let buf = Array<Byte>(bufSize, repeat: 0)
    var readOptions = ReadOptions(
        offset: readSize,
        length: UIntNative(bufSize)
    )
    var readLen = FileFs.read(srcFile.fd, buf, options: readOptions)
    while (readLen > 0) {
        readSize += readLen
        let writeOptions = WriteOptions(length: UIntNative(readLen))
        FileFs.write(destFile.fd, buf, options: writeOptions)
        readOptions.offset = readSize
        readLen = FileFs.read(srcFile.fd, buf, options: readOptions)
    }
    // 关闭文件
    FileFs.close(srcFile)
    FileFs.close(destFile)
}
```

> **说明：**
>
> 使用读写接口时，需注意可选项参数offset的设置。对于已存在且读写过的文件，文件偏移指针默认在上次读写操作的终止位置。