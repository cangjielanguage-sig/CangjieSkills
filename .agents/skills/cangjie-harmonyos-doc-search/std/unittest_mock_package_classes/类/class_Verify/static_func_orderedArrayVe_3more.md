### static func ordered(Array\<VerifyStatement>)

```cangjie
public static func ordered(statements: Array<VerifyStatement>): Unit
```

功能：此函数支持验证“验证语句”是否被执行或执行的次数是否符合定义，并且校验执行顺序。默认情况下，“验证语句”的执行次数为一次。
传入列表中的“验证语句”必须是不相交的（即当单个调用行为，可以匹配多个“验证语句”时，将抛出异常）。
验证模式为 `exhaustive` (全量匹配，验证范围内的所有执行情况都应在验证动作中被指定)。

举例来说:

```cangjie
for (i in 0..4) {
    foo.bar(i % 2)
}

Verify.ordered(
    @Called(foo.bar(0)),
    @Called(foo.bar(1)),
    @Called(foo.bar(0)),
    @Called(foo.bar(1)),
)

// 将抛出异常，验证范围内有 4 次 foo.bar() 表达式的执行动作，此处只验证了2次执行。
Verify.ordered(
    @Called(foo.bar(0)),
    @Called(foo.bar(_)),
)
```

参数：

- statements: Array\<[VerifyStatement](unittest_mock_package_classes.md#class-verifystatement)> - 所需验证的“验证语句”。

异常：

- [VerificationFailedException](./unittest_mock_package_exceptions.md#class-verificationfailedexception) - 验证不通过时，将抛出异常。

### static func that(VerifyStatement)

```cangjie
public static func that(statement: VerifyStatement): Unit
```

功能：验证是否正确执行了传入的单个“验证语句”。

参数：

- statement: [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 所需验证的“验证语句”。

异常：

- [VerificationFailedException](./unittest_mock_package_exceptions.md#class-verificationfailedexception) - 验证不通过时，将抛出异常。

### static func unordered((UnorderedVerifier) -> Unit)

```cangjie
public static func unordered(collectStatements: (UnorderedVerifier) -> Unit): Unit
```

功能：此函数支持验证“验证语句”是否被执行或执行的次数是否符合定义，并且不校验执行顺序。默认情况下，“验证语句”的执行次数为至少一次。
传入列表中的“验证语句”必须是不相交的（即当单个调用行为，可以匹配多个“验证语句”时，将抛出异常）。
验证模式为 `exhaustive` (全量匹配，验证范围内的所有执行情况都应在验证动作中被指定)。
“验证语句”通过入参中的闭包动态增加。举例来说：

```cangjie

let totalTimes = getTimes()
for (i in 0..totalTimes) {
    foo.bar(i % 2)
}
// 通过闭包使得“验证语句”可以通过 totalTimes 的值确定内容
Verify.unordered { v =>
    for (j in 0..totalTimes) {
        v.checkThat(@Called(foo.bar(eq(j % 2))))
    }
}
```

参数：

- collectStatements: ([UnorderedVerifier](unittest_mock_package_classes.md#class-unorderedverifier)) ->[Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 支持可动态增加“验证语句”的闭包。

异常：

- [VerificationFailedException](./unittest_mock_package_exceptions.md#class-verificationfailedexception) - 验证不通过时，抛出异常。