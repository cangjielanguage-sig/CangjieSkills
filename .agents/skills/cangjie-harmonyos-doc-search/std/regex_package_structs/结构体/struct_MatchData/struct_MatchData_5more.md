## struct MatchData

```cangjie
public struct MatchData {}
```

功能：存储正则表达式匹配结果，并提供对正则匹配结果进行查询的函数。

### func groupCount()

```cangjie
public func groupCount(): Int64
```

功能：获取捕获组的个数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 捕获组的个数。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    let iter = r.lazyFindAll("2024-10-24&2025-01-01", group: true)
    while (true) {
        match (iter.next()) {
            case Some(md) => println("found: `${md.matchString()}` and groupCount: ${md.groupCount()}")
            case None => break
        }
    }
}
```

运行结果：

```text
found: `2024-10-24` and groupCount: 3
found: `2025-01-01` and groupCount: 3
```

### func groupNumber() <sup>(deprecated)</sup>

```cangjie
public func groupNumber(): Int64
```

功能：获取捕获组的个数。

> **注意：**
>
> 未来版本即将废弃，使用 [groupCount()](#func-groupcount) 替代。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 捕获组的个数。

### func matchPosition()

```cangjie
public func matchPosition(): Position
```

功能：获取上一次匹配到的子字符串在输入字符串中起始位置和末尾位置的索引。

返回值：

- [Position](#struct-position) - 匹配结果位置信息。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    let iter = r.lazyFindAll("2024-10-24&2025-01-01", group: true)
    while (true) {
        match (iter.next()) {
            case Some(md) =>
                println("found: ${md.matchString()} and groupCount: ${md.groupCount()}")
                let pos = md.matchPosition(0)
                println(" pos: [${pos.start}, ${pos.end}]")
            case None => break
        }
    }
}
```

运行结果：

```text
found: 2024-10-24 and groupCount: 3
 pos: [0, 10]
found: 2025-01-01 and groupCount: 3
 pos: [11, 21]
```

### func matchPosition(Int64)

```cangjie
public func matchPosition(group: Int64): Position
```

功能：根据给定的索引获取上一次匹配中该捕获组匹配到的子字符串在输入字符串中的位置信息。

参数：

- group: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 指定组。

返回值：

- [Position](#struct-position) - 对应捕获组的位置信息。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当未开启捕获组提取，或 group 小于 0 或者大于 groupCount 时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    let iter = r.lazyFindAll("2024-10-24&2025-01-01", group: true)
    while (true) {
        match (iter.next()) {
            case Some(md) =>
                println("found: ${md.matchString()} and groupCount: ${md.groupCount()}")
                /* 月份的捕获组索引为 2 */
                let pos = md.matchPosition(2)
                println(" month: [${pos.start}, ${pos.end}]")
            case None => break
        }
    }
}
```

运行结果：

```text
found: 2024-10-24 and groupCount: 3
 month: [5, 7]
found: 2025-01-01 and groupCount: 3
 month: [16, 18]
```