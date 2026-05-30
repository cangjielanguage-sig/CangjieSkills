## class ZStream

```cangjie
public class ZStream {
    public let nextIn:?Array<Byte>
    public let availableIn:?UInt32
    public let totalIn:?UInt64
    public let nextOut:?Array<Byte>
    public let availableOut:?UInt32
    public let totalOut:?UInt64
    public let dataType:?Int32
    public let adler:?UInt64
    public init(nextIn!: ?Array<Byte> = None, availableIn!: ?UInt32 = None, totalIn!: ?UInt64 = None,
        nextOut!: ?Array<Byte> = None, availableOut!: ?UInt32 = None, totalOut!: ?UInt64 = None,
        dataType!: ?Int32 = None, adler!: ?UInt64 = None)
}
```

**功能：** 压缩内部流。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

### let adler

```cangjie
public let adler:?UInt64
```

**功能：** 未压缩数据的Adler-32或CRC-32值。

**类型：** ?UInt64

**读写能力：** 只读

**起始版本：** 20

### let availableIn

```cangjie
public let availableIn:?UInt32
```

**功能：** nextIn可用的字节数。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 20

### let availableOut

```cangjie
public let availableOut:?UInt32
```

**功能：** nextOut的剩余可用字节数。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 20

### let dataType

```cangjie
public let dataType:?Int32
```

**功能：** 关于数据类型的最佳猜测：deflate的二进制或文本，或inflate的解码状态。

**类型：** ?Int32

**读写能力：** 只读

**起始版本：** 20

### let nextIn

```cangjie
public let nextIn:?Array<Byte>
```

**功能：** 需要压缩的输入字节。

**类型：** ?Array\<Byte>

**读写能力：** 只读

**起始版本：** 20

### let nextOut

```cangjie
public let nextOut:?Array<Byte>
```

**功能：** 压缩后的输出字节。

**类型：** ?Array\<Byte>

**读写能力：** 只读

**起始版本：** 20

### let totalIn

```cangjie
public let totalIn:?UInt64
```

**功能：** 到目前为止读取的输入字节总数。

**类型：** ?UInt64

**读写能力：** 只读

**起始版本：** 20

### let totalOut

```cangjie
public let totalOut:?UInt64
```

**功能：** 到目前为止输出字节总数。

**类型：** ?UInt64

**读写能力：** 只读

**起始版本：** 20

### init(?Array\<Byte>, ?UInt32, ?UInt64, ?Array\<Byte>, ?UInt32, ?UInt64, ?Int32, ?UInt64)

```cangjie
public init(nextIn!: ?Array<Byte> = None, availableIn!: ?UInt32 = None, totalIn!: ?UInt64 = None,
    nextOut!: ?Array<Byte> = None, availableOut!: ?UInt32 = None, totalOut!: ?UInt64 = None,
    dataType!: ?Int32 = None, adler!: ?UInt64 = None)
```

**功能：** ZStream的构造函数。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

**参数：**

|参数名|类型|必填性|默认值|说明|
|:---|:---|:---|:---|:---|
|nextIn|?Array\<Byte>|否|None|**命名参数。** 需要压缩的输入字节。|
|availableIn|?UInt32|否|None|**命名参数。** nextIn可用的字节数。|
|totalIn|?UInt64|否|None|**命名参数。** 到目前为止读取的输入字节总数。|
|nextOut|?Array\<Byte>|否|None|**命名参数。** 压缩后的输出字节。|
|availableOut|?UInt32|否|None|**命名参数。** nextOut的剩余可用字节数。|
|totalOut|?UInt64|否|None|**命名参数。** 到目前为止输出字节总数。|
|dataType|?Int32|否|None|**命名参数。** 关于数据类型的最佳猜测：deflate的二进制或文本，或inflate的解码状态。|
|adler|?UInt64|否|None|**命名参数。** 未压缩数据的Adler-32或CRC-32值。|