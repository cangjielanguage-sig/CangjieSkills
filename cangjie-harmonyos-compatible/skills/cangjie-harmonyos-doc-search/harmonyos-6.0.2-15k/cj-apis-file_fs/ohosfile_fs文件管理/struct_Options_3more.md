## struct Options

```cangjie
public struct Options {
    public Options(public var encoding!: String = "utf-8")
}
```

**功能：** 可选项类型，支持readLines接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### var encoding

```cangjie
public var encoding: String = "utf-8"
```

**功能：** 文件编码方式。可选项。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### Options(String)

```cangjie
public Options(public var encoding!: String = "utf-8")
```

**功能：** 构造Options对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|encoding|String|否|"utf-8"| **命名参数。** 用于指定字符串的编码方式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。

## struct Progress

```cangjie
public struct Progress {
    public let processedSize: UInt64
    public let totalSize: UInt64
}
```

**功能：** 拷贝进度回调数据。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 19

### let processedSize

```cangjie
public let processedSize: UInt64
```

**功能：** 已拷贝的数据大小。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let totalSize

```cangjie
public let totalSize: UInt64
```

**功能：** 待拷贝的数据总大小。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

## struct ReadOptions

```cangjie
public struct ReadOptions {
    public ReadOptions(
        public var length!: Option<UIntNative> = None,
        public var offset!: Option<Int64> = None
    )
}
```

**功能：** 可选项类型，支持read接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### var length

```cangjie
public var length: Option<UIntNative> = None
```

**功能：** 期望读取数据的长度。默认缓冲区长度。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Option\<UIntNative>

**读写能力：** 可读写

**起始版本：** 12

### var offset

```cangjie
public var offset: Option<Int64> = None
```

**功能：** 期望读取文件位置（基于当前filePointer加上offset的位置）。默认从偏置指针（filePointer）开始读。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Option\<Int64>

**读写能力：** 可读写

**起始版本：** 12

### ReadOptions(Option\<UIntNative>, Option\<Int64>)

```cangjie
public ReadOptions(
    public var length!: Option<UIntNative> = None,
    public var offset!: Option<Int64> = None
)
```

**功能：** 构造ReadOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|length|Option\<UIntNative>|否|None| **命名参数。** 期望读取数据的长度。默认缓冲区长度。|
|offset|Option\<Int64>|否|None| **命名参数。** 期望读取文件位置（基于当前filePointer加上offset的位置）。默认从偏置指针（filePointer）开始读。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。