## interface GreaterOrEqual\<T>

```cangjie
public interface GreaterOrEqual<T> {
    operator func >=(rhs: T): Bool
}
```

功能：该接口表示大于等于计算。

### operator func >=(T)

```cangjie
operator func >=(rhs: T): Bool
```

功能：判断当前 `T` 类型实例是否大于等于参数指向的 `T` 类型实例。

参数：

- rhs: T - 待与当前实例比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果大于等于，返回 true，否则返回 false。

## interface Hashable

```cangjie
public interface Hashable {
    func hashCode(): Int64
}
```

功能：该接口用于计算哈希值。

已为部分仓颉类型实现该接口，包括：[Bool](core_package_intrinsics.md#bool)、[Rune](core_package_intrinsics.md#rune)、[IntNative](core_package_intrinsics.md#intnative)、[Int64](core_package_intrinsics.md#int64)、[Int32](core_package_intrinsics.md#int32)、[Int16](core_package_intrinsics.md#int16)、[Int8](core_package_intrinsics.md#int8)、[UIntNative](core_package_intrinsics.md#uintnative)、[UInt64](core_package_intrinsics.md#uint64)、[UInt32](core_package_intrinsics.md#uint32)、[UInt16](core_package_intrinsics.md#uint16)、[UInt8](core_package_intrinsics.md#uint8)、[Float64](core_package_intrinsics.md#float64)、[Float32](core_package_intrinsics.md#float32)、[Float16](core_package_intrinsics.md#float16)、[String](core_package_structs.md#struct-string)、[Box](core_package_classes.md#class-boxt)。

### func hashCode()

```cangjie
func hashCode(): Int64
```

功能：获得实例类型的哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 返回实例类型的哈希值。