## class TaskSignal

```cangjie
public class TaskSignal {
    public init()
}
```

**功能：** 拷贝中断信号。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 构造TaskSignal对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

### func cancel()

```cangjie
public func cancel(): Unit
```

**功能：** 取消拷贝任务。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

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
let mySig = TaskSignal()
let myProgress = ProgressListener(
    {
        progress => if (progress.totalSize < progress.processedSize * 2) {
            mySig.cancel()
        }
    })
let myOpt = CopyOptions(myProgress, mySig)
FileFs.copy(srcPath, destPath, myOpt)
```

## class WatchEventListener

```cangjie
public class WatchEventListener <: Callback1Argument<WatchEvent> {
    public init(callback: (WatchEvent) -> Unit)
}
```

**功能：** 事件监听类。继承[单参回调抽象类](../BasicServicesKit/cj-apis-base.md#class-callback1argument)实现，使用需要的回调能力初始化回调对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**父类型：**

- [Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[WatchEvent](#class-watchevent)>

### init((WatchEvent) -> Unit)

```cangjie
public init(callback: (WatchEvent) -> Unit)
```

**功能：** 构造WatchEventListener对象。它接收一个参数`callback`，这是一个闭包，当接收到文件系统事件时，该闭包会被调用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([WatchEvent](#class-watchevent)) -> Unit|是|-|表示闭包接受一个`WatchEvent`类型的参数，并不返回任何值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

### func invoke(WatchEvent)

```cangjie
public func invoke(val: WatchEvent): Unit
```

**功能：** 这个方法用于触发之前定义的回调闭包。当文件系统中发生某些变化时，可以通过调用此方法来通知注册的监听者。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|val|[WatchEvent](#class-watchevent)|是|-|表示触发回调的具体事件类型，例如文件创建、删除等。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。