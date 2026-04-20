### func replaceAll(String, String, Int64)

```cangjie
public func replaceAll(input: String, replacement: String, limit: Int64): String
```

功能：将输入序列中与正则匹配的前 limit 个子序列替换为给定的替换字符串。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。
- replacement: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定替换字符串。
- limit: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 替换次数。如果 limit 等于 0，返回原来的序列；如果 limit 为负数，将尽可能多次的替换。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 替换后字符串。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    println(r.replaceAll("2019-4-5&2024-10-24&2025-01-01", "time", 10))
}
```

运行结果：

```text
2019-4-5&time&time
```

### func split(String)

```cangjie
public func split(input: String): Array<String>
```

功能：将给定的输入序列根据正则尽可能的分割成多个子序列。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 子序列数组。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex("&")
    for (subStr in r.split("2019-4-5&2024-10-24&2025-01-01")) {
        println(subStr)
    }
}
```

运行结果：

```text
2019-4-5
2024-10-24
2025-01-01
```

### func split(String, Int64)

```cangjie
public func split(input: String, limit: Int64): Array<String>
```

功能：将给定的输入序列根据正则尽可能的分割成多个子序列 （最多分割成 limit 个子串）。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。
- limit: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 最多分割的子串个数。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 如果 limit>0，返回最多 limit 个子串；如果 limit<=0，返回最大可分割数个子串。

### func string()

```cangjie
public func string(): String
```

功能：获取正则的输入序列。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 输入序列。