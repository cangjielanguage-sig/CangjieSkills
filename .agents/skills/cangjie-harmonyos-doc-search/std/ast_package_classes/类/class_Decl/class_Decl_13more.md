## class Decl

```cangjie
public open class Decl <: Node
```

功能：所有声明节点的父类，继承自 [Node](ast_package_classes.md#class-node) 节点，提供了所有声明节点的通用接口。

> **说明：**
>
> 类定义、接口定义、函数定义、变量定义、枚举定义、结构体定义、扩展定义、类型别名定义、宏定义等都属于 [Decl](ast_package_classes.md#class-decl) 节点。

父类型：

- [Node](#class-node)

### var identifier_

```cangjie
protected var identifier_: Token
```

功能：获取或设置声明节点的标识符，如 `class foo {}` 中的 `foo`。

类型：[Token](ast_package_structs.md#struct-token)

### var keyword_

```cangjie
protected var keyword_: Token
```

功能：获取或设置声明节点的关键字。

类型：[Token](ast_package_structs.md#struct-token)

### var modifiers_

```cangjie
protected var modifiers_: ArrayList<Modifier>
```

功能：获取或设置节点的修饰符列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Modifier](ast_package_classes.md#class-modifier)>

### var node

```cangjie
protected var node: Node
```

功能：获取或设置[Decl](ast_package_classes.md#class-decl) 节点的形参节点。

类型：[Node](ast_package_classes.md#class-node)

### prop annotations

```cangjie
public mut prop annotations: ArrayList<Annotation>
```

功能：获取或设置作用于 [Decl](ast_package_classes.md#class-decl) 节点的注解列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Annotation](ast_package_classes.md#class-annotation)>

### prop constraintCommas

```cangjie
public mut prop constraintCommas: Tokens
```

功能：获取或设置 [Decl](ast_package_classes.md#class-decl) 节点中的 "," 词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "," 词法单元序列时，抛出异常。

### prop genericConstraint

```cangjie
public mut prop genericConstraint: ArrayList<GenericConstraint>
```

功能：获取或设置声明节点的泛型约束，可能为空，如 `func foo<T>() where T <: Comparable<T> {}` 中的 `where T <: Comparable<T>`。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[GenericConstraint](ast_package_classes.md#class-genericconstraint)>

### prop genericParam

```cangjie
public mut prop genericParam: GenericParam
```

功能：获取或设置形参列表，类型形参列表由 `<>` 括起，多个类型形参之间用逗号分隔。

类型：[GenericParam](ast_package_classes.md#class-genericparam)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当节点未定义类型形参列表时，抛出异常。

### prop identifier

```cangjie
public mut open prop identifier: Token
```

功能：获取或设置声明节点的标识符，如 `class foo {}` 中的 `foo`。

类型：[Token](ast_package_structs.md#struct-token)

### prop isGenericDecl

```cangjie
public mut prop isGenericDecl: Bool
```

功能：判断是否是一个泛型节点。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是一个泛型节点为 true；反之为 false。

### prop keyword

```cangjie
public mut prop keyword: Token
```

功能：获取或设置声明节点的关键字。

类型：[Token](ast_package_structs.md#struct-token)

### prop modifiers

```cangjie
public mut prop modifiers: ArrayList<Modifier>
```

功能：获取或设置节点的修饰符列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Modifier](ast_package_classes.md#class-modifier)>