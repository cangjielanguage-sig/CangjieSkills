## 修改 HashMap

HashMap 是一种可变的引用类型，HashMap 类型提供了修改元素、添加元素、删除元素的功能。

HashMap 的可变性是一个非常有用的特征，可以让同一个 HashMap 实例的所有引用都共享同样的元素，并且对它们统一进行修改。

可以使用下标语法对某个键对应的值进行修改。

<!-- run -->

```cangjie
let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
map["a"] = 3
```

HashMap 是引用类型，HashMap 在作为表达式使用时不会拷贝副本，同一个 HashMap 实例的所有引用都会共享同样的数据。

因此对 HashMap 元素的修改会影响到该实例的所有引用。

<!-- run -->

```cangjie
let map1 = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
let map2 = map1
map2["a"] = 3
// map1 contains the elements ("a", 3), ("b", 1), ("c", 2)
// map2 contains the elements ("a", 3), ("b", 1), ("c", 2)
```

如果需要将单个键值对添加到 HashMap 里，请使用 add 函数。如果希望同时添加多个键值对，可以使用 `add(all!: Collection<(K, V)>)` 函数。当键不存在时，add 函数会执行添加的操作，当键存在时，add 函数会将新的值覆盖旧的值。

<!-- run -->

```cangjie
let map = HashMap<String, Int64>()
map.add("a", 0) // map contains the element ("a", 0)
map.add("b", 1) // map contains the elements ("a", 0), ("b", 1)
let map2 = HashMap<String, Int64>([("c", 2), ("d", 3)])
map.add(all: map2) // map contains the elements ("a", 0), ("b", 1), ("c", 2), ("d", 3)
```

除了使用 add 函数以外，也可以使用赋值的方式直接将新的键值对添加到 HashMap。

<!-- run -->

```cangjie
let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
map["d"] = 3 // map contains the elements ("a", 0), ("b", 1), ("c", 2), ("d", 3)
```

从 HashMap 中删除元素，可以使用 remove 函数，需要指定删除的键。

<!-- run -->

```cangjie
let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2), ("d", 3)])
map.remove("d") // map contains the elements ("a", 0), ("b", 1), ("c", 2)
```