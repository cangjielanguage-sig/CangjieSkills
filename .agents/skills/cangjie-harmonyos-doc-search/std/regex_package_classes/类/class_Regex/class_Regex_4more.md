## class Regex

```cangjie
public class Regex {
    public init(pattern: String, flags: Array<RegexFlag>)
    public init(pattern: String, option: RegexOption)
}
```

功能：用来指定编译类型并创建正则表达式实例。

正则匹配规则详见 [regex 规则集](../regex_package_overview.md#regex-规则集)。

### init(String, Array\<RegexFlag>)

```cangjie
public init(pattern: String, flags: Array<RegexFlag>)
```

功能：创建 [Regex](regex_package_classes.md#class-regex) 实例。

参数：

- pattern: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 正则表达式。
- flags: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[RegexFlag](regex_package_enums.md#enum-regexflag)> - 正则匹配的模式列表。

异常：

- [RegexException](regex_package_exceptions.md#class-regexexception) - 当初始化失败时，抛出异常。

### init(String, RegexOption) <sup>(deprecated)</sup>

```cangjie
public init(pattern: String, option: RegexOption)
```

功能：使用指定的模式创建一个 [Regex](regex_package_classes.md#class-regex) 实例。

> **注意：**
>
> 未来版本即将废弃，使用 [init(String, Array\<RegexFlag>)](#initstring-arrayregexflag) 替代。

参数：

- pattern: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 正则表达式。
- option: [RegexOption](#class-regexoption-deprecated) - 正则匹配的模式。

异常：

- [RegexException](regex_package_exceptions.md#class-regexexception) - 当初始化失败时，抛出异常。

### func find(String, Bool)

```cangjie
public func find(input: String, group!: Bool = false): Option<MatchData>
```

功能：查找第一个匹配到的子序列。

参数：

- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待匹配序列。
- group!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 指定是否开启捕获组的提取。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)> - 匹配到结果返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>，如果匹配不到，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>.None。

异常：

- [RegexException](regex_package_exceptions.md#class-regexexception) - 当存在匹配但提取匹配信息失败时，抛出异常。

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    let r1 = Regex("ab")
    let r2 = Regex("ab", IgnoreCase)
    match (r1.find("aB")) {
        case Some(r) => println(r.matchString())
        case None => println("None")
    }
    match (r2.find("aB")) {
        case Some(r) => println(r.matchString())
        case None => println("None")
    }
}
```

运行结果：

```text
None
aB
```