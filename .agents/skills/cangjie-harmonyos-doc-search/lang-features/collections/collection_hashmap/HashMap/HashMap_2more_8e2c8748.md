# HashMap

使用 HashMap 类型需要导入 collection 包：

<!-- run -->

```cangjie
import std.collection.*
```

可以使用 HashMap 类型来构造元素为键值对的 Collection。

HashMap 是一种哈希表，提供对其包含的元素的快速访问。表中的每个元素都使用其键作为标识，可以使用键来访问相应的值。

仓颉使用 `HashMap<K, V>` 表示 HashMap 类型，K 表示 HashMap 的键类型，K 必须是实现了 Hashable 和 `Equatable<K>` 接口的类型，例如数值或 String。V 表示 HashMap 的值类型，V 可以是任意类型。

```cangjie
var a: HashMap<Int64, Int64> = ... // HashMap whose key type is Int64 and value type is Int64
var b: HashMap<String, Int64> = ... // HashMap whose key type is String and value type is Int64
```

元素类型不相同的 HashMap 是不相同的类型，所以它们之间不可以互相赋值。

因此以下例子是不合法的。

```cangjie
b = a // Type mismatch
```

仓颉中可以使用构造函数的方式构造一个指定的 HashMap。

<!-- run -->

```cangjie
let a = HashMap<String, Int64>() // Created an empty HashMap whose key type is String and value type is Int64
let b = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)]) // whose key type is String and value type is Int64, containing elements ("a", 0), ("b", 1), ("c", 2)
let c = HashMap<String, Int64>(b) // Use another Collection to initialize a HashMap
let d = HashMap<String, Int64>(10) // Created a HashMap whose key type is String and value type is Int64 and capacity is 10
let e = HashMap<Int64, Int64>(10, {x: Int64 => (x, x * x)}) // Created a HashMap whose key and value type is Int64 and size is 10. All elements are initialized by specified rule function
```

## 访问 HashMap 成员

当需要对 HashMap 的所有元素进行访问时，可以使用 for-in 循环遍历 HashMap 的所有元素。

需要注意的是，HashMap 并不保证按插入元素的顺序排列，因此遍历的顺序和插入的顺序可能不同。

<!-- verify -->

```cangjie
import std.collection.HashMap

main() {
    let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
    for ((k, v) in map) {
        println("The key is ${k}, the value is ${v}")
    }
}
```

编译并执行上面的代码，有可能会输出：

```text
The key is a, the value is 0
The key is b, the value is 1
The key is c, the value is 2
```

当需要知道某个 HashMap 包含的元素个数时，可以使用 size 属性获得对应信息。

<!-- verify -->

```cangjie
import std.collection.HashMap

main() {
    let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
    if (map.size == 0) {
        println("This is an empty hashmap")
    } else {
        println("The size of hashmap is ${map.size}")
    }
}
```

编译并执行上面的代码，会输出：

```text
The size of hashmap is 3
```

当想判断 HashMap 中是否包含某个键时，可以使用 contains 函数。如果该键存在会返回 true，否则返回 false。

<!-- run -->

```cangjie
let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
let a = map.contains("a") // a == true
let b = map.contains("d") // b == false
```

当想访问指定键对应的元素时，可以使用下标语法访问（下标的类型必须是键类型）。使用不存在的键作为索引会触发运行时异常。

```cangjie
let map = HashMap<String, Int64>([("a", 0), ("b", 1), ("c", 2)])
let a = map["a"] // a == 0
let b = map["b"] // b == 1
let c = map["d"] // Runtime exceptions
```