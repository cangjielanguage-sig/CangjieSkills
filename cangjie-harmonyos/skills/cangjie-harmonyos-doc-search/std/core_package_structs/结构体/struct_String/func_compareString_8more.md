### func compare(String)

```cangjie
public func compare(str: String): Ordering
```

功能：按字典序比较当前字符串和参数指定的字符串。

参数：

- str: [String](core_package_structs.md#struct-string) - 被比较的字符串。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 返回 enum 值 [Ordering](core_package_enums.md#enum-ordering) 表示结果，[Ordering](core_package_enums.md#enum-ordering).GT 表示当前字符串字典序大于 str 字符串，[Ordering](core_package_enums.md#enum-ordering).LT 表示当前字符串字典序小于 str 字符串，[Ordering](core_package_enums.md#enum-ordering).EQ 表示两个字符串字典序相等。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 如果两个字符串的原始数据中存在无效的 UTF-8 编码，抛出异常。

### func contains(String)

```cangjie
public func contains(str: String): Bool
```

功能：判断原字符串中是否包含字符串 str。

参数：

- str: [String](core_package_structs.md#struct-string) - 待搜索的字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果字符串 str 在原字符串中，返回 true，否则返回 false。特别地，如果 str 字符串长度为 0，返回 true。

### func count(String)

```cangjie
public func count(str: String): Int64
```

功能：返回子字符串 str 在原字符串中出现的次数。

参数：

- str: [String](core_package_structs.md#struct-string) - 被搜索的子字符串。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 出现的次数，当 str 为空字符串时，返回原字符串中 Rune 的数量加一。

### func endsWith(String)

```cangjie
public func endsWith(suffix: String): Bool
```

功能：判断原字符串是否以 suffix 字符串为后缀结尾。

参数：

- suffix: [String](core_package_structs.md#struct-string) - 被判断的后缀字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果字符串 str 是原字符串的后缀，返回 true，否则返回 false，特别地，如果 str 字符串长度为 0，返回 true。

### func equalsIgnoreAsciiCase(String): Bool

```cangjie
public func equalsIgnoreAsciiCase(that: String): Bool
```

功能：判断当前字符串和指定字符串是否相等，忽略大小写。

参数：

- that: [String](./core_package_structs.md#struct-string) - 待比较的字符串。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果当前字符串与待比较字符串相等，返回 true，否则返回 false。

### func get(Int64)

```cangjie
public func get(index: Int64): Option<Byte>
```

功能：返回字符串下标 index 对应的 UTF-8 编码字节值。

参数：

- index: [Int64](core_package_intrinsics.md#int64) - 要获取的字节值的下标。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Byte](core_package_types.md#type-byte)> - 获取得到下标对应的 UTF-8 编码字节值，当 index 小于 0 或者大于等于字符串长度，则返回 [Option](core_package_enums.md#enum-optiont)\<[Byte](core_package_types.md#type-byte)>.None。

### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取字符串的哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 返回字符串的哈希值。

### func indexOf(Byte)

```cangjie
public func indexOf(b: Byte): Option<Int64>
```

功能：获取指定字节 b 第一次出现的在原字符串内的索引。

参数：

- b: [Byte](core_package_types.md#type-byte) - 待搜索的字节。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 如果原字符串中包含指定字节，返回其第一次出现的索引，如果原字符串中没有此字节，返回 [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)>.None。