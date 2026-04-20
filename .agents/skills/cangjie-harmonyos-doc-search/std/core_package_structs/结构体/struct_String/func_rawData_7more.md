### func rawData()

```cangjie
public unsafe func rawData(): Array<Byte>
```

功能：获取字符串的 UTF-8 编码的原始字节数组。

> **注意：**
>
> 用户不应该对获取的数组进行修改，这将破坏字符串的不可变性。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<[Byte](core_package_types.md#type-byte)> - 当前字符串对应的原始字节数组。

### func removePrefix(String)

```cangjie
public func removePrefix(prefix: String): String
```

功能：去除字符串的 prefix 前缀。

参数：

- prefix: [String](core_package_structs.md#struct-string) - 待去除的前缀。

返回值：

- [String](core_package_structs.md#struct-string) - 去除前缀后得到的新字符串。

### func removeSuffix(String)

```cangjie
public func removeSuffix(suffix: String): String
```

功能：去除字符串的 suffix 后缀。

参数：

- suffix: [String](core_package_structs.md#struct-string) - 待去除的后缀。

返回值：

- [String](core_package_structs.md#struct-string) - 去除后缀后得到的新字符串。

### func replace(String, String)

```cangjie
public func replace(old: String, new: String): String
```

功能：使用新字符串替换原字符串中旧字符串。

参数：

- old: [String](core_package_structs.md#struct-string) - 旧字符串。
- new: [String](core_package_structs.md#struct-string) - 新字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 替换后的新字符串。

异常：

- [OutOfMemoryError](core_package_exceptions.md#class-outofmemoryerror) - 如果此函数分配内存时产生错误，抛出异常。

### func runes()

```cangjie
public func runes(): Iterator<Rune>
```

功能：获取字符串的 Rune 迭代器。

返回值：

- [Iterator](core_package_classes.md#class-iteratort)\<Rune> - 字符串的 Rune 迭代器。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 使用 `for-in` 或者 `next()` 方法遍历迭代器时，如果读取到非法字符，抛出异常。

### func split(String, Bool)

```cangjie
public func split(str: String, removeEmpty!: Bool = false): Array<String>
```

功能：对原字符串按照字符串 str 分隔符分割，指定是否删除空串。

当 str 未出现在原字符串中，返回长度为 1 的字符串数组，唯一的元素为原字符串。

参数：

- str: [String](core_package_structs.md#struct-string) - 字符串分隔符。
- removeEmpty!: [Bool](core_package_intrinsics.md#bool) - 移除分割结果中的空字符串，默认值为 false。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<[String](core_package_structs.md#struct-string)> - 分割后的字符串数组。

### func split(String, Int64, Bool)

```cangjie
public func split(str: String, maxSplits: Int64, removeEmpty!: Bool = false): Array<String>
```

功能：对原字符串按照字符串 str 分隔符分割，指定最多分隔子串数，以及是否删除空串。

- 当 maxSplit 为 0 时，返回空的字符串数组；
- 当 maxSplit 为 1 时，返回长度为 1 的字符串数组，唯一的元素为原字符串；
- 当 maxSplit 为负数时，返回完整分割后的字符串数组；
- 当 maxSplit 大于完整分割出来的子字符串数量时，返回完整分割的字符串数组；
- 当 str 未出现在原字符串中，返回长度为 1 的字符串数组，唯一的元素为原字符串；
- 当 str 为空时，对每个字符进行分割；当原字符串和分隔符都为空时，返回空字符串数组。

参数：

- str: [String](core_package_structs.md#struct-string) - 字符串分隔符。
- maxSplits: [Int64](core_package_intrinsics.md#int64) - 最多分割为 maxSplit 个子字符串。
- removeEmpty!: [Bool](core_package_intrinsics.md#bool) - 移除分割结果中的空字符串，默认值为 false。

返回值：

- [Array](core_package_structs.md#struct-arrayt)\<[String](core_package_structs.md#struct-string)> - 分割后的字符串数组。