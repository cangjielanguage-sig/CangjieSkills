### func isImportAlias()

```cangjie
public func isImportAlias(): Bool
```

功能：判断 [ImportContent](ast_package_classes.md#class-importcontent) 节点是否对导入项取了别名。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - [ImportContent](ast_package_classes.md#class-importcontent) 节点是否对导入项取了别名。

### func isImportAll()

```cangjie
public func isImportAll(): Bool
```

功能：判断 [ImportContent](ast_package_classes.md#class-importcontent) 节点是否为全导入。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - [ImportContent](ast_package_classes.md#class-importcontent) 节点是否为全导入。

### func isImportMulti()

```cangjie
public func isImportMulti(): Bool
```

功能：判断 [ImportContent](ast_package_classes.md#class-importcontent) 节点是否导入了多个顶级定义或声明。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - [ImportContent](ast_package_classes.md#class-importcontent) 节点是否导入了多个顶级定义或声明。

### func isImportSingle()

```cangjie
public func isImportSingle(): Bool
```

功能：判断 [ImportContent](ast_package_classes.md#class-importcontent) 节点是否为单导入。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - [ImportContent](ast_package_classes.md#class-importcontent) 节点是否为单导入。

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