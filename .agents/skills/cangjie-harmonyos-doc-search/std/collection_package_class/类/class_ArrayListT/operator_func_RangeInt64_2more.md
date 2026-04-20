### operator func \[](Range\<Int64>)

```cangjie
public operator func [](range: Range<Int64>): ArrayList<T>
```

功能：运算符重载 - 切片。

> **注意：**
>
> - 如果参数 range 是使用 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 构造函数构造的 [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例，有如下行为：
>     - start 的值就是构造函数传入的值本身，不受构造时传入的 hasStart 的值的影响。
>     - hasEnd 为 false 时，end 值不生效，且不受构造时传入的 isClosed 的值的影响，数组切片取到原数组最后一个元素。
>
> - 切片操作返回的 [ArrayList](collection_package_class.md#class-arraylistt) 为全新的对象，与原 [ArrayList](collection_package_class.md#class-arraylistt) 无引用关系。

参数：

- range: [Range](../../core/core_package_api/core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)> - 传递切片的范围。

返回值：

- [ArrayList](collection_package_class.md#class-arraylistt)\<T> - 切片所得的数组。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 range.[step](collection_package_function.md#func-steptint64) 不等于 1 时，抛出异常。
- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 range 无效时，抛出异常。

### extend\<T> ArrayList\<T> <: Equatable\<ArrayList\<T>> where T <: Equatable\<T>

```cangjie
extend<T> ArrayList<T> <: Equatable<ArrayList<T>> where T <: Equatable<T>
```

功能：为 [ArrayList](./collection_package_class.md#class-arraylistt)\<T> 类型扩展 [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[ArrayList](./collection_package_class.md#class-arraylistt)\<T>> 接口，支持判等操作。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[ArrayList](#class-arraylistt)\<T>>

#### func contains(T)

```cangjie
public func contains(element: T): Bool
```

功能：判断当前数组中是否含有指定元素 `element`。

参数：

- element: T - 待寻找的元素。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果数组中包含指定元素，返回 true，否则返回 false。

#### operator func !=(ArrayList\<T>)

```cangjie
public operator func !=(that: ArrayList<T>): Bool
```

功能：判断当前实例与参数指向的 [ArrayList](./collection_package_class.md#class-arraylistt) 实例是否不等。

参数：

- that: [ArrayList](./collection_package_class.md#class-arraylistt)\<T> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果不等，则返回 true，否则返回 false。

#### operator func ==(ArrayList\<T>)

```cangjie
public operator func ==(that: ArrayList<T>): Bool
```

功能：判断当前实例与参数指向的 [ArrayList](./collection_package_class.md#class-arraylistt) 实例是否相等。

两个数组相等指的是两者对应位置的元素分别相等。

参数：

- that: [ArrayList](./collection_package_class.md#class-arraylistt)\<T> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果相等，则返回 true，否则返回 false。