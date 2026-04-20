## class BinaryExpr

```cangjie
public class BinaryExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个二元操作表达式节点。

一个 [BinaryExpr](ast_package_classes.md#class-binaryexpr) 节点：`a + b`, `a - b` 等。

父类型：

- [Expr](#class-expr)

### prop leftExpr

```cangjie
public mut prop leftExpr: Expr
```

功能：获取或设置 [BinaryExpr](ast_package_classes.md#class-binaryexpr) 节点中操作符左侧的表达式节点。

类型：[Expr](ast_package_classes.md#class-expr)

### prop op

```cangjie
public mut prop op: Token
```

功能：获取或设置 [BinaryExpr](ast_package_classes.md#class-binaryexpr) 节点中的二元操作符。

类型：[Token](ast_package_structs.md#struct-token)

### prop rightExpr

```cangjie
public mut prop rightExpr: Expr
```

功能：获取或设置 [BinaryExpr](ast_package_classes.md#class-binaryexpr) 节点中操作符右侧的表达式节点。

类型：[Expr](ast_package_classes.md#class-expr)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [BinaryExpr](ast_package_classes.md#class-binaryexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [BinaryExpr](ast_package_classes.md#class-binaryexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [BinaryExpr](ast_package_classes.md#class-binaryexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [BinaryExpr](ast_package_classes.md#class-binaryexpr) 节点时，抛出异常。

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