## interface Hasher

```cangjie
public interface Hasher {
    func finish(): Int64
    mut func reset(): Unit
    mut func write(value: Bool): Unit
    mut func write(value: Rune): Unit
    mut func write(value: Int8): Unit
    mut func write(value: Int16): Unit
    mut func write(value: Int32): Unit
    mut func write(value: Int64): Unit
    mut func write(value: UInt8): Unit
    mut func write(value: UInt16): Unit
    mut func write(value: UInt32): Unit
    mut func write(value: UInt64): Unit
    mut func write(value: Float16): Unit
    mut func write(value: Float32): Unit
    mut func write(value: Float64): Unit
    mut func write(value: String): Unit
}
```

功能：该接口用于处理哈希组合运算。

可以使用一系列 write 函数传入不同数据类型实例，并计算它们的组合哈希值。

### func finish()

```cangjie
func finish(): Int64
```

功能：获取哈希运算的结果。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 经过计算后的哈希值。

### func reset()

```cangjie
mut func reset(): Unit
```

功能：重置哈希值到 0。

### func write(Bool)

```cangjie
mut func write(value: Bool): Unit
```

功能：把想要哈希运算的 [Bool](core_package_intrinsics.md#bool) 值传入，然后进行哈希组合运算。

参数：

- value: [Bool](core_package_intrinsics.md#bool) - 待运算的值。

### func write(Float16)

```cangjie
mut func write(value: Float16): Unit
```

功能：通过该函数把想要哈希运算的 [Float16](core_package_intrinsics.md#float16) 值传入，然后进行哈希组合运算。

参数：

- value: [Float16](core_package_intrinsics.md#float16) - 待运算的值。

### func write(Float32)

```cangjie
mut func write(value: Float32): Unit
```

功能：通过该函数把想要哈希运算的 [Float32](core_package_intrinsics.md#float32) 值传入，然后进行哈希组合运算。

参数：

- value: [Float32](core_package_intrinsics.md#float32) - 待运算的值。

### func write(Float64)

```cangjie
mut func write(value: Float64): Unit
```

功能：通过该函数把想要哈希运算的 [Float64](core_package_intrinsics.md#float64) 值传入，然后进行哈希组合运算。

参数：

- value: [Float64](core_package_intrinsics.md#float64) - 待运算的值。

### func write(Int16)

```cangjie
mut func write(value: Int16): Unit
```

功能：通过该函数把想要哈希运算的 [Int16](core_package_intrinsics.md#int16) 值传入，然后进行哈希组合运算。

参数：

- value: [Int16](core_package_intrinsics.md#int16) - 待运算的值。

### func write(Int32)

```cangjie
mut func write(value: Int32): Unit
```

功能：通过该函数把想要哈希运算的 [Int32](core_package_intrinsics.md#int32) 值传入，然后进行哈希组合运算。

参数：

- value: [Int32](core_package_intrinsics.md#int32) - 待运算的值。

### func write(Int64)

```cangjie
mut func write(value: Int64): Unit
```

功能：通过该函数把想要哈希运算的 [Int64](core_package_intrinsics.md#int64) 值传入，然后进行哈希组合运算。

参数：

- value: [Int64](core_package_intrinsics.md#int64) - 待运算的值。

### func write(Int8)

```cangjie
mut func write(value: Int8): Unit
```

功能：通过该函数把想要哈希运算的 [Int8](core_package_intrinsics.md#int8) 值传入，然后进行哈希组合运算。

参数：

- value: [Int8](core_package_intrinsics.md#int8) - 待运算的值。

### func write(Rune)

```cangjie
mut func write(value: Rune): Unit
```

功能：通过该函数把想要哈希运算的 [Rune](core_package_intrinsics.md#rune) 值传入，然后进行哈希组合运算。

参数：

- value: [Rune](core_package_intrinsics.md#rune) - 待运算的值。

### func write(String)

```cangjie
mut func write(value: String): Unit
```

功能：通过该函数把想要哈希运算的 [String](core_package_structs.md#struct-string) 值传入，然后进行哈希组合运算。

参数：

- value: [String](core_package_structs.md#struct-string) - 待运算的值。