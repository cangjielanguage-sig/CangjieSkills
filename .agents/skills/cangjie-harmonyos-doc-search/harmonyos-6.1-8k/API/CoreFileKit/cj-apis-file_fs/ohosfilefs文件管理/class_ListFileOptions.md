## class ListFileOptions

```cangjie
public class ListFileOptions {
    public var recursion: Bool
    public var listNum: Int32
    public var filter: Filter
    public init(
        recursion!: Bool = false,
        listNum!: Int32 = 0,
        filter!: Filter = Filter()
    )
}
```

**功能：** 可选项类型，支持listFile接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var filter

```cangjie
public var filter: Filter
```

**功能：** 文件过滤配置项。

**类型：** [Filter](#class-filter)

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var listNum

```cangjie
public var listNum: Int32
```

**功能：** 列出文件名数量。当设置0时，列出所有文件。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var recursion

```cangjie
public var recursion: Bool
```

**功能：** 是否递归子目录下文件名。当recursion为false时，返回当前目录下满足过滤要求的文件名及目录名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以/开头）。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### init(Bool, Int32, Filter)

```cangjie
public init(
    recursion!: Bool = false,
    listNum!: Int32 = 0,
    filter!: Filter = Filter()
)
```

**功能：** 构造ListFileOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|recursion|Bool|否|false|**命名参数。** 是否递归子目录下文件名。可选，默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及目录名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以/开头）。|
|listNum|Int32|否|0|**命名参数。** 列出文件名数量。可选，当设置0时，列出所有文件，默认为0。|
|filter|[Filter](#class-filter)|否|Filter()|**命名参数。** 文件过滤配置项。 可选，设置过滤条件。|