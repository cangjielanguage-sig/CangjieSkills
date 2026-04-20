## class PropDecl

```cangjie
public class PropDecl <: Decl {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个属性定义节点。

一个 [PropDecl](ast_package_classes.md#class-propdecl) 节点：`prop X: Int64 { get() { 0 } }`。

父类型：

- [Decl](#class-decl)

### prop colon

```cangjie
public mut prop colon: Token
```

功能：获取或设置 [PropDecl](ast_package_classes.md#class-propdecl) 节点的冒号。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是冒号时，抛出异常。

### prop declType

```cangjie
public mut prop declType : TypeNode
```

功能：获取或设置 [PropDecl](ast_package_classes.md#class-propdecl) 节点的返回类型。

类型：[TypeNode](ast_package_classes.md#class-typenode)

### prop getter

```cangjie
public mut prop getter: FuncDecl
```

功能：获取或设置 [PropDecl](ast_package_classes.md#class-propdecl) 节点的 getter 函数。

类型：[FuncDecl](ast_package_classes.md#class-funcdecl)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [PropDecl](ast_package_classes.md#class-propdecl) 节点不存在 getter 函数时，抛出异常。

### prop lBrace

```cangjie
public mut prop lBrace: Token
```

功能：获取或设置 [PropDecl](ast_package_classes.md#class-propdecl) 节点的 "{"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "{" 时，抛出异常。

### prop rBrace

```cangjie
public mut prop rBrace: Token
```

功能：获取或设置 [PropDecl](ast_package_classes.md#class-propdecl) 节点的 "}"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "}" 时，抛出异常。

### prop setter

```cangjie
public mut prop setter: FuncDecl
```

功能：获取或设置 [PropDecl](ast_package_classes.md#class-propdecl) 节点的 setter 函数。

类型：[FuncDecl](ast_package_classes.md#class-funcdecl)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [PropDecl](ast_package_classes.md#class-propdecl) 节点不存在 setter 函数时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [PropDecl](ast_package_classes.md#class-propdecl) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [PropDecl](ast_package_classes.md#class-propdecl) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [PropDecl](ast_package_classes.md#class-propdecl) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [PropDecl](ast_package_classes.md#class-propdecl) 节点时，抛出异常。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。