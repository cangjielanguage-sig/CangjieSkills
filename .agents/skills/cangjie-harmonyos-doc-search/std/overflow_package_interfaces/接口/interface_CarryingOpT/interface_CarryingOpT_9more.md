## interface CarryingOp\<T>

```cangjie
public interface CarryingOp<T> {
  func carryingAdd(y: T): (Bool, T)
  func carryingSub(y: T): (Bool, T)
  func carryingMul(y: T): (Bool, T)
  func carryingDiv(y: T): (Bool, T)
  func carryingMod(y: T): (Bool, T)
  func carryingInc(): (Bool, T)
  func carryingDec(): (Bool, T)
  func carryingNeg(): (Bool, T)
  func carryingShl(y: UInt64): (Bool, T)
  func carryingShr(y: UInt64): (Bool, T)
}
```

功能：提供返回整数运算是否发生了截断以及运算结果的接口。

### func carryingAdd(T)

```cangjie
func carryingAdd(y: T): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示加法运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

参数：

- y: T - 加数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 加法运算是否发生截断以及运算的结果。

### func carryingDec()

```cangjie
func carryingDec(): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示自减运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 自减运算是否发生截断以及运算的结果。

### func carryingDiv(T)

```cangjie
func carryingDiv(y: T): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示除法运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

参数：

- y: T - 除数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 除法运算是否发生截断以及运算的结果。

### func carryingInc()

```cangjie
func carryingInc(): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示自增运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 自增运算是否发生截断以及运算的结果。

### func carryingMod(T)

```cangjie
func carryingMod(y: T): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示取余运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

参数：

- y: T - 除数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 取余运算是否发生截断以及运算的结果。

### func carryingMul(T)

```cangjie
func carryingMul(y: T): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示乘法运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

参数：

- y: T - 乘数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 乘法运算是否发生截断以及运算的结果。

### func carryingNeg()

```cangjie
func carryingNeg(): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示负号运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 负号运算是否发生截断以及运算的结果。

### func carryingShl(UInt64)

```cangjie
func carryingShl(y: UInt64): (Bool, T)
```

功能：返回一个元组，元组的第一个元素表示左移运算是否发生了截断，发生截断时为 `true`，元组的第二个元素是运算的结果。

参数：

- y: [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - 移位位数。

返回值：

- ([Bool](../../core/core_package_api/core_package_intrinsics.md#bool), T) - 左移运算是否发生截断以及运算的结果。