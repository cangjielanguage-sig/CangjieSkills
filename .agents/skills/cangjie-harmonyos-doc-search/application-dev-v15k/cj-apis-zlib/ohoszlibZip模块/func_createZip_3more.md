## func createZip()

```cangjie
public func createZip(): Zip
```

**功能：** 创建压缩解压缩对象实例，成功时返回压缩解压缩对象实例。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[Zip](#class-zip)|返回压缩解压缩对象实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let zip = createZip()
```

## func deCompressFile(String, String, Option\<ZipOptions>)

```cangjie
public func deCompressFile(inFile: String, outFile: String, options!: Option<ZipOptions> = None): Unit
```

**功能：** 解压文件，失败时返回错误码。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 19

**参数：**

|参数名|类型|必填性|默认值|说明|
|:---|:---|:---|:---|:---|
|inFile|String|是|-|指定的待解压缩文件的文件路径，文件后缀需要以.zip结尾。文件路径必须为沙箱路径。|
|outFile|String|是|-|指定的解压后的文件夹路径，文件夹目录路径需要在系统中存在，不存在则会解压失败。路径必须为沙箱路径，如果待解压的文件或文件夹在解压后的路径下已经存在，则会直接覆盖同名文件或同名文件夹中的同名文件。|
|options|Option\<[ZipOptions](#class-zipoptions)>|否|None|**命名参数。** 解压的配置参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |900001| The input source file is invalid.|
  |900002| The input destination file is invalid.|
  |900003| The input source file is not ZIP format or damaged.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let inFile = "/data/storage/el2/base/a.zip"
let outFileDir = "/data/storage/el2/base/"
let options = ZipOptions(CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION, MemLevel.MEM_LEVEL_DEFAULT, CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY)
deCompressFile(inFile, outFileDir, options: options)
```

## func getOriginalSize(String)

```cangjie
public func getOriginalSize(compressedFile: String): Int64
```

**功能：** 获取压缩文件的原始大小，成功时返回压缩文件的原始大小，失败时返回错误码。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|compressedFile|String|是|指定的压缩文件的文件路径，只支持zip格式压缩文件。文件路径必须为沙箱路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回压缩文件的原始大小，单位字节。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |900001| The input source file is invalid.|
  |900003| The input source file is not ZIP format or damaged.|
  |17800009|Internal structure error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let inFile = "/data/storage/el2/base/a.zip"
let originSize = getOriginalSize(inFile)
```