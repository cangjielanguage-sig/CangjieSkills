## class ReadOptions

```cangjie
public open class ReadOptions {
    public var offset: Option<Int64>
    public var length: Option<UIntNative>
    public init(
        offset!: Option<Int64> = None,
        length!: Option<UIntNative> = None
    )
}
```

**功能：** 可选项类型，支持read接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var length

```cangjie
public var length: Option<UIntNative>
```

**功能：** 期望读取数据的长度，单位为字节。

**类型：** Option\<UIntNative>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var offset

```cangjie
public var offset: Option<Int64>
```

**功能：** 期望读取文件位置，单位为字节（基于当前filePointer加上offset的位置）。

**类型：** Option\<Int64>

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### init(Option\<Int64>, Option\<UIntNative>)

```cangjie
public init(
    offset!: Option<Int64> = None,
    length!: Option<UIntNative> = None
)
```

**功能：** 构造ReadOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Option\<Int64>|否|None|**命名参数。** 期望读取文件位置，单位为字节（基于当前filePointer加上offset的位置）。可选，默认从偏移指针（filePointer）开始读。|
|length|Option\<UIntNative>|否|None|**命名参数。** 期望读取数据的长度，单位为字节。可选，默认缓冲区长度。|

## class ReadTextOptions

```cangjie
public class ReadTextOptions <: ReadOptions {
    public var encoding: String
    public init(
        offset!: Option<Int64> = None,
        length!: Option<UIntNative> = None,
        encoding!: String = "utf-8"
    )
}
```

**功能：** 可选项类型，支持readText接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**父类型：**

- [ReadOptions](#class-readoptions)

### var encoding

```cangjie
public var encoding: String
```

**功能：** 当数据是 String 类型时有效，表示数据的编码方式，仅支持 'utf-8'。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### init(Option\<Int64>, Option\<UIntNative>, String)

```cangjie
public init(
    offset!: Option<Int64> = None,
    length!: Option<UIntNative> = None,
    encoding!: String = "utf-8"
)
```

**功能：** 构造ReadOptions对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Option\<Int64>|否|None|**命名参数。** 期望读取文件的位置，单位为字节。可选，默认从当前位置开始读取。|
|length|Option\<UIntNative>|否|None|**命名参数。** 期望读取数据的长度，单位为字节。可选，默认文件长度。|
|encoding|String|否|"utf-8"|**命名参数。** 当数据是 String 类型时有效，表示数据的编码方式，默认 'utf-8'，仅支持 'utf-8'。|