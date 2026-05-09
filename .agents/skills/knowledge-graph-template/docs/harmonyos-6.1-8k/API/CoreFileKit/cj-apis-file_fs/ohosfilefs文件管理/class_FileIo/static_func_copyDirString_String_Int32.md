### static func copyDir(String, String, Int32)

```cangjie
public static func copyDir(src: String, dest: String, mode!: Int32 = 0): Unit
```

**功能：** 复制源文件夹至目标路径下。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|源文件夹的应用沙箱路径。|
|dest|String|是|-|目标文件夹的应用沙箱路径。|
|mode|Int32|否|0| **命名参数。** 复制模式，默认值为0。<br/>-&nbsp; mode为0，文件级别抛异常。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array\<[ConflictFiles](#class-conflictfiles)>形式提供。<br/>-&nbsp; mode为1，文件级别强制覆盖。目标目录下存在与源目录名冲突的目录，若冲突目录下存在同名文件，则强制覆盖冲突目录下所有同名文件，未冲突文件将继续保留。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900002 | No such file or directory. |
  | 13900004 | Interrupted system call. |
  | 13900005 | I/O error. |
  | 13900008 | Bad file descriptor. |
  | 13900010 | Try again. |
  | 13900011 | Out of memory. |
  | 13900012 | Permission denied. |
  | 13900013 | Bad address. |
  | 13900015 | File exists. |
  | 13900018 | Not a directory. |
  | 13900019 | Is a directory. |
  | 13900020 | Invalid argument. |
  | 13900030 | File name too long. |
  | 13900031 | Function not implemented. |
  | 13900033 | Too many symbolic links encountered. |
  | 13900034 | Operation would block. |
  | 13900038 | Value too large for defined data type. |
  | 13900042 | Unknown error. |
  | 13900044 | Network is unreachable. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let pathDir = "path/to/file"
    let srcPath = pathDir + "/srcDir/"
    let destPath = pathDir + "/destDir/"
    FileIo.copyDir(srcPath, destPath, mode: 0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```