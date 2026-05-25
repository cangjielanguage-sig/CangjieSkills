## class FileUri

```cangjie
public class FileUri <: ToString {
    public init(uriOrPath: String)
}
```

**功能：** 提供在分享过程中将uri转分享路径path、应用自己的沙箱路径在分享时生成对应应用自己的uri、获取uri所在目录路径的uri等接口能力，方便应用对文件分享业务中uri的访问。

**系统能力：** SystemCapability.FileManagement.AppFileService

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.CoreFileKit.*

let pathDir = '123'
let path = pathDir + "/test"
let fileUriObject = FileUri(path)
AppLog.info("The path of FileUri is " + fileUriObject.path)
AppLog.info("The name of FileUri is " + fileUriObject.name)
```

### prop name

```cangjie
public prop name: String
```

**功能：** 获取FileUri对应文件名。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop path

```cangjie
public prop path: String
```

**功能：** 获取FileUri对应路径名。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### init(String)

```cangjie
public init(uriOrPath: String)
```

**功能：** FileUri的构造函数。

**系统能力：** SystemCapability.FileManagement.AppFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uriOrPath|String|是|-|URI或路径。URI类型：<br/>-&nbsp; 应用沙箱URI：file://\<bundleName>/\<sandboxPath> <br/>-&nbsp; 公共目录文件类URI：file://docs/storage/Users/currentUser/\<publicPath> <br/>-&nbsp; 公共目录媒体类URI：file://media/\<mediaType>/IMG_DATATIME_ID/\<displayName>|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |13900020|Invalid argument.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = '123'
let path = pathDir + "/test"
let uri = FileUri.getUriFromPath(path) // file://<packageName>/data/storage/el2/base/haps/entry/files/test
let fileUriObject = FileUri(uri)
```

### static func getUriFromPath(String)

```cangjie
public static func getUriFromPath(path: String): String
```

**功能：** 通过传入的路径path生成应用自己的uri(不支持媒体类型uri的获取)。将path转uri时，路径中的中文及非数字字母的特殊字符将会被编译成对应的ASCII码，拼接在uri中。

**系统能力：** SystemCapability.FileManagement.AppFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件的沙箱路径。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回文件URI。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The input parameter is invalid.|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串类型URI。

**系统能力：** SystemCapability.FileManagement.AppFileService

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串类型URI。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.CoreFileKit.*

let pathDir = '123'
let path = pathDir + "/test"
let fileUriObject = FileUri(path)
AppLog.info("The uri of FileUri is " + fileUriObject.toString())
```