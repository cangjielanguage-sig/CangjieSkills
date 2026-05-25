## class VArrayType

```cangjie
public class VArrayType <: TypeNode {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示 `VArray` 类型节点。

使用泛型 `VArray<T, size: Int64>` 表示 `VArray` 类型。

父类型：

- [TypeNode](#class-typenode)

### prop dollar

```cangjie
public mut prop dollar: Token
```

功能：获取或设置 [VArrayType](ast_package_classes.md#class-varraytype) 节点中的操作符 `$` 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `$` 词法单元时，抛出异常。

### prop elementTy

```cangjie
public mut prop elementTy: TypeNode
```

功能：获取或设置 [VArrayType](ast_package_classes.md#class-varraytype) 节点中的类型变元节点，如 `VArray<Int16, $0>` 中的 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16)。

类型：[TypeNode](ast_package_classes.md#class-typenode)

### prop keyword

```cangjie
public mut prop keyword: Token
```

功能：获取或设置 [VArrayType](ast_package_classes.md#class-varraytype) 节点的关键字 `VArray` 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

### prop lAngle

```cangjie
public mut prop lAngle: Token
```

功能：获取或设置 [VArrayType](ast_package_classes.md#class-varraytype) 节点左尖括号的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是左尖括号时，抛出异常。

### prop rAngle

```cangjie
public mut prop rAngle: Token
```

功能：获取或设置 [VArrayType](ast_package_classes.md#class-varraytype) 节点右尖括号的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是右尖括号时，抛出异常。

### prop size

```cangjie
public mut prop size: Token
```

功能：获取或设置 [VArrayType](ast_package_classes.md#class-varraytype) 节点中类型长度的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [VArrayType](ast_package_classes.md#class-varraytype) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [VArrayType](ast_package_classes.md#class-varraytype) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [VArrayType](ast_package_classes.md#class-varraytype) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [VArrayType](ast_package_classes.md#class-varraytype) 节点时，抛出异常。

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