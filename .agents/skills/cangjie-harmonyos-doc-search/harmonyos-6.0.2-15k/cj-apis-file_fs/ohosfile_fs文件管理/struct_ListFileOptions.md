## struct ListFileOptions

```cangjie
public struct ListFileOptions {
    public ListFileOptions(
        public let recursion!: Bool = false,
        public let listNum!: Int32 = 0,
        public let filter!: Filter = Filter()
    )
}
```

**功能：** 可选项类型，支持listFile接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### let filter

```cangjie
public let filter: Filter = Filter()
```

**功能：** 当数据是String类型时有效，表示数据的编码方式，默认"utf-8"。仅支持"utf-8"。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** [Filter](#struct-filter)

**读写能力：** 只读

**起始版本：** 12

### let listNum

```cangjie
public let listNum: Int32 = 0
```

**功能：** 列出文件名数量。当设置0时，列出所有文件，默认为0。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let recursion

```cangjie
public let recursion: Bool = false
```

**功能：** 是否递归子目录下文件名。默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及文件夹名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以/开头）。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### ListFileOptions(Bool, Int32, Filter)

```cangjie
public ListFileOptions(
   public let recursion!: Bool = false,
   public let listNum!: Int32 = 0,
   public let filter!: Filter = Filter()
)
```

**功能：** 构造ListFileOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|recursion|Bool|否|false| **命名参数。** 是否递归子目录下文件名。默认为false。当recursion为false时，返回当前目录下满足过滤要求的文件名及文件夹名。当recursion为true时，返回此目录下所有满足过滤要求的文件的相对路径（以/开头）。|
|listNum|Int32|否|0| **命名参数。** 列出文件名数量。当设置0时，列出所有文件，默认为0。|
|filter|[Filter](#struct-filter)|否|Filter()| **命名参数。** 当数据是String类型时有效，表示数据的编码方式，默认"utf-8"。仅支持"utf-8"。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。