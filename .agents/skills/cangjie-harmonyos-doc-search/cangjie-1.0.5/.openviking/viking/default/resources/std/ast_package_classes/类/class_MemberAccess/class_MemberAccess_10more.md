## class MemberAccess

```cangjie
public class MemberAccess <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示成员访问表达式。

可以用于访问 class、interface、struct 等类型的成员。一个 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点的形式为 `T.a`，`T` 为成员访问表达式的主体，`a` 表示成员的名字。

父类型：

- [Expr](#class-expr)

### prop baseExpr

```cangjie
public mut prop baseExpr: Expr
```

功能：获取或设置 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点的成员访问表达式主体。

类型：[Expr](ast_package_classes.md#class-expr)

### prop commas

```cangjie
public mut prop commas: Tokens
```

功能：获取或设置 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点中的 "," 词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "," 词法单元序列时，抛出异常。

### prop dot

```cangjie
public mut prop dot: Token
```

功能：获取或设置 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点中的 "."。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "." 词法单元类型时，抛出异常。

### prop field

```cangjie
public mut prop field: Token
```

功能：获取或设置 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点成员的名字。

类型：[Token](ast_package_structs.md#struct-token)

### prop lAngle

```cangjie
public mut prop lAngle: Token
```

功能：获取或设置 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点中的左尖括号。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是左尖括号时，抛出异常。

### prop rAngle

```cangjie
public mut prop rAngle: Token
```

功能：获取或设置 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点中的右尖括号。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是右尖括号时，抛出异常。

### prop typeArguments

```cangjie
public mut prop typeArguments: ArrayList<TypeNode>
```

功能：获取或设置 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点中的实例化类型。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[TypeNode](ast_package_classes.md#class-typenode)>

### init()

```cangjie
public init()
```

功能：构造一个默认的 [MemberAccess](ast_package_classes.md#class-memberaccess) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [MemberAccess](ast_package_classes.md#class-memberaccess) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [MemberAccess](ast_package_classes.md#class-memberaccess) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [MemberAccess](ast_package_classes.md#class-memberaccess) 节点时，抛出异常。