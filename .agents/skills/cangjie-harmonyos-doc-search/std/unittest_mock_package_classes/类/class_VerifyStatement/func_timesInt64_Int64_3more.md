### func times(Int64, Int64)

```cangjie
public func times(min!: Int64, max!: Int64): VerifyStatement
```

功能：指定此“验证语句”验证在验证范围内“桩签名”的执行次数在指定范围内。

参数：

- min!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预期验证的最小执行次数。
- max!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预期验证的最大执行次数。

返回值：

- [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 返回对象自身。

异常：

- [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) - 当对象已被指定过执行次数或已被传入过“验证动作”中时，将抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当传入的`min`或`max`参数为负数时，抛出异常。

### static func fromStub\<R>(() -> R, Array\<ArgumentMatcher>, Option\<String>, String, String, Int64)

```cangjie
public static func fromStub<R>(
    stubCall: () -> R,
    matchers: Array<ArgumentMatcher>,
    objName: Option<String>,
    declarationName: String,
    callDescription: String,
    _: Int64
): VerifyStatement
```

功能：构造一个 [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement)。框架内部使用，不建议用户直接调用。

参数：

- stubCall: () -> R - 桩签名对应的调用表达式。
- matchers: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[ArgumentMatcher](#class-argumentmatcher)> - 入参的参数匹配器。
- objName: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 被插桩的对象的名称。
- declarationName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 声明的名称。
- callDescription: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 桩签名对应的调用表达式的字符串表达。
- _: Int64 - 行号。

返回值：

- [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 返回对象自身。

### func never()

```cangjie
public func never(): VerifyStatement
```

功能：指明这条语句将永远不会被执行。

返回值：

- [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 返回对象自身。