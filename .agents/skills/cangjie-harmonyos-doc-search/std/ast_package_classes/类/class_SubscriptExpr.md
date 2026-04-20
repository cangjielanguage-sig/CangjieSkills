## class SubscriptExpr

```cangjie
public class SubscriptExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示索引访问表达式。

[SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 节点：用于那些支持索引访问的类型（包括 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 类型和 `Tuple` 类型）通过下标来访问其具体位置的元素，如 `arr[0]`。

父类型：

- [Expr](#class-expr)

### prop baseExpr

```cangjie
public mut prop baseExpr: Expr
```

功能：获取或设置 [SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 中的表达式。

类型：[Expr](ast_package_classes.md#class-expr)

### prop indexList

```cangjie
public mut prop indexList: ArrayList<Expr>
```

功能：获取或设置 [SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 中的索引表达式序列。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Expr](ast_package_classes.md#class-expr)>

### prop lSquare

```cangjie
public mut prop lSquare: Token
```

功能：获取或设置 [SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 中的 "["。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "[" 时，抛出异常。

### prop rSquare

```cangjie
public mut prop rSquare: Token
```

功能：获取或设置 [SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 中的 "]"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "]" 时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [SubscriptExpr](ast_package_classes.md#class-subscriptexpr) 节点时，抛出异常。

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