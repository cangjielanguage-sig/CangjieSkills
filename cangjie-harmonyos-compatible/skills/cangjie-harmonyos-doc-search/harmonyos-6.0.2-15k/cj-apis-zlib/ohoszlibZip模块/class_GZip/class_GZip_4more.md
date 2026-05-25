## class GZip

```cangjie
public class GZip {}
```

**功能：** Gzip相关接口。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

### func gzclose()

```cangjie
public func gzclose(): ReturnStatus
```

**功能：** 清除文件的所有挂起输出，如有必要，关闭文件和释放(解)压缩状态。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[ReturnStatus](#enum-returnstatus)|返回结果状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17800004|ZStream error.|
  |17800006|Memory allocation failed.|
  |17800009|Internal structure error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let inFile = "/data/storage/el2/base/a.gz"
let gzip = createGZip()
gzip.gzopen(inFile, "wb")
let state = gzip.gzclose()
AppLog.info("gzclose return state: ${state}")
```

### func gzdopen(Int32, String)

```cangjie
public func gzdopen(fd: Int32, mode: String): Unit
```

**功能：** 将gzFile与文件描述符fd相关联，打开文件，用于进行读取并解压缩，或者压缩并写入。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|fd|Int32|是|文件描述符。通常情况下，通过系统调用“open”或其他方法获得的。|
|mode|String|是|用于指定访问模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[zlib子系统错误码](../../errorcodes/cj-errorcode-zlib.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17800002|No such file or access mode error.|
  |17800009|Internal structure error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let inFile = "/data/storage/el2/base/a.gz"
let gzip = createGZip()
let file = FileFs.open(inFile, mode: OpenMode.READ_WRITE.mode | OpenMode.CREATE.mode)
gzip.gzdopen(file.fd, "wb")
let state = gzip.gzclose()
AppLog.info("gzclose return state: ${state}")
```

### func gzeof()

```cangjie
public func gzeof(): Int32
```

**功能：** 检查gzip压缩文件的读取位置是否已到达文件的末尾。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Int32|如果在读取时设置了文件的文件结束指示符，则返回1。|

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