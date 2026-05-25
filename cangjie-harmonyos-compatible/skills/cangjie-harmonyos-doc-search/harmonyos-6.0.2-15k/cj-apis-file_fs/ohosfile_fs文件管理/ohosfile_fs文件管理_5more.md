# ohos.file_fs（文件管理）

该模块为基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

## 导入模块

```cangjie
import kit.CoreFileKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class ConflictFileException

```cangjie
public class ConflictFileException <: BusinessException {
    public let data: Array<ConflictFiles>
}
```

**功能：** 异常类型，支持moveDir、copyDir使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**父类型：**

- [BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)

### let data

```cangjie
public let data: Array<ConflictFiles>
```

**功能：** 冲突文件信息。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** Array\<[ConflictFiles](#struct-conflictfiles)>

**读写能力：** 只读

**起始版本：** 12

## class CopyOptions

```cangjie
public class CopyOptions {
    public init(progressListener: ProgressListener, copySignal: TaskSignal)
}
```

**功能：** 拷贝进度回调监听。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

### prop copySignal

```cangjie
public prop copySignal: TaskSignal
```

**功能：** 取消拷贝信号。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** [TaskSignal](#class-tasksignal)

**读写能力：** 只读

**起始版本：** 19

### prop progressListener

```cangjie
public prop progressListener: ProgressListener
```

**功能：** 拷贝进度监听。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** [ProgressListener](#class-progresslistener)

**读写能力：** 只读

**起始版本：** 19

### init(ProgressListener, TaskSignal)

```cangjie
public init(progressListener: ProgressListener, copySignal: TaskSignal)
```

**功能：** 构造CopyOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|progressListener|[ProgressListener](#class-progresslistener)|是|-|拷贝进度监听。|
|copySignal|[TaskSignal](#class-tasksignal)|是|-|取消拷贝信号。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*

let mySig = TaskSignal()
let myProgress = ProgressListener(
    {
        progress => if (progress.totalSize < progress.processedSize * 2) {
            mySig.cancel()
        }
    })
let myOpt = CopyOptions(myProgress, mySig)
let srcPath = '123'
let destPath = '456'
FileFs.copy(srcPath, destPath, myOpt)
```