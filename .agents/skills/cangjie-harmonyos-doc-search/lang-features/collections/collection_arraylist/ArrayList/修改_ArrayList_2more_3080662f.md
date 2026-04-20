## 修改 ArrayList

可以使用下标语法对某个位置的元素进行修改。

<!-- run -->

```cangjie
let list = ArrayList<Int64>([0, 1, 2])
list[0] = 3
```

ArrayList 是引用类型，ArrayList 在作为表达式使用时不会拷贝副本，同一个 ArrayList 实例的所有引用都会共享同样的数据。

因此对 ArrayList 元素的修改会影响到该实例的所有引用。

<!-- run -->

```cangjie
let list1 = ArrayList<Int64>([0, 1, 2])
let list2 = list1
list2[0] = 3
// list1 contains elements 3, 1, 2
// list2 contains elements 3, 1, 2
```

如果需要将单个元素添加到 ArrayList 的末尾，请使用 add 函数。如果希望同时添加多个元素到末尾，可以使用 `add(all!: Collection<T>)` 函数，这个函数可以接受其他相同元素类型的 Collection 类型，如 Array。Collection 类型详见[基础 Collection 类型概述](collection_overview.md)。

<!-- run -->

```cangjie
import std.collection.ArrayList

main() {
    let list = ArrayList<Int64>()
    list.add(0) // list contains element 0
    list.add(1) // list contains elements 0, 1
    let li = [2, 3]
    list.add(all: li) // list contains elements 0, 1, 2, 3
}
```

可以通过 `add(T, at!: Int64)` 和 `add(all!: Collection<T>, at!: Int64)` 函数将指定的单个元素或相同元素类型的 Collection 值插入到指定索引的位置。该索引处的元素和后面的元素会被挪后以腾出空间。

<!-- run -->

```cangjie
let list = ArrayList<Int64>([0, 1, 2]) // list contains elements 0, 1, 2
list.add(4, at: 1) // list contains elements 0, 4, 1, 2
```

从 ArrayList 中删除元素，可以使用 remove 函数，需要指定删除的索引。该索引处后面的元素会前移以填充空间。

<!-- run -->

```cangjie
let list = ArrayList<String>(["a", "b", "c", "d"]) // list contains the elements "a", "b", "c", "d"
list.remove(at: 1) // Delete the element at subscript 1, now the list contains elements "a", "c", "d"
```

## 增加 ArrayList 的大小

每个 ArrayList 都需要特定数量的内存来保存其内容。当向 ArrayList 添加元素并且该 ArrayList 开始超出其保留容量时，该 ArrayList 会分配更大的内存区域并将其所有元素复制到新内存中。这种增长策略意味着触发重新分配内存的添加操作具有性能成本，但随着 ArrayList 的保留内存变大，它们发生的频率会越来越低。

如果知道大约需要添加多少个元素，可以在添加之前预备足够的内存以避免中间重新分配，这样可以提升性能表现。

<!-- run -->

```cangjie
import std.collection.ArrayList

main() {
    let list = ArrayList<Int64>(100) // Allocate space at once
    for (i in 0..100) {
        list.add(i) // Does not trigger reallocation of space
    }
    list.reserve(100) // Prepare more space
    for (i in 0..100) {
        list.add(i) // Does not trigger reallocation of space
    }
}
```