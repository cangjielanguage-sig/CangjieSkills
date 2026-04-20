## func setItem(String, Bool)

```cangjie
public func setItem(key: String, value: Bool): Unit
```

功能：内层宏通过该接口发送 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型的信息到外层宏。

> **注意：**
>
> 该函数只能作为函数被直接调用，不能作为赋值给变量，不能作为实参或返回值使用。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 发送的关键字，用于检索信息。
- value: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 要发送的 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型的信息。

## func setItem(String, Int64)

```cangjie
public func setItem(key: String, value: Int64): Unit
```

功能：内层宏通过该接口发送 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的信息到外层宏。

> **注意：**
>
> 该函数只能作为函数被直接调用，不能作为赋值给变量，不能作为实参或返回值使用。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 发送的关键字，用于检索信息。
- value: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 要发送的 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的信息。

## func setItem(String, String)

```cangjie
public func setItem(key: String, value: String): Unit
```

功能：内层宏通过该接口发送 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型的信息到外层宏。

> **注意：**
>
> 该函数只能作为函数被直接调用，不能作为赋值给变量，不能作为实参或返回值使用。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 发送的关键字，用于检索信息。
- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 要发送的 [String](../../core/core_package_api/core_package_structs.md#struct-string) 类型的信息。

## func setItem(String, Tokens)

```cangjie
public func setItem(key: String, value: Tokens): Unit
```

功能：内层宏通过该接口发送 [Tokens](ast_package_classes.md#class-tokens) 类型的信息到外层宏。

> **注意：**
>
> 该函数只能作为函数被直接调用，不能作为赋值给变量，不能作为实参或返回值使用。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 发送的关键字，用于检索信息。
- value: [Tokens](ast_package_classes.md#class-tokens) - 要发送的 [Tokens](ast_package_classes.md#class-tokens) 类型的信息。