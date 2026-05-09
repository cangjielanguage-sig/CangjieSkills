## interface WrappingOp\<T>

```cangjie
public interface WrappingOp<T> {
    func wrappingAdd(y: T): T
    func wrappingDec(): T
    func wrappingDiv(y: T): T
    func wrappingInc(): T
    func wrappingMod(y: T): T
    func wrappingMul(y: T): T
    func wrappingNeg(): T
    func wrappingShl(y: UInt64): T
    func wrappingShr(y: UInt64): T
    func wrappingSub(y: T): T
}
```

功能：当整数运算出现溢出，高位截断。

### func wrappingAdd(T)

```cangjie
func wrappingAdd(y: T): T
```

功能：使用高位截断策略的加法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: T - 加数。

返回值：

- T - 加法运算结果。

### func wrappingDec()

```cangjie
func wrappingDec(): T
```

功能：使用高位截断策略的自减运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- T - 自减运算结果。

### func wrappingDiv(T)

```cangjie
func wrappingDiv(y: T): T
```

功能：使用高位截断策略的除法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: T - 除数。

返回值：

- T - 除法运算结果。

### func wrappingInc()

```cangjie
func wrappingInc(): T
```

功能：使用高位截断策略的自增运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- T - 自增运算结果。

### func wrappingMod(T)

```cangjie
func wrappingMod(y: T): T
```

功能：使用高位截断策略的取余运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: T - 除数。

返回值：

- T - 取余运算结果。

### func wrappingMul(T)

```cangjie
func wrappingMul(y: T): T
```

功能：使用高位截断策略的乘法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: T - 乘数。

返回值：

- T - 乘法运算结果。

### func wrappingNeg()

```cangjie
func wrappingNeg(): T
```

功能：使用高位截断策略的负号运算。

当运算出现溢出时，高位截断，否则返回运算结果。

返回值：

- T - 负号运算结果。

### func wrappingShl(UInt64)

```cangjie
func wrappingShl(y: UInt64): T
```

功能：使用高位截断策略的左移运算。

当移位位数大于等于操作数位数时，高位截断。例如，对 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型的数进行移位，当 y（移位位数）超大于等于 8 时，仅取 y 的低 3 位作为移位位数，以此保证移位位数在 0 到 7 之间。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- T - 左移运算结果。

### func wrappingShr(UInt64)

```cangjie
func wrappingShr(y: UInt64): T
```

功能：使用高位截断策略的右移运算。

当移位位数大于等于操作数位数时，高位截断。例如，对 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型的数进行移位，当 y （移位位数）超大于等于 8 时，仅取 y 的低 3 位作为移位位数，以此保证移位位数在 0 到 7 之间。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- T - 右移运算结果。

### func wrappingSub(T)

```cangjie
func wrappingSub(y: T): T
```

功能：使用高位截断策略的减法运算。

当运算出现溢出时，高位截断，否则返回运算结果。

参数：

- y: T - 减数。

返回值：

- T - 减法运算结果。