# ohos.zlib（Zip模块）

本模块提供压缩解压缩文件的能力。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## func compressFile(String, String, ZipOptions)

```cangjie
public func compressFile(inFile: String, outFile: String, options: ZipOptions): Unit
```

**功能：** 压缩文件，失败返回错误码。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 19

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|inFile|String|是|指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径。待压缩的文件夹不可为空，否则使用deCompressFile对压缩后的文件解压时会报错。|
|outFile|String|是|指定的压缩结果的文件路径。|
|options|[ZipOptions](#class-zipoptions)|是|压缩的配置参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |900001|The input source file is invalid.|
  |900002|The input destination file is invalid.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let inFile = "/data/storage/el2/base/a.txt"
let outFileDir = "/data/storage/el2/base/a.zip"
let options = ZipOptions(CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION, MemLevel.MEM_LEVEL_DEFAULT, CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY)
compressFile(inFile, outFileDir, options)
```

## func compressFiles(Array\<String>, String, ZipOptions)

```cangjie
public func compressFiles(inFiles: Array<String>, outFile: String, options: ZipOptions): Unit
```

**功能：** 压缩指定的多个文件，失败时返回错误码。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|inFiles|Array\<String>|是|指定压缩的文件夹路径或者文件路径，路径必须为沙箱路径。待压缩的文件夹不可为空，否则使用deCompressFile对压缩后的文件解压时会报错。|
|outFile|String|是|指定的压缩结果的文件路径。|
|options|[ZipOptions](#class-zipoptions)|是|压缩的配置参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |900001|The input source file is invalid.|
  |900002|The input destination file is invalid.|
  |17800009|Internal structure error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let inFile = "/data/storage/el2/base/a.txt"
let outFileDir = "/data/storage/el2/base/a.zip"
let options = ZipOptions(CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION, MemLevel.MEM_LEVEL_DEFAULT, CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY)
compressFiles([inFile], outFileDir, options)
```

## func createChecksum()

```cangjie
public func createChecksum(): Checksum
```

**功能：** 创建校验对象，成功时返回Checksum对象实例。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[Checksum](#class-checksum)|返回校验对象实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let checksum = createChecksum()
```

## func createGZip()

```cangjie
public func createGZip(): GZip
```

**功能：** 创建GZip对象，成功时返回Gzip对象实例。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[GZip](#class-gzip)|返回GZip对象实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let gzip = createGZip()
```