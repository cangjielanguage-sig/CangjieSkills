### prop size

```cangjie
public prop size: Int64
```

功能：返回键值的个数。

> **注意：**
>
> 此方法不保证并发场景下的原子性，建议在环境中没有其他线程并发地修改 [ConcurrentHashMap](#class-concurrenthashmapk-v-where-k--hashable--equatablek) 时调用。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)

### init(Collection\<(K, V)>, Int64)

```cangjie
public init(elements: Collection<(K, V)>, concurrencyLevel!: Int64 = 16)
```

功能：构造一个带有传入迭代器和指定并发度的 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek)。该构造函数根据传入迭代器元素 elements 的 size 设置 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek) 的容量。

参数：

- elements: [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<(K, V)> - 初始化迭代器元素。
- concurrencyLevel!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 用户指定的并发度。

### init(Int64)

```cangjie
public init(concurrencyLevel!: Int64 = 16)
```

功能：构造一个具有默认初始容量（16）和指定并发度（默认等于 16）的 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek)。

参数：

- concurrencyLevel!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 用户指定的并发度。

### init(Int64, (Int64) -> (K, V), Int64)

```cangjie
public init(size: Int64, initElement: (Int64) -> (K, V), concurrencyLevel!: Int64 = 16)
```

功能：构造具有传入大小和初始化函数元素以及指定并发度的 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek)。该构造函数根据参数 size 设置 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek) 的容量。

参数：

- size: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化函数元素的大小。
- initElement: ([Int64](../../core/core_package_api/core_package_intrinsics.md#int64)) -> (K, V) - 初始化函数元素。
- concurrencyLevel!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 用户指定并发度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 size 小于 0 则抛出异常。

### init(Int64, Int64)

```cangjie
public init(capacity: Int64, concurrencyLevel!: Int64 = 16)
```

功能：构造一个带有传入容量大小和指定并发度（默认等于 16）的 [ConcurrentHashMap](collection_concurrent_class.md#class-concurrenthashmapk-v-where-k--hashable--equatablek)。

参数：

- capacity: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 初始化容量大小。
- concurrencyLevel!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 用户指定的并发度。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 如果 capacity 小于 0 则抛出异常。