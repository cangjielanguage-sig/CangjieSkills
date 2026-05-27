# ArrayList

使用 ArrayList 类型需要导入 collection 包：

<!-- run -->

```cangjie
import std.collection.*
```

仓颉使用 `ArrayList<T>` 表示 ArrayList 类型，T 表示 ArrayList 的元素类型，T 可以是任意类型。

ArrayList 具备非常好的扩容能力，适合于需要频繁增加和删除元素的场景。

相比 Array，ArrayList 既可以原地修改元素，也可以原地增加和删除元素。

ArrayList 的可变性是一个非常有用的特征，可以让同一个 ArrayList 实例的所有引用都共享同样的元素，并且对它们统一进行修改。

```cangjie
var a: ArrayList<Int64> = ... // ArrayList whose element type is Int64
var b: ArrayList<String> = ... // ArrayList whose element type is String
```

元素类型不相同的 ArrayList 是不相同的类型，所以它们之间不可以互相赋值。

因此以下例子是不合法的。

```cangjie
b = a // Type mismatch
```

仓颉中可以使用构造函数的方式构造一个指定的 ArrayList。

<!-- run -->

```cangjie
let a = ArrayList<String>() // Created an empty ArrayList whose element type is String
let b = ArrayList<String>(100) // Created an ArrayList whose element type is String, and allocate a space of 100
let c = ArrayList<Int64>([0, 1, 2]) // Created an ArrayList whose element type is Int64, containing elements 0, 1, 2
let d = ArrayList<Int64>(c) // Use another Collection to initialize an ArrayList
let e = ArrayList<String>(2, {x: Int64 => x.toString()}) // Created an ArrayList whose element type is String and size is 2. All elements are initialized by specified rule function
```

## 访问 ArrayList 成员

当需要对 ArrayList 的所有元素进行访问时，可以使用 for-in 循环遍历 ArrayList 的所有元素。

<!-- verify -->

```cangjie
import std.collection.ArrayList

main() {
    let list = ArrayList<Int64>([0, 1, 2])
    for (i in list) {
        println("The element is ${i}")
    }
}
```

编译并执行上面的代码，会输出：

```text
The element is 0
The element is 1
The element is 2
```

当需要知道某个 ArrayList 包含的元素个数时，可以使用 size 属性获得对应信息。

<!-- verify -->

```cangjie
import std.collection.ArrayList

main() {
    let list = ArrayList<Int64>([0, 1, 2])
    if (list.size == 0) {
        println("This is an empty arraylist")
    } else {
        println("The size of arraylist is ${list.size}")
    }
}
```

编译并执行上面的代码，会输出：

```text
The size of arraylist is 3
```

当想访问单个指定位置的元素时，可以使用下标语法访问（下标的类型必须是 Int64）。非空 ArrayList 的第一个元素总是从位置 0 开始的。可以从 0 开始访问 ArrayList 的任意一个元素，直到最后一个位置（ArrayList 的 size - 1）。使用负数或大于等于 size 的索引会触发运行时异常。

```cangjie
let a = list[0] // a == 0
let b = list[1] // b == 1
let c = list[-1] // Runtime exceptions
```

ArrayList 也支持下标中使用 Range 的语法，详见 [Array](../basic_data_type/array.md#array) 章节。