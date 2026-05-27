### static func copyDir(String, String, Int32)

```cangjie
public static func copyDir(src: String, dest: String, mode!: Int32 = 0): Unit
```

**功能：** 复制源文件夹至目标路径下。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|源文件夹的应用沙箱路径。|
|dest|String|是|-|目标文件夹的应用沙箱路径。|
|mode|Int32|否|0| **命名参数。** 复制模式。默认mode为0。<br/>-&nbsp; mode为0，文件级别抛异常。目标文件夹下存在与源文件夹名冲突的文件夹，若冲突文件夹下存在同名文件，则抛出异常。源文件夹下未冲突的文件全部移动至目标文件夹下，目标文件夹下未冲突文件将继续保留，且冲突文件信息将在抛出异常(ConfilictFileException)的data属性中以Array\<ConflictFiles>形式提供。<br/>-&nbsp; mode为1，文件级别强制覆盖。目标文件夹下存在与源文件夹名冲突的文件夹，若冲突文件夹下存在同名文件，则强制覆盖冲突文件夹下所有同名文件，未冲突文件将继续保留。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let srcPath = pathDir + "/srcDir/"
let destPath = pathDir + "/destDir/"
FileFs.copyDir(srcPath, destPath, mode: 0)
```

### static func copyFile(String, String, Int32)

```cangjie
public static func copyFile(src: String, dest: String, mode!: Int32 = 0): Unit
```

**功能：** 复制文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|待复制文件的文件描述符。|
|dest|String|是|-|目标文件的文件描述符。|
|mode|Int32|否|0| **命名参数。** mode提供覆盖文件的选项，当前仅支持0，且默认为0。<br/>0：完全覆盖目标文件，未覆盖部分将被裁切掉。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
let srcPath = pathDir + "/srcDir/test.txt"
let dstPath = pathDir + "/dstDir/test.txt"
FileFs.copyFile(srcPath, dstPath, mode: 0)
```

### static func copyFile(String, Int32, Int32)

```cangjie
public static func copyFile(src: String, dest: Int32, mode!: Int32 = 0): Unit
```

**功能：** 复制文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|待复制文件的文件描述符。|
|dest|Int32|是|-|目标文件的文件描述符。|
|mode|Int32|否|0| **命名参数。** mode提供覆盖文件的选项，当前仅支持0，且默认为0。<br/>0：完全覆盖目标文件，未覆盖部分将被裁切掉。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。