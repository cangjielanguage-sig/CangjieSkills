## class ForInExpr

```cangjie
public class ForInExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示 `for-in` 表达式。

[ForInExpr](ast_package_classes.md#class-forinexpr) 类型中，关键字 `for` 之后是 [Pattern](ast_package_classes.md#class-pattern), 此后是一个 `in` 关键字和表达式节点，最后是一个执行循环体 [Block](ast_package_classes.md#class-block)。

父类型：

- [Expr](#class-expr)

### prop block

```cangjie
public mut prop block: Block
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中的循环体。

类型：[Block](ast_package_classes.md#class-block)

### prop expr

```cangjie
public mut prop expr: Expr
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中的表达式。

类型：[Expr](ast_package_classes.md#class-expr)

### prop keywordF

```cangjie
public mut prop keywordF: Token
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中的关键字 `for`。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `for` 关键字时，抛出异常。

### prop keywordI

```cangjie
public mut prop keywordI: Token
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中的关键字 `in`。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `in` 关键字时，抛出异常。

### prop keywordW

```cangjie
public mut prop keywordW: Token
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中的关键字 `where`。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `where` 关键字时，抛出异常。

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中关键字 `for` 后的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop pattern

```cangjie
public mut prop pattern: Pattern
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中的 [Pattern](ast_package_classes.md#class-pattern) 节点。

类型：[Pattern](ast_package_classes.md#class-pattern)

### prop patternGuard

```cangjie
public mut prop patternGuard: Expr
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中的 `patternGuard` 条件表达式。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [ForInExpr](ast_package_classes.md#class-forinexpr) 节点中不存在 `patternGuard` 表达式时，抛出异常。

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [ForInExpr](ast_package_classes.md#class-forinexpr) 中的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [ForInExpr](ast_package_classes.md#class-forinexpr) 对象。