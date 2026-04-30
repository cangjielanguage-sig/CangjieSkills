## enum ValueType

```cangjie
public enum ValueType {
    | NULL(Option<Int32>)
    | STRING(String)
    | INT32(Int32)
    | INT64(Int64)
    | FLOAT64(Float64)
    | BOOL(Bool)
    | FD(Int32)
    | ARRSTRING(Array<String>)
    | ARRAYI32(Array<Int32>)
    | ARRAYI64(Array<Int64>)
    | ARRAYBOOL(Array<Bool>)
    | ARRAYF64(Array<Float64>)
    | ARRAYFD(Array<Int32>)
    | LOOP_MODE(LoopMode)
    | PIXEL_MAP(PixelMap)
    | HASH_MAP(HashMap<String, ValueType>)
    | ...
}
```

**功能：** 包含公共事件附加信息的类型取值。

**起始版本：** 19

### ARRAYBOOL(Array\<Bool>)

```cangjie
ARRAYBOOL(Array<Bool>)
```

**功能：** 表示Bool数组类型数据。

**起始版本：** 19

### ARRAYF64(Array\<Float64>)

```cangjie
ARRAYF64(Array<Float64>)
```

**功能：** 表示Float64数组类型数据。

**起始版本：** 19

### ARRAYFD(Array\<Int32>)

```cangjie
ARRAYFD(Array<Int32>)
```

**功能：** 表示文件描述符数组类型数据。

**起始版本：** 19

### ARRAYI32(Array\<Int32>)

```cangjie
ARRAYI32(Array<Int32>)
```

**功能：** 表示Int32数组类型数据。

**起始版本：** 19

### ARRAYI64(Array\<Int64>)

```cangjie
ARRAYI64(Array<Int64>)
```

**功能：** 表示Int64数组类型数据。

**起始版本：** 19

### ARRSTRING(Array\<String>)

```cangjie
ARRSTRING(Array<String>)
```

**功能：** 表示String数组类型数据。

**起始版本：** 19

### BOOL(Bool)

```cangjie
BOOL(Bool)
```

**功能：** 表示Bool类型数据。

**起始版本：** 19

### FD(Int32)

```cangjie
FD(Int32)
```

**功能：** 表示文件描述符类型数据。

**起始版本：** 19

### FLOAT64(Float64)

```cangjie
FLOAT64(Float64)
```

**功能：** 表示Float64类型数据。

**起始版本：** 19

### HASH_MAP(HashMap\<String, ValueType>)

```cangjie
HASH_MAP(HashMap<String, ValueType>)
```

**功能：** 表示HashMap类型数据。

**起始版本：** 20

### INT32(Int32)

```cangjie
INT32(Int32)
```

**功能：** 表示Int32类型数据。

**起始版本：** 19

### INT64(Int64)

```cangjie
INT64(Int64)
```

**功能：** 表示Int64类型数据。

**起始版本：** 19

### LOOP_MODE(LoopMode)

```cangjie
LOOP_MODE(LoopMode)
```

**功能：** 表示[LoopMode](#enum-loopmode)类型数据。

**起始版本：** 19

### NULL(Option\<Int32>)

```cangjie
NULL(Option<Int32>)
```

**功能：** 表示Null类型数据。

**起始版本：** 19

### PIXEL_MAP(PixelMap)

```cangjie
PIXEL_MAP(PixelMap)
```

**功能：** 表示[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)类型数据。

**起始版本：** 19

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示String类型数据。

**起始版本：** 19