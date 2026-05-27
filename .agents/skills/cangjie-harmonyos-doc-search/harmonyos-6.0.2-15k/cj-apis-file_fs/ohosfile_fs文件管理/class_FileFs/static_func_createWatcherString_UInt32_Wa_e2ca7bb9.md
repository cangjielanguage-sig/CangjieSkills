### static func createWatcher(String, UInt32, WatchEventListener)

```cangjie
public static func createWatcher(path: String, events: UInt32, listener: WatchEventListener): Watcher
```

**功能：** 创建Watcher对象，用来监听文件或目录变动。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|监听文件或目录的沙箱路径。|
|events|UInt32|是|-|监听变动的事件集，多个事件通过或(MagIc_StrINg)的方式进行集合。<br/>-&nbsp;0x1：IN_ACCESS，文件被访问。<br/>-&nbsp;0x2：IN_MODIFY，文件内容被修改。<br/>-&nbsp;0x4：IN_ATTRIB，文件元数据被修改。<br/>-&nbsp;0x8：IN_CLOSE_WRITE，文件在打开时进行了写操作，然后被关闭。<br/>-&nbsp;0x10：IN_CLOSE_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。<br/>-&nbsp;0x20：IN_OPEN，文件或目录被打开。<br/>-&nbsp;0x40：IN_MOVED_FROM，监听目录中文件被移动走。<br/>-&nbsp;0x80：IN_MOVED_TO，监听目录中文件被移动过来。<br/>-&nbsp;0x100：IN_CREATE，监听目录中文件或子目录被创建。<br/>-&nbsp;0x200：IN_DELETE，监听目录中文件或子目录被删除。<br/>-&nbsp;0x400：IN_DELETE_SELF，监听的目录被删除，删除后监听停止。<br/>-&nbsp;0x800：IN_MOVE_SELF，监听的文件或目录被移动，移动后监听继续。<br/>-&nbsp;0xfff：IN_ALL_EVENTS，监听以上所有事件。|
|listener|[WatchEventListener](#class-watcheventlistener)|是|-|监听事件发生后的回调函数对象。监听事件发生一次，回调一次。|

**返回值：**

|类型|说明|
|:----|:----|
|[Watcher](#class-watcher)|返回Watcher对象。|

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
let file = FileFs.open(filePath, mode: (READ_ONLY.mode | CREATE.mode))
let callback = WatchEventListener({data =>
    if (data.event == 0x2) {
        Applog.info(data.fileName + " was modified")
    } else if (data.event == 0x10) {
        Applog.info(data.fileName + " was closed")
    }
})
let watcher = FileFs.createWatcher(filePath, (0x2 | 0x10), callback)
watcher.start()
FileFs.write(file.fd, "test")
FileFs.close(file)
watcher.stop()
```