## class VarDecl

```cangjie
public class VarDecl <: Decl {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示变量定义节点。

一个 [VarDecl](ast_package_classes.md#class-vardecl) 节点: `var a: String`，`var b: Int64 = 1`。

> **说明：**
>
> 变量的定义主要包括如下几个部分：修饰符、关键字、patternsMaybeIrrefutable、变量类型和变量初始值。

父类型：

- [Decl](#class-decl)

### prop assign

```cangjie
public mut prop assign: Token
```

功能：获取或设置 [VarDecl](ast_package_classes.md#class-vardecl) 节点中的赋值操作符的位置信息。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是赋值操作符时，抛出异常。

### prop colon

```cangjie
public mut prop colon: Token
```

功能：获取或设置 [VarDecl](ast_package_classes.md#class-vardecl) 节点中的冒号位置信息。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是冒号时，抛出异常。

### prop declType

```cangjie
public mut prop declType: TypeNode
```

功能：获取或设置 [VarDecl](ast_package_classes.md#class-vardecl) 节点的变量类型。

类型：[TypeNode](ast_package_classes.md#class-typenode)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [VarDecl](ast_package_classes.md#class-vardecl) 节点没有声明变量类型时，抛出异常。

### prop expr

```cangjie
public mut prop expr: Expr
```

功能：获取或设置 [VarDecl](ast_package_classes.md#class-vardecl) 节点的变量初始化节点。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [VarDecl](ast_package_classes.md#class-vardecl) 节点没有对变量进行初始化时，抛出异常。

### prop pattern

```cangjie
public mut prop pattern: Pattern
```

功能：获取或设置 [VarDecl](ast_package_classes.md#class-vardecl) 节点的 pattern 节点。

类型：[Pattern](ast_package_classes.md#class-pattern)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [VarDecl](ast_package_classes.md#class-vardecl) 节点没有声明 pattern 节点时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [VarDecl](ast_package_classes.md#class-vardecl) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [VarDecl](ast_package_classes.md#class-vardecl) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [VarDecl](ast_package_classes.md#class-vardecl) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [VarDecl](ast_package_classes.md#class-vardecl) 节点时，抛出异常。

### func isConst()

```cangjie
public func isConst(): Bool
```

功能：判断是否是一个 `Const` 类型的节点。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是一个 `Const` 类型的节点返回 true；反之，返回 false。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。