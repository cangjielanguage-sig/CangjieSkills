## class PackageHeader

```cangjie
public class PackageHeader <: Node {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示包声明节点。

一个 [PackageHeader](ast_package_classes.md#class-packageheader) 节点: `package define` 或者 `macro package define`。

> **说明：**
>
> 包声明以关键字 `package` 或 `macro package` 开头，后面紧跟包名，且包声明必须在源文件的首行。

父类型：

- [Node](#class-node)

### prop accessible

```cangjie
public mut prop accessible: Token
```

功能：获取或设置 [PackageHeader](ast_package_classes.md#class-packageheader) 节点中的访问性修饰符的词法单元，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

### prop keywordM

```cangjie
public mut prop keywordM: Token
```

功能：获取或设置 [PackageHeader](ast_package_classes.md#class-packageheader) 节点中的 `macro` 关键字的词法单元（`M` 为关键字首字母，下同），可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `macro` 关键字时，抛出异常。

### prop keywordP

```cangjie
public mut prop keywordP: Token
```

功能：获取或设置 [PackageHeader](ast_package_classes.md#class-packageheader) 节点中的 `package` 关键字的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Token](ast_package_structs.md#struct-token) 不是 `package` 关键字时，抛出异常。

### prop prefixPaths

```cangjie
public mut prop prefixPaths: Tokens
```

功能：获取或设置 [PackageHeader](ast_package_classes.md#class-packageheader) 节点中完整包名的前缀部分的词法单元序列，可能为空。如 `package a.b.c` 中的 `a` 和 `b`。

类型：[Tokens](ast_package_classes.md#class-tokens)

### prop prefixDots

```cangjie
public mut prop prefixDots: Tokens
```

功能：获取或设置 [PackageHeader](ast_package_classes.md#class-packageheader) 节点中完整包名中用于分隔每层子包的词法单元序列，可能为空。如 `package a.b.c` 中的两个 "."。

类型：[Tokens](ast_package_classes.md#class-tokens)

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当设置的 [Tokens](ast_package_classes.md#class-tokens) 不是 "." 词法单元序列时，抛出异常。

### prop packageIdentifier

```cangjie
public mut prop packageIdentifier: Token
```

功能：获取或设置 [PackageHeader](ast_package_classes.md#class-packageheader) 节点中当前包的名字，如果当前包为 root 包，即为完整包名，若当前包为子包，则为最后一个 "." 后的名字。

类型：[Token](ast_package_structs.md#struct-token)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [PackageHeader](ast_package_classes.md#class-packageheader) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [PackageHeader](ast_package_classes.md#class-packageheader) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [PackageHeader](ast_package_classes.md#class-packageheader) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens)) 序列。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [PackageHeader](ast_package_classes.md#class-packageheader) 节点时，抛出异常。