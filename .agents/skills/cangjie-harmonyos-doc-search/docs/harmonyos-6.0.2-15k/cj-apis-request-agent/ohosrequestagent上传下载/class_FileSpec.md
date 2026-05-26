## class FileSpec

```cangjie
public class FileSpec {
    public FileSpec(
        public var path!: String,
        public var mimeType!: ?String = None,
        public var filename!: ?String = None,
        public var extras!: ?HashMap<String, String> = None
    )
}
```

**功能：** 表单项的文件信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

### var extras

```cangjie
public var extras: ?HashMap<String, String> = None
```

**功能：** 文件信息的附加内容。

**类型：** ?HashMap\<String, String>

**读写能力：** 可读写

**起始版本：** 12

### var filename

```cangjie
public var filename: ?String = None
```

**功能：** 文件名，默认值通过路径获取。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var mimeType

```cangjie
public var mimeType: ?String = None
```

**功能：** 文件的mimetype通过文件名获取。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var path

```cangjie
public var path: String
```

**功能：** 文件路径：位于调用方的缓存文件夹下的相对路径或用户公共文件，如"file://media/Photo/path/to/file.img"。
仅支持前端任务。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### FileSpec(String, ?String, ?String, ?HashMap\<String, String>)

```cangjie
public FileSpec(
    public var path!: String,
    public var mimeType!: ?String = None,
    public var filename!: ?String = None,
    public var extras!: ?HashMap<String, String> = None
)
```

**功能：** 创建FileSpec对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-| **命名参数。** 文件路径：<br>- 位于调用方的缓存文件夹下的相对路径。<br>- 用户公共文件，如"file://media/Photo/path/to/file.img"。仅支持前端任务。 |
|mimeType|?String|否|None| **命名参数。** 文件的mimetype通过文件名获取。|
|filename|?String|否|None| **命名参数。** 文件名，默认值通过路径获取。|
|extras|?HashMap\<String, String>|否|None| **命名参数。** 文件信息的附加内容。|