## class Video

```cangjie
public class Video <: File {}
```

**功能：** 视频类型数据，用于描述视频文件。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

### prop imageUri

```cangjie
public mut prop videoUri: String
```

**功能：** 本地视频数据uri或网络视频uri。本地视频数据uri可通过[getUriFromPath](../../apis/CoreFileKit/cj-apis-file_fileuri.md#static-func-geturifrompathstring)函数获取。

**类型：** String

**读写能力：** 可读写。

**起始版本：** 20

**父类型：**

- [File](#class-file)

## enum Intention

```cangjie
public enum Intention {
    | DATA_HUB
    | DRAG
    | ...
}
```

**功能：** UDMF已经支持的数据通路枚举类型。其主要用途是标识各种UDMF数据通路所面向的不同业务场景。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

### DATA_HUB

```cangjie
DATA_HUB
```

**功能：** 公共数据通路。

**起始版本：** 19

### DRAG

```cangjie
DRAG
```

**功能：** 拖拽类型数据通道。

**起始版本：** 19

### func getValue ()

```cangjie
public func getValue(): String
```

**功能：** 获取enum对应的String值。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|字符串。|

## enum ShareOptions

```cangjie
public enum ShareOptions {
    | IN_APP
    | CROSS_APP
    | ...
}
```

**功能：** UDMF支持的设备内使用范围类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

### CROSS_APP

```cangjie
CROSS_APP
```

**功能：** 表示允许在本设备内跨应用使用。

**起始版本：** 19

### IN_APP

```cangjie
IN_APP
```

**功能：** 表示允许在本设备同应用内使用。

**起始版本：** 19

## enum UnifiedDataChannelValueType

```cangjie
public enum UnifiedDataChannelValueType {
    | INTEGER32(Int32)
    | INTEGER64(Int64)
    | DOUBLE(Float64)
    | BOOLEAN(Bool)
    | STRING(String)
    | ARRAYBUFFER(Array<UInt8>)
    | PIXELMAP(PixelMap)
    | NULL
    | UNDEFINED
    | ...
}
```

**功能：** 用于表示统一数据记录允许的数据字段类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

### ARRAYBUFFER(Array\<UInt8>)

```cangjie
ARRAYBUFFER(Array<UInt8>)
```

**功能：** 表示Array\<UInt8>的类型。

**起始版本：** 19

### BOOLEAN(Bool)

```cangjie
BOOLEAN(Bool)
```

**功能：** 表示Bool的类型。

**起始版本：** 19

### DOUBLE(Float64)

```cangjie
DOUBLE(Float64)
```

**功能：** 表示Float64的类型。

**起始版本：** 19

### INTEGER32(Int32)

```cangjie
INTEGER32(Int32)
```

**功能：** 表示Int32的类型。

**起始版本：** 19

### INTEGER64(Int64)

```cangjie
INTEGER64(Int64)
```

**功能：** 表示Int64的类型。

**起始版本：** 19

### NULL

```cangjie
NULL
```

**功能：** 表示null。

**起始版本：** 19

### PIXELMAP(PixelMap)

```cangjie
PIXELMAP(PixelMap)
```

**功能：** 表示PixelMap的类型。

**起始版本：** 19

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示String的类型。

**起始版本：** 19

### UNDEFINED

```cangjie
UNDEFINED
```

**功能：** 表示undefined。

**起始版本：** 19