## Any 类型

Any 类型是一个内置的接口，它的定义如下：

<!-- compile -->

```cangjie
interface Any {}
```

仓颉中所有接口都默认继承它，所有非接口类型都默认实现它，因此所有类型都可以作为 Any 类型的子类型使用。

如下面的代码，可以将一系列不同类型的变量赋值给 Any 类型的变量。

<!-- compile -->

```cangjie
main() {
    var any: Any = 1
    any = 2.0
    any = "hello, world!"
}
```