### static func listFile(String, ListFileOptions)

```cangjie
public static func listFile(path: String, options!: ListFileOptions = ListFileOptions()): Array<String>
```

**功能：** 以同步方式列出文件夹下所有文件名，支持递归列出所有文件名（包含子目录下），支持文件过滤。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件夹的应用沙箱路径。|
|options|[ListFileOptions](#struct-listfileoptions)|否|ListFileOptions()| **命名参数。** 文件过滤选项。默认不进行过滤。|

**options参数说明：**

| 参数名    | 类型     | 必填   | 说明                          |
| :------ | :------ | :---- | :--------------------------- |
| recursion | Bool | 否    | 是否递归子目录下文件名，默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及文件夹名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以/开头）。 |
| listNum | Int32 | 否    | 列出文件名数量。当设置0时，列出所有文件，默认为0。 |
| filter | [Filter](#struct-filter) | 否    |文件过滤选项。当前仅支持后缀名匹配、文件名模糊查询、文件大小过滤、最近修改时间过滤。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回文件名数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let filter = Filter(suffix: [".png", ".jpg", ".jpeg"], displayName: ["*abc", "efg*"])
let listFileOptions = ListFileOptions(recursion: false, listNum: 0, filter: filter)
let filenames = FileFs.listFile(pathDir, options: listFileOptions)
for (name in filenames) {
  Applog.info(name)
}
```

### static func lseek(Int32, Int64, WhenceType)

```cangjie
public static func lseek(fd: Int32, offset: Int64, whence!: WhenceType = SEEK_SET): Int64
```

**功能：** 调整文件偏置指针位置。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|文件描述符。|
|offset|Int64|是|-|相对偏移位置。|
|whence|[WhenceType](#enum-whencetype)|否|SEEK_SET| **命名参数。** 偏移指针相对位置类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|当前文件偏置指针位置（相对于文件头的偏移量）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let filePath = pathDir + "/test.txt"
let file = FileFs.open(filePath, mode: CREATE.mode)
let offset = FileFs.lseek(file.fd, 5, whence: WhenceType.SEEK_SET)
Applog.info("The current offset is at " + offset.toString())
FileFs.close(file)
```