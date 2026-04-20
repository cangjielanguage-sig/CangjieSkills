### operator func +(Token)

```cangjie
public operator func +(r: Token): Tokens
```

功能：使用当前 [Tokens](ast_package_classes.md#class-tokens) 与另一个 [Token](ast_package_structs.md#struct-token) 相加以获取新的 [Tokens](ast_package_classes.md#class-tokens)。

参数：

- r: [Token](ast_package_structs.md#struct-token) - 待操作的另一个 [Token](ast_package_structs.md#struct-token) 对象。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 新拼接 [Tokens](ast_package_classes.md#class-tokens) 后的词法单元集合。

### operator func +(Tokens)

```cangjie
public operator func +(r: Tokens): Tokens
```

功能：使用当前 [Tokens](ast_package_classes.md#class-tokens) 与 [Tokens](ast_package_classes.md#class-tokens) 相加以获取新的 [Tokens](ast_package_classes.md#class-tokens) 类型。

参数：

- r: [Tokens](ast_package_classes.md#class-tokens) - 待操作的一组 [Tokens](ast_package_classes.md#class-tokens) 对象。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 新拼接 [Tokens](ast_package_classes.md#class-tokens) 后的词法单元集合。

### operator func \[](Int64)

```cangjie
public operator func [](index: Int64): Token
```

功能：操作符重载，通过索引值获取对应 [Token](ast_package_structs.md#struct-token)。

参数：

- index: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 待索引的数值。

返回值：

- [Token](ast_package_structs.md#struct-token) - 返回索引对应的 [Token](ast_package_structs.md#struct-token)。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 `index` 无效时，抛出异常。

### operator func \[](Range\<Int64>)

```cangjie
public open operator func [](range: Range<Int64>): Tokens
```

功能：操作符重载，通过 `range` 获取对应 [Tokens](ast_package_classes.md#class-tokens) 切片。

参数：

- range: [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 待索引的切片范围。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 返回切片索引对应的 [Tokens](ast_package_classes.md#class-tokens)。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 `range.step` 不等于 1 时，抛出异常。
- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 range 无效时，抛出异常。