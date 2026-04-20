## struct String

```cangjie
public struct String <: Collection<Byte> & Comparable<String> & Hashable & ToString {
    public static const empty: String = String()
    public const init()
    public init(value: Array<Rune>)
    public init(value: Collection<Rune>)
}
```

功能：该结构体表示仓颉字符串，提供了构造、查找、拼接等一系列字符串操作。

> **注意：**
>
> - `String` 类型仅支持 UTF-8 编码。
> - 出于 `String` 对象内存开销方面的优化，`String` 的长度被限制在 `4GB`大小，即 `String`的最大长度不超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32)。

父类型：

- [Collection](core_package_interfaces.md#interface-collectiont)\<Byte>
- [Comparable](core_package_interfaces.md#interface-comparablet)\<[String](#struct-string)>
- [Hashable](core_package_interfaces.md#interface-hashable)
- [ToString](core_package_interfaces.md#interface-tostring)

### static const empty

```cangjie
public static const empty: String = String()
```

功能：创建一个空的字符串并返回。

类型：[String](core_package_structs.md#struct-string)

### prop size

```cangjie
public prop size: Int64
```

功能：获取字符串 UTF-8 编码后的字节长度。

类型：[Int64](core_package_intrinsics.md#int64)

### init()

```cangjie
public const init()
```

功能：构造一个空的字符串。

### init(Array\<Rune>)

```cangjie
public init(value: Array<Rune>)
```

功能：根据字符数组构造一个字符串，字符串内容为数组中的所有字符。

参数：

- value: [Array](core_package_structs.md#struct-arrayt)\<Rune> - 根据该字符数组构造字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当试图构造长度超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32) 的字符串时，抛出异常。

### init(Collection\<Rune>)

```cangjie
public init(value: Collection<Rune>)
```

功能：据字符集合构造一个字符串，字符串内容为集合中的所有字符。

参数：

- value: [Collection](core_package_interfaces.md#interface-collectiont)\<Rune> - 根据该字符集合构造字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当试图构造长度超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32) 的字符串时，抛出异常。

### static func checkUtf8Encoding(Array\<UInt8>)

```cangjie
public static func checkUtf8Encoding(data: Array<UInt8>): Bool
```

功能：检查一个 Byte 数组是否符合 UTF-8 编码。

参数：

- data: [Array](core_package_structs.md#struct-arrayt)\<[UInt8](core_package_intrinsics.md#uint8)> - 根据该字节数组构造字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果 Byte 数组符合 UTF-8 编码，返回 true，否则返回 false。

### static func fromUtf8(Array\<UInt8>)

```cangjie
public static func fromUtf8(utf8Data: Array<UInt8>): String
```

功能：根据 UTF-8 编码的字节数组构造一个字符串。

参数：

- utf8Data: [Array](core_package_structs.md#struct-arrayt)\<[UInt8](core_package_intrinsics.md#uint8)> - 根据该字节数组构造字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 构造的字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 入参不符合 utf-8 序列规则，或者试图构造长度超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32) 的字符串时，抛出异常。