## class QualifiedType

```cangjie
public class QualifiedType <: TypeNode {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个用户自定义成员类型。

例如 `var a : T.a` 中的 `T.a`, 其中 T 是包名，a 是从 T 包中导入的类型。

父类型：

- [TypeNode](#class-typenode)

### prop baseType

```cangjie
public mut prop baseType: TypeNode
```

功能：获取或设置 [QualifiedType](ast_package_classes.md#class-qualifiedtype) 节点的成员访问类型主体，如 `var a : T.a` 中的 `T`。

类型：[TypeNode](ast_package_classes.md#class-typenode)

### prop commas

```cangjie
public mut prop commas: Tokens
```

功能：获取或设置 [QualifiedType](ast_package_classes.md#class-qualifiedtype) 节点中的 "," 词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "," 词法单元序列时，抛出异常。

### prop dot

```cangjie
public mut prop dot: Token
```

功能：获取或设置 [QualifiedType](ast_package_classes.md#class-qualifiedtype) 节点中的 "." 。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "." 词法单元时，抛出异常。

### prop identifier

```cangjie
public mut prop identifier: Token
```

功能：获取或设置 [QualifiedType](ast_package_classes.md#class-qualifiedtype) 节点成员的标识符，如 `var a : T.a` 中的 `a`。

类型：[Token](ast_package_structs.md#struct-token)

### prop lAngle

```cangjie
public mut prop lAngle: Token
```

功能：获取或设置 [QualifiedType](ast_package_classes.md#class-qualifiedtype) 节点中的左尖括号词法单元，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是左尖括号时，抛出异常。

### prop rAngle

```cangjie
public mut prop rAngle: Token
```

功能：获取或设置 [QualifiedType](ast_package_classes.md#class-qualifiedtype) 节点中的右尖括号词法单元，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是右尖括号时，抛出异常。

### prop typeArguments

```cangjie
public mut prop typeArguments: ArrayList<TypeNode>
```

功能：获取或设置 [QualifiedType](ast_package_classes.md#class-qualifiedtype) 节点中的实例化类型的列表，如 `T.a<Int32>` 中的 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32)，列表可能为空。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[TypeNode](ast_package_classes.md#class-typenode)>

### init()

```cangjie
public init()
```

功能：构造一个默认的 [QualifiedType](ast_package_classes.md#class-qualifiedtype) 对象。