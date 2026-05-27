### static func moveDir(String, String, Int32)

```cangjie
public static func moveDir(src: String, dest: String, mode!: Int32 = 0): Unit
```

**功能：** 移动源文件夹至目标路径下。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|源文件夹的应用沙箱路径。|
|dest|String|是|-|目标文件夹的应用沙箱路径。|
|mode|Int32|否|0| **命名参数。** 移动模式。默认mode为0。<br/>-&nbsp;mode为0，文件夹级别抛异常。若目标文件夹下存在与源文件夹名冲突的同名非空文件夹，则抛出异常。<br/>-&nbsp;mode为1，文件级别抛异常。目标文件夹下存在与源文件夹名冲突的文件夹，若冲突文件夹下存在同名文件，则抛出异常。源文件夹下未冲突的文件全部移动至目标文件夹下，目标文件夹下未冲突文件将继续保留，且冲突文件信息将在抛出异常(ConfilictFileException)的data属性中以Array\<ConflictFiles>形式提供。<br/>-&nbsp; mode为2，文件级别强制覆盖。目标文件夹下存在与源文件夹名冲突的文件夹，若冲突文件夹下存在同名文件，则强制覆盖冲突文件夹下所有同名文件，未冲突文件将继续保留。<br/>-&nbsp; mode为3，文件夹级别强制覆盖。移动源文件夹至目标文件夹下，目标文件夹下移动的文件夹内容与源文件夹完全一致。若目标文件夹下存在与源文件夹名冲突的文件夹，该文件夹下所有原始文件将不会保留。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let pathDir = "path/to/file"
// move directory from srcPath to destPath
let srcPath = pathDir + "/srcDir/"
let destPath = pathDir + "/destDir/"
FileFs.moveDir(srcPath, destPath, mode: 1)
```

### static func moveFile(String, String, Int32)

```cangjie
public static func moveFile(src: String, dest: String, mode!: Int32 = 0): Unit
```

**功能：** 以同步方式移动文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|源文件的应用沙箱路径。|
|dest|String|是|-|目的文件的应用沙箱路径。|
|mode|Int32|否|0| **命名参数。** 移动模式。若mode为0，移动位置存在同名文件时，强制移动覆盖。若mode为1，移动位置存在同名文件时，抛出异常。默认为0。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let pathDir = "path/to/file"
let srcPath = pathDir + "/srcDir/"
let destPath = pathDir + "/destDir/"
FileFs.moveFile(srcPath, destPath, mode: 0)
Applog.info("move file succeed")
```