### func lazySplit(String, Int64, Bool)

```cangjie
public func lazySplit(str: String, maxSplits: Int64, removeEmpty!: Bool = false): Iterator<String>
```

功能：对原字符串按照字符串 str 分隔符分割，该函数不立即对字符串进行分割，而是返回迭代器，使用迭代器进行遍历时再实际执行分隔操作。

- 当 maxSplit 为 0 时，返回空的字符串迭代器；
- 当 maxSplit 为 1 时，返回大小为 1 的字符串迭代器，唯一的元素为原字符串；
- 当 maxSplit 为负数时，直接返回分割后的字符串迭代器；
- 当 maxSplit 大于完整分割出来的子字符串数量时，返回完整分割的字符串迭代器；
- 当 str 未出现在原字符串中，返回大小为 1 的字符串迭代器，唯一的元素为原字符串；
- 当 str 为空时，对每个字符进行分割；当原字符串和分隔符都为空时，返回空字符串迭代器。

参数：

- str: [String](core_package_structs.md#struct-string) - 字符串分隔符。
- maxSplits: [Int64](core_package_intrinsics.md#int64) - 最多分割为 maxSplit 个子字符串。
- removeEmpty!: [Bool](core_package_intrinsics.md#bool) - 移除分割结果中的空字符串，默认值为 false。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<[String](core_package_structs.md#struct-string)> - 分割后的字符串迭代器。

### func lines()

```cangjie
public func lines(): Iterator<String>
```

功能：获取字符串的行迭代器，每行都由换行符进行分隔，换行符是 `\n` `\r` `\r\n` 之一，结果中每行不包括换行符。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<[String](core_package_structs.md#struct-string)> - 字符串的行迭代器。

示例：

<!-- verify -->
```cangjie
main() {
    var str = "I\rlike\nCangjie\r"
    var iter = str.lines()
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

### func padEnd(Int64, String)

```cangjie
public func padEnd(totalWidth: Int64, padding!: String = " "): String
```

功能：按指定长度左对齐原字符串，如果原字符串长度小于指定长度，在其右侧添加指定字符串。

当指定长度小于字符串长度时，返回字符串本身，不会发生截断；当指定长度大于字符串长度时，在右侧添加 padding 字符串，当 padding 长度大于 1 时，返回字符串的长度可能大于指定长度。

参数：

- totalWidth: [Int64](core_package_intrinsics.md#int64) - 指定对齐后字符串长度，取值需大于等于 0。
- padding!: [String](core_package_structs.md#struct-string) - 当长度不够时，在右侧用指定的字符串 padding 进行填充。

返回值：

- [String](core_package_structs.md#struct-string) - 填充后的字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 如果 totalWidth 小于 0，抛出异常。

### func padStart(Int64, String)

```cangjie
public func padStart(totalWidth: Int64, padding!: String = " "): String
```

功能：按指定长度右对齐原字符串，如果原字符串长度小于指定长度，在其左侧添加指定字符串。

当指定长度小于字符串长度时，返回字符串本身，不会发生截断；当指定长度大于字符串长度时，在左侧添加 padding 字符串，当 padding 长度大于 1 时，返回字符串的长度可能大于指定长度。

参数：

- totalWidth: [Int64](core_package_intrinsics.md#int64) - 指定对齐后字符串长度，取值需大于等于 0。
- padding!: [String](core_package_structs.md#struct-string) - 当长度不够时，在左侧用指定的字符串 padding 进行填充

返回值：

- [String](core_package_structs.md#struct-string) - 填充后的字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 如果 totalWidth 小于 0，抛出异常。