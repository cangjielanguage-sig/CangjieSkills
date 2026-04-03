### 以流的形式读写文件

以下示例代码演示了如何使用流接口读取test.txt的文件内容并写入到destFile.txt文件中。

```cangjie
// xxx.cj
import kit.CoreFileKit.*
import kit.AbilityKit.*
import ohos.base.*

// 见获取UIAbility的上下文信息章节
let context = getContext()
// 获取应用文件路径
let filesDir = context.filesDirectory

func readWriteFileWithStream() {
    // 创建并打开输入文件流
    let inputStream = FileFs.createStream(filesDir + '/test.txt', 'r+')
    // 创建并打开输出文件流
    let outputStream = FileFs.createStream(filesDir + '/destFile.txt', "w+")

    let bufSize = 4096
    var readSize = 0
    let buf = Array<Byte>(bufSize, repeat: 0)
    var readOptions = ReadOptions(
        offset: readSize,
        length: UIntNative(bufSize)
    )
    // 以流的形式读取源文件内容并写入到目标文件
    var readLen = inputStream.read(buf, options: readOptions)
    readSize += readLen
    while (readLen > 0) {
        outputStream.write(buf[0..readLen])
        readOptions.offset = readSize
        readLen = inputStream.read(buf, options: readOptions)
        readSize += readLen
    }
    // 关闭文件流
    inputStream.close()
    outputStream.close()
}
```

> **说明：**
>
> 使用流接口时，需注意流的及时关闭。流接口不支持并发读写。

### 查看文件列表

以下示例代码演示了如何查看文件列表。

```cangjie
import kit.CoreFileKit.*
import kit.CoreFileKit.*
import kit.AbilityKit.*
import ohos.base.*

// 见获取UIAbility的上下文信息章节
let context = getContext()
// 获取应用文件路径
let filesDir = context.filesDirectory

// 查看文件列表
func getListFile() {
    let listFileOption = ListFileOptions(
        recursion: false,
        listNum: 0,
        filter: Filter(
            suffix: [".png", ".jpg", ".txt"],
            displayName: ["test*"],
            fileSizeOver: 0,
            lastModifiedAfter: 10000.0
        )
    )
    let files = FileFs.listFile(filesDir, options: listFileOption)
    for (item in files) {
        AppLog.info("The name of file: ${item}")
    }
}
```