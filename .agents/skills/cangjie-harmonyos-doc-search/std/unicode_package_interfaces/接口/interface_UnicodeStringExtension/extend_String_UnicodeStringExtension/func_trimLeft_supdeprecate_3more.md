#### func trimLeft() <sup>(deprecated)</sup>

```cangjie
public func trimLeft(): String
```

功能：去除字符串开头的空字符，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

> **注意：**
>
> 未来版本即将废弃，使用 [trimStart](./unicode_package_interfaces.md#func-trimend) 替代。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除开头空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。

示例：

```cangjie
import std.unicode.*

main(): Unit {
    let str = "  x  "
    println("\"${str.trimLeft()}\"")
}
```

运行结果：

```text
"x  "
```

#### func trimRight() <sup>(deprecated)</sup>

```cangjie
public func trimRight(): String
```

功能：去除字符串结尾的空字符，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

> **注意：**
>
> 未来版本即将废弃，使用 [trimEnd](./unicode_package_interfaces.md#func-trimend) 替代。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除结尾空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。

示例：

```cangjie
import std.unicode.*

main(): Unit {
    let str = "  x  "
    println("\"${str.trimRight()}\"")
}
```

运行结果：

```text
"  x"
```

#### func trimStart()

```cangjie
public func trimStart(): String
```

功能：去除字符串开头的空字符，空字符定义见 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型的扩展函数 [isWhiteSpace](#func-iswhitespace)。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 去除开头空字符后的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果字符串中不存在有效的 UTF-8 编码，抛出异常。

示例：
<!-- verify -->
```cangjie
import std.unicode.*

main(): Unit {
    let str = "  x  "
    println("\"${str.trimStart()}\"")
}
```

运行结果：

```text
"x  "
```