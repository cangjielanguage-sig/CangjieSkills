### func dump(UInt16)

```cangjie
protected open func dump(indent: UInt16): String
```

功能：将当前语法树节点转化为树形结构的形态并进行打印。语法树节点的树形结构将按照以下形式进行输出：

- `-` 字符串：表示当前节点的公共属性， 如 `-keyword` , `-identifier`。
- 节点属性后紧跟该节点的具体类型， 如 `-declType: PrimitiveType` 表示节点类型是一个 [PrimitiveType](ast_package_classes.md#class-primitivetype) 节点。
- 每个类型使用大括号表示类型的作用区间。

语法树输出的详细格式请参见[语法树节点打印](../ast_samples/dump.md)。

参数：

- indent: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 格式化输出的缩进空格数量。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化输出内容。

### func getAttrs()

```cangjie
public func getAttrs(): Tokens
```

功能：获取当前节点的属性（一般通过内置的 `Attribute` 来设置某个声明设置属性值）。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 当前节点的属性。

### func hasAttr(String)

```cangjie
public func hasAttr(attr: String): Bool
```

功能：判断当前节点是否具有某个属性（一般通过内置的 `Attribute` 来设置某个声明的属性值）。

参数：

- attr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将要判断是否存在于该节点的属性。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当前节点具有该属性时，返回 true；反之，返回 false。

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