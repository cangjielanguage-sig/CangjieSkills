## class CardinalitySelector\<A>

```cangjie
public class CardinalitySelector<A> where A <: ActionSelector {}
```

功能：此类提供了可定义桩签名的最近一次行为的执行次数的 API 。
例如：`@On(foo.bar()).returns("Predefined value").atLeastOnce()` 。
为方便表达，后文将桩签名的最近一次行为称为“桩行为”。
此接口提供的 API 提供的验证能力如下：

- 桩签名的调用次数超过指定次数将立即抛出 [ExpectationFailedException](./unittest_mock_package_exceptions.md#class-expectationfailedexception) 。
- 桩签名的调用次数不足时，框架将在测试用例执行完成后抛出 [ExceptionFailedException](./unittest_mock_package_exceptions.md#class-expectationfailedexception) 。

### func anyTimes()

```cangjie
func anyTimes(): Unit
```

功能：定义“桩行为”可以执行任意次数。此函数对桩签名的调用次数不做任何校验。

### func atLeastOnce()

```cangjie
func atLeastOnce(): Unit
```

功能：定义“桩行为”最少被执行一次。验证不到一次时，抛出异常。

异常：

- [ExceptionFailedException](./unittest_mock_package_exceptions.md#class-expectationfailedexception) - 验证“桩行为”执行次数不到一次时，抛出异常。

### func atLeastTimes(Int64)

```cangjie
func atLeastTimes(minTimesExpected: Int64): Unit
```

功能：定义“桩行为”最少被执行指定次数的行为。验证实际执行次数低于最少指定次数时，抛出异常。

参数：

- minTimesExpected: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预期“桩行为”最少被执行的次数。

异常：

- [ExceptionFailedException](./unittest_mock_package_exceptions.md#class-expectationfailedexception) - 验证“桩行为”执行少于指定次数时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当作为`minTimesExpected`参数传递的数字为负数时，抛出异常。

### func once()

```cangjie
func once(): Continuation<A>
```

功能：定义“桩行为”仅被执行一次。此函数将在验证桩签名执行次数超出一次时，抛出异常。

返回值：

- [Continuation](#class-continuationa)\<A> - 对象实例可调用方法继续生成 [ActionSelector](#class-actionselector) 对象。

异常：

- [ExceptionFailedException](./unittest_mock_package_exceptions.md#class-expectationfailedexception) - 验证“桩行为”执行次数超过一次时，立即抛出异常。

### func times(Int64)

```cangjie
func times(expectedTimes: Int64): Continuation<A>
```

功能：定义“桩行为”被执行指定次数。验证不是指定次数时，抛出异常。

参数：

- expectedTimes: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预期“桩行为”被执行的次数。

返回值：

- [Continuation](#class-continuationa)\<A> - 对象实例可调用方法继续生成 [ActionSelector](#class-actionselector) 对象。

异常：

- [ExceptionFailedException](./unittest_mock_package_exceptions.md#class-expectationfailedexception) - 验证“桩行为”执行次数不是指定次数时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当作为`expectedTimes`参数传递的数字为负数时，抛出异常。