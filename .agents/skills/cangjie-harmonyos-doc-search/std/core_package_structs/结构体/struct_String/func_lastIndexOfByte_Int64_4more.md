### func lastIndexOf(Byte, Int64)

```cangjie
public func lastIndexOf(b: Byte, fromIndex: Int64): Option<Int64>
```

功能：从原字符串 fromIndex 索引开始搜索，返回指定 UTF-8 编码字节 b 最后一次出现的在原字符串内的索引。

参数：

- b: [Byte](core_package_types.md#type-byte) - 待搜索的字节。
- fromIndex: [Int64](core_package_intrinsics.md#int64) - 以指定的索引 fromIndex 开始搜索。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 如果搜索成功，返回指定字节最后一次出现的索引，否则返回 `None`。特别地，当 fromIndex 小于零，效果同 0，当 fromIndex 大于等于原字符串长度，返回 `None`。

### func lastIndexOf(String)

```cangjie
public func lastIndexOf(str: String): Option<Int64>
```

功能：返回指定字符串 str 最后一次出现的在原字符串的起始索引。

参数：

- str: [String](core_package_structs.md#struct-string) - 待搜索的字符串。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 如果原字符串中包含 str 字符串，返回其最后一次出现的索引，否则返回 `None`。

### func lastIndexOf(String, Int64)

```cangjie
public func lastIndexOf(str: String, fromIndex: Int64): Option<Int64>
```

功能：从原字符串指定索引开始搜索，获取指定字符串 str 最后一次出现的在原字符串的起始索引。

参数：

- str: [String](core_package_structs.md#struct-string) - 待搜索的字符串。
- fromIndex: [Int64](core_package_intrinsics.md#int64) - 以指定的索引 fromIndex 开始搜索。

返回值：

- [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 如果这个字符串在位置 fromIndex 及其之后没有出现，则返回 `None`。特别地，当 str 是空字符串时，如果 fromIndex 大于 0，返回 `None`，否则返回 `Some(0)`，当 fromIndex 小于零，效果同 0，当 fromIndex 大于等于原字符串长度返回 `None`。

### func lazySplit(String, Bool)

```cangjie
public func lazySplit(str: String, removeEmpty!: Bool = false): Iterator<String>
```

功能：对原字符串按照字符串 str 分隔符分割，该函数不立即对字符串进行分割，而是返回迭代器，使用迭代器进行遍历时再实际执行分隔操作。

当 str 未出现在原字符串中，返回大小为 1 的字符串迭代器，唯一的元素为原字符串。

参数：

- str: [String](core_package_structs.md#struct-string) - 字符串分隔符。
- removeEmpty!: [Bool](core_package_intrinsics.md#bool) - 移除分割结果中的空字符串，默认值为 false。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<[String](core_package_structs.md#struct-string)> - 分割后的字符串迭代器。

示例：

<!-- verify -->
```cangjie
main() {
    var str = "I like Cangjie"
    var iter = str.lazySplit(" ")
    while (true) {
        match (iter.next()) {
            case Some(i) => println(i)
            case None => break
        }
    }
}
```

运行结果：

```text
I
like
Cangjie
```