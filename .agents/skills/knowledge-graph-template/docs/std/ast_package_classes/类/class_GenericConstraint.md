## class GenericConstraint

```cangjie
public class GenericConstraint <: Node {
    public init()
}
```

功能：表示一个泛型约束节点。

一个 [GenericConstraint](ast_package_classes.md#class-genericconstraint) 节点：`interface Enumerable<U> where U <: Bounded {}` 中的 `where U <: Bounded`。

> **说明：**
>
> 通过 `where` 之后的 `<:` 运算符来声明，由一个下界与一个上界来组成。其中 `<:` 左边称为约束的下界，下界只能为类型变元。`<:` 右边称为约束上界，约束上界可以为类型。

父类型：

- [Node](#class-node)

### prop bitAnds

```cangjie
public mut prop bitAnds: Tokens
```

功能：获取或设置 [GenericConstraint](ast_package_classes.md#class-genericconstraint) 节点中的 `&` 操作符的词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 `&` 词法单元序列时，抛出异常。

### prop keyword

```cangjie
public mut prop keyword: Token
```

功能：获取或设置 [GenericConstraint](ast_package_classes.md#class-genericconstraint) 节点中关键字 `where` 词法单元，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `where` 关键字时，抛出异常。

### prop typeArgument

```cangjie
public mut prop typeArgument: TypeNode
```

功能：获取或设置 [GenericConstraint](ast_package_classes.md#class-genericconstraint) 节点中的约束下界。

类型：[TypeNode](ast_package_classes.md#class-typenode)

### prop upperBound

```cangjie
public mut prop upperBound: Token
```

功能：获取或设置 [GenericConstraint](ast_package_classes.md#class-genericconstraint) 节点中的 `<:` 运算符。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `<:` 运算符时，抛出异常。

### prop upperBounds

```cangjie
public mut prop upperBounds: ArrayList<TypeNode>
```

功能：获取或设置 [GenericConstraint](ast_package_classes.md#class-genericconstraint) 节点约束上界的 [TypeNode](ast_package_classes.md#class-typenode) 类型节点的集合。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[TypeNode](ast_package_classes.md#class-typenode)>

### init()

```cangjie
public init()
```

功能：构造一个默认的 [GenericConstraint](ast_package_classes.md#class-genericconstraint) 对象。

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