### func remove(K)

```cangjie
public func remove(key: K): Option<V>
```

功能：从此 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中删除指定键的映射（如果存在）。

参数：

- key: K - 传入要删除的 key。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<V> - 被从 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中移除的键对应的值，用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 封装，如果 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中不存该键，返回 None 。

示例：

使用示例见 [HashMap 的 add/remove/clear 函数](../collection_package_samples/sample_hashmap_add_remove_clear.md)。

### func removeIf((K, V) -> Bool)

```cangjie
public func removeIf(predicate: (K, V) -> Bool): Unit
```

功能：传入 lambda 表达式，如果满足条件，则删除对应的键值对。

该函数会遍历整个 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)，所以满足 `predicate(K, V) == true` 的键值对都会被删除。

参数：

- predicate: (K, V) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传递一个 lambda 表达式进行判断。

异常：

- [ConcurrentModificationException](./collection_package_exception.md#class-concurrentmodificationexception) - 当 `predicate` 中增删或者修改 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 内键值对时，抛出异常。

### func reserve(Int64)

```cangjie
public func reserve(additional: Int64): Unit
```

功能：扩容当前的 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)。

将 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 扩容 additional 大小当 additional 小于等于零时，不发生扩容；当 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 剩余容量大于等于 additional 时，不发生扩容；当 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 剩余容量小于 additional 时，取（原始容量的 1.5 倍向下取整）与（additional + 已使用容量）中的最大值进行扩容。

参数：

- additional: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 将要扩容的大小。

异常：

- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当 additional + 已使用容量超过 Int64.Max 时，抛出异常。

### func toArray()

```cangjie
public func toArray(): Array<(K, V)>
```

功能：构造一个包含 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 内键值对的数组，并返回。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<(K, V)> - 包含容器内所有键值对的数组。

### func values()

```cangjie
public func values(): Collection<V>
```

功能：返回 [HashMap](collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek) 中包含的值，并将所有的 value 存储在一个 Values 容器中。

返回值：

- [Collection](../../core/core_package_api/core_package_interfaces.md#interface-collectiont)\<V> - 保存所有返回的 value。