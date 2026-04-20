## interface Integer\<T>

```cangjie
public interface Integer<T> <: Number<T> {
    static func isSigned(): Bool
    operator func %(rhs: T): T
    operator func &(rhs: T): T
    operator func |(rhs: T): T
    operator func ^(rhs: T): T
    operator func !(): T
    operator func >>(n: Int64): T
    operator func <<(n: Int64): T
}
```

功能：本接口提供了整数类型相关的方法。

父类型：

- [Number\<T>](#interface-numbert)

### static func isSigned()

```cangjie
static func isSigned(): Bool
```

功能：判断类型是否是有符号的。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果类型是有符号的，返回 `true`；否则返回 `false`。

### operator func !()

```cangjie
operator func !(): T
```

功能：位运算符，按位取反。

返回值：

- T - 计算所得结果。

### operator func %(T)

```cangjie
operator func %(rhs: T): T
```

功能：算术运算符，计算余数。

参数：

- rhs: T - 运算符右边的数，表示除数。

返回值：

- T - 计算所得余数。

### operator func &(T)

```cangjie
operator func &(rhs: T): T
```

功能：位运算符，按位与。

参数：

- rhs: T - 运算符右边的数。

返回值：

- T - 计算所得结果。

### operator func <<(Int64)

```cangjie
operator func <<(n: Int64): T
```

功能：位运算符，按位左移。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 运算符右边的数，表示左移的位数。

返回值：

- T - 计算所得结果。

### operator func >>(Int64)

```cangjie
operator func >>(n: Int64): T
```

功能：位运算符，按位右移。

参数：

- n: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 运算符右边的数，表示右移的位数。

返回值：

- T - 计算所得结果。

### operator func ^(T)

```cangjie
operator func ^(rhs: T): T
```

功能：位运算符，按位异或。

参数：

- rhs: T - 运算符右边的数。

返回值：

- T - 计算所得结果。

### operator func |(T)

```cangjie
operator func |(rhs: T): T
```

功能：位运算符，按位或。

参数：

- rhs: T - 运算符右边的数。

返回值：

- T - 计算所得结果。

### extend Int16 <: Integer\<Int16>

```cangjie
extend Int16 <: Integer<Int16>
```

功能：为 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型扩展 [Integer\<T>](#interface-integert) 接口。

父类型：

- [Integer](#interface-integert)\<[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)>

#### static func isSigned()

```cangjie
public static func isSigned(): Bool
```

功能：判断 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型是否是有符号类型。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 总是返回 `true`。

### extend Int32 <: Integer\<Int32>

```cangjie
extend Int32 <: Integer<Int32>
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型扩展 [Integer\<T>](#interface-integert) 接口。

父类型：

- [Integer](#interface-integert)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### static func isSigned()

```cangjie
public static func isSigned(): Bool
```

功能：判断 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型是否是有符号类型。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 总是返回 `true`。