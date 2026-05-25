### func removeFirst()

```cangjie
public func removeFirst(): ?(K, V)
```

功能：删除 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的第一个元素。

返回值：

- ?(K, V) - 如果存在第一个元素，那么删除该元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该元素并返回；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<(K, V)>.None。

### func removeIf((K, V) -> Bool)

```cangjie
public func removeIf(predicate: (K, V) -> Bool): Unit
```

功能：传入 lambda 表达式，如果满足条件，则删除对应的键值。

参数：

- predicate: (K, V) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传递一个 lambda 表达式进行判断。

异常：

- [ConcurrentModificationException](./collection_package_exception.md#class-concurrentmodificationexception) - 当 `predicate` 中增删或者修改 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 内键值对时，抛出异常。

### func removeLast()

```cangjie
public func removeLast(): ?(K, V)
```

功能：删除 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 的最后一个元素。

返回值：

- ?(K, V) - 如果存在最后一个元素，那么删除该元素，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装该元素并返回；否则返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<(K, V)>.None。

### func values()

```cangjie
public func values(): Collection<V>
```

功能：返回 [TreeMap](collection_package_class.md#class-treemapk-v-where-k--comparablek) 中包含的值，并将所有的 value 存储在一个容器中。

返回值：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<V> - 包含所有值的集合。

### operator func \[](K)

```cangjie
public operator func [](key: K): V
```

功能：运算符重载集合，如果键存在，返回键对应的值。

参数：

- key: K - 传递值进行判断。

返回值：

- V - 与键对应的值。

异常：

- [NoneValueException](../../core/core_package_api/core_package_exceptions.md#class-nonevalueexception) - 如果该 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 不存在该键，抛出异常。

### operator func \[](K, V)

```cangjie
public operator func [](key: K, value!: V): Unit
```

功能：运算符重载集合，如果键存在，新 value 覆盖旧 value，如果键不存在，添加此键值对。

参数：

- key: K - 传递值进行判断。
- value!: V - 传递要设置的值。