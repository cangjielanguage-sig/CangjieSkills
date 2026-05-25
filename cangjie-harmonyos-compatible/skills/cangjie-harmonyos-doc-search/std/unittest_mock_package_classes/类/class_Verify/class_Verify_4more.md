## class Verify

```cangjie
public class Verify {}
```

功能：[Verify](unittest_mock_package_classes.md#class-verify) 提供了一系列静态方法来支持定义所需验证的动作，如 `that` 、 `ordered` 以及 `unorder` 。

一个验证动作可以包含多个由 `@Called` 生成的[验证语句](../unittest_mock_samples/mock_framework_verification.md#验证语句和-called-宏)，来描述需要验证的动作。
通常验证的范围为所在测试用例的函数体，但 [Verify](unittest_mock_package_classes.md#class-verify) 提供了 `clearInvocationLog` 函数来清除此前的执行记录，以缩小验证范围。
行为验证是指，验证“桩签名”的操作是否按所定义的方式执行，当验证实际执行与定义不一致时，将抛出异常。

具体支持验证的行为如下：

- 所指定的“桩签名”是否被执行。
- 所指定的“桩签名”是否执行指定的次数。
- 所指定的“桩签名”在执行时，被传入的参数是否满足要求。
- 所指定的多个“桩签名”的调用顺序是否满足要求。

行为验证主要通过以下两个步骤完成：

- 通过调用 [Verify](unittest_mock_package_classes.md#class-verify) 的静态方法定义一个验证动作。
- 通过 `@Called` 宏调用表达式定义所需验证的 “桩签名”的执行动作。为简化表达，后文将其称为“验证语句”。

举例来说：

```cangjie
let foo = mock<Foo>()
// 定义“桩签名”的“桩行为”
@On(foo.bar().returns(1))
// 实际“桩签名”在用例中的执行情况
foo.bar()
// 验证“桩签名”的执行情况：foo.bar() 至少执行了一次
Verify.that(@Called(foo.bar()))
```

值得注意的是， [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<R> 提供了一些 API ，其支持验证一些行为 。因此，用户可自由选择不同的方式进行行为验证。

### static func clearInvocationLog()

```cangjie
public static func clearInvocationLog(): Unit
```

功能：清除前序的执行记录，以缩小验证范围。

### static func noInteractions(Array\<Object>)

```cangjie
public static func noInteractions(mocks: Array<Object>): Unit
```

功能：在验证范围内，对象没有任何执行动作时，验证通过。

参数：

- mocks: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Object](../../core/core_package_api/core_package_classes.md#class-object)> - 被验证的对象列表。

异常：

- [VerificationFailedException](./unittest_mock_package_exceptions.md#class-verificationfailedexception) - 验证不通过时，抛出异常。

### static func ordered((OrderedVerifier) -> Unit)

```cangjie
public static func ordered( collectStatements: (OrderedVerifier) -> Unit): Unit
```

功能：此函数支持验证“验证语句”是否被执行或执行的次数是否符合定义，并且校验执行顺序。默认情况下，“验证语句”的执行次数为一次。
传入列表中的“验证语句”必须是不相交的（即当单个调用行为，可以匹配多个“验证语句”时，将抛出异常）。
“验证语句”通过入参中的闭包动态增加。
验证模式为 `exhaustive` (全量匹配，验证范围内的所有执行情况都应在验证动作中被指定)。

参数：

- collectStatements: ([OrderedVerifier](unittest_mock_package_classes.md#class-orderedverifier)) ->[Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 支持可动态增加“验证语句”的闭包。

异常：

- [VerificationFailedException](./unittest_mock_package_exceptions.md#class-verificationfailedexception) - 验证不通过时，抛出异常。