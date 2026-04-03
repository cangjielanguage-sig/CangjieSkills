## class TokensIterator

```cangjie
public class TokensIterator <: Iterator<Token> {
    public init(tokens: Tokens)
}
```

功能：实现 [Tokens](ast_package_classes.md#class-tokens) 的迭代器功能。

父类型：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<[Token](ast_package_structs.md#struct-token)>

### init(Tokens)

```cangjie
public init(tokens: Tokens)
```

功能：构造一个 [TokensIterator](ast_package_classes.md#class-tokensiterator) 对象。

参数：

- tokens: [Tokens](ast_package_classes.md#class-tokens) - 传入 [Tokens](ast_package_classes.md#class-tokens)。

### func next()

```cangjie
public func next(): Option<Token>
```

功能：获取迭代器中的下一个值。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Token](ast_package_structs.md#struct-token)> - 返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Token](ast_package_structs.md#struct-token)> 类型，当遍历结束后，返回 None。

### func peek()

```cangjie
public func peek(): Option<Token>
```

功能：获取迭代器中的当前值。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Token](ast_package_structs.md#struct-token)> - 返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[Token](ast_package_structs.md#struct-token)> 类型，当遍历结束后，返回 None。

### func seeing(TokenKind)

```cangjie
public func seeing(kind: TokenKind): Bool
```

功能：判断当前节点的 [Token](ast_package_structs.md#struct-token) 类型是否是传入的类型。

参数：

- kind: [TokenKind](ast_package_enums.md#enum-tokenkind) - 需要判断的 [TokenKind](ast_package_enums.md#enum-tokenkind) 类型。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果当前节点的 [TokenKind](ast_package_enums.md#enum-tokenkind) 与传入类型相同，返回 true，否则返回 false。