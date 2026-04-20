### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：构造一个带有传入容量大小的 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化容量大小。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 capacity 小于 0 则抛出异常。

### init(Int64, (Int64) -> (K, V))

```cangjie
public init(size: Int64, initElement: (Int64) -> (K, V))
```

功能：通过传入的元素个数 size 和函数规则来构造 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。

构造出的 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的容量受 size 大小影响。由于 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 内部不允许键重复，当函数 initElement 生成相同的键时，后构造的键值对将会覆盖之前出现的键值对。

参数：

- size: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化该 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的函数规则。
- initElement: ([Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) -> (K, V) - 初始化该 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的函数规则。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 size 小于 0 则抛出异常。

### func add(Collection\<(K, V)>)

```cangjie
public func add(all!: Collection<(K, V)>): Unit
```

功能：按照 elements 的迭代器顺序将新的键值对集合放入 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中。

对于 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中已有的键，该键的值将被新值替换。

参数：

- all!: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<(K, V)> - 需要添加进 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 的键值对集合。

示例：

使用示例见 [HashMap 的 add/remove/clear 函数](../collection_package_samples/sample_hashmap_add_remove_clear.md)。

### func add(K, V)

```cangjie
public func add(key: K, value: V): Option<V>
```

功能：将键值对放入 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中。

对于 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中已有的键，该键的值将被新值替换，并且返回旧的值。

参数：

- key: K - 要放置的键。
- value: V - 要分配的值。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V> - 如果赋值之前 key 存在，旧的 value 用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装；否则，返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V>.None。

示例：

使用示例见 [HashMap 的 get/add/contains 函数](../collection_package_samples/sample_hashmap_get_add_contains.md)。

### func clear()

```cangjie
public func clear(): Unit
```

功能：清除所有键值对。

示例：

使用示例见 [HashMap 的 add/remove/clear 函数](../collection_package_samples/sample_hashmap_add_remove_clear.md)。