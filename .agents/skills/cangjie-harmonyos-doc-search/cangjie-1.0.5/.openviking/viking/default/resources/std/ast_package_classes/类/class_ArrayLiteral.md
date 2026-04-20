## class ArrayLiteral

```cangjie
public class ArrayLiteral <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 字面量节点。

[ArrayLiteral](ast_package_classes.md#class-arrayliteral) 节点：使用格式 `[element1, element2, ... , elementN]` 表示， 每个 `element` 是一个表达式。

父类型：

- [Expr](#class-expr)

### prop elements

```cangjie
public mut prop elements: ArrayList<Expr>
```

功能：获取或设置 [ArrayLiteral](ast_package_classes.md#class-arrayliteral) 中的表达式列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Expr](ast_package_classes.md#class-expr)>

### prop lSquare

```cangjie
public mut prop lSquare: Token
```

功能：获取或设置 [ArrayLiteral](ast_package_classes.md#class-arrayliteral) 中的 "["。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "[" 时，抛出异常。

### prop rSquare

```cangjie
public mut prop rSquare: Token
```

功能：获取或设置 [ArrayLiteral](ast_package_classes.md#class-arrayliteral) 中的 "]"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "]" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [ArrayLiteral](ast_package_classes.md#class-arrayliteral) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [ArrayLiteral](ast_package_classes.md#class-arrayliteral) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [ArrayLiteral](ast_package_classes.md#class-arrayliteral) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [ArrayLiteral](ast_package_classes.md#class-arrayliteral) 节点时，抛出异常。

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