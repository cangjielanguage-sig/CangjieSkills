## class SynchronizedExpr

```cangjie
public class SynchronizedExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示 `synchronized` 表达式。

一个 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 节点由 `synchronized` 关键字和 `StructuredMutex` 对以及后面的代码块组成, 例如 `synchronized(m) { foo() }`。

父类型：

- [Expr](#class-expr)

### prop block

```cangjie
public mut prop block: Block
```

功能：获取或设置 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 修饰的代码块。

类型：[Block](ast_package_classes.md#class-block)

### prop keyword

```cangjie
public mut prop keyword: Token
```

功能：获取或设置 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 中的 `synchronized` 关键字。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `synchronized` 关键字时，抛出异常。

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 中的 "("。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 中的 ")"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### prop structuredMutex

```cangjie
public mut prop structuredMutex: Expr
```

功能：获取或设置 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 中的 `StructuredMutex` 的对象。

类型：[Expr](ast_package_classes.md#class-expr)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [SynchronizedExpr](ast_package_classes.md#class-synchronizedexpr) 节点时，抛出异常。

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