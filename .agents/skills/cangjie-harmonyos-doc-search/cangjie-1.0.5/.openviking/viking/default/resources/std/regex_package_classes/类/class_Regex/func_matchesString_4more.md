### func matches(String)

```cangjie
public func matches(input: String): Bool
```

功能：判断入参 input 与正则表达式是否存在匹配。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要匹配的字符串。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果存在匹配，返回 true，否则返回 false。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    println(r.matches("2024-10-24&2025-01-01"))
}
```

运行结果：

```text
true
```

### func replace(String, String)

```cangjie
public func replace(input: String, replacement: String): String
```

功能：自当前字符串起始位置开始，匹配到的第一个子序列替换为目标字符串。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。
- replacement: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定替换字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 替换后字符串。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    println(r.replace("2024-10-24&2025-01-01", "time"))
}
```

运行结果：

```text
time&2025-01-01
```

### func replace(String, String, Int64)

```cangjie
public func replace(input: String, replacement: String, index: Int64): String
```

功能：从输入序列的 index 位置起匹配正则，将匹配到的第一个子序列替换为目标字符串。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。
- replacement: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定替换字符串。
- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 匹配开始位置。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 替换后字符串。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 index 小于 0，或 index 大于等于输入序列的 size 时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    println(r.replace("2024-10-24&2025-01-01", "time", 10))
}
```

运行结果：

```text
2024-10-24&time
```

### func replaceAll(String, String)

```cangjie
public func replaceAll(input: String, replacement: String): String
```

功能：将输入序列中所有与正则匹配的子序列替换为给定的目标字符串。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。
- replacement: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定替换字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 替换后的字符串。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    println(r.replaceAll("2024-10-24&2025-01-01", "time"))
}
```

运行结果：

```text
time&time
```