## func assertCaughtUnexpectedE(String, String, String, ?AssertionCtx)

```cangjie
public func assertCaughtUnexpectedE(
    message: String,
    expectedExceptions: String,
    caughtException: String,
    optParentCtx!: ?AssertionCtx = None
): Nothing
```

功能：捕获的异常不符合预期，记录信息，抛出异常。

参数：

- message: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 不符合预期时的提示信息。
- expectedExceptions: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 期望的捕获的异常。
- caughtException: [String](../../core/core_package_api/core_package_structs.md#struct-string)  - 实际捕获的异常。
- optParentCtx!: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[AssertionCtx](./unittest_package_classes.md#class-assertionctx)> - 存储嵌套断言失败消息的上下文。

## func assertEqual\<T>(String, String, T, T, ?AssertionCtx)

```cangjie
public func assertEqual<T>(
    leftStr: String,
    rightStr: String,
    expected: T,
    actual: T,
    optParentCtx!: ?AssertionCtx = None
): Unit where T <: Equatable<T>
```

功能：比较 `expected` 和 `actual` 值是否相等。若不等，直接抛出异常。

参数：

- leftStr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 期望的表达式的字符串。
- rightStr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 实际的表达式的字符串。
- expected: T - 期望的值。
- actual: T - 实际值。
- optParentCtx!: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[AssertionCtx](./unittest_package_classes.md#class-assertionctx)> - 存储嵌套断言失败消息的上下文。

## func assertEqual\<T>(String, String, T, T, Bool, ?AssertionCtx)

```cangjie
public func assertEqual<T>(
    leftStr: String,
    rightStr: String,
    expected: T,
    actual: T,
    isDelta!: Bool = false,
    optParentCtx!: ?AssertionCtx = None
): Unit where T <: Equatable<T>
```

功能：比较 `expected` 和 `actual` 值是否相等。若不等，直接抛出异常。

参数：

- leftStr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 期望的表达式的字符串。
- rightStr: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 实际的表达式的字符串。
- expected: T - 期望的值。
- actual: T - 实际值。
- isDelta!: Bool - 是否使用近似相等。默认不使能。
- optParentCtx!: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[AssertionCtx](./unittest_package_classes.md#class-assertionctx)> - 存储嵌套断言失败消息的上下文。

## func defaultConfiguration()

```cangjie
public func defaultConfiguration(): Configuration
```

功能：生成默认的配置信息。

返回值：

- [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) - 配置信息。

## func entryMain(TestPackage)

```cangjie
public func entryMain(testPackage: TestPackage): Int64
```

功能：提供给 `cjc --test` 使用，框架执行测试用例的入口函数。

参数：

- testPackage: [TestPackage](./unittest_package_classes.md#class-testpackage) - 测试包对象。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 执行结果。