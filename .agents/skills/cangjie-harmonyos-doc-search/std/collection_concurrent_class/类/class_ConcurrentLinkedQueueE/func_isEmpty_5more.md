### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

功能：判断当前队列是否为空。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当前队列为空返回 true，否则返回 false。

### func iterator()

```cangjie
public func iterator(): Iterator<E>
```

功能：获取当前队列的迭代器，用于遍历当前队列。

> **说明：**
>
> 遍历操作不会删除队列中的元素。
> 遍历操作不保证原子性，如果有其他线程并发修改当前队列，不保遍历得到的元素是当前队列某一时刻的静态切片。

返回值：

- [Iterator](../../core/core_package_api/core_package_classes.md#class-iteratort)\<E> - 当前队列的迭代器。

### func peek()

```cangjie
public func peek(): Option<E>
```

功能：获取队首元素，不会删除该元素。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 成功获取则返回队首元素，队列为空则返回 None。

### func remove()

```cangjie
public func remove(): Option<E>
```

功能：获取并删除队首元素。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<E> - 成功删除则返回队首元素，队列为空则返回 None。

### func toArray()

```cangjie
public func toArray(): Array<E>
```

功能：将当前队列中所有元素按顺序存入数组，先入队的元素在数组下标较小的位置。

> **说明：**
>
> 该操作不会删除队列中的元素。
> 该操作不保证原子性，如果有其他线程并发修改当前队列，不保证该操作得到的数组是当前队列某一时刻的静态切片。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<E> - 得到的数组，里面的元素为当前队列中的元素。