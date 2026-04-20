## 变长参数

变长参数是一种特殊的函数调用语法糖。当形参最后一个非命名参数是 `Array` 类型时，实参中对应位置可以直接传入参数序列代替 `Array` 字面量（参数个数可以是 0 个或多个）。示例如下：

<!-- verify -->

```cangjie
func sum(arr: Array<Int64>) {
    var total = 0
    for (x in arr) {
        total += x
    }
    return total
}

main() {
    println(sum())
    println(sum(1, 2, 3))
}
```

程序输出：

```text
0
6
```

需要注意，只有最后一个非命名参数可以作为变长参数，命名参数不能使用这个语法糖。

<!-- compile.error -->

```cangjie
func length(arr!: Array<Int64>) {
    return arr.size
}

main() {
    println(length())        // Error, expected 1 argument, found 0
    println(length(1, 2, 3)) // Error, expected 1 argument, found 3
}
```

变长参数可以出现在全局函数、静态成员函数、实例成员函数、局部函数、构造函数、函数变量、lambda、函数调用操作符重载、索引操作符重载的调用处。不支持其他操作符重载、composition、pipeline 这几种调用方式。示例如下：

<!-- verify -->

```cangjie
class Counter {
    var total = 0
    init(data: Array<Int64>) { total = data.size }
    operator func ()(data: Array<Int64>) { total += data.size }
}

main() {
    let counter = Counter(1, 2)
    println(counter.total)
    counter(3, 4, 5)
    println(counter.total)
}
```

程序输出：

```text
2
5
```

函数重载决议总是会优先考虑不使用变长参数就能匹配的函数，只有在所有函数都不能匹配，才尝试使用变长参数解析。示例如下：

<!-- verify -->

```cangjie
func f<T>(x: T) where T <: ToString {
    println("item: ${x}")
}

func f(arr: Array<Int64>) {
    println("array: ${arr}")
}

main() {
    f()
    f(1)
    f(1, 2)
}
```

程序输出：

```text
array: []
item: 1
array: [1, 2]
```

当编译器无法决议时会报错：

<!-- compile.error -->

```cangjie
func f(arr: Array<Int64>) { arr.size }
func f(first: Int64, arr: Array<Int64>) { first + arr.size }

main() {
    println(f(1, 2, 3)) // Error
}
```