## class RefType

```cangjie
public class RefType <: TypeNode {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个非基础类型节点。

例如用户通过 `class`、`struct`、`enum` 等定义的自定义类型，以及 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)、[String](../../core/core_package_api/core_package_structs.md#struct-string) 等内置类型都可以使用 [RefType](ast_package_classes.md#class-reftype) 表示。例如 `var a : A` 中的 `A`。

父类型：

- [TypeNode](#class-typenode)

### prop commas

```cangjie
public mut prop commas: Tokens
```

功能：获取或设置 [RefType](ast_package_classes.md#class-reftype) 节点中的 "," 词法单元序列，可能为空。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "," 词法单元序列时，抛出异常。

### prop identifier

```cangjie
public mut prop identifier: Token
```

功能：获取或设置构造 [RefType](ast_package_classes.md#class-reftype) 类型的关键字，如 `var a : A = A()` 中的 `A`。

类型：[Token](ast_package_structs.md#struct-token)

### prop lAngle

```cangjie
public mut prop lAngle: Token
```

功能：获取或设置 [RefType](ast_package_classes.md#class-reftype) 节点中的左尖括号词法单元，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是左尖括号时，抛出异常。

### prop rAngle

```cangjie
public mut prop rAngle: Token
```

功能：获取或设置 [RefType](ast_package_classes.md#class-reftype) 节点中的右尖括号词法单元，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是右尖括号时，抛出异常。

### prop typeArguments

```cangjie
public mut prop typeArguments: ArrayList<TypeNode>
```

功能：获取或设置 [RefType](ast_package_classes.md#class-reftype) 节点中的实例化类型的列表，可能为空，如 `var a : Array<Int32>` 中的 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32)。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[TypeNode](ast_package_classes.md#class-typenode)>

### init()

```cangjie
public init()
```

功能：构造一个默认的 [RefType](ast_package_classes.md#class-reftype) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [RefType](ast_package_classes.md#class-reftype) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [RefType](ast_package_classes.md#class-reftype) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [RefType](ast_package_classes.md#class-reftype) 节点时，抛出异常。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。