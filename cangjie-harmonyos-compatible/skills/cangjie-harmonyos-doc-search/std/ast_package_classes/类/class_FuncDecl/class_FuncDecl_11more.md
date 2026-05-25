## class FuncDecl

```cangjie
public class FuncDecl <: Decl {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个函数定义节点。

由可选的函数修饰符，关键字 `func` ，函数名，可选的类型形参列表，函数参数，可缺省的函数返回类型来定义一个函数，函数定义时必须有函数体，函数体是一个块。

父类型：

- [Decl](#class-decl)

### prop block

```cangjie
public mut prop block: Block
```

功能：获取或设置 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点的函数体。

类型：[Block](ast_package_classes.md#class-block)

### prop colon

```cangjie
public mut prop colon: Token
```

功能：获取或设置 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点的冒号。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是冒号时，抛出异常。

### prop declType

```cangjie
public mut prop declType: TypeNode
```

功能：获取或设置 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点的函数返回类型。

类型：[TypeNode](ast_package_classes.md#class-typenode)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点的函数返回类型是一个缺省值时，抛出异常。

### prop funcParams

```cangjie
public mut prop funcParams: ArrayList<FuncParam>
```

功能：获取或设置 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点的函数参数。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[FuncParam](ast_package_classes.md#class-funcparam)>

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop overloadOp

```cangjie
public mut prop overloadOp: Tokens
```

功能：获取或设置 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点的重载操作符。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [FuncDecl](ast_package_classes.md#class-funcdecl) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [FuncDecl](ast_package_classes.md#class-funcdecl) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [FuncDecl](ast_package_classes.md#class-funcdecl) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [FuncDecl](ast_package_classes.md#class-funcdecl) 节点时，抛出异常。

### func isConst()

```cangjie
public func isConst(): Bool
```

功能：判断是否是一个 `Const` 类型的节点。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是一个 `Const` 类型的节点返回 true；反之，返回 false。