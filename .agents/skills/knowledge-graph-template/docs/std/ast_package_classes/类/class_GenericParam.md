## class GenericParam

```cangjie
public class GenericParam <: Node {
    public init()
    public init(parameters: Tokens)
}
```

功能：表示一个类型形参节点。

一个 [GenericParam](ast_package_classes.md#class-genericparam) 节点：`<T1, T2, T3>`。

> **说明：**
>
> 类型形参用 `<>` 括起并用 "," 分隔多个类型形参名称。

父类型：

- [Node](#class-node)

### prop lAngle

```cangjie
public mut prop lAngle: Token
```

功能：获取或设置 [GenericParam](ast_package_classes.md#class-genericparam) 节点中的左尖括号词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是左尖括号时，抛出异常。

### prop parameters

```cangjie
public mut prop parameters: Tokens
```

功能：获取或设置 [GenericParam](ast_package_classes.md#class-genericparam) 节点中的类型形参的 [Tokens](ast_package_classes.md#class-tokens) 类型，可能为空，如 `<T1, T2, T3>` 中的 `T1` `T2` 和 `T3`。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop rAngle

```cangjie
public mut prop rAngle: Token
```

功能：获取或设置 [GenericParam](ast_package_classes.md#class-genericparam) 节点中的右尖括号词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是右尖括号时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [GenericParam](ast_package_classes.md#class-genericparam) 对象。

### init(Tokens)

```cangjie
public init(parameters: Tokens)
```

功能：构造一个 [GenericParam](ast_package_classes.md#class-genericparam) 对象。

参数：

- parameters: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [GenericParam](ast_package_classes.md#class-genericparam) 的类型形参的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

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