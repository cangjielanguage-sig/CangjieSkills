## class IfExpr

```cangjie
public class IfExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示条件表达式。

可以根据判定条件是否成立来决定执行哪条代码分支。一个 [IfExpr](ast_package_classes.md#class-ifexpr) 节点中 `if` 是关键字，`if` 之后是一个小括号，小括号内可以是一个表达式或者一个 `let` 声明的解构匹配，接着是一个 [Block](ast_package_classes.md#class-block)，[Block](ast_package_classes.md#class-block) 之后是可选的 `else` 分支。 `else` 分支以 `else` 关键字开始，后接新的 `if` 表达式或一个 [Block](ast_package_classes.md#class-block)。

父类型：

- [Expr](#class-expr)

### prop condition

```cangjie
public mut prop condition: Expr
```

功能：获取或设置 [IfExpr](ast_package_classes.md#class-ifexpr) 节点中的 `if` 后的条件表达式。

类型：[Expr](ast_package_classes.md#class-expr)

### prop elseExpr

```cangjie
public mut prop elseExpr: Expr
```

功能：获取或设置 [IfExpr](ast_package_classes.md#class-ifexpr) 节点中 `else` 分支节点。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当前 [IfExpr](ast_package_classes.md#class-ifexpr) 节点没有 else 分支节点。

### prop ifBlock

```cangjie
public mut prop ifBlock: Block
```

功能：获取或设置 [IfExpr](ast_package_classes.md#class-ifexpr) 节点中的 `if` 后的 block 节点。

类型：[Block](ast_package_classes.md#class-block)

### prop keywordE

```cangjie
public mut prop keywordE: Token
```

功能：获取或设置 [IfExpr](ast_package_classes.md#class-ifexpr) 节点中 `else` 关键字。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `else` 关键字时，抛出异常。

### prop keywordI

```cangjie
public mut prop keywordI: Token
```

功能：获取或设置 [IfExpr](ast_package_classes.md#class-ifexpr) 节点中的 `if` 关键字。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `if` 关键字时，抛出异常。

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [IfExpr](ast_package_classes.md#class-ifexpr) 节点中的 `if` 后的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [IfExpr](ast_package_classes.md#class-ifexpr) 节点中的 `if` 后的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [IfExpr](ast_package_classes.md#class-ifexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [IfExpr](ast_package_classes.md#class-ifexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [IfExpr](ast_package_classes.md#class-ifexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [IfExpr](ast_package_classes.md#class-ifexpr) 节点时，抛出异常。