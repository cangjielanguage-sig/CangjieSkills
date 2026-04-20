## class ImportList

```cangjie
public class ImportList <: Node {
    public init()
    public init(inputs: Tokens)
}
```

功能：表示包导入节点。

一个 [ImportList](ast_package_classes.md#class-importlist) 节点: `import moduleName.packageName.foo as bar`。

> **说明：**
>
> 导入节点以可选的访问性修饰符（`public/protected/internal/private`）加关键字 `import` 开头。以 `import pkga.pkgb.item` 为例，`pkga.pkgb` 为导入的顶级定义或声明所在的包的名字，`item` 为导入的顶级定义或声明。

父类型：

- [Node](#class-node)

### prop content

```cangjie
public mut prop content: ImportContent
```

功能：获取或设置 [ImportList](ast_package_classes.md#class-importlist) 节点中的被导入的具体项。如 `import a.b.c` 中的 `a.b.c` 部分。

类型：[ImportContent](ast_package_classes.md#class-importcontent)

### prop keywordI

```cangjie
public mut prop keywordI: Token
```

功能：获取或设置 [ImportList](ast_package_classes.md#class-importlist) 节点中的 `import` 关键字的词法单元，`I` 为关键字首字母。

类型：[Token](ast_package_structs.md#struct-token)

### prop modifier

```cangjie
public mut prop modifier: Token
```

功能：获取或设置 [ImportList](ast_package_classes.md#class-importlist) 节点中的修饰符，可能为 [ILLEGAL](ast_package_enums.md#illegal) 的词法单元。

类型：[Token](ast_package_structs.md#struct-token)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [ImportList](ast_package_classes.md#class-importlist) 对象。

### init(Tokens)

```cangjie
public init(inputs: Tokens)
```

功能：构造一个 [ImportList](ast_package_classes.md#class-importlist) 对象。

参数：

- inputs: [Tokens](ast_package_classes.md#class-tokens) - 将要构造 [ImportList](ast_package_classes.md#class-importlist) 类型的词法单元集合 ([Tokens](ast_package_classes.md#class-tokens)) 序列。

异常：

- [ASTException](ast_package_exceptions.md#class-astexception) - 当输入的 [Tokens](ast_package_classes.md#class-tokens) 类型无法构造为 [ImportList](ast_package_classes.md#class-importlist) 节点时，抛出异常。

### func isImportMulti()

```cangjie
public func isImportMulti(): Bool
```

功能：判断 [ImportList](ast_package_classes.md#class-importlist) 节点是否导入了多个顶级定义或声明。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果 [ImportList](ast_package_classes.md#class-importlist) 节点导入了多个顶级定义或声明，返回 true；反之，返回 false。

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