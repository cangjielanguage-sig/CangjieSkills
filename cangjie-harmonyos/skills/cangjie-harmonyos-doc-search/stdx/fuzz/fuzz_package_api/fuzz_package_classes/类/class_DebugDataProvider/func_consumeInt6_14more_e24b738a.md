### func consumeInt64s(Int64)

```cangjie
public override func consumeInt64s(count: Int64): Array<Int64>
```

功能：将指定数量的数据转换成 Int64 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<Int64> - Int64 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeInt8()

```cangjie
public override func consumeInt8(): Int8
```

功能：将数据转换成 Int8 类型实例。

返回值：

- Int8 - Int8 类型实例。

### func consumeInt8s(Int64)

```cangjie
public override func consumeInt8s(count: Int64): Array<Int8>
```

功能：将指定数量的数据转换成 Int8 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<Int8> - Int8 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeRune()

```cangjie
public override func consumeRune(): Rune
```

功能：将数据转换成 Rune 类型实例。

返回值：

- Rune - Rune 类型实例。

### func consumeString(Int64)

```cangjie
public override func consumeString(maxLength: Int64): String
```

功能：将数据转换成 utf8 String 类型实例。

参数：

- maxLength: Int64 - String 类型的最大长度。

返回值：

- String - String 类型实例。

异常：

- IllegalArgumentException - 如果 maxLength 为负数，则抛出异常。

### func consumeUInt16()

```cangjie
public override func consumeUInt16(): UInt16
```

功能：将数据转换成 UInt16 类型实例。

返回值：

- UInt16 - UInt16 类型实例。

### func consumeUInt16s(Int64)

```cangjie
public override func consumeUInt16s(count: Int64): Array<UInt16>
```

功能：将指定数量的数据转换成 UInt16 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<UInt16> - UInt16 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeUInt32()

```cangjie
public override func consumeUInt32(): UInt32
```

功能：将数据转换成 UInt32 类型实例。

返回值：

- UInt32 - UInt32 类型实例。

### func consumeUInt32s(Int64)

```cangjie
public override func consumeUInt32s(count: Int64): Array<UInt32>
```

功能：将指定数量的数据转换成 UInt32 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<UInt32> - UInt32 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeUInt64()

```cangjie
public override func consumeUInt64(): UInt64
```

功能：将数据转换成 UInt64 类型实例。

返回值：

- UInt64 - UInt64 类型实例。

### func consumeUInt64s(Int64)

```cangjie
public override func consumeUInt64s(count: Int64): Array<UInt64>
```

功能：将指定数量的数据转换成 UInt64 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<UInt64> - UInt64 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func consumeUInt8()

```cangjie
public override func consumeUInt8(): UInt8
```

功能：将数据转换成 UInt8 类型实例。

返回值：

- UInt8 - UInt8 类型实例。

### func consumeUInt8s(Int64)

```cangjie
public override func consumeUInt8s(count: Int64): Array<UInt8>
```

功能：将指定数量的数据转换成 UInt8 类型数组。

参数：

- count: Int64 - 指定转换的数据量。

返回值：

- Array\<UInt8> - UInt8 类型数组。

异常：

- IllegalArgumentException - 如果 count 为负数，则抛出异常。

### func wrap(FuzzDataProvider)

```cangjie
public static func wrap(dp: FuzzDataProvider): DebugDataProvider
```

功能：根据 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 实例创建 [DebugDataProvider](fuzz_package_classes.md#class-debugdataprovider) 实例。

参数：

- dp: [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) - [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 类型实例。

返回值：

- [DebugDataProvider](fuzz_package_classes.md#class-debugdataprovider) - 类型实例。