### func entryView(K, (MapEntryView\<K, V>) -> Unit)

```cangjie
public func entryView(key: K, fn: (MapEntryView<K, V>) -> Unit): ?V
```

功能：根据指定键 key 获取当前映射中相应的键值对视图 entryView，并调用函数 fn 对该键值对进行增、删、改操作，并返回最终映射中键 key 对应的值。

如果当前映射中不包含键 key，则将获取一个空视图 entryView，如果将其 value 置为非 None 值，则将在当前映射中增加 key-value 键值对。

如果当前映射中包含键 key，则将获取 key-value 的视图，如果将 value 置为 None，则相当于从当前映射中删除该键值对；如果将 value 置为新的非 None 值，则相当于修改当前映射中键 key 对应的值。

注意参数 fn 中不能并发调用函数 [entryView](#func-entryviewk-mapentryviewk-v---unit)、[remove](#func-remove)、[replace](#func-replacek-v)，如：

```cangjie
map.entryView(1) { _ =>
    let f = spawn {
        map.entryView(17) { _ => () }
    }
    f.get()
}
```

> **说明：**
>
> - 该操作具有原子性。
>
> - 回调 fn 调用过程中对 key-value 键值对的修改不会即时更新到当前映射中，等到 entryView 函数调用结束再将修改整体更新到当前映射中。

参数：

- key: K - 待获取其相应视图的键。
- fn: ([MapEntryView](../../collection/collection_package_api/collection_package_interface.md#interface-mapentryviewk-v)\<K, V>) -> [Unit](../../core/core_package_api/core_package_intrinsics.md#unit) - 对指定视图进行的自定义操作，可用于对映射中键值对进行增、删、改操作。

返回值：

- ?V - 函数 fn 调用结束后当前映射中键 key 对应的值，如果 key 不存在，返回 None。

示例：

<!-- verify -->
```cangjie
import std.collection.concurrent.*

main() {
    let map: ConcurrentHashMap<Int64, Int64> = ConcurrentHashMap<Int64, Int64>(2, {value => (value, value)})
    map.add(2, 2)

    /* 当前映射不包含 key 为 3 的键值对，对 entryView.value 设置新值 7，等价于添加新的键值对 (3,7) */
    let num1 = map.entryView(3, {view => view.value = 7})
    println(num1)

    /* 当前映射包含 key 为 2 的键值对，对 entryView.value 设置新值 6，等价更新 key 为 1 的值为 6 */
    let num2 = map.entryView(1, {view => view.value = 6})
    println(num2)

    /* 当前映射包含 key 为 0 的键值对，对 entryView.value 设置新值 None，等价删除 key 为 0 的键值对 */
    let num3 = map.entryView(0, {view => view.value = None})
    println(num3)

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
Some(7)
Some(6)
None
(1,6)
(2,2)
(3,7)
```