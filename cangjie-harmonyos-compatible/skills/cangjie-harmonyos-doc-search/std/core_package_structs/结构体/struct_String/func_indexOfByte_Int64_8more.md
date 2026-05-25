### func indexOf(Byte, Int64)

```cangjie
public func indexOf(b: Byte, fromIndex: Int64): Option<Int64>
```

功能：从原字符串指定索引开始搜索，获取指定字节第一次出现的在原字符串内的索引。

参数：

- b: [Byte](core_package_types.md#type-byte) - 待搜索的字节。
- fromIndex: [Int64](core_package_intrinsics.md#int64) - 以指定的索引 fromIndex 开始搜索。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 如果搜索成功，返回指定字节第一次出现的索引，否则返回 `None`。特别地，当 fromIndex 小于零，效果同 0，当 fromIndex 大于等于原字符串长度，返回 [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)>.None。

### func indexOf(String)

```cangjie
public func indexOf(str: String): Option<Int64>
```

功能：返回指定字符串 str 在原字符串中第一次出现的起始索引。

参数：

- str: [String](core_package_structs.md#struct-string) - 待搜索的字符串。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 如果原字符串包含 str 字符串，返回其第一次出现的索引，如果原字符串中没有 str 字符串，返回 None。

### func indexOf(String, Int64)

```cangjie
public func indexOf(str: String, fromIndex: Int64): Option<Int64>
```

功能：从原字符串 fromIndex 索引开始搜索，获取指定字符串 str 第一次出现的在原字符串的起始索引。

参数：

- str: [String](core_package_structs.md#struct-string) - 待搜索的字符串。
- fromIndex: [Int64](core_package_intrinsics.md#int64) - 以指定的索引 fromIndex 开始搜索。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 如果搜索成功，返回 str 第一次出现的索引，否则返回 None。特别地，当 str 是空字符串时，如果 fromIndex 大于 0，返回 None，否则返回 Some(0)。当 fromIndex 小于零，效果同 0，当 fromIndex 大于等于原字符串长度返回 None。

### func isAscii()

```cangjie
public func isAscii(): Bool
```

功能：判断字符串是否是一个 Ascii 字符串，如果字符串为空或没有 Ascii 以外的字符，则返回 true。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 是则返回 true，不是则返回 false。

### func isAsciiBlank()

```cangjie
public func isAsciiBlank(): Bool
```

功能：判断字符串是否为空或者字符串中的所有 Rune 都是 ascii 码的空白字符（包括：0x09、0x10、0x11、0x12、0x13、0x20）。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果是返回 true，否则返回 false。

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断原字符串是否为空字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果为空返回 true，否则返回 false。

### func iterator()

```cangjie
public func iterator(): Iterator<Byte>
```

功能：获取字符串的 UTF-8 编码字节迭代器，可用于支持 for-in 循环。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<[Byte](core_package_types.md#type-byte)> - 字符串的 UTF-8 编码字节迭代器。

示例：

<!-- verify -->
```cangjie
main() {
    var str = "abc"

    /* 迭代器元素为每个字符的 utf-8 编码 */
    for (i in str) {
        println(i)
    }
}
```

运行结果：

```text
97
98
99
```

### func lastIndexOf(Byte)

```cangjie
public func lastIndexOf(b: Byte): Option<Int64>
```

功能：返回指定字节 b 最后一次出现的在原字符串内的索引。

参数：

- b: [Byte](core_package_types.md#type-byte) - 待搜索的字节。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 如果原字符串中包含此字节，返回其最后一次出现的索引，否则返回 `None`。