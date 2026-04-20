## class MacroExpandExpr

```cangjie
public class MacroExpandExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示宏调用节点。

一个 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 节点： `@M (a is Int64)`。

父类型：

- [Expr](#class-expr)

### prop at

```cangjie
public mut prop at: Token
```

功能：获取或设置 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 节点中的 `@` 操作符。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `@` 操作符时，抛出异常。

### prop identifier

```cangjie
public mut prop identifier: Token
```

功能：获取或设置宏调用节点的标识符。

类型：[Token](ast_package_structs.md#struct-token)

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 宏调用的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop lSquare

```cangjie
public mut prop lSquare: Token
```

功能：获取或设置 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 属性宏调用的 "["。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "[" 时，抛出异常。

### prop macroAttrs

```cangjie
public mut prop macroAttrs: Tokens
```

功能：获取或设置 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 属性宏调用的输入。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop macroInputs

```cangjie
public mut prop macroInputs: Tokens
```

功能：获取或设置 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 宏调用的输入。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 宏调用的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### prop rSquare

```cangjie
public mut prop rSquare: Token
```

功能：获取或设置 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 属性宏调用的 "]"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "]" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [MacroExpandExpr](ast_package_classes.md#class-macroexpandexpr) 节点时，抛出异常。