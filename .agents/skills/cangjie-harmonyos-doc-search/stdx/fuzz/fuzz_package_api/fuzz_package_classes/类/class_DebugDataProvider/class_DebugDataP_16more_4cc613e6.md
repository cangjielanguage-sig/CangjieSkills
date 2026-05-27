## class DebugDataProvider

```cangjie
public class DebugDataProvider <: FuzzDataProvider
```

功能：此类继承了 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 类型，额外增加了调试信息。

父类型：

- [FuzzDataProvider](#class-fuzzdataprovider)

### func consumeAll()

```cangjie
public override func consumeAll(): Array<UInt8>
```

功能：将所有数据转换成 UInt8 类型数组。

返回值：

- Array\<UInt8> - UInt8 类型数组。

### func consumeAllAsAscii()

```cangjie
public override func consumeAllAsAscii(): String
```

功能：将所有数据转换成 Ascii String 类型。

返回值：

- String - Ascii String 类型实例。

### func consumeAllAsString()

```cangjie
public override func consumeAllAsString(): String
```

功能：将所有数据转换成 utf8 String 类型。

返回值：

- String - utf8 String 类型实例。

### func consumeAsciiString(Int64)

```cangjie
public override func consumeAsciiString(maxLength: Int64): String
```

功能：将数据转换成 Ascii  String 类型实例。

参数：

- maxLength: Int64 - String 类型的最大长度。

返回值：

- String - String 类型实例。

异常：

- IllegalArgumentException - 如果 maxLength 为负数，则抛出异常。

### func consumeBool()

```cangjie
public override func consumeBool(): Bool
```

功能：将数据转换成 Bool 类型实例。

返回值：

- Bool - Bool 类型实例。

### func consumeBools(Int64)

```cangjie
public override func consumeBools(count: Int64): Array<Bool>
```

功能：将指定数量的数据转换成 Bool 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<Bool> - Bool 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeByte()

```cangjie
public override func consumeByte(): Byte
```

功能：将数据转换成 Byte 类型实例。

返回值：

- Byte - Byte 类型实例。

### func consumeBytes(Int64)

```cangjie
public override func consumeBytes(count: Int64): Array<Byte>
```

功能：将指定数量的数据转换成 Byte 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<Byte> - Byte 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeFloat32()

```cangjie
public override func consumeFloat32(): Float32
```

功能：将数据转换成 Float32 类型实例。

返回值：

- Float32 - Float32 类型实例。

### func consumeFloat64()

```cangjie
public override func consumeFloat64(): Float64
```

功能：将数据转换成 Float64 类型实例。

返回值：

- Float64 - Float64 类型实例。

### func consumeInt16()

```cangjie
public override func consumeInt16(): Int16
```

功能：将数据转换成 Int16 类型实例。

返回值：

- Int16 - Int16 类型实例。

### func consumeInt16s(Int64)

```cangjie
public override func consumeInt16s(count: Int64): Array<Int16>
```

功能：将指定数量的数据转换成 Int16 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<Int16> - Int16 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeInt32()

```cangjie
public override func consumeInt32(): Int32
```

功能：将数据转换成 Int32 类型实例。

返回值：

- Int32 - Int32 类型实例。

### func consumeInt32s(Int64)

```cangjie
public override func consumeInt32s(count: Int64): Array<Int32>
```

功能：将指定数量的数据转换成 Int32 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<Int32> - Int32 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeInt64()

```cangjie
public override func consumeInt64(): Int64
```

功能：将数据转换成 Int64 类型实例。

返回值：

- Int64 - Int64 类型实例。