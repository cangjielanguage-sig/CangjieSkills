### func times(Int64, Int64)

```cangjie
func times(min!: Int64, max!: Int64): Unit
```

功能：定义“桩行为”执行指定次数范围。验证超出指定次数范围时，抛出异常。

参数：

- min!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预期“桩行为”被执行的最小次数。
- max!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 预期“桩行为”被执行的最大次数。

异常：

- [ExceptionFailedException](./unittest_mock_package_exceptions.md#class-expectationfailedexception) - 验证“桩行为”执行次数不是指定次数范围时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当传入的`min`或`max`参数为负数时，抛出异常。