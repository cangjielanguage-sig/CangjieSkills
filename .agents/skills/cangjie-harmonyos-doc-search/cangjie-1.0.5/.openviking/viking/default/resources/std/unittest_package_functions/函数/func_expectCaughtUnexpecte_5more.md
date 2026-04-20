## func expectCaughtUnexpectedE(String, String, String, ?AssertionCtx)

```cangjie
public func expectCaughtUnexpectedE(
    message: String,
    expectedExceptions: String,
    caughtException: String,
    optParentCtx!: ?AssertionCtx = None
): Unit
```

功能：捕获的异常不符合预期，记录信息，不抛出异常。

参数：

- message: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 不符合预期时的提示信息。
- expectedExceptions: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 期望的捕获的异常。
- caughtException: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 实际捕获的异常。
- optParentCtx!: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[AssertionCtx](./unittest_package_classes.md#class-assertionctx)> - 存储嵌套断言失败消息的上下文。

## func expectEqual\<T>(String, String, T, T, ?AssertionCtx)

```cangjie
public func expectEqual<T>(
    leftStr: String,
    rightStr: String,
    expected: T,
    actual: T,
    optParentCtx!: ?AssertionCtx
): Unit where T <: Equatable<T>
```

功能：比较 `expected` 和 `actual` 值是否相等。记录比较结果，不抛出异常。

参数：

- leftStr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 期望的表达式的字符串。
- rightStr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 实际的表达式的字符串。
- expected: T - 期望的值。
- actual: T  - 实际值。
- optParentCtx!: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[AssertionCtx](./unittest_package_classes.md#class-assertionctx)> - 存储嵌套断言失败消息的上下文。

## func expectEqual\<T>(String, String, T, T, Bool, ?AssertionCtx)

```cangjie
public func expectEqual<T>(
    leftStr: String,
    rightStr: String,
    expected: T,
    actual: T,
    isDelta!: Bool = false,
    optParentCtx!: ?AssertionCtx
): Unit where T <: Equatable<T>
```

功能：比较 `expected` 和 `actual` 值是否相等。记录比较结果，不抛出异常。

参数：

- leftStr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 期望的表达式的字符串。
- rightStr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 实际的表达式的字符串。
- expected: T - 期望的值。
- actual: T  - 实际值。
- isDelta!: Bool - 是否使用近似相等。默认不使能。
- optParentCtx!: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[AssertionCtx](./unittest_package_classes.md#class-assertionctx)> - 存储嵌套断言失败消息的上下文。

## func fail(String)

```cangjie
public func fail(message: String): Nothing
```

功能：使该用例失败，直接抛出异常。

参数：

- message: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 失败信息。

## func failExpect(String)

```cangjie
public func failExpect(message: String): Unit
```

功能：使该用例失败，记录信息，不抛出异常。

参数：

- message: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 失败信息。