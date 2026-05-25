## interface ThrowingPow

```cangjie
public interface ThrowingPow {
    func throwingPow(y: UInt64): Int64
}
```

功能：提供使用抛出异常策略的幂运算接口。

### func throwingPow(UInt64)

```cangjie
func throwingPow(y: UInt64): Int64
```

功能：使用抛出异常策略的幂运算。

当运算出现溢出时，抛出异常，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 指数。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 幂运算结果。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当幂运算出现溢出时，抛出异常。