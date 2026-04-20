## struct WriteOptions

```cangjie
public struct WriteOptions {
    public WriteOptions(
    public var length!: Option<UIntNative> = None,
    public var offset!: Option<Int64> = None,
    public var encoding!: String = "utf-8")
}
```

**功能：** 可选项类型，支持write接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### var encoding

```cangjie
public var encoding: String = "utf-8"
```

**功能：** 当数据是String类型时有效，表示数据的编码方式，默认"utf-8"。仅支持"utf-8"。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var length

```cangjie
public var length: Option<UIntNative> = None
```

**功能：** 期望写入数据的长度。默认缓冲区长度。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Option\<UIntNative>

**读写能力：** 可读写

**起始版本：** 12

### var offset

```cangjie
public var offset: Option<Int64> = None
```

**功能：** 期望写入文件位置（基于当前filePointer加上offset的位置）。默认从偏置指针（filePointer）开始写。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Option\<Int64>

**读写能力：** 可读写

**起始版本：** 12

### WriteOptions(Option\<UIntNative>, Option\<Int64>, String)

```cangjie
public WriteOptions(
    public var length!: Option<UIntNative> = None,
    public var offset!: Option<Int64> = None,
    public var encoding!: String = "utf-8"
)
```

**功能：** 构造WriteOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|length|Option\<UIntNative>|否|None| **命名参数。** 期望写入数据的长度。默认缓冲区长度。|
|offset|Option\<Int64>|否|None| **命名参数。** 期望写入文件位置（基于当前filePointer加上offset的位置）。默认从偏置指针（filePointer）开始写。|
|encoding|String|否|"utf-8"| **命名参数。** 当数据是String类型时有效，表示数据的编码方式，默认"utf-8"。仅支持"utf-8"。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。