## struct DefaultHasher

```cangjie
public struct DefaultHasher <: Hasher {
 public init(res!: Int64 = 0)
}
```

功能：该结构体提供了默认哈希算法实现。

可以使用一系列 write 函数传入不同数据类型实例，并计算它们的组合哈希值。

父类型：

- [Hasher](core_package_interfaces.md#interface-hasher)

### init(Int64)

```cangjie
public init(res!: Int64 = 0)
```

功能：构造函数，创建一个 [DefaultHasher](core_package_structs.md#struct-defaulthasher)。

参数：

- res!: [Int64](core_package_intrinsics.md#int64) - 初始哈希值，默认为 0。

### func finish()

```cangjie
public func finish(): Int64
```

功能：获取哈希运算的结果。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希运算的结果。

### func reset()

```cangjie
public mut func reset(): Unit
```

功能：重置哈希值为 0。

### func write(Bool)

```cangjie
public mut func write(value: Bool): Unit
```

功能：通过该函数把想要哈希运算的 [Bool](core_package_intrinsics.md#bool) 值传入，然后进行哈希组合运算。

参数：

- value: [Bool](core_package_intrinsics.md#bool) - 待运算的值。

### func write(Float16)

```cangjie
public mut func write(value: Float16): Unit
```

功能：通过该函数把想要哈希运算的 [Float16](core_package_intrinsics.md#float16) 值传入，然后进行哈希组合运算。

参数：

- value: [Float16](core_package_intrinsics.md#float16) - 待运算的值。

### func write(Float32)

```cangjie
public mut func write(value: Float32): Unit
```

功能：通过该函数把想要哈希运算的 [Float32](core_package_intrinsics.md#float32) 值传入，然后进行哈希组合运算。

参数：

- value: [Float32](core_package_intrinsics.md#float32) - 待运算的值。

### func write(Float64)

```cangjie
public mut func write(value: Float64): Unit
```

功能：通过该函数把想要哈希运算的 [Float64](core_package_intrinsics.md#float64) 值传入，然后进行哈希组合运算。

参数：

- value: [Float64](core_package_intrinsics.md#float64) - 待运算的值。

### func write(Int16)

```cangjie
public mut func write(value: Int16): Unit
```

功能：通过该函数把想要哈希运算的 [Int16](core_package_intrinsics.md#int16) 值传入，然后进行哈希组合运算。

参数：

- value: [Int16](core_package_intrinsics.md#int16) - 待运算的值。

### func write(Int32)

```cangjie
public mut func write(value: Int32): Unit
```

功能：通过该函数把想要哈希运算的 [Int32](core_package_intrinsics.md#int32) 值传入，然后进行哈希组合运算。

参数：

- value: [Int32](core_package_intrinsics.md#int32) - 待运算的值。

### func write(Int64)

```cangjie
public mut func write(value: Int64): Unit
```

功能：通过该函数把想要哈希运算的 [Int64](core_package_intrinsics.md#int64) 值传入，然后进行哈希组合运算。

参数：

- value: [Int64](core_package_intrinsics.md#int64) - 待运算的值。

### func write(Int8)

```cangjie
public mut func write(value: Int8): Unit
```

功能：通过该函数把想要哈希运算的 [Int8](core_package_intrinsics.md#int8) 值传入，然后进行哈希组合运算。

参数：

- value: [Int8](core_package_intrinsics.md#int8) - 待运算的值。

### func write(Rune)

```cangjie
public mut func write(value: Rune): Unit
```

功能：通过该函数把想要哈希运算的 [Rune](core_package_intrinsics.md#rune) 值传入，然后进行哈希组合运算。

参数：

- value: [Rune](core_package_intrinsics.md#rune) - 待运算的值。

### func write(String)

```cangjie
public mut func write(value: String): Unit
```

功能：通过该函数把想要哈希运算的 [String](core_package_structs.md#struct-string) 值传入，然后进行哈希组合运算。

参数：

- value: [String](core_package_structs.md#struct-string) - 待运算的值。