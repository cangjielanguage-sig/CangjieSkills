## class DocumentSelectOptions

```cangjie
public class DocumentSelectOptions {
    public DocumentSelectOptions(
        public var maxSelectNumber!: Int64 = 1,
        public var defaultFilePathUri!: ?String = None,
        public var fileSuffixFilters!: Array<String> = Array<String>(),
        public var selectMode!: DocumentSelectMode = FILE,
        public var authMode!: Bool = false
    )
}
```

**功能：** 文档选择选项。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### var authMode

```cangjie
public var authMode: Bool = false
```

**功能：** 拉起授权picker，默认为false（非授权模式）。当authMode为true时为授权模式，defaultFilePathUri必填，表明待授权uri。仅支持2in1设备。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var defaultFilePathUri

```cangjie
public var defaultFilePathUri: ?String = None
```

**功能：** 指定选择的文件或者目录路径。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var fileSuffixFilters

```cangjie
public var fileSuffixFilters: Array<String> = Array<String>()
```

**功能：** 选择文件的后缀类型，若选择项存在多个后缀名，则每一个后缀名之间用英文逗号进行分隔。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var maxSelectNumber

```cangjie
public var maxSelectNumber: Int64 = 1
```

**功能：** 选择文件最大个数，默认值和上限都是500，有效值范围1-500（输入有效值之外的数采用默认值。选择目录仅支持特定设备）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

### var selectMode

```cangjie
public var selectMode: DocumentSelectMode = FILE
```

**功能：** 支持选择的资源类型，比如：文件、文件夹和二者混合，仅支持特定设备。

**类型：** [DocumentSelectMode](#enum-documentselectmode)

**读写能力：** 可读写

**起始版本：** 12

### DocumentSelectOptions(Int64, ?String, Array\<String>, DocumentSelectMode, Bool)

```cangjie
public DocumentSelectOptions(
    public var maxSelectNumber!: Int64 = 1,
    public var defaultFilePathUri!: ?String = None,
    public var fileSuffixFilters!: Array<String> = Array<String>(),
    public var selectMode!: DocumentSelectMode = FILE,
    public var authMode!: Bool = false
)
```

**功能：** 创建DocumentSelectOptions对象。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|maxSelectNumber|Int64|否|1| **命名参数。** 选择文件最大个数，默认值和上限都是500，有效值范围1-500（输入有效值之外的数采用默认值。选择目录仅支持特定设备）。|
|defaultFilePathUri|?String|否|None| **命名参数。** 指定选择的文件或者目录路径。|
|fileSuffixFilters|Array\<String>|否|Array\<String>()| **命名参数。** 选择文件的后缀类型，若选择项存在多个后缀名，则每一个后缀名之间用英文逗号进行分隔。|
|selectMode|[DocumentSelectMode](#enum-documentselectmode)|否|FILE| **命名参数。** 支持选择的资源类型，比如：文件、文件夹和二者混合，仅支持特定设备。|
|authMode|Bool|否|false| **命名参数。** 拉起授权picker，默认为false（非授权模式）。当authMode为true时为授权模式，defaultFilePathUri必填，表明待授权uri。仅支持2in1设备。|