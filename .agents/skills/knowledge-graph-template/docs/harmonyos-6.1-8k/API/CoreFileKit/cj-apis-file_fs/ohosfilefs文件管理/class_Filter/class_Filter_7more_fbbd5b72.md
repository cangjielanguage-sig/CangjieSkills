## class Filter

```cangjie
public class Filter {
    public var suffix: Array<String>
    public var displayName: Array<String>
    public var mimeType: Array<String>
    public var fileSizeOver:?Int64
    public var lastModifiedAfter:?Float64
    public var excludeMedia: Bool
    public init(
        suffix!: Array<String> = Array<String>(),
        displayName!: Array<String> = Array<String>(),
        mimeType!: Array<String> = Array<String>(),
        fileSizeOver!: ?Int64 = None,
        lastModifiedAfter!: ?Float64 = None,
        excludeMedia!: Bool = false
    )
}
```

**功能：** 文件过滤配置项，支持listFile接口使用。其中mimeType与excludeMedia过滤暂不支持。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var displayName

```cangjie
public var displayName: Array<String>
```

**功能：** 文件名模糊匹配，各个关键词OR关系。当前仅支持通配符*。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var excludeMedia

```cangjie
public var excludeMedia: Bool
```

**功能：** 是否排除Media中已有的文件。true：排除Media中已有的文件；false：不排除Media中已有的文件。预留字段，暂不支持使用。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var fileSizeOver

```cangjie
public var fileSizeOver:?Int64
```

**功能：** 文件大小匹配，大于指定大小的文件。

**类型：** ?Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var lastModifiedAfter

```cangjie
public var lastModifiedAfter:?Float64
```

**功能：** 文件最近修改时间匹配，在指定时间点及之后的文件。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var mimeType

```cangjie
public var mimeType: Array<String>
```

**功能：** mime类型完全匹配，各个关键词OR关系。预留字段，暂不支持使用。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var suffix

```cangjie
public var suffix: Array<String>
```

**功能：** 文件后缀名完全匹配，各个关键词OR关系。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22