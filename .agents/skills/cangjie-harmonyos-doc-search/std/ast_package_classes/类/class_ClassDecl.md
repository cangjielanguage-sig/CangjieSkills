## class ClassDecl

```cangjie
public class ClassDecl <: Decl {
    public init()
    public init(inputs: Tokens)
}
```

功能：类定义节点。

类的定义使用 `class` 关键字，定义依次为：可缺省的修饰符、class 关键字、class 名、可选的类型参数、是否指定父类或父接口、可选的泛型约束、类体的定义。

父类型：

- [Decl](#class-decl)

### prop body

```cangjie
public mut prop body: Body
```

功能：获取或设置 [ClassDecl](ast_package_classes.md#class-classdecl) 节点的类体。

类型：[Body](ast_package_classes.md#class-body)

### prop superTypeBitAnds

```cangjie
public mut prop superTypeBitAnds: Tokens
```

功能：获取或设置 [ClassDecl](ast_package_classes.md#class-classdecl) 节点的父类或父接口声明中的 `&` 操作符的词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 `&` 词法单元序列时，抛出异常。

### prop superTypes

```cangjie
public mut prop superTypes: ArrayList<TypeNode>
```

功能：获取或设置 [ClassDecl](ast_package_classes.md#class-classdecl) 节点的父类或者父接口。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[TypeNode](ast_package_classes.md#class-typenode)>

### prop upperBound

```cangjie
public mut prop upperBound: Token
```

功能：获取或设置 `<:` 操作符。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `<:` 操作符时，抛出异常。

### init()

```cangjie
public init()
```

功能：构造一个默认的 [ClassDecl](ast_package_classes.md#class-classdecl) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [ClassDecl](ast_package_classes.md#class-classdecl) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [ClassDecl](ast_package_classes.md#class-classdecl) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [ClassDecl](ast_package_classes.md#class-classdecl) 节点时，抛出异常。

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