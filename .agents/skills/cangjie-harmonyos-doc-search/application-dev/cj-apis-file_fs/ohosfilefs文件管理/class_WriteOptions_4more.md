## class WriteOptions

```cangjie
public class WriteOptions <: Options {
    public var length: Option<UIntNative>
    public var offset: Option<Int64>
    public init(
        length!: Option<UIntNative> = None,
        offset!: Option<Int64> = None,
        encoding!: String = "utf-8"
    )
}
```

**功能：** 可选项类型，支持write接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**父类型：**

- [Options](#class-options)

### var length

```cangjie
public var length: Option<UIntNative>
```

**功能：** 期望写入数据的长度，单位为字节。

**类型：** Option\<UIntNative>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var offset

```cangjie
public var offset: Option<Int64>
```

**功能：** 期望写入文件位置，单位为字节（基于当前filePointer加上offset的位置）。

**类型：** Option\<Int64>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### init(Option\<UIntNative>, Option\<Int64>, String)

```cangjie
public init(
    length!: Option<UIntNative> = None,
    offset!: Option<Int64> = None,
    encoding!: String = "utf-8"
)
```

**功能：** 构造WriteOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|length|Option\<UIntNative>|否|None|**命名参数。** 期望写入数据的长度，单位为字节。可选，默认缓冲区长度。|
|offset|Option\<Int64>|否|None|**命名参数。** 期望写入文件位置，单位为字节（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始写。|
|encoding|String|否|"utf-8"|**命名参数。** 当数据是String类型时有效，表示数据的编码方式，默认"utf-8"，仅支持"utf-8"。|

## enum AccessFlagType

```cangjie
public enum AccessFlagType {
    | Local
    | ...
}
```

**功能：** 枚举，表示需要校验的文件位置。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### Local

```cangjie
Local
```

**功能：** 文件是否在本地。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

## enum AccessModeType

```cangjie
public enum AccessModeType {
    | Exist
    | Write
    | Read
    | ReadWrite
    | ...
}
```

**功能：** 枚举，表示需要校验的具体权限。若不填，默认校验文件是否存在。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### Exist

```cangjie
Exist
```

**功能：** 文件是否存在。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### Read

```cangjie
Read
```

**功能：** 文件是否具有读取权限。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### ReadWrite

```cangjie
ReadWrite
```

**功能：** 文件是否具有读写权限。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### Write

```cangjie
Write
```

**功能：** 文件是否具有写入权限。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

## enum WhenceType

```cangjie
public enum WhenceType {
    | SeekSet
    | SeekCur
    | SeekEnd
    | ...
}
```

**功能：** 枚举，文件偏移指针相对偏移位置类型，支持lseek接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### SeekCur

```cangjie
SeekCur
```

**功能：** 当前文件偏移指针位置处。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### SeekEnd

```cangjie
SeekEnd
```

**功能：** 文件末尾位置处。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### SeekSet

```cangjie
SeekSet
```

**功能：** 文件起始位置处。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22