## class PrimitiveType

```cangjie
public class PrimitiveType <: TypeNode {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个基本类型节点。

例如数值类型，[Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型，布尔类型等。

父类型：

- [TypeNode](#class-typenode)

### prop keyword

```cangjie
public mut prop keyword: Token
```

功能：获取或设置构造 [PrimitiveType](ast_package_classes.md#class-primitivetype) 类型的关键字，如 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8)。

类型：[Token](ast_package_structs.md#struct-token)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [PrimitiveType](ast_package_classes.md#class-primitivetype) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [PrimitiveType](ast_package_classes.md#class-primitivetype) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [PrimitiveType](ast_package_classes.md#class-primitivetype) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [PrimitiveType](ast_package_classes.md#class-primitivetype) 节点时，抛出异常。

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