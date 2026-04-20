## interface Shrink\<T>

```cangjie
public interface Shrink<T> {
    func shrink(): Iterable<T>
}
```

功能：将 T 类型的值缩减到多个“更小”的值。

### func shrink()

```cangjie
func shrink(): Iterable<T>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 一组可能的“较小”值的迭代器。

### extend Bool <: Shrink\<Bool>

```cangjie
extend Bool <: Shrink<Bool>
```

功能：为 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)>

#### func shrink()

```cangjie
func shrink(): Iterable<Bool>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<Bool> - 一组可能的“较小”值的迭代器。

### extend Int16 <: Shrink\<Int16>

```cangjie
extend Int16 <: Shrink<Int16>
```

功能：为 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)>

#### func shrink()

```cangjie
func shrink(): Iterable<Int16>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<Int16> - 一组可能的“较小”值的迭代器。

### extend Int32 <: Shrink\<Int32>

```cangjie
extend Int32 <: Shrink<Int32>
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### func shrink()

```cangjie
func shrink(): Iterable<Int32>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<Int32> - 一组可能的“较小”值的迭代器。

### extend Int64 <: Shrink\<Int64>

```cangjie
extend Int64 <: Shrink<Int64>
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>

#### func shrink()

```cangjie
func shrink(): Iterable<Int64>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<Int64> - 一组可能的“较小”值的迭代器。

### extend Int8 <: Shrink\<Int8>

```cangjie
extend Int8 <: Shrink<Int8>
```

功能：为 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)>

#### func shrink()

```cangjie
func shrink(): Iterable<Int8>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<Int8> - 一组可能的“较小”值的迭代器。