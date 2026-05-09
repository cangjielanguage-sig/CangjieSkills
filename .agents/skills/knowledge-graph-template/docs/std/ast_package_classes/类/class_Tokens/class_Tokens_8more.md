## class Tokens

```cangjie
public open class Tokens <: ToString & Iterable<Token> & ToBytes {
    public init()
    public init(tokArray: Array<Token>)
    public init(tokArrayList: ArrayList<Token>)
}
```

功能：对 [Token](ast_package_structs.md#struct-token) 序列进行封装的类型。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<[Token](ast_package_structs.md#struct-token)>
- [ToBytes](ast_package_interfaces.md#interface-tobytes)

### var tokens

```cangjie
protected var tokens: ArrayList<Token>
```

功能：获取或设置内部以[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Token](ast_package_structs.md#struct-token)>格式存储的全部[Token](ast_package_structs.md#struct-token)。

类型：[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Token](ast_package_structs.md#struct-token)>

### prop size

```cangjie
public open prop size: Int64
```

功能：获取 [Tokens](ast_package_classes.md#class-tokens) 对象中 [Token](ast_package_structs.md#struct-token) 类型的数量。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个默认的 [Tokens](ast_package_classes.md#class-tokens) 对象。

### init(Array\<Token>)

```cangjie
public init(tokArray: Array<Token>)
```

功能：构造一个 [Tokens](ast_package_classes.md#class-tokens) 对象。

参数：

- tokArray: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Token](ast_package_structs.md#struct-token)> - 一组包含 [Token](ast_package_structs.md#struct-token) 的 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt) 类型。

### init(ArrayList\<Token>)

```cangjie
public init(tokArrayList: ArrayList<Token>)
```

功能：构造一个 [Tokens](ast_package_classes.md#class-tokens) 对象。

参数：

- tokArrayList: [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<[Token](ast_package_structs.md#struct-token)> - 一组包含 [Token](ast_package_structs.md#struct-token) 的 [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt) 类型。

### func append(Node)

```cangjie
public func append(node: Node): Tokens
```

功能：将当前的 [Tokens](ast_package_classes.md#class-tokens) 与传入节点所转换得到的 [Tokens](ast_package_classes.md#class-tokens) 进行拼接。

参数：

- node: [Node](ast_package_classes.md#class-node) - 待拼接的 [Node](ast_package_classes.md#class-node) 对象。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 拼接后的 [Tokens](ast_package_classes.md#class-tokens) 类型。

### func append(Token)

```cangjie
public open func append(token: Token): Tokens
```

功能：将当前的 [Tokens](ast_package_classes.md#class-tokens) 与传入的 [Token](ast_package_structs.md#struct-token) 进行拼接。

参数：

- token: [Token](ast_package_structs.md#struct-token) - 待拼接的 [Token](ast_package_structs.md#struct-token) 对象。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 拼接后的 [Tokens](ast_package_classes.md#class-tokens) 类型。