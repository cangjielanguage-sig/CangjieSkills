## class MacroMessage

```cangjie
public class MacroMessage
```

功能：记录内层宏发送的信息。

### func getBool(String)

```cangjie
public func getBool(key: String): Bool
```

功能：获取对应 key 值的 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型信息。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于检索的关键字的名字。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 返回存在 key 值对应的 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型的信息。

异常：

- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 当不存在 key 值对应的 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型的信息时，抛出异常。

### func getInt64(String)

```cangjie
public func getInt64(key: String): Int64
```

功能：获取对应 key 值的 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型信息。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于检索的关键字的名字。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 返回存在 key 值对应的 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的信息。

异常：

- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 当不存在 key 值对应的 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的信息时，抛出异常。

### func getString(String)

```cangjie
public func getString(key: String): String
```

功能：获取对应 key 值的 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型信息。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于检索的关键字的名字。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 返回存在 key 值对应的 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型的信息。

异常：

- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 当不存在 key 值对应的 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型的信息时，抛出异常。

### func getTokens(String)

```cangjie
public func getTokens(key: String): Tokens
```

功能：获取对应 key 值的 [Tokens](ast_package_classes.md#class-tokens) 类型信息。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于检索的关键字的名字。

返回值：

- [Tokens](ast_package_classes.md#class-tokens) - 返回存在 key 值对应的 [Tokens](ast_package_classes.md#class-tokens) 类型的信息。

异常：

- [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 当不存在 key 值对应的 [Tokens](ast_package_classes.md#class-tokens) 类型的信息时，抛出异常。

### func hasItem(String)

```cangjie
public func hasItem(key: String): Bool
```

功能：检查是否有 key 值对应的相关信息。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 用于检索的关键字名字。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 若存在 key 值对应的相关信息，返回 true；反之，返回 false。