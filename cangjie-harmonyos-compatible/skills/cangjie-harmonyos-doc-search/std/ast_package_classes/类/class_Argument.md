## class Argument

```cangjie
public class Argument <: Node {
    public init()
}
```

功能：表示函数调用的实参节点。

例如 `foo(arg:value)` 中的 `arg:value`。

父类型：

- [Node](#class-node)

### prop colon

```cangjie
public mut prop colon: Token
```

功能：获取或设置 [Argument](ast_package_classes.md#class-argument) 节点中的操作符 ":"，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ":" 操作符时，抛出异常。

### prop expr

```cangjie
public mut prop expr: Expr
```

功能：获取或设置 [Argument](ast_package_classes.md#class-argument) 节点中的表达式，如 `arg:value` 中的 `value`。

类型：[Expr](ast_package_classes.md#class-expr)

### prop identifier

```cangjie
public mut prop identifier: Token
```

功能：获取或设置 [Argument](ast_package_classes.md#class-argument) 节点中的标识符，如 `arg:value` 中的 `arg`，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当获取和设置的 [Token](ast_package_structs.md#struct-token) 类型不是 [IDENTIFIER](ast_package_enums.md#identifier) 标识符或 [Token](ast_package_structs.md#struct-token) 的字面量值是空时，抛出异常。

### prop keyword

```cangjie
public mut prop keyword: Token
```

功能：获取或设置 [Argument](ast_package_classes.md#class-argument) 节点中的关键字 `inout`，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Argument](ast_package_classes.md#class-argument) 对象。

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