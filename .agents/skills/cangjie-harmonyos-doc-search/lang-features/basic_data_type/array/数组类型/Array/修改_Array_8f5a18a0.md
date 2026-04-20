### 修改 Array

Array 是一种长度不变的 [Collection 类型](../../source_zh_cn/collections/collection_overview.md)，因此 Array 没有提供添加和删除元素的成员函数。

但是 Array 允许对其中的元素进行修改，同样使用下标语法。

<!-- verify -->

```cangjie
main() {
    let arr = [0, 1, 2, 3, 4, 5]
    arr[0] = 3
    println("The first element is ${arr[0]}")
}
```

编译并执行上面的代码，会输出：

```text
The first element is 3
```

Array 虽然是 struct 类型，但其内部持有的只是元素的引用，因此在作为表达式使用时不会拷贝副本，同一个 Array 实例的所有引用都会共享同样的元素数据。

因此对 Array 元素的修改会影响到该实例的所有引用。

<!-- compile -->

```cangjie
let arr1 = [0, 1, 2]
let arr2 = arr1
arr2[0] = 3
// arr1 contains elements 3, 1, 2
// arr2 contains elements 3, 1, 2
```