## interface ToTokens

```cangjie
public interface ToTokens {
    func toTokens(): Tokens
}
```

功能：实现对应类型的实例到 [Tokens](ast_package_classes.md#class-tokens) 类型转换的接口，作为支持 `quote` 插值操作必须实现的接口。

### func toTokens()

```cangjie
func toTokens(): Tokens
```

功能：实现对应类型的实例到 [Tokens](ast_package_classes.md#class-tokens) 类型的转换。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转换后的 [Tokens](ast_package_classes.md#class-tokens)。

### extend\<T> Array\<T> <: ToTokens

```cangjie
extend<T> Array<T> <: ToTokens
```

功能：实现 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> 类型到 [Tokens](ast_package_classes.md#class-tokens) 类型的转换。

父类型：

- [ToTokens](#interface-totokens)

#### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：实现 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> 类型到 [Tokens](ast_package_classes.md#class-tokens) 类型的转换，仅支持数值类型、[Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型、[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型、[String](../../core/core_package_api/core_package_structs.md#struct-string) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转换后的 [Tokens](ast_package_classes.md#class-tokens)。

### extend\<T> ArrayList\<T> <: ToTokens

```cangjie
extend<T> ArrayList<T> <: ToTokens
```

功能：实现 [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T> 类型到 [Tokens](ast_package_classes.md#class-tokens) 类型的转换。

父类型：

- [ToTokens](#interface-totokens)

#### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：实现 [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt) 类型到 [Tokens](ast_package_classes.md#class-tokens) 类型的转换，目前支持的类型有 [Decl](ast_package_classes.md#class-decl)、[Node](ast_package_classes.md#class-node)、[Constructor](ast_package_classes.md#class-constructor)、[Argument](ast_package_classes.md#class-argument)、[FuncParam](ast_package_classes.md#class-funcparam)、[MatchCase](ast_package_classes.md#class-matchcase)、[Modifier](ast_package_classes.md#class-modifier)、[Annotation](ast_package_classes.md#class-annotation)、[ImportList](ast_package_classes.md#class-importlist)、[Pattern](ast_package_classes.md#class-pattern)、[TypeNode](ast_package_classes.md#class-typenode) 等。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转换后的 [Tokens](ast_package_classes.md#class-tokens)。

### extend Bool <: ToTokens

```cangjie
extend Bool <: ToTokens
```

功能：实现 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型到 [Tokens](ast_package_classes.md#class-tokens) 类型的转换。

父类型：

- [ToTokens](#interface-totokens)

#### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：实现 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型到 [Tokens](ast_package_classes.md#class-tokens) 类型的转换。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转换后的 [Tokens](ast_package_classes.md#class-tokens)。