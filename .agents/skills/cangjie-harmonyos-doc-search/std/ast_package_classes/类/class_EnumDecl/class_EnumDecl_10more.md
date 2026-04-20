## class EnumDecl

```cangjie
public class EnumDecl <: Decl {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个 `Enum` 定义节点。

Enum 的定义使用 `enum` 关键字，定义依次为：可缺省的修饰符、enum 关键字、enum 名、可选的类型参数、是否指定父接口、可选的泛型约束、enum 体的定义。

父类型：

- [Decl](#class-decl)

### prop constructors

```cangjie
public mut prop constructors: ArrayList<Constructor>
```

功能：获取或设置 [EnumDecl](ast_package_classes.md#class-enumdecl) 节点内 constructor 的成员。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Constructor](ast_package_classes.md#class-constructor)>

### prop decls

```cangjie
public mut prop decls: ArrayList<Decl>
```

功能：获取或设置 [EnumDecl](ast_package_classes.md#class-enumdecl) 节点内除 constructor 的其他成员。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Decl](ast_package_classes.md#class-decl)>

### prop ellipsis

```cangjie
public mut prop ellipsis: Token
```

功能：获取或设置 [EnumDecl](ast_package_classes.md#class-enumdecl) 节点中可选的 `...` 词法单元，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元类型。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `...` 词法单元时，抛出异常。

### prop lBrace

```cangjie
public mut prop lBrace: Token
```

功能：获取或设置 [EnumDecl](ast_package_classes.md#class-enumdecl) 节点的 `{` 词法单元类型。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `{` 词法单元类型时，抛出异常。

### prop rBrace

```cangjie
public mut prop rBrace: Token
```

功能：获取或设置 [EnumDecl](ast_package_classes.md#class-enumdecl) 节点的 `}` 词法单元类型。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `}` 词法单元类型时，抛出异常。

### prop superTypeBitAnds

```cangjie
public mut prop superTypeBitAnds: Tokens
```

功能：获取或设置 [EnumDecl](ast_package_classes.md#class-enumdecl) 节点的父接口声明中的 `&` 操作符的词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 `&` 词法单元序列时，抛出异常。

### prop superTypes

```cangjie
public mut prop superTypes: ArrayList<TypeNode>
```

功能：获取或设置 [EnumDecl](ast_package_classes.md#class-enumdecl) 节点的父接口。

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

功能：构造一个默认的 [EnumDecl](ast_package_classes.md#class-enumdecl) 对象。