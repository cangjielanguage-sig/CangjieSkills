## class TryExpr

```cangjie
public class TryExpr <: Expr {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示 `try` 表达式节点。

`try` 表达式包括三个部分：`try` 块，`catch` 块和 `finally` 块。

父类型：

- [Expr](#class-expr)

### prop catchBlocks

```cangjie
public mut prop catchBlocks: ArrayList<Block>
```

功能：获取或设置 [TryExpr](ast_package_classes.md#class-tryexpr) 中的 Catch 块。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Block](ast_package_classes.md#class-block)>

### prop catchPatterns

```cangjie
public mut prop catchPatterns: ArrayList<Pattern>
```

功能：获取或设置 [TryExpr](ast_package_classes.md#class-tryexpr) 中通过模式匹配的方式匹配待捕获的异常序列。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Pattern](ast_package_classes.md#class-pattern)>

### prop finallyBlock

```cangjie
public mut prop finallyBlock: Block
```

功能：获取或设置 [TryExpr](ast_package_classes.md#class-tryexpr) 中的关键字 `Finally` 块。

类型：[Block](ast_package_classes.md#class-block)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [TryExpr](ast_package_classes.md#class-tryexpr) 节点无 `Finally` 块节点时，抛出异常。

### prop keywordF

```cangjie
public mut prop keywordF: Token
```

功能：获取或设置 [TryExpr](ast_package_classes.md#class-tryexpr) 中的 `finally` 关键字。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `finally` 关键字时，抛出异常。

### prop keywordT

```cangjie
public mut prop keywordT: Token
```

功能：获取或设置 [TryExpr](ast_package_classes.md#class-tryexpr) 中的 `try` 关键字。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `try` 关键字时，抛出异常。

### prop keywordsC

```cangjie
public mut prop keywordsC: Tokens
```

功能：获取或设置 [TryExpr](ast_package_classes.md#class-tryexpr) 中的关键字 `catch`。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `catch` 关键字时，抛出异常。

### prop resourceSpec

```cangjie
public mut prop resourceSpec: ArrayList<VarDecl>
```

功能：获取或设置 [TryExpr](ast_package_classes.md#class-tryexpr) 中 Try-with-resources 类型表达式的实例化对象序列。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[VarDecl](ast_package_classes.md#class-vardecl)>

### prop tryBlock

```cangjie
public mut prop tryBlock: Block
```

功能：获取或设置 [TryExpr](ast_package_classes.md#class-tryexpr) 中由表达式与声明组成的块。

类型：[Block](ast_package_classes.md#class-block)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [TryExpr](ast_package_classes.md#class-tryexpr) 对象。