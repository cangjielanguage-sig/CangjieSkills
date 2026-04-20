## class RangeExpr

```cangjie
public class RangeExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示包含区间操作符的表达式。

[RangeExpr](ast_package_classes.md#class-rangeexpr) 节点：存在两种 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 操作符：`..` 和 `..=`，分别用于创建左闭右开和左闭右闭的 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例。它们的使用方式分别为 `start..end:step` 和 `start..=end:step`。

父类型：

- [Expr](#class-expr)

### prop colon

```cangjie
public mut prop colon: Token
```

功能：获取或设置 [RangeExpr](ast_package_classes.md#class-rangeexpr) 中的 ":" 操作符。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ":" 操作符时，抛出异常。

### prop end

```cangjie
public mut prop end: Expr
```

功能：获取或设置 [RangeExpr](ast_package_classes.md#class-rangeexpr) 中的终止值。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 终止表达式省略。只有在 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> 类型的实例用在下标操作符 `[]` 为空的场景。

### prop op

```cangjie
public mut prop op: Token
```

功能：获取或设置 [RangeExpr](ast_package_classes.md#class-rangeexpr) 中的 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 的操作符。

类型：[Token](ast_package_structs.md#struct-token)

### prop start

```cangjie
public mut prop start: Expr
```

功能：获取或设置 [RangeExpr](ast_package_classes.md#class-rangeexpr) 中的起始值。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 起始表达式省略。只有在 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> 类型的实例用在下标操作符 `[]` 为空的场景。

### prop step

```cangjie
public mut prop step: Expr
```

功能：获取或设置 [RangeExpr](ast_package_classes.md#class-rangeexpr) 中序列中前后两个元素之间的差值。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [RangeExpr](ast_package_classes.md#class-rangeexpr) 中未设置序列前后两个元素之间的差值时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [RangeExpr](ast_package_classes.md#class-rangeexpr) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [RangeExpr](ast_package_classes.md#class-rangeexpr) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [RangeExpr](ast_package_classes.md#class-rangeexpr) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [RangeExpr](ast_package_classes.md#class-rangeexpr) 节点时，抛出异常。