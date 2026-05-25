## class Matcher <sup>(deprecated)</sup>

```cangjie
public class Matcher {
    public init(regex: Regex, input: String)
}
```

功能：正则匹配器，用于扫描输入序列并进行匹配。

> **注意：**
>
> 未来版本即将废弃，使用 [Regex](#class-regex) 替代。

### init(Regex, String)

```cangjie
public init(regex: Regex, input: String)
```

功能：使用传入的正则表达式和输入序列创建 [Matcher](#class-matcher-deprecated) 实例。

参数：

- regex: [Regex](regex_package_classes.md#class-regex) - 正则表达式。
- input: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 输入序列。

### func allCount()

```cangjie
public func allCount(): Int64
```

功能：获取正则表示式的匹配结果总数。

默认是从头到尾匹配的结果，使用了 setRegion 后只会在设置的范围内查找。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 匹配结果总数。

### func find()

```cangjie
public func find(): Option<MatchData>
```

功能：自当前字符串偏移位置起，查找第一个匹配到的子序列。

find 调用一次，当前偏移位置为最新一次匹配到的子序列后第一个字符位置，下次调用时，find 从当前位置开始匹配。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)> - 匹配到结果返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>，如果匹配不到，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>.None。

异常：

- [RegexException](regex_package_exceptions.md#class-regexexception) - 当存在匹配但提取匹配信息失败时，抛出异常。

### func find(Int64)

```cangjie
public func find(index: Int64): Option<MatchData>
```

功能：重置该匹配器索引位置，从 index 对应的位置处开始对输入序列进行匹配，返回匹配到的子序列。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)> - 匹配到结果返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>，如果匹配不到，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>.None。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 index 小于 0，或 index 大于等于输入序列的 size 时，抛出异常。
- [RegexException](regex_package_exceptions.md#class-regexexception) - 当存在匹配但提取匹配信息失败时，抛出异常。