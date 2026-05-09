### func append(Tokens)

```cangjie
public open func append(tokens: Tokens): Tokens
```

功能：在当前的 [Tokens](ast_package_classes.md#class-tokens) 后追加传入的 [Tokens](ast_package_classes.md#class-tokens) 进行拼接（该接口性能较其他拼接函数表现更好）。

参数：

- tokens: [Tokens](ast_package_classes.md#class-tokens) - 待拼接的 [Tokens](ast_package_classes.md#class-tokens) 对象。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 拼接后的 [Tokens](ast_package_classes.md#class-tokens) 类型。

### func concat(Tokens)

```cangjie
public func concat(tokens: Tokens): Tokens
```

功能：将当前的 [Tokens](ast_package_classes.md#class-tokens) 与传入的 [Tokens](ast_package_classes.md#class-tokens) 进行拼接。

参数：

- tokens: [Tokens](ast_package_classes.md#class-tokens) - 待拼接的 [Tokens](ast_package_classes.md#class-tokens) 对象。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 拼接后的 [Tokens](ast_package_classes.md#class-tokens)。

### func dump()

```cangjie
public func dump(): Unit
```

功能：将 [Tokens](ast_package_classes.md#class-tokens) 内所有 [Token](ast_package_structs.md#struct-token) 的信息打印出来。

### func get(Int64)

```cangjie
public open func get(index: Int64): Token
```

功能：通过索引值获取 [Token](ast_package_structs.md#struct-token) 元素。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 待索引的数值。

返回值：

- [Token](ast_package_structs.md#struct-token) - 指定索引的 [Token](ast_package_structs.md#struct-token)。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 `index` 无效时，抛出异常。

### func iterator()

```cangjie
public func iterator(): TokensIterator
```

功能：获取 [Tokens](ast_package_classes.md#class-tokens) 对象中的一个迭代器对象。

返回值：

- [TokensIterator](ast_package_classes.md#class-tokensiterator) - [Tokens](ast_package_classes.md#class-tokens) 对象的迭代器对象。

### func remove(Int64)

```cangjie
public func remove(index: Int64): Tokens
```

功能：删除指定位置的 [Token](ast_package_structs.md#struct-token) 对象。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 被删除的 [Token](ast_package_structs.md#struct-token) 的索引。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 删除指定位置的 [Token](ast_package_structs.md#struct-token) 后的 [Tokens](ast_package_classes.md#class-tokens) 对象。

### func toBytes()

```cangjie
public func toBytes(): Array<UInt8>
```

功能：Tokens 类型的序列化。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)> - 序列化后的字节序列。

### func toString()

```cangjie
public func toString(): String
```

功能：将 [Tokens](ast_package_classes.md#class-tokens) 转化为 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转化后的字符串。