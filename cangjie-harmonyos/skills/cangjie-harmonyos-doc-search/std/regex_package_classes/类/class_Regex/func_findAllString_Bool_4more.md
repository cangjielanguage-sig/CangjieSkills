### func findAll(String, Bool)

```cangjie
public func findAll(input: String, group!: Bool = false): Array<MatchData>
```

功能：对整个输入序列进行匹配，查找所有匹配到的子序列。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。
- group!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 指定是否开启捕获组的提取。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[MatchData](regex_package_structs.md#struct-matchdata)> - 存储匹配结果的数组，如果未匹配到，数组为空。

异常：

- [RegexException](regex_package_exceptions.md#class-regexexception) - 当存在匹配但提取匹配信息失败时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex("ab")
    let arr = r.findAll("ababaaab")
    let iter = arr.iterator()
    println(arr.size)
    while (true) {
        match (iter.next()) {
            case Some(i) => println(i.matchString())
            case None => break
        }
    }
}
```

运行结果：

```text
3
ab
ab
ab
```

### func getNamedGroups()

```cangjie
public func getNamedGroups(): Map<String, Int64>
```

功能：获取命名捕获组的名称与索引映射。

返回值：

- [Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v)\<[String](../../core/core_package_api/core_package_structs.md#struct-string), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 命名捕获组的名称与索引映射。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    let arr = r.findAll("2024-10-24&2025-01-01", group: true)
    for (md in arr) {
        println("found: `${md.matchString()}` and groupCount: ${md.groupCount()}")
        for ((name, index) in r.getNamedGroups()) {
            println(" ${name} => ${index}")
        }
    }
}
```

运行结果：

```text
found: `2024-10-24` and groupCount: 3
 day => 3
 month => 2
 year => 1
found: `2025-01-01` and groupCount: 3
 day => 3
 month => 2
 year => 1
```

### func lazyFindAll(String, Bool)

```cangjie
public func lazyFindAll(input: String, group!: Bool = false): Iterator<MatchData>
```

功能：对整个输入序列进行匹配，获取匹配的迭代器。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。
- group!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 指定是否开启捕获组的提取。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<[MatchData](regex_package_structs.md#struct-matchdata)> - 匹配的迭代器。

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
                println("found: `${md.matchString()}` and groupCount: ${md.groupCount()}")
                for ((name, index) in r.getNamedGroups()) {
                    println(" ${name} => ${index}")
                }
            case None => break
        }
    }
}
```

运行结果：

```text
found: `2024-10-24` and groupCount: 3
 day => 3
 month => 2
 year => 1
found: `2025-01-01` and groupCount: 3
 day => 3
 month => 2
 year => 1
```

### func matcher(String) <sup>(deprecated)</sup>

```cangjie
public func matcher(input: String): Matcher
```

功能：创建匹配器。

> **注意：**
>
> 未来版本即将废弃。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要匹配的字符串。

返回值：

- [Matcher](#class-matcher-deprecated) - 创建的匹配器。