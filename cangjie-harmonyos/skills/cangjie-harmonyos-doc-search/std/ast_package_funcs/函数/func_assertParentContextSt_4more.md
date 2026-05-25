## func assertParentContext(String)

```cangjie
public func assertParentContext(parentMacroName: String): Unit
```

功能：检查当前宏调用是否在特定的宏调用内。若检查不符合预期，编译器出现一个错误提示。

> **注意：**
>
> 该函数只能作为函数被直接调用，不能作为赋值给变量，不能作为实参或返回值使用。

参数：

- parentMacroName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待检查的外层宏调用的名字。

## func cangjieLex(String)

```cangjie
public func cangjieLex(code: String): Tokens
```

功能：将字符串转换为 [Tokens](ast_package_classes.md#class-tokens) 对象。

参数：

- code: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待词法解析的字符串。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 词法解析得到的 [Tokens](ast_package_classes.md#class-tokens)。

异常：

- [IllegalMemoryException](../../core/core_package_api/core_package_exceptions.md#class-illegalmemoryexception) - 当申请内存失败时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当输入的 code 无法被正确的解析为 [Tokens](ast_package_classes.md#class-tokens) 时，抛出异常。

## func cangjieLex(String, Bool)

```cangjie
public func cangjieLex(code: String, truncated: Bool): Tokens
```

功能：将字符串转换为 [Tokens](ast_package_classes.md#class-tokens) 对象。

参数：

- code: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待词法解析的字符串。
- truncated: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否删减解析后 [Tokens](ast_package_classes.md#class-tokens) 中的 Token([END](ast_package_enums.md#end))。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 词法解析得到的 [Tokens](ast_package_classes.md#class-tokens)。

异常：

- [IllegalMemoryException](../../core/core_package_api/core_package_exceptions.md#class-illegalmemoryexception) - 当申请内存失败时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当输入的 code 无法被正确的解析为 [Tokens](ast_package_classes.md#class-tokens) 时，抛出异常。

## func compareTokens(Tokens, Tokens)

```cangjie
public func compareTokens(tokens1: Tokens, tokens2: Tokens): Bool
```

功能：用于比较两个 [Tokens](ast_package_classes.md#class-tokens) 是否一致。

参数：

- tokens1: [Tokens](ast_package_classes.md#class-tokens) - 需要比较的第一个 [Tokens](ast_package_classes.md#class-tokens)。
- tokens2: [Tokens](ast_package_classes.md#class-tokens) - 需要比较的第二个 [Tokens](ast_package_classes.md#class-tokens)。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果两个 [Tokens](ast_package_classes.md#class-tokens) 内容相同（除了换行符、结束符和位置信息）则返回 `true`。