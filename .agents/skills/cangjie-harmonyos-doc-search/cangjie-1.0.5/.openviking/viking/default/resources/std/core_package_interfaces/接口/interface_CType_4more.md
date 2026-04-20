## interface CType

```cangjie
sealed interface CType
```

功能：表示支持与 C 语言互操作的接口。

[CType](core_package_interfaces.md#interface-ctype) 接口是一个语言内置的空接口，它是 [CType](core_package_interfaces.md#interface-ctype) 约束的具体实现，所有 C 互操作支持的类型都隐式地实现了该接口，因此所有 C 互操作支持的类型都可以作为 [CType](core_package_interfaces.md#interface-ctype) 类型的子类型使用。

> **注意：**
>
> - [CType](core_package_interfaces.md#interface-ctype) 接口是仓颉中的一个接口类型，它本身不满足 [CType](core_package_interfaces.md#interface-ctype) 约束。
> - [CType](core_package_interfaces.md#interface-ctype) 接口不允许被用户继承、扩展。
> - [CType](core_package_interfaces.md#interface-ctype) 接口不会突破子类型的使用限制。

示例：

<!-- run -->
```cangjie
@C
struct Data {}

@C
func foo() {}

main() {
    var c: CType = Data() // ok
    c = 0 // ok
    c = true // ok
    c = CString(CPointer<UInt8>()) // ok
    c = CPointer<Int8>() // ok
    c = foo // ok
}
```

## interface Equal\<T>

```cangjie
public interface Equal<T> {
    operator func ==(rhs: T): Bool
}
```

功能：该接口用于支持判等操作。

### operator func ==(T)

```cangjie
operator func ==(rhs: T): Bool
```

功能：判断两个实例是否相等。

参数：

- rhs: T - 待比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果相等，返回 true，否则返回 false。

## interface Equatable\<T>

```cangjie
public interface Equatable<T> <: Equal<T> & NotEqual<T> {
    operator func !=(rhs: T): Bool
}
```

功能：该接口是判等和判不等两个接口的集合体。

该接口中提供运算符 != 重载的默认实现，默认实现根据 == 运算的返回值来确定其返回值。例如：如果 a == b 的返回值为 true，则 a != b 返回 false，否则返回 true。

已为部分仓颉类型实现该接口，包括：[Unit](core_package_intrinsics.md#unit)、[Bool](core_package_intrinsics.md#bool) 、[Rune](core_package_intrinsics.md#rune)、[Int64](core_package_intrinsics.md#int64)、[Int32](core_package_intrinsics.md#int32)、[Int16](core_package_intrinsics.md#int16)、[Int8](core_package_intrinsics.md#int8)、[UIntNative](core_package_intrinsics.md#uintnative)、[UInt64](core_package_intrinsics.md#uint64)、[UInt32](core_package_intrinsics.md#uint32)、[UInt16](core_package_intrinsics.md#uint16)、[UInt8](core_package_intrinsics.md#uint8)、[Float64](core_package_intrinsics.md#float64)、[Float32](core_package_intrinsics.md#float32)、[Float16](core_package_intrinsics.md#float16)、[String](core_package_structs.md#struct-string)、[Array](core_package_structs.md#struct-arrayt)、[Box](core_package_classes.md#class-boxt)、[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)、[HashSet](../../collection/collection_package_api/collection_package_class.md#class-hashsett-where-t--hashable--equatablet)。

父类型：

- [Equal](#interface-equalt)\<T>
- [NotEqual](#interface-notequalt)\<T>

### operator func !=(T)

```cangjie
operator func !=(rhs: T): Bool
```

功能：判断两个实例是否不相等，该函数是此接口的一个默认实现函数。

参数：

- rhs: T - 待比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果不相等，返回 true，否则返回 false。

## interface Greater\<T>

```cangjie
public interface Greater<T> {
    operator func >(rhs: T): Bool
}
```

功能：该接口表示大于计算。

### operator func >(T)

```cangjie
operator func >(rhs: T): Bool
```

功能：判断当前 `T` 类型实例是否大于参数指向的 `T` 类型实例。

参数：

- rhs: T - 待与当前实例比较的另一个实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 如果大于，返回 true，否则返回 false。