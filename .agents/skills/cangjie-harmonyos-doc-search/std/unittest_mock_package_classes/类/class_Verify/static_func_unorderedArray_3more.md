### static func unordered(Array\<VerifyStatement>)

```cangjie
public static func unordered(statements: Array<VerifyStatement>): Unit
```

功能：此函数支持验证“验证语句”是否被执行或执行的次数是否符合定义，并且不校验执行顺序。默认情况下，“验证语句”的执行次数为至少一次。
传入列表中的“验证语句”必须是不相交的（即当单个调用行为，可以匹配多个“验证语句”时，将抛出异常）。
验证模式为 `exhaustive` (全量匹配，验证范围内的所有执行情况都应在验证动作中被指定)。

举例来说:

```cangjie
let foo = mock<Foo>()
for (i in 0..4) {
    foo.bar(i % 2)
}

// 验证 bar() 在传入参数为 0 或 1 的情况下均至少执行一次
Verify.unordered(
    @Called(foo.bar(0)),
    @Called(foo.bar(1))
)

// 此处的验证动作将抛出异常，因为 `foo.bar(_)` 包含了 `foo.bar(1)`
Verify.unordered(
    @Called(foo.bar(_)).times(2),
    @Called(foo.bar(1)).times(2)
)
// 可以通过如下方式进行验证
// 验证入参为 1 的调用表达式执行了2次
Verify.that(@Called(foo.bar(1)).times(2))
// 验证任意入参的调用表达式执行了2次
Verify.that(@Called(foo.bar(_)).times(2)) // called four times in total
```

参数：

- statements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[VerifyStatement](unittest_mock_package_classes.md#class-verifystatement)> - 待验证的多条“验证语句”，变长参数语法支持参数省略 `[]` 。

异常：

- [VerificationFailedException](./unittest_mock_package_exceptions.md#class-verificationfailedexception) - 验证不通过时，抛出异常。

### static func unordered(Exhaustiveness, (UnorderedVerifier) -> Unit)

```cangjie
public static func unordered(exhaustive: Exhaustiveness, collectStatements: (UnorderedVerifier) -> Unit): Unit
```

功能：此函数支持验证“验证语句”是否被执行或执行的次数是否符合定义，并且不校验执行顺序。默认情况下，“验证语句”的执行次数为至少一次。
传入列表中的“验证语句”必须是不相交的（即当单个调用行为，可以匹配多个“验证语句”时，将抛出异常）。
“验证语句”通过入参中的闭包动态增加。

参数：

- collectStatements: ([UnorderedVerifier](unittest_mock_package_classes.md#class-unorderedverifier)) ->[Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 支持可动态增加“验证语句”的闭包。
- exhaustive: [Exhaustiveness](unittest_mock_package_enums.md#enum-exhaustiveness) - 验证模式。

异常：

- [VerificationFailedException](./unittest_mock_package_exceptions.md#class-verificationfailedexception) - 验证不通过时，抛出异常。

### static func unordered(Exhaustiveness, Array\<VerifyStatement>)

```cangjie
public static func unordered(exhaustive: Exhaustiveness, statements: Array<VerifyStatement>): Unit
```

功能：此函数支持验证“验证语句”是否被执行或执行的次数是否符合定义，并且不校验执行顺序。默认情况下，“验证语句”的执行次数为至少一次。
传入列表中的“验证语句”必须是不相交的（即当单个调用行为，可以匹配多个“验证语句”时，将抛出异常）。

参数：

- statements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[VerifyStatement](unittest_mock_package_classes.md#class-verifystatement)> - 待验证的多条“验证语句”，变长参数语法支持参数省略 `[]` 。
- exhaustive: [Exhaustiveness](unittest_mock_package_enums.md#enum-exhaustiveness) - 验证模式。

异常：

- [VerificationFailedException](./unittest_mock_package_exceptions.md#class-verificationfailedexception) - 验证不通过时，抛出异常。