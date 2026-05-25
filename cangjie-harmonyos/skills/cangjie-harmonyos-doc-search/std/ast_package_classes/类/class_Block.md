## class Block

```cangjie
public class Block <: Expr {
    public init()
}
```

功能：表示块节点。

[Block](ast_package_classes.md#class-block) 由一对匹配的大括号及其中可选的表达式声明序列组成的结构，简称 “块”。

父类型：

- [Expr](#class-expr)

### prop lBrace

```cangjie
public mut prop lBrace: Token
```

功能：获取或设置 [Block](ast_package_classes.md#class-block) 的 "{"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "{" 时，抛出异常。

### prop nodes

```cangjie
public mut prop nodes: ArrayList<Node>
```

功能：获取或设置 [Block](ast_package_classes.md#class-block) 中的表达式或声明序列。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Node](ast_package_classes.md#class-node)>

### prop rBrace

```cangjie
public mut prop rBrace: Token
```

功能：获取或设置 [Block](ast_package_classes.md#class-block) 的 "}"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "}" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Block](ast_package_classes.md#class-block) 对象。

> **说明：**
>
> [Block](ast_package_classes.md#class-block) 节点无法脱离表达式或声明节点单独存在，因此不提供其他的构造函数。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。

### func traverse(Visitor)

```cangjie
public func traverse(v: Visitor): Unit
```

功能：遍历当前语法树节点及其子节点。若提前终止遍历子节点的行为，可重写 `visit` 函数并调用 `breakTraverse` 函数提前终止遍历行为，请参见[自定义访问函数遍历 AST 对象示例](../ast_samples/traverse.md)。

参数：

- v: [Visitor](ast_package_classes.md#class-visitor) - [Visitor](ast_package_classes.md#class-visitor) 类型的实例。