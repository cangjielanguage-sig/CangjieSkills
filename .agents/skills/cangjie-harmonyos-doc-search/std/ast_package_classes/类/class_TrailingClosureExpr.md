## class TrailingClosureExpr

```cangjie
public class TrailingClosureExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示尾随 `Lambda` 节点。

一个 [TrailingClosureExpr](ast_package_classes.md#class-trailingclosureexpr) 节点将 lambda 表达式放在函数调用的尾部，括号外面，如 `f(a){ i => i * i }`。

父类型：

- [Expr](#class-expr)

### prop expr

```cangjie
public mut prop expr: Expr
```

功能：获取或设置 [TrailingClosureExpr](ast_package_classes.md#class-trailingclosureexpr) 中的表达式。

类型：[Expr](ast_package_classes.md#class-expr)

### prop lambdaExpr

```cangjie
public mut prop lambdaExpr: LambdaExpr
```

功能：获取或设置 [TrailingClosureExpr](ast_package_classes.md#class-trailingclosureexpr) 中的尾随 lambda。

类型：[LambdaExpr](ast_package_classes.md#class-lambdaexpr)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [TrailingClosureExpr](ast_package_classes.md#class-trailingclosureexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [TrailingClosureExpr](ast_package_classes.md#class-trailingclosureexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [TrailingClosureExpr](ast_package_classes.md#class-trailingclosureexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [TrailingClosureExpr](ast_package_classes.md#class-trailingclosureexpr) 节点。

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