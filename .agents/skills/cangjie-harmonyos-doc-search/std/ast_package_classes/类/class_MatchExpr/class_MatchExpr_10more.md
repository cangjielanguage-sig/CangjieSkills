## class MatchExpr

```cangjie
public class MatchExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示模式匹配表达式实现模式匹配。

模式匹配表达式分为带 selector 的 `match` 表达式和不带 selector 的 `match` 表达式。

父类型：

- [Expr](#class-expr)

### prop keyword

```cangjie
public mut prop keyword: Token
```

功能：获取或设置 [MatchExpr](ast_package_classes.md#class-matchexpr) 节点中 `match` 关键字。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `matcch` 关键字时，抛出异常。

### prop lBrace

```cangjie
public mut prop lBrace: Token
```

功能：获取或设置 [MatchExpr](ast_package_classes.md#class-matchexpr) 之后的 "{"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "{" 时，抛出异常。

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [MatchExpr](ast_package_classes.md#class-matchexpr) 之后的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop matchCases

```cangjie
public mut prop matchCases: ArrayList<MatchCase>
```

功能：获取或设置 [MatchExpr](ast_package_classes.md#class-matchexpr) 内的 `matchCase`, `matchCase` 以关键字 `case` 开头，后跟一个或者多个由 [Pattern](ast_package_classes.md#class-pattern) 或 [Expr](ast_package_classes.md#class-expr)节点，具体见 [MatchCase](ast_package_classes.md#class-matchcase)。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[MatchCase](ast_package_classes.md#class-matchcase)>

### prop rBrace

```cangjie
public mut prop rBrace: Token
```

功能：获取或设置 [MatchExpr](ast_package_classes.md#class-matchexpr) 之后的 "}"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "}" 时，抛出异常。

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [MatchExpr](ast_package_classes.md#class-matchexpr) 之后的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### prop selector

```cangjie
public mut prop selector: Expr
```

功能：获取或设置关键字 `match` 之后的 [Expr](ast_package_classes.md#class-expr)。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当该表达式是一个不带 selector 的 `match` 表达式时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [MatchExpr](ast_package_classes.md#class-matchexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [MatchExpr](ast_package_classes.md#class-matchexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [MatchExpr](ast_package_classes.md#class-matchexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [MatchExpr](ast_package_classes.md#class-matchexpr) 节点时，抛出异常。