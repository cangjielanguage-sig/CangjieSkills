## interface CheckedOp\<T>

```cangjie
public interface CheckedOp<T> {
    func checkedAdd(y: T): ?T
    func checkedDec(): ?T
    func checkedDiv(y: T): ?T
    func checkedInc(): ?T
    func checkedMod(y: T): ?T
    func checkedMul(y: T): ?T
    func checkedNeg(): ?T
    func checkedShl(y: UInt64): ?T
    func checkedShr(y: UInt64): ?T
    func checkedSub(y: T): ?T
}
```

功能：当整数运算出现溢出，返回 `None`。

### func checkedAdd(T)

```cangjie
func checkedAdd(y: T): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的加法运算。

当运算出现溢出时，返回 `?T.None`，否则返回运算结果。

参数：

- y: T - 加数。

返回值：

- ?T - 加法运算结果。

### func checkedDec()

```cangjie
func checkedDec(): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自减运算。

当运算出现溢出时，返回 `?T.None`，否则返回运算结果。

返回值：

- ?T - 自减运算结果。

### func checkedDiv(T)

```cangjie
func checkedDiv(y: T): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的除法运算。

当运算出现溢出时，返回 `?T.None`，否则返回运算结果。

参数：

- y: T - 除数。

返回值：

- ?T - 除法运算结果。

### func checkedInc()

```cangjie
func checkedInc(): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的自增运算。

当运算出现溢出时，返回 `?T.None`，否则返回运算结果。

返回值：

- ?T - 自增运算结果。

### func checkedMod(T)

```cangjie
func checkedMod(y: T): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的取余运算。

当运算出现溢出时，返回 `?T.None`，否则返回运算结果。

参数：

- y: T - 除数。

返回值：

- ?T - 取余运算结果。

### func checkedMul(T)

```cangjie
func checkedMul(y: T): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的乘法运算。

当运算出现溢出时，返回 `?T.None`，否则返回运算结果。

参数：

- y: T - 乘数。

返回值：

- ?T - 乘法运算结果。

### func checkedNeg()

```cangjie
func checkedNeg(): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的负号运算。

当运算出现溢出时，返回 `?T.None`，否则返回运算结果。

返回值：

- ?T - 负号运算结果。

### func checkedShl(UInt64)

```cangjie
func checkedShl(y: UInt64): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的左移运算。

当移位位数大于等于操作数位数时，返回 `?T.None`，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- ?T - 左移运算结果。

### func checkedShr(UInt64)

```cangjie
func checkedShr(y: UInt64): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的右移运算。

当移位位数大于等于操作数位数时，返回 `?T.None`，否则返回运算结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- ?T - 右移运算结果。

### func checkedSub(T)

```cangjie
func checkedSub(y: T): ?T
```

功能：使用返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 策略的减法运算。

当运算出现溢出时，返回 `?T.None`，否则返回运算结果。

参数：

- y: T - 减数。

返回值：

- ?T - 减法运算结果。