### func findAll()

```cangjie
public func findAll(): Option<Array<MatchData>>
```

功能：对整个输入序列进行匹配，查找所有匹配到的子序列。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[MatchData](regex_package_structs.md#struct-matchdata)>> - 如果匹配到结果，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[MatchData](regex_package_structs.md#struct-matchdata)>>；如果匹配不到，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[MatchData](regex_package_structs.md#struct-matchdata)>>.None。

异常：

- [RegexException](regex_package_exceptions.md#class-regexexception) - 当存在匹配但提取匹配信息失败时，抛出异常。

### func fullMatch()

```cangjie
public func fullMatch(): Option<MatchData>
```

功能：对整个输入序列进行匹配。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)> - 如果全部匹配成功，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>.None。

异常：

- [RegexException](regex_package_exceptions.md#class-regexexception) - 当存在匹配但提取匹配信息失败时，抛出异常。

### func getString()

```cangjie
public func getString(): String
```

功能：获取匹配序列。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 匹配序列。

### func matchStart()

```cangjie
public func matchStart(): Option<MatchData>
```

功能：对输入序列的头部进行匹配。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)> - 如果匹配成功，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[MatchData](regex_package_structs.md#struct-matchdata)>.None。

异常：

- [RegexException](regex_package_exceptions.md#class-regexexception) - 当存在匹配但提取匹配信息失败时，抛出异常。

### func region()

```cangjie
public func region(): Position
```

功能：返回匹配器的区域设置。

返回值：

- [Position](regex_package_structs.md#struct-position) - 匹配器的区域设置。

### func replace(String)

```cangjie
public func replace(replacement: String): String
```

功能：自当前字符串偏移位置起，匹配到的第一个子序列替换为目标字符串，并将当前索引位置设置到匹配子序列的下一个位置。

参数：

- replacement: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 指定替换字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 替换后字符串。