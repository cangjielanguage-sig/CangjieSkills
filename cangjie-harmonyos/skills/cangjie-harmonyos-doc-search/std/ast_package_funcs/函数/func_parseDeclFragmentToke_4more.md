## func parseDeclFragment(Tokens, Int64)

```cangjie
public func parseDeclFragment(input: Tokens, startFrom !: Int64 = 0): (Decl, Int64)
```

功能：用于解析一组词法单元，获取一个 [Decl](ast_package_classes.md#class-decl) 类型的节点和继续解析节点的索引。

> **注意：**
>
> 该函数不支持解析 [FuncParam](ast_package_classes.md#class-funcparam)、 [PropDecl](ast_package_classes.md#class-propdecl)、[PrimaryCtorDecl](ast_package_classes.md#class-primaryctordecl) 类型。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。
- startFrom!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 起始位置。

返回值：

- ([Decl](ast_package_classes.md#class-decl), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) - 语法树节点，继续解析的位置。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [Decl](ast_package_classes.md#class-decl) 节点时，抛出异常，异常中包含报错提示信息。

## func parseExpr(Tokens)

```cangjie
public func parseExpr(input: Tokens): Expr
```

功能：用于解析一组词法单元，获取一个 [Expr](ast_package_classes.md#class-expr) 类型的节点。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。

返回值：

- [Expr](ast_package_classes.md#class-expr) - 一个 [Expr](ast_package_classes.md#class-expr) 类型的节点。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [Expr](ast_package_classes.md#class-expr) 节点时，抛出异常，异常中包含报错提示信息。

## func parseExprFragment(Tokens, Int64)

```cangjie
public func parseExprFragment(input: Tokens, startFrom !: Int64 = 0): (Expr, Int64)
```

功能：用于解析一组词法单元，获取一个 [Expr](ast_package_classes.md#class-expr) 类型的节点和继续解析节点的索引。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。
- startFrom!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 起始位置。

返回值：

- ([Expr](ast_package_classes.md#class-expr), [Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) - 语法树节点，继续解析的位置。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [Expr](ast_package_classes.md#class-expr) 节点时，抛出异常，异常中包含报错提示信息。

## func parsePattern(Tokens)

```cangjie
public func parsePattern(input: Tokens): Pattern
```

功能：用于解析一组词法单元，获取一个 [Pattern](ast_package_classes.md#class-pattern) 类型的节点。

参数：

- input: [Tokens](ast_package_classes.md#class-tokens) - 待解析源码的词法单元。

返回值：

- [Pattern](ast_package_classes.md#class-pattern) - 一个 [Pattern](ast_package_classes.md#class-pattern) 类型的节点。

异常：

- [ParseASTException](ast_package_exceptions.md#class-parseastexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [Pattern](ast_package_classes.md#class-pattern) 节点时，抛出异常，异常中包含报错提示信息。