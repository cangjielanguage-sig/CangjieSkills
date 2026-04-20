## interface Number\<T>

```cangjie
public interface Number<T> {
    operator func +(rhs: T): T
    operator func -(rhs: T): T
    operator func *(rhs: T): T
    operator func /(rhs: T): T
    operator func -(): T
}
```

功能：提供数值类型相关的方法。

### operator func *(T)

```cangjie
operator func *(rhs: T): T
```

功能：算术运算符，计算乘法。

参数：

- rhs: T - 运算符右边的数，表示另一个乘数。

返回值：

- T - 计算所得积。

### operator func +(T)

```cangjie
operator func +(rhs: T): T
```

功能：算术运算符，计算加法。

参数：

- rhs: T - 运算符右边的数，表示另一个加数。

返回值：

- T - 计算所得和。

### operator func -()

```cangjie
operator func -(): T
```

功能：算术运算符，计算取负的值。

返回值：

- T - 取负的值。

### operator func -(T)

```cangjie
operator func -(rhs: T): T
```

功能：算术运算符，计算减法。

参数：

- rhs: T - 运算符右边的数，表示减数。

返回值：

- T - 计算所得差。

### operator func /(T)

```cangjie
operator func /(rhs: T): T
```

功能：算术运算符，计算除法。

参数：

- rhs: T - 运算符右边的数，表示除数。

返回值：

- T - 计算所得商。

### extend Float16 <: Number\<Float16>

```cangjie
extend Float16 <: Number<Float16> {}
```

功能：为 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型扩展 [Number\<T>](#interface-numbert) 接口。

父类型：

- [Number](#interface-numbert)\<[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)>

### extend Float32 <: Number\<Float32>

```cangjie
extend Float32 <: Number<Float32> {}
```

功能：为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型扩展 [Number\<T>](#interface-numbert) 接口。

父类型：

- [Number](#interface-numbert)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)>

### extend Float64 <: Number\<Float64>

```cangjie
extend Float64 <: Number<Float64> {}
```

功能：为 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型扩展 [Number\<T>](#interface-numbert) 接口。

父类型：

- [Number](#interface-numbert)\<[Float64](../../core/core_package_api/core_package_intrinsics.md#float64)>

### extend Int16 <: Number\<Int16>

```cangjie
extend Int16 <: Number<Int16> {}
```

功能：为 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型扩展 [Number\<T>](#interface-numbert) 接口。

父类型：

- [Number](#interface-numbert)\<[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)>

### extend Int32 <: Number\<Int32>

```cangjie
extend Int32 <: Number<Int32> {}
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型扩展 [Number\<T>](#interface-numbert) 接口。

父类型：

- [Number](#interface-numbert)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

### extend Int64 <: Number\<Int64>

```cangjie
extend Int64 <: Number<Int64> {}
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型扩展 [Number\<T>](#interface-numbert) 接口。

父类型：

- [Number](#interface-numbert)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>

### extend Int8 <: Number\<Int8>

```cangjie
extend Int8 <: Number<Int8> {}
```

功能：为 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 类型扩展 [Number\<T>](#interface-numbert) 接口。

父类型：

- [Number](#interface-numbert)\<[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)>