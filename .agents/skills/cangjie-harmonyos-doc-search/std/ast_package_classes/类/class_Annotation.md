## class Annotation

```cangjie
public class Annotation <: Node {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示编译器内置的注解节点。

一个 [Annotation](ast_package_classes.md#class-annotation) 节点：`@CallingConv[xxx]`, `@Attribute[xxx]`, `@When[condition]`等。

父类型：

- [Node](#class-node)

### prop arguments

```cangjie
public mut prop arguments: ArrayList<Argument>
```

功能：获取或设置 [Annotation](ast_package_classes.md#class-annotation) 中的参数序列，如 `@CallingConv[xxx]` 中的 `xxx`。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Argument](ast_package_classes.md#class-argument)>

### prop at

```cangjie
public mut prop at: Token
```

功能：获取或设置 [Annotation](ast_package_classes.md#class-annotation) 节点中的 `@` 操作符或 `@!` 操作符。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `@` 操作符或 `@!` 操作符时，抛出异常。

### prop attributes

```cangjie
public mut prop attributes: Tokens
```

功能：获取或设置 `Attribute` 中设置的属性值，仅用于 `@Attribute`，如 `@Attribute[xxx]` 中的 `xxx`。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop condition

```cangjie
public mut prop condition: Expr
```

功能：获取或设置条件编译中的条件表达式，用于 `@When`，如 `@When[xxx]` 中的 `xxx`。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当 [Annotation](ast_package_classes.md#class-annotation) 节点中没有条件表达式时，抛出异常。

### prop identifier

```cangjie
public mut prop identifier: Token
```

功能：获取或设置 [Annotation](ast_package_classes.md#class-annotation) 节点的标识符，如 `@CallingConv[xxx]` 中的 `CallingConv`。

类型：[Token](ast_package_structs.md#struct-token)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Annotation](ast_package_classes.md#class-annotation) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：根据输入的词法单元，构造一个 [Annotation](ast_package_classes.md#class-annotation) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [Annotation](ast_package_classes.md#class-annotation) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [Annotation](ast_package_classes.md#class-annotation) 节点时，抛出异常。

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