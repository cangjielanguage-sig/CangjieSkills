### func gzgets(Array\<Byte>)

```cangjie
public func gzgets(buf: Array<Byte>): String
```

**功能：** 从文件中读取字节并将其解压缩到buf中，直到读取len-1字符，或者直到读取换行符并将其传输到buf，或者遇到文件结束条件。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|buf|Array\<Byte>|是|存储读取的行数据。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回以'\0'结尾的字符串。|

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
let getsBuf = Array<Byte>(16, repeat: 0)
let getsRes = gzip.gzgets(getsBuf)
AppLog.info("gzgets return getsRes: ${getsRes}")
gzip.gzclose()
```

### func gzopen(String, String)

```cangjie
public func gzopen(path: String, mode: String): Unit
```

**功能：** 打开位于指定路径的gzip(.gz)文件，用于进行读取并解压缩，或者压缩并写入。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|path|String|是|需要打开的文件路径。|
|mode|String|是|指定文件打开方法。|

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
gzip.gzopen(inFile, "wb")
let state = gzip.gzclose()
AppLog.info("gzclose return state: ${state}")
```

### func gzputs(String)

```cangjie
public func gzputs(str: String): Int32
```

**功能：** 压缩给定的以'\0'结尾的字符串并将其写入文件，不包括终止的'\0'字符。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|str|String|是|格式化描述符和纯文本。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回写入的字符数。|

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
gzip.gzopen(inFile, "wb")
let putsNum = gzip.gzputs("testdata")
AppLog.info("gzputs return putsNum: ${putsNum}")
gzip.gzclose()
```