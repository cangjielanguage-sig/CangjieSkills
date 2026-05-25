## class MacroDecl

```cangjie
public class MacroDecl <: Decl {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个宏定义节点。

一个 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点：`public macro M(input: Tokens): Tokens {...}`。

父类型：

- [Decl](#class-decl)

### prop block

```cangjie
public mut prop block: Block
```

功能：获取或设置 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点的函数体。

类型：[Block](ast_package_classes.md#class-block)

### prop colon

```cangjie
public mut prop colon: Token
```

功能：获取或设置 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点的冒号。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是冒号时，抛出异常。

### prop declType

```cangjie
public mut prop declType: TypeNode
```

功能：获取或设置 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点的函数返回类型。

类型：[TypeNode](ast_package_classes.md#class-typenode)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点的函数返回类型是一个缺省值时，抛出异常。

### prop funcParams

```cangjie
public mut prop funcParams: ArrayList<FuncParam>
```

功能：获取或设置 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点的参数。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[FuncParam](ast_package_classes.md#class-funcparam)>

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [MacroDecl](ast_package_classes.md#class-macrodecl) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [MacroDecl](ast_package_classes.md#class-macrodecl) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [MacroDecl](ast_package_classes.md#class-macrodecl) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [MacroDecl](ast_package_classes.md#class-macrodecl) 节点时，抛出异常。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。