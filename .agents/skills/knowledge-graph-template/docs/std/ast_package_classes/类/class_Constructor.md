## class Constructor

```cangjie
public class Constructor <: Node {
    public init()
}
```

功能：表示 `enum` 类型中的 [Constructor](ast_package_classes.md#class-constructor) 节点。

一个 [Constructor](ast_package_classes.md#class-constructor) 节点：enum TimeUnit { Year | Month([Float32](../../core/core_package_api/core_package_intrinsics.md#float32), [Float32](../../core/core_package_api/core_package_intrinsics.md#float32))} 中的 Year 和 Month([Float32](../../core/core_package_api/core_package_intrinsics.md#float32), [Float32](../../core/core_package_api/core_package_intrinsics.md#float32))。

> **说明：**
>
> [Constructor](ast_package_classes.md#class-constructor) 可以没有参数，也可以有一组不同类型的参数。

父类型：

- [Node](#class-node)

### prop annotations

```cangjie
public mut prop annotations: ArrayList<Annotation>
```

功能：获取或设置作用于 [Constructor](ast_package_classes.md#class-constructor) 节点的注解列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Annotation](ast_package_classes.md#class-annotation)>

### prop identifier

```cangjie
public mut prop identifier: Token
```

功能：获取或设置 [Constructor](ast_package_classes.md#class-constructor) 的标识符词法单元。

类型：[Token](ast_package_structs.md#struct-token)

### prop lParen

```cangjie
public mut prop lParen: Token
```

功能：获取或设置 [Constructor](ast_package_classes.md#class-constructor) 节点中的 "(" 词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 "(" 时，抛出异常。

### prop rParen

```cangjie
public mut prop rParen: Token
```

功能：获取或设置 [Constructor](ast_package_classes.md#class-constructor) 节点中的 ")" 词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ")" 时，抛出异常。

### prop typeArguments

```cangjie
public mut prop typeArguments: ArrayList<TypeNode>
```

功能：获取或设置 [Constructor](ast_package_classes.md#class-constructor) 节点可选的参数类型节点的集合。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[TypeNode](ast_package_classes.md#class-typenode)>

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Constructor](ast_package_classes.md#class-constructor) 对象。

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