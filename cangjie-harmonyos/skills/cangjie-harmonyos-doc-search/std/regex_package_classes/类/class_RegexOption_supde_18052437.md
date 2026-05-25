## class RegexOption <sup>(deprecated)</sup>

```cangjie
public class RegexOption <: ToString {
    public init()
}
```

功能：用于指定正则匹配的模式。

> **注意：**
>
> 未来版本即将废弃，使用 [RegexFlag](regex_package_enums.md#enum-regexflag) 替代。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### init()

```cangjie
public init()
```

功能：创建一个 [RegexOption](#class-regexoption-deprecated) 实例， 匹配模式为普通模式（NORMAL）。

### func ignoreCase()

```cangjie
public func ignoreCase(): RegexOption
```

功能：修改 [RegexOption](#class-regexoption-deprecated)，修改匹配模式为忽略大小写（IGNORECASE）。

返回值：

- [RegexOption](#class-regexoption-deprecated) - 修改后的 [RegexOption](#class-regexoption-deprecated)。

### func multiLine()

```cangjie
public func multiLine(): RegexOption
```

功能：修改 [RegexOption](#class-regexoption-deprecated)，修改匹配模式为多行文本模式（MULTILINE）。

返回值：

- [RegexOption](#class-regexoption-deprecated) - 修改后的 [RegexOption](#class-regexoption-deprecated)。

### func toString()

```cangjie
public func toString(): String
```

功能：获取 [RegexOption](#class-regexoption-deprecated) 当前表示的正则匹配模式。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 正则匹配模式。