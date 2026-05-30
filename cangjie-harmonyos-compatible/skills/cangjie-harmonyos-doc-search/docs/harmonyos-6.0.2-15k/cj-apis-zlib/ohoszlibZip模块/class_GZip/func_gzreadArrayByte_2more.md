### func gzread(Array\<Byte>)

```cangjie
public func gzread(buf: Array<Byte>): Int64
```

**功能：** 从文件中读取最多len个未压缩字节并将其解压缩到buf中。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|buf|Array\<Byte>|是|目标偏移位置。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回实际读取的未压缩字节数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17800009|Internal structure error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let inFile = "/data/storage/el2/base/a.gz"
let gzip = createGZip()
gzip.gzopen(inFile, "rb")
let readData = Array<Byte>(100, repeat: 0)
let readNum = gzip.gzread(readData)
let eofNum = gzip.gzeof()
AppLog.info("gzeof return eofNum: ${eofNum}")
let state = gzip.gzclose()
AppLog.info("gzclose return state: ${state}")
```

### func gzwrite(Array\<Byte>, Int64)

```cangjie
public func gzwrite(buf: Array<Byte>, len: Int64): Int64
```

**功能：** 将buf中的len长度的未压缩字节进行压缩并将其写入文件。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|buf|Array\<Byte>|是|对象指向要写入的数据缓冲区。|
|len|Int64|是|未压缩字节长度。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回写入的未压缩字节数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17800009|Internal structure error.|

- IllegalArgumentException：参数校验错误。

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |The parameter check failed.|参数校验错误。|请检查传入的参数是否正确。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let inFile = "/data/storage/el2/base/a.gz"
let gzip = createGZip()
gzip.gzopen(inFile, "wb")
let testData = [b'h', b'e', b'l', b'l', b'o', b' ', b'w', b'o', b'r', b'l', b'd', b'!']
let writeNum = gzip.gzwrite(testData, testData.size)
AppLog.info("gzwrite return writeNum: ${writeNum}")
let state = gzip.gzclose()
```