### func replace(String, Int64)

```cangjie
public func replace(replacement: String, index: Int64): String
```

功能：从输入序列的 index 位置起匹配正则，将匹配到的第一个子序列替换为目标字符串。

参数：

- replacement: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定替换字符串。
- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 匹配开始位置。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 替换后字符串。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 index 小于 0，或 index 大于等于输入序列的 size 时，抛出异常。

### func replaceAll(String)

```cangjie
public func replaceAll(replacement: String): String
```

功能：将输入序列中所有与正则匹配的子序列替换为给定的目标字符串。

参数：

- replacement: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定替换字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 替换后的字符串。

### func replaceAll(String, Int64)

```cangjie
public func replaceAll(replacement: String, limit: Int64): String
```

功能：将输入序列中与正则匹配的前 limit 个子序列替换为给定的替换字符串。

参数：

- replacement: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定替换字符串。
- limit: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 替换次数。如果 limit 等于 0，返回原来的序列；如果 limit 为负数，将尽可能多次的替换。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 替换后字符串。

### func resetRegion()

```cangjie
public func resetRegion(): Matcher
```

功能：重置匹配器开始位置和结束位置。

返回值：

- [Matcher](#class-matcher-deprecated) - 匹配器自身。

### func resetString(String)

```cangjie
public func resetString(input: String): Matcher
```

功能：重设匹配序列，并重置匹配器。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 新的匹配序列。

返回值：

- [Matcher](#class-matcher-deprecated) - 匹配器自身。

### func setRegion(Int64, Int64)

```cangjie
public func setRegion(beginIndex: Int64, endIndex: Int64): Matcher
```

功能：设置匹配器可搜索区域的位置信息，具体位置由指定的 begin 和 end 决定。

参数：

- beginIndex: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 区域开始位置。
- endIndex: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 区域结束位置。

返回值：

- [Matcher](#class-matcher-deprecated) - 匹配器自身。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 beginIndex 小于 0，或 beginIndex 大于输入序列的 size 时，抛出异常；当 endIndex 小于 0，或 endIndex 大于输入序列的 size 时，抛出异常；当 beginIndex 大于 endIndex 时，抛出异常。

### func split()

```cangjie
public func split(): Array<String>
```

功能：将给定的输入序列根据正则尽可能的分割成多个子序列。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 子序列数组。