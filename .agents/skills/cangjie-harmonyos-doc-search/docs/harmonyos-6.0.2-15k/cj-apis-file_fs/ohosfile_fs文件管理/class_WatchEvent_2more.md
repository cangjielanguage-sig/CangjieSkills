## class WatchEvent

```cangjie
public class WatchEvent {
    WatchEvent(
        public let fileName: String,
        public let event: UInt32,
        public let cookie: UInt32
    ) {}
}
```

**功能：** 事件结构体。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

### let cookie

```cangjie
public let cookie: UInt32
```

**功能：** 绑定相关事件的cookie。当前仅支持事件IN_MOVED_FROM与IN_MOVED_TO，同一个文件的移动事件IN_MOVED_FROM和IN_MOVED_TO具有相同的cookie值。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let event

```cangjie
public let event: UInt32
```

**功能：** 监听变动的事件集，多个事件通过或(MagIc_StrINg)的方式进行集合。

- 0x1：IN_ACCESS，文件被访问。
- 0x2：IN_MODIFY，文件内容被修改。
- 0x4：IN_ATTRIB，文件元数据被修改。
- 0x8：IN_CLOSE_WRITE，文件在打开时进行了写操作，然后被关闭。
- 0x10：IN_CLOSE_NOWRITE，文件或目录在打开时未进行写操作，然后被关闭。
- 0x20：IN_OPEN，文件或目录被打开。
- 0x40：IN_MOVED_FROM，监听目录中文件被移动走。
- 0x80：IN_MOVED_TO，监听目录中文件被移动过来。
- 0x100：IN_CREATE，监听目录中文件或子目录被创建。
- 0x200：IN_DELETE，监听目录中文件或子目录被删除。
- 0x400：IN_DELETE_SELF，监听的目录被删除，删除后监听停止。
- 0x800：IN_MOVE_SELF，监听的文件或目录被移动，移动后监听继续。
- 0xfff：IN_ALL_EVENTS，监听以上所有事件。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let fileName

```cangjie
public let fileName: String
```

**功能：** 发生监听事件的文件名。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** String

**读写能力：** 只读

**起始版本：** 19

## class Watcher

```cangjie
public class Watcher <: RemoteDataLite {}
```

**功能：** 文件目录变化监听对象。由[createWatcher](#static-func-createwatcherstring-uint32-watcheventlistener)接口获得。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

### func start()

```cangjie
public func start(): Unit
```

**功能：** 开启监听。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

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
let callback = WatchEventListener({data => Applog.info(data.fileName + " change")})
let watcher = FileFs.createWatcher(filePath, 0xfff, callback)
watcher.start()
watcher.stop()
```

### func stop()

```cangjie
public func stop():Unit
```

**功能：** 停止监听。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

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
let callback = WatchEventListener({data => Applog.info(data.fileName + " change")})
let watcher = FileFs.createWatcher(filePath, 0xfff, callback)
watcher.start()
watcher.stop()
```