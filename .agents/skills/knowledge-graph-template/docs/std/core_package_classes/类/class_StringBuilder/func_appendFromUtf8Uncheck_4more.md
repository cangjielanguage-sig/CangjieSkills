### func appendFromUtf8Unchecked(Array\<Byte>)

```cangjie
public unsafe func appendFromUtf8Unchecked(arr: Array<Byte>): Unit
```

功能：在 [StringBuilder](core_package_classes.md#class-stringbuilder) 末尾插入参数 `arr` 指向的字节数组。

相较于 `appendFromUtf8` 函数，它并没有针对于字节数组进行 UTF-8 相关规则的检查，所以它所构建的字符串并不一定保证是合法的，甚至出现非预期的异常，如果不是某些场景下的速度考虑，请优先使用安全的 `appendFromUtf8` 函数。

参数：

- arr: [Array](core_package_structs.md#struct-arrayt)\<[Byte](core_package_types.md#type-byte)> - 插入的字节数组。

### func reserve(Int64)

```cangjie
public func reserve(additional: Int64): Unit
```

功能：将 [StringBuilder](core_package_classes.md#class-stringbuilder) 扩容 `additional` 大小。

当 `additional` 小于等于零，或剩余容量大于等于 `additional` 时，不发生扩容；当剩余容量小于 `additional` 时，扩容至当前容量的 1.5 倍（向下取整）与 `size` + `additional` 的最大值。

参数：

- additional: [Int64](core_package_intrinsics.md#int64) - 指定 [StringBuilder](core_package_classes.md#class-stringbuilder) 的扩容大小。

### func reset(Option\<Int64>)

```cangjie
public func reset(capacity!: Option<Int64> = None): Unit
```

功能：清空当前 [StringBuilder](core_package_classes.md#class-stringbuilder)，并将容量重置为 `capacity` 指定的值。

参数：

- capacity!: [Option](core_package_enums.md#enum-optiont)\<[Int64](core_package_intrinsics.md#int64)> - 重置后 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例的容量大小，取值范围为 `None` 和 (`Some(0)`, `Some(Int64.Max)`]，默认值 `None` 表示采用默认大小容量（32）。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当参数 `capacity` 的值小于等于 0 时，抛出异常。

### func toString()

```cangjie
public func toString(): String
```

功能：获取 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例中的字符串。

> **注意：**
>
> 该函数不会将字符串数据进行拷贝。

返回值：

- [String](core_package_structs.md#struct-string) - [StringBuilder](core_package_classes.md#class-stringbuilder) 实例中的字符串。