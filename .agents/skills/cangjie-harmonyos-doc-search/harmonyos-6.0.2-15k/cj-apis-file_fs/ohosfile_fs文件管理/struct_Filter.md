## struct Filter

```cangjie
public struct Filter {
    public Filter(
        public var suffix!: Array<String> = Array<String>(),
        public var displayName!: Array<String> = Array<String>(),
        public var mimeType!: Array<String> = Array<String>(),
        public var fileSizeOver!: ?Int64 = None,
        public var lastModifiedAfter!: ?Float64 = None,
        public var excludeMedia!: Bool = false
    )
}
```

**功能：** 文件过滤配置项类型，支持listFile接口使用。其中mimeType与excludeMedia过滤暂不支持。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### var displayName

```cangjie
public var displayName: Array<String> = Array<String>()
```

**功能：** 文件名模糊匹配，各个关键词OR关系。当前仅支持通配符*。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var excludeMedia

```cangjie
public var excludeMedia: Bool = false
```

**功能：** 是否排除Media中已有的文件。预留能力，暂不支持。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var fileSizeOver

```cangjie
public var fileSizeOver: ?Int64 = None
```

**功能：** 文件大小匹配，大于指定大小的文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 12

### var lastModifiedAfter

```cangjie
public var lastModifiedAfter: ?Float64 = None
```

**功能：** 文件最近修改时间匹配，在指定时间点之后的文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** ?Float64

**读写能力：** 可读写

**起始版本：** 12

### var mimeType

```cangjie
public var mimeType: Array<String> = Array<String>()
```

**功能：** mime类型完全匹配，各个关键词OR关系。预留能力，暂不支持。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var suffix

```cangjie
public var suffix: Array<String> = Array<String>()
```

**功能：** 文件后缀名完全匹配，各个关键词OR关系。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### Filter(Array\<String>, Array\<String>, Array\<String>, ?Int64, ?Float64, Bool)

```cangjie
public Filter(
    public var suffix!: Array<String> = Array<String>(),
    public var displayName!: Array<String> = Array<String>(),
    public var mimeType!: Array<String> = Array<String>(),
    public var fileSizeOver!: ?Int64 = None,
    public var lastModifiedAfter!: ?Float64 = None,
    public var excludeMedia!: Bool = false
)
```

**功能：** 构造Filter对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|suffix|Array\<String>|否|Array\<String>()| **命名参数。** 文件后缀名完全匹配，各个关键词OR关系。|
|displayName|Array\<String>|否|Array\<String>()| **命名参数。** 文件名模糊匹配，各个关键词OR关系。当前仅支持通配符*。|
|mimeType|Array\<String>|否|Array\<String>()| **命名参数。** mime类型完全匹配，各个关键词OR关系。预留能力，暂不支持。|
|fileSizeOver|?Int64|否|None| **命名参数。** 文件大小匹配，大于指定大小的文件。|
|lastModifiedAfter|?Float64|否|None| **命名参数。** 文件最近修改时间匹配，在指定时间点之后的文件。|
|excludeMedia|Bool|否|false| **命名参数。** 是否排除Media中已有的文件。预留能力，暂不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。