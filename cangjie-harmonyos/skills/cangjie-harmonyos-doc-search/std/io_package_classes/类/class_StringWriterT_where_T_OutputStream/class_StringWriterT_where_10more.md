## class StringWriter\<T> where T <: OutputStream

```cangjie
public class StringWriter<T> where T <: OutputStream {
    public init(output: T)
}
```

功能：提供将 [String](../../core/core_package_api/core_package_structs.md#struct-string) 以及一些 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 类型转换成指定编码格式和字节序配置的字符串并写入到输出流的能力。

> **说明：**
>
> - [StringWriter](io_package_classes.md#class-stringwritert-where-t--outputstream) 内部默认有缓冲区，缓冲区容量 4096 个字节。
> - [StringWriter](io_package_classes.md#class-stringwritert-where-t--outputstream) 目前仅支持 UTF-8 编码，暂不支持 UTF-16、UTF-32。

### init(T)

```cangjie
public init(output: T)
```

功能：创建 [StringWriter](io_package_classes.md#class-stringwritert-where-t--outputstream) 实例。

参数：

- output: T - 待写入数据的输出流。

### func flush()

```cangjie
public func flush(): Unit
```

功能：刷新内部缓冲区，将缓冲区数据写入 output 中，并刷新 output。

### func write(Bool)

```cangjie
public func write(v: Bool): Unit
```

功能：写入 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型。

参数：

- v: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 类型的实例。

### func write(Float16)

```cangjie
public func write(v: Float16): Unit
```

功能：写入 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型。

参数：

- v: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型的实例。

### func write(Float32)

```cangjie
public func write(v: Float32): Unit
```

功能：写入 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型。

参数：

- v: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型的实例。

### func write(Float64)

```cangjie
public func write(v: Float64): Unit
```

功能：写入 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型。

参数：

- v: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的实例。

### func write(Int16)

```cangjie
public func write(v: Int16): Unit
```

功能：写入 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型。

参数：

- v: [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 类型的实例。

### func write(Int32)

```cangjie
public func write(v: Int32): Unit
```

功能：写入 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型。

参数：

- v: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 类型的实例。

### func write(Int64)

```cangjie
public func write(v: Int64): Unit
```

功能：写入 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型。

参数：

- v: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 类型的实例。