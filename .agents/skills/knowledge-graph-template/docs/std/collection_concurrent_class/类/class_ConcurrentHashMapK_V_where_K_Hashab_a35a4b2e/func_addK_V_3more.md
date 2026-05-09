### func add(K, V)

```cangjie
public func add(key: K, value: V): ?V
```

功能：将指定的值 value 与此 [ConcurrentHashMap](#class-concurrenthashmapk-v-where-k--hashable--equatablek) 中指定的键 key 关联。如果  [ConcurrentHashMap](#class-concurrenthashmapk-v-where-k--hashable--equatablek) 中已经包含键 key 的关联，则旧值将被替换；如果 [ConcurrentHashMap](#class-concurrenthashmapk-v-where-k--hashable--equatablek) 中不包含键 key 的关联，则添加键 key 与值 value 的关联。

参数：

- key: K - 要放置的键。
- value: V - 要关联的值。

返回值：

- ?V - 如果赋值之前 key 存在，则返回旧的值 Some(V)；当赋值前 key 不存在时，返回 None。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let map: ConcurrentHashMap<Int64, Int64> = ConcurrentHashMap<Int64, Int64>(3, {value => (value, value)})
    let oldValue = map.add(2, 3)
    println(oldValue)
    let newValue = map.add(3, 3)
    println(newValue)
    let iter = ConcurrentHashMapIterator<Int64, Int64>(map)
    while (true) {
        match (iter.next()) {
            case Some(i) => println("(${i[0]},${i[1]})")
            case None => break
        }
    }
}
```

运行结果：

```text
Some(2)
None
(0,0)
(1,1)
(2,3)
(3,3)
```

### func addIfAbsent(K, V)

```cangjie
public func addIfAbsent(key: K, value: V): ?V
```

功能：当此 [ConcurrentHashMap](#class-concurrenthashmapk-v-where-k--hashable--equatablek) 中不存在键 key 时，在 [ConcurrentHashMap](#class-concurrenthashmapk-v-where-k--hashable--equatablek) 中添加指定的值 value 与指定的键 key 的关联。如果 [ConcurrentHashMap](#class-concurrenthashmapk-v-where-k--hashable--equatablek) 已经包含键 key，则不执行赋值操作。

参数：

- key: K - 要放置的键。
- value: V - 要分配的值。

返回值：

- ?V - 如果赋值之前 key 存在，则返回当前 key 对应的值 Some(V)，且不执行赋值操作；当赋值前 key 不存在时，返回 None。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let map: ConcurrentHashMap<Int64, Int64> = ConcurrentHashMap<Int64, Int64>(3, {value => (value, value)})
    let oldValue = map.addIfAbsent(2, 3)
    println(oldValue)
    let newValue = map.addIfAbsent(3, 3)
    println(newValue)
    let iter = ConcurrentHashMapIterator<Int64, Int64>(map)
    while (true) {
        match (iter.next()) {
            case Some(i) => println("(${i[0]},${i[1]})")
            case None => break
        }
    }
}
```

运行结果：

```text
Some(2)
None
(0,0)
(1,1)
(2,2)
(3,3)
```

### func contains(K)

```cangjie
public func contains(key: K): Bool
```

功能：判断此映射中是否包含指定键 key 的映射。

参数：

- key: K - 传递要判断的 key。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否包含指定键 key 的映射，包含为 true，不包含为 false。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let map: ConcurrentHashMap<Int64, Int64> = ConcurrentHashMap<Int64, Int64>(3, {value => (value, value)})
    map.add(3, 3)
    println(map.contains(3))
    println(map.contains(6))
}
```

运行结果：

```text
true
false
```