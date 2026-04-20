## class Pattern

```cangjie
public open class Pattern <: Node
```

功能：所有模式匹配节点的父类，继承自 [Node](ast_package_classes.md#class-node) 节点。

父类型：

- [Node](#class-node)

### func dump(UInt16)

```cangjie
protected open func dump(_: UInt16): String
```

功能：将当前语法树节点转化为树形结构的形态并进行打印，需要被子类重写。

参数：

- _: [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - 格式化输出的缩进空格数量。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化输出内容。

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