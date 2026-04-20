## class DoWhileExpr

```cangjie
public class DoWhileExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示 `do-while` 表达式。

父类型：

- [Expr](#class-expr)

### prop block

```cangjie
public mut prop block: Block
```

功能：获取或设置 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 中的块表达式。

类型：[Block](ast_package_classes.md#class-block)

### prop condition

```cangjie
public mut prop condition: Expr
```

功能：获取或设置关键字 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 中的条件表达式。

类型：[Expr](ast_package_classes.md#class-expr)

### prop keywordD

```cangjie
public mut prop keywordD: Token
```

功能：获取或设置 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 节点中 `do` 关键字，其中 keywordD 中的 D 为关键字 `do` 的首字母大写，代表关键字 `do` 。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `do` 关键字时，抛出异常。

### prop keywordW

```cangjie
public mut prop keywordW: Token
```

功能：获取或设置 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 节点中 `while` 关键字，其中 keywordW 中的 W 为关键字 `while` 的首字母大写，代表关键字 `while` 。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `while` 关键字时，抛出异常。

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 中 `while` 关键字之后的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 中 `while` 关键字之后的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [DoWhileExpr](ast_package_classes.md#class-dowhileexpr) 节点时，抛出异常。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。