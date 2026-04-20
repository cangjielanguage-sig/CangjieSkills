## interface CheckedPow

```cangjie
public interface CheckedPow {
    func checkedPow(y: UInt64): ?Int64
}
```

功能：提供返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的幂运算接口。

### func checkedPow(UInt64)

```cangjie
func checkedPow(y: UInt64): ?Int64
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的幂运算。

当运算出现溢出时，返回 ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64).None，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 指数。

返回值：

- ?[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 幂运算结果。