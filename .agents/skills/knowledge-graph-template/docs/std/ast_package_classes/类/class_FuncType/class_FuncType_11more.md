## class FuncType

```cangjie
public class FuncType <: TypeNode {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示函数类型节点。

由函数的参数类型和返回类型组成，参数类型与返回类型之间用 `->` 分隔，如：`(Int32) -> Unit`。

父类型：

- [TypeNode](#class-typenode)

### prop arrow

```cangjie
public mut prop arrow: Token
```

功能：获取或设置 [FuncType](ast_package_classes.md#class-functype) 节点参数类型与返回类型之间的 `->`的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `->`的词法单元时，抛出异常。

### prop commas

```cangjie
public mut prop commas: Tokens
```

功能：获取或设置 [FuncType](ast_package_classes.md#class-functype) 节点中的 "," 词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "," 词法单元序列时，抛出异常。

### prop keyword

```cangjie
public mut prop keyword: Token
```

功能：获取或设置 [FuncType](ast_package_classes.md#class-functype) 节点的中的关键字 `CFunc` 的词法单元，若不是一个 `CFunc` 类型，则获取一个 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [FuncType](ast_package_classes.md#class-functype) 节点的 "(" 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [FuncType](ast_package_classes.md#class-functype) 节点的 ")" 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### prop returnType

```cangjie
public mut prop returnType: TypeNode
```

功能：获取或设置 [FuncType](ast_package_classes.md#class-functype) 返回类型节点。

类型：[TypeNode](ast_package_classes.md#class-typenode)

### prop types

```cangjie
public mut prop types: ArrayList<TypeNode>
```

功能：获取或设置 [FuncType](ast_package_classes.md#class-functype) 节点中函数的参数类型列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[TypeNode](ast_package_classes.md#class-typenode)>

### init()

```cangjie
public init()
```

功能：构造一个默认的 [FuncType](ast_package_classes.md#class-functype) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [FuncType](ast_package_classes.md#class-functype) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [FuncType](ast_package_classes.md#class-functype) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [FuncType](ast_package_classes.md#class-functype) 节点时，抛出异常。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。