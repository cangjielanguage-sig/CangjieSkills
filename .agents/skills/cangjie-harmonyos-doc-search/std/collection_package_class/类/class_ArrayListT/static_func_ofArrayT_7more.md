### static func of(Array\<T>)

```cangjie
public static func of(elements: Array<T>): ArrayList<T>
```

功能：构造一个包含指定数组中所有元素的 [ArrayList](collection_package_class.md#class-arraylistt)。

参数：

- elements: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 传入数组，变长参数语法支持参数省略数组字面量的 `[]` 。

返回值：

- [ArrayList](#class-arraylistt)\<T> - 元素为 T 类型的 ArrayList。

> **说明：**
>
> 此函数的参数可使用变长参数方式提供，例如： `ArrayList.of(1, 2, 3)` 等价于 `ArrayList.of([1, 2, 3])` 。

### func add(Collection\<T>)

```cangjie
public func add(all!: Collection<T>): Unit
```

功能：将指定集合中的所有元素附加到此 [ArrayList](collection_package_class.md#class-arraylistt) 的末尾。

函数会按照迭代器顺序遍历入参中的集合，并且将所有元素插入到此 [ArrayList](collection_package_class.md#class-arraylistt) 的尾部。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 需要插入的元素的集合。

### func add(Collection\<T>, Int64)

```cangjie
public func add(all!: Collection<T>, at!: Int64): Unit
```

功能：从指定位置开始，将指定集合中的所有元素插入此 [ArrayList](collection_package_class.md#class-arraylistt)。

函数会按照迭代器顺序遍历入参中的集合，并且将所有元素插入到指定位置，原先在指定位置及其后的元素会后移。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<T> - 要插入的 T 类型元素集合。
- at!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 插入集合的目标索引。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 at 超出范围时，抛出异常。

示例：

使用示例见 [ArrayList 的 add 函数](../collection_package_samples/sample_arraylist_add.md)。

### func add(T)

```cangjie
public func add(element: T): Unit
```

功能：将指定的元素附加到此 [ArrayList](collection_package_class.md#class-arraylistt) 的末尾。

参数：

- element: T - 插入的元素，类型为 T。

示例：

使用示例见 [ArrayList 的 add 函数](../collection_package_samples/sample_arraylist_add.md)。

### func add(T, Int64)

```cangjie
public func add(element: T, at!: Int64): Unit
```

功能：在此 [ArrayList](collection_package_class.md#class-arraylistt) 中的指定位置插入指定元素。

参数：

- element: T - 要插入的 T 类型元素。
- at!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 插入元素的目标索引。

异常：

- [IndexOutOfBoundsException](../../core/core_package_api/core_package_exceptions.md#class-indexoutofboundsexception) - 当 at 超出范围时，抛出异常。

示例：

使用示例见 [ArrayList 的 add 函数](../collection_package_samples/sample_arraylist_add.md)。

### func clear()

```cangjie
public func clear(): Unit
```

功能：从此 [ArrayList](collection_package_class.md#class-arraylistt) 中删除所有元素。

示例：

使用示例见 [ArrayList 的 remove/clear/slice 函数](../collection_package_samples/sample_arraylist_remove_clear_slice.md)。

### func clone()

```cangjie
public func clone(): ArrayList<T>
```

功能：返回此 [ArrayList](collection_package_class.md#class-arraylistt) 实例的拷贝（浅拷贝）。

返回值：

- [ArrayList](collection_package_class.md#class-arraylistt)\<T> - 返回新 [ArrayList](collection_package_class.md#class-arraylistt)\<T>。