## class Modifier

```cangjie
public class Modifier <: Node {
    public init()
    public init(keyword: Token)
}
```

功能：表示该定义具备某些特性，通常放在定义处的最前端。

一个 [Modifier](ast_package_classes.md#class-modifier) 节点：`public func foo()` 中的 `public`。

父类型：

- [Node](#class-node)

### prop keyword(Token)

```cangjie
public mut prop keyword: Token
```

功能：获取或设置 [Modifier](ast_package_classes.md#class-modifier) 节点中的修饰符词法单元。

类型：[Token](ast_package_structs.md#struct-token)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Modifier](ast_package_classes.md#class-modifier) 对象。

### init(Token)

```cangjie
public init(keyword: Token)
```

功能：构造一个 [Modifier](ast_package_classes.md#class-modifier) 对象。

参数：

- keyword: [Token](ast_package_structs.md#struct-token) - 将要构造 [Modifier](ast_package_classes.md#class-modifier) 类型的词法单元。

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

## class Node

```cangjie
abstract sealed class Node <: ToTokens
```

功能：所有仓颉语法树节点的父类。

该类提供了所有数据类型通用的操作接口。

父类型：

- [ToTokens](ast_package_interfaces.md#interface-totokens)

### prop beginPos

```cangjie
public mut prop beginPos: Position
```

功能：获取或设置当前节点的起始的位置信息。

类型：[Position](ast_package_structs.md#struct-position)

### prop endPos

```cangjie
public mut prop endPos: Position
```

功能：获取或设置当前节点的终止的位置信息。

类型：[Position](ast_package_structs.md#struct-position)

### func dump()

```cangjie
public func dump(): Unit
```

功能：将当前语法树节点转化为树形结构的形态并进行打印。

语法树节点的树形结构将按照以下形式进行输出：

- `-` 字符串：表示当前节点的公共属性， 如 `-keyword` , `-identifier`。
- 节点属性后紧跟该节点的具体类型， 如 `-declType: PrimitiveType` 表示节点类型是一个 [PrimitiveType](ast_package_classes.md#class-primitivetype) 节点。
- 每个类型使用大括号表示类型的作用区间。

语法树输出的详细格式请参见[语法树节点打印](../ast_samples/dump.md)。

### func toTokens()

```cangjie
public func toTokens(): Tokens
```

功能：将语法树节点转化为 [Tokens](ast_package_classes.md#class-tokens) 类型。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 转化后的 [Tokens](ast_package_classes.md#class-tokens) 类型节点。

### func traverse(Visitor)

```cangjie
public func traverse(v: Visitor): Unit
```

功能：遍历当前语法树节点及其子节点。若提前终止遍历子节点的行为，可重写 `visit` 函数并调用 `breakTraverse` 函数提前终止遍历行为，请参见[自定义访问函数遍历 AST 对象示例](../ast_samples/traverse.md)。

参数：

- v: [Visitor](ast_package_classes.md#class-visitor) - [Visitor](ast_package_classes.md#class-visitor) 类型的实例。