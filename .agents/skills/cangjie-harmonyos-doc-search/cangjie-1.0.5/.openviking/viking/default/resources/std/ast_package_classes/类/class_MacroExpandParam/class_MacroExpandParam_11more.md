## class MacroExpandParam

```cangjie
public class MacroExpandParam <: FuncParam {
    public init()
}
```

功能：表示宏调用节点。

一个 [MacroExpandDecl](ast_package_classes.md#class-macroexpanddecl) 节点： `func foo (@M a: Int64)` 中的 `@M a: Int64`。

父类型：

- [FuncParam](#class-funcparam)

### prop fullIdentifier

```cangjie
public mut prop fullIdentifier: Token
```

功能：获取或设置宏调用节点的完整标识符。

类型：[Token](ast_package_structs.md#struct-token)

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 宏调用的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop lSquare

```cangjie
public mut prop lSquare: Token
```

功能：获取或设置 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 属性宏调用的 "["。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "[" 时，抛出异常。

### prop macroAttrs

```cangjie
public mut prop macroAttrs: Tokens
```

功能：获取或设置 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 属性宏调用的输入。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop macroInputDecl

```cangjie
public mut prop macroInputDecl: Decl
```

功能：获取或设置 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 中的声明节点。

类型：[Decl](ast_package_classes.md#class-decl)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 节点中没有声明节点时，抛出异常。

### prop macroInputs

```cangjie
public mut prop macroInputs: Tokens
```

功能：获取或设置 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 宏调用的输入。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 宏调用的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### prop rSquare

```cangjie
public mut prop rSquare: Token
```

功能：获取或设置 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 属性宏调用的 "]"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "]" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [MacroExpandParam](ast_package_classes.md#class-macroexpandparam) 对象。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。