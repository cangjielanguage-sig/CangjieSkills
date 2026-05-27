## class MatchCase

```cangjie
public class MatchCase <: Node {
    public init()
}
```

功能：表示 `match` 表达式中的一个 `case` 节点。

一个 [MatchCase](ast_package_classes.md#class-matchcase) 节点：`case failScore where score > 0 => 0`。

> **说明：**
>
> - [MatchCase](ast_package_classes.md#class-matchcase) 以关键字 `case` 开头，后跟 [Expr](ast_package_classes.md#class-expr) 或者一个或多个由 `|` 分隔的相同种类的 `pattern`，一个可选的 `patternguard`，一个 `=>` 和一系列声明或表达式。
> - 该节点与 [MatchExpr](ast_package_classes.md#class-matchexpr) 存在强绑定关系。

父类型：

- [Node](#class-node)

### prop arrow

```cangjie
public mut prop arrow: Token
```

功能：获取或设置 [MatchCase](ast_package_classes.md#class-matchcase) 中的 `=>` 操作符的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `=>` 操作符时，抛出异常。

### prop bitOrs

```cangjie
public mut prop bitOrs: Tokens
```

功能：获取或设置 [MatchCase](ast_package_classes.md#class-matchcase) 中的 `|` 操作符的词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 `|` 词法单元序列时，抛出异常。

### prop block

```cangjie
public mut prop block: Block
```

功能：获取或设置 [MatchCase](ast_package_classes.md#class-matchcase) 中的一系列声明或表达式节点。

类型：[Block](ast_package_classes.md#class-block)

### prop expr

```cangjie
public mut prop expr: Expr
```

功能：获取或设置 [MatchCase](ast_package_classes.md#class-matchcase) 中位于 case 后的表达式节点。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [MatchCase](ast_package_classes.md#class-matchcase) 节点中不存在表达式节点时，抛出异常。

### prop keywordC

```cangjie
public mut prop keywordC: Token
```

功能：获取或设置 [MatchCase](ast_package_classes.md#class-matchcase) 内的 `case` 关键字的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `case` 关键字时，抛出异常。

### prop keywordW

```cangjie
public mut prop keywordW: Token
```

功能：获取或设置 [MatchCase](ast_package_classes.md#class-matchcase) 中可选的关键字 `where` 的词法单元，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `where` 关键字时，抛出异常。

### prop patternGuard

```cangjie
public mut prop patternGuard: Expr
```

功能：获取或设置 [MatchCase](ast_package_classes.md#class-matchcase) 中可选的 pattern guard 表达式节点。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [MatchCase](ast_package_classes.md#class-matchcase) 节点中不存在 pattern guard 表达式时，抛出异常。

### prop patterns

```cangjie
public mut prop patterns: ArrayList<Pattern>
```

功能：获取或设置 [MatchCase](ast_package_classes.md#class-matchcase) 中位于 case 后的 `pattern` 列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Pattern](ast_package_classes.md#class-pattern)>