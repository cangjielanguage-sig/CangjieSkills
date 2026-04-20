### var saveas

```cangjie
public var saveas:String
```

**功能：** 保存下载文件的路径，包括如下几种：

相对路径，位于调用方的缓存路径下，如"./xxx/yyy/zzz.html"、"xxx/yyy/zzz.html"。

internal协议路径，支持"internal://"及其子路径，internal为调用方（传入的context）对应路径，"internal://cache"对应context.cacheDir。如"internal://cache/path/to/file.txt"。

应用沙箱目录，只支持到base及其子目录下，如"/data/storage/el1/base/path/to/file.txt"。

file协议路径，支持应用文件和用户文件，应用文件必须匹配应用包名，只支持到base及其子目录下，如"file://com.example.test/data/storage/el2/base/file.txt"。用户文件必须为调用方创建好的用户文件uri。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var title

```cangjie
public var title:?String
```

**功能：** 任务标题，其最大长度为256个字符。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var token

```cangjie
public var token: ?String
```

**功能：** 任务令牌。查询带有token的任务需提供token并通过[request.agent.touch](#func-touchstring-string)查询，否则无法查询到指定任务。其最小为8个字节，最大为2048个字节。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var url

```cangjie
public var url: String
```

**功能：** 资源地址。最大长度为8192个字符。支持HTTP拦截功能。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22