## class Program

```cangjie
public class Program <: Node {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示一个仓颉源码文件节点。

一个仓颉源码文件节点主要包括包定义节点，包导入节点和 TopLevel 作用域内的所有声明节点。

> **说明：**
>
> 任何一个仓颉源码文件都可以被解析为一个 [Program](ast_package_classes.md#class-program) 类型。

父类型：

- [Node](#class-node)

### prop decls

```cangjie
public mut prop decls: ArrayList<Decl>
```

功能：获取或设置仓颉源码文件中 TopLevel 作用域内定义的声明节点列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Decl](ast_package_classes.md#class-decl)>

### prop importLists

```cangjie
public mut prop importLists: ArrayList<ImportList>
```

功能：获取或设置仓颉源码文件中包导入节点 [ImportList](ast_package_classes.md#class-importlist) 的列表。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[ImportList](ast_package_classes.md#class-importlist)>

### prop packageHeader

```cangjie
public mut prop packageHeader: PackageHeader
```

功能：获取或设置仓颉源码文件中包的声明节点 [PackageHeader](ast_package_classes.md#class-packageheader)。

类型：[PackageHeader](ast_package_classes.md#class-packageheader)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Program](ast_package_classes.md#class-program) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [Program](ast_package_classes.md#class-program) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [Program](ast_package_classes.md#class-program) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens)) 序列。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为一个文件节点时，抛出异常。

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