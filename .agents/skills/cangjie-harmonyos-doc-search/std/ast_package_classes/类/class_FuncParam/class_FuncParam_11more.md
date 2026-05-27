## class FuncParam

```cangjie
public open class FuncParam <: Decl {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示函数参数节点，包括非命名参数和命名参数。

一个 [FuncParam](ast_package_classes.md#class-funcparam) 节点： `func foo(a: Int64, b: Float64) {...}` 中的 `a: Int64` 和 `b: Float64`。

父类型：

- [Decl](#class-decl)

### prop assign

```cangjie
public mut prop assign: Token
```

功能：获取或设置具有默认值的函数参数中的 `=`。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `=` 时，抛出异常。

### prop colon

```cangjie
public mut prop colon: Token
```

功能：获取或设置置形参中的 ":"。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 ":" 时，抛出异常。

### prop expr

```cangjie
public mut prop expr: Expr
```

功能：获取或设置具有默认值的函数参数的变量初始化节点。

类型：[Expr](ast_package_classes.md#class-expr)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当函数参数没有进行初始化时，抛出异常。

### prop not

```cangjie
public mut prop not: Token
```

功能：获取或设置命名形参中的 `!`。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `!` 时，抛出异常。

### prop paramType

```cangjie
public mut prop paramType: TypeNode
```

功能：获取或设置函数参数的类型。

类型：[TypeNode](ast_package_classes.md#class-typenode)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [FuncParam](ast_package_classes.md#class-funcparam) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [FuncParam](ast_package_classes.md#class-funcparam) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [FuncParam](ast_package_classes.md#class-funcparam) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens))。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [FuncParam](ast_package_classes.md#class-funcparam) 节点时，抛出异常。

### func dump(UInt16)

```cangjie
protected open func dump(indent: UInt16): String
```

功能：将当前语法树节点转化为树形结构的形态并进行打印。

参数：

- indent: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 格式化输出的缩进空格数量。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化输出内容。

### func isMemberParam()

```cangjie
public func isMemberParam(): Bool
```

功能：当前的函数参数是否是主构造函数中的参数。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 布尔类型，如果是主构造函数中的参数，返回 `true`。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将当前语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。