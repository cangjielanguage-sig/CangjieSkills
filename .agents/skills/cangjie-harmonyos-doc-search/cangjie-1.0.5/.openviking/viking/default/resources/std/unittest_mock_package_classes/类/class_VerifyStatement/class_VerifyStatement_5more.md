## class VerifyStatement

```cangjie
public class VerifyStatement {}
```

功能：此类型表示对“桩签名”在验证范围内的单个验证验证语句（即上文中的“验证语句”），提供了成员函数指定“桩签名”的执行次数。
该类型的对象仅可通过 `@Called` 宏调用表达式创建。
对一个对象连续调用多个成员函数没有意义，并且会抛出异常。即，执行次数仅可被指定一次。
当未调用成员函数指定执行次数时，将基于语句所在的验证动作类型定义默认的执行次数验证值。例如在 [Verify](unittest_mock_package_classes.md#class-verify).ordered() 中的“验证语句”默认为验证执行一次。

### func atLeastOnce()

```cangjie
public func atLeastOnce(): VerifyStatement
```

功能：指定此“验证语句”验证在验证范围内“桩签名”最少被执行一次。

返回值：

- [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 返回对象自身。

异常：

- [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) - 当对象已被指定过执行次数或已被传入过“验证动作”中时，将抛出异常。

### func atLeastTimes(Int64)

```cangjie
public func atLeastTimes(minTimesExpected: Int64): VerifyStatement
```

功能：指定此“验证语句”验证在验证范围内“桩签名”最少执行指定的次数。

参数：

- minTimesExpected: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预期验证的执行最少次数。

返回值：

- [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 返回对象自身。

异常：

- [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) - 当对象已被指定过执行次数或已被传入过“验证动作”中时，将抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当作为`minTimesExpected`参数传递的数字为负数时，抛出异常。

### func once()

```cangjie
public func once(): VerifyStatement
```

功能：指定此“验证语句”验证在验证范围内“桩签名”仅被执行一次。

返回值：

- [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 返回对象自身。

异常：

- [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) - 当对象已被指定过执行次数或已被传入过“验证动作”中时，将抛出异常。

### func times(Int64)

```cangjie
public func times(expectedTimes: Int64): VerifyStatement
```

功能：指定此“验证语句”验证在验证范围内“桩签名”被执行指定次数。

参数：

- expectedTimes: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预期验证的执行次数。

返回值：

- [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 返回对象自身。

异常：

- [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) - 当对象已被指定过执行次数或已被传入过“验证动作”中时，将抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当作为`expectedTimes`参数传递的数字为负数时，抛出异常。