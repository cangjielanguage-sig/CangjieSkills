### extend IntNative <: Shrink\<IntNative>

```cangjie
extend IntNative <: Shrink<IntNative>
```

功能：为 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)>

#### func shrink()

```cangjie
func shrink(): Iterable<IntNative>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<IntNative> - 一组可能的“较小”值的迭代器。

### extend Rune <: Shrink\<Rune>

```cangjie
extend Rune <: Shrink<Rune>
```

功能：为 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)>

#### func shrink()

```cangjie
func shrink(): Iterable<Rune>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<Rune> - 一组可能的“较小”值的迭代器。

### extend String <: Shrink\<String>

```cangjie
extend String <: Shrink<String>
```

功能：为 [String](../../core/core_package_api/core_package_structs.md#struct-string) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>

#### func shrink()

```cangjie
func shrink(): Iterable<String>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<String> - 一组可能的“较小”值的迭代器。

### extend UInt16 <: Shrink\<UInt16>

```cangjie
extend UInt16 <: Shrink<UInt16>
```

功能：为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)>

#### func shrink()

```cangjie
func shrink(): Iterable<UInt16>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<UInt16> - 一组可能的“较小”值的迭代器。

### extend UInt32 <: Shrink\<UInt32>

```cangjie
extend UInt32 <: Shrink<UInt32>
```

功能：为 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)>

#### func shrink()

```cangjie
func shrink(): Iterable<UInt32>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<UInt32> - 一组可能的“较小”值的迭代器。

### extend UInt64 <: Shrink\<UInt64>

```cangjie
extend UInt64 <: Shrink<UInt64>
```

功能：为 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 实现了 [Shrink](#interface-shrinkt)\<T> 接口。

父类型：

- [Shrink](#interface-shrinkt)\<[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)>

#### func shrink()

```cangjie
func shrink(): Iterable<UInt64>
```

功能：将该值缩小为一组可能的“较小”值。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<UInt64> - 一组可能的“较小”值的迭代器。