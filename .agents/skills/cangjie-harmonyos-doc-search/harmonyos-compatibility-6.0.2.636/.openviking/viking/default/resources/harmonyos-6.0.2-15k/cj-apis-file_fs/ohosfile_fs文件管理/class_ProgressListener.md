## class ProgressListener

```cangjie
public class ProgressListener <: Callback1Argument<Progress> {
    public init(callback: (Progress) -> Unit)
}
```

**功能：** 拷贝进度监听。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**父类型：**

- [Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[Progress](#struct-progress)>

### init((Progress) -> Unit)

```cangjie
public init(callback: (Progress) -> Unit)
```

**功能：** 构造ProgressListener对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([Progress](#struct-progress)) -> Unit|是|-|监听对象的回调执行函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.*

let mySig = TaskSignal()
let myProgress = ProgressListener(
    {
    progress => Applog.info("processedSize: ${progress.processedSize}, totalSize: ${progress.totalSize}")
})
let myOpt = CopyOptions(myProgress, mySig)
```

### func invoke(Progress)

```cangjie
public func invoke(val: Progress): Unit
```

**功能：** 触发回调函数。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|[Progress](#struct-progress)|是|-|事件触发时，传递给回调事件的参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。