# 压缩与解压

本文针对常见的几种压缩、解压场景，介绍相关函数的使用方法。

## 接口说明

以下是示例中使用的主要接口，更多接口及使用方式请见[接口文档](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-bundle_manager.md)。

| 接口名                                                       | 接口描述                     |
| ------------------------------------------------------------ | ---------------------------- |
| compressFile(inFile: String, outFile: String, options: ZipOptions): Unit | 压缩文件。               |
| decompressFile(inFile: String, outFile: String, options?: ZipOptions): Unit | 解压文件。               |

## 开发步骤

### 环境准备

在应用沙箱目录下创建一个测试文件data.txt，并写入测试数据。示例代码如下。

<!-- run -->

```cangjie
import kit.CoreFileKit.*
import kit.BasicServicesKit.*

@Entry
@Component
class EntryView {
    @State
    var dataSize: Int64 = 0

    func build() {
        Row {
            Column {
                Button("创建测试文件data.txt").onClick {
                    =>
                    let fpath = "/data/storage/el2/base/"
                    // 创建文件data.txt
                    let inFile = FileFs.open(
                        fpath + '/data.txt',
                        mode: (OpenMode.CREATE.mode | READ_WRITE.mode)
                    )
                    // 写入测试数据
                    FileFs.write(inFile.fd, "hello world, hello world, hello world, hello world, hello world.")
                    // 获取测试数据原始大小，并保存到dataSize中
                    let stat = FileFs.stat(inFile.path)
                    this.dataSize = stat.size
                    AppLog.info("dataSize: ${this.dataSize}")
                    // 关闭文件
                    FileFs.close(inFile)
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

### Zip文件的压缩与解压

采用接口[compressFile()](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-bundle_manager.md#static-func-compressfilestring-string-zipoptions)将文件data.txt压缩并归档到data.zip中，采用接口[zlib.decompressFile()](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-bundle_manager.md#static-func-decompressfilestring-string-zipoptions)将data.zip解压到应用沙箱目录下，示例代码如下。

<!-- run -->

```cangjie
import kit.CoreFileKit.*
import kit.BasicServicesKit.*
import kit.AbilityKit.*

@Entry
@Component
class EntryView {
    @State
    var dataSize: Int64 = 0

    func build() {
        Row {
            Column {
                Button("compressFile").onClick {
                    =>
                    let inFile = "/data/storage/el2/base/data.txt"
                    let outFileDir = "/data/storage/el2/base/data.zip"

                    let options = ZipOptions(CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
                        MemLevel.MEM_LEVEL_DEFAULT, CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY)
                    try {
                        Zip.compressFile(inFile, outFileDir, options)
                    } catch (e: Exception) {
                        Hilog.info(0, "test_zlib_compressFile", "${e.toString()}")
                    }
                }

                Button("decompressFile").onClick {
                    =>
                    let inFile = "/data/storage/el2/base/data.zip"
                    let outFileDir = "/data/storage/el2/base/"

                    let options = ZipOptions(CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
                        MemLevel.MEM_LEVEL_DEFAULT, CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY)
                    try {
                        Zip.deCompressFile(inFile, outFileDir, options: options)
                    } catch (e: Exception) {
                        Hilog.info(0, "test_zlib_decompressFile", "${e.toString()}")
                    }
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}
```
