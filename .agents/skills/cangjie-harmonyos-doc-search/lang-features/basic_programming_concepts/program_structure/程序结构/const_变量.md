## `const` 变量

`const` 变量是一种特殊的变量，它以关键字 `const` 修饰，定义在编译时完成求值，并且在运行时不可改变的变量。例如，下面的例子定义了万有引力常数 `G`：

<!-- verify -const -->

```cangjie
const G = 6.674e-11
```

`const` 变量可以省略类型标注，但是不可省略初始化表达式。`const` 变量可以是全局变量，局部变量，静态成员变量。但是 `const` 变量不能在扩展中定义。`const` 变量可以访问对应类型的所有实例成员，也可以调用对应类型的所有非 `mut` 实例成员函数。

下例定义了一个 `struct`，记录行星的质量和半径，同时定义了一个 `const` 成员函数 `gravity` 用来计算该行星对距离为 `r` 质量为 `m` 的物体的万有引力：

<!-- verify -const -->

```cangjie
struct Planet {
    const Planet(let mass: Float64, let radius: Float64) {}

    const func gravity(m: Float64, r: Float64) {
        G * mass * m / r**2
    }
}

main() {
    const myMass = 71.0
    const earth = Planet(5.972e24, 6.378e6)
    println(earth.gravity(myMass, earth.radius))
}
```

编译执行得到地球对地面上一个质量为 71 kg 的成年人的万有引力：

<!-- verify -const -->

```text
695.657257
```

`const` 变量初始化后该类型实例的所有成员都是 `const` 的（深度 `const`，包含成员的成员），因此不能被用于左值。

<!-- compile.error -->

```cangjie
main() {
    const myMass = 71.0
    myMass = 70.0 // Error, cannot assign to immutable value
}
```

### 值类型和引用类型变量

从编译器实现层面看，任何变量总会关联一个值（一般是通过内存地址/寄存器关联），只是在使用时，对有些变量，将直接取用这个值本身，这被称为**值类型变量**；而对另一些变量，将这个值作为索引、取用这个索引指示的数据，这被称为**引用类型变量**。值类型变量通常在线程栈上分配，每个变量都有自己的数据副本；引用类型变量通常在进程堆中分配，多个变量可引用同一数据对象，对一个变量执行的操作可能会影响其他变量。

从语言层面看，值类型变量对它所绑定的数据/存储空间是独占的，而引用类型变量所绑定的数据/存储空间可以和其他引用类型变量共享。

基于上述原理，在使用值类型变量和引用类型变量时，会存在一些行为差异，以下几点值得注意：

1. 在给值类型变量赋值时，一般会产生拷贝操作，且原来绑定的数据/存储空间会被覆盖。在给引用类型变量赋值时，只是改变了引用关系，原来绑定的数据/存储空间不会被覆盖。
2. 用 `let` 定义的变量，要求变量被初始化后都不能再赋值。对于引用类型，这只是限定了引用关系不可改变，但是所引用的数据是可以被修改的。

在仓颉编程语言中，`class` 和 `Array` 等类型属于引用类型，其他基础数据类型和 `struct` 等类型属于值类型。

例如，以下程序演示了 `struct` 和 `class` 类型变量的行为差异：

<!-- verify -->

```cangjie
struct Copy {
    var data = 2012
}

class Share {
    var data = 2012
}

main() {
    let c1 = Copy()
    var c2 = c1
    c2.data = 2023
    println("${c1.data}, ${c2.data}")

    let s1 = Share()
    let s2 = s1
    s2.data = 2023
    println("${s1.data}, ${s2.data}")
}
```

运行以上程序，将输出：

```text
2012, 2023
2023, 2023
```

由此可以看出，对于值类型的 `Copy` 类型变量，在赋值时总是获取 `Copy` 实例的拷贝，如 `c2 = c1`，随后对 `c2` 成员的修改并不影响 `c1`。对于引用类型的 `Share` 类型变量，在赋值时将建立变量和实例之间的引用关系，如 `s2 = s1`，随后对 `s2` 成员的修改会影响 `s1`。

如果将以上程序中的 `var c2 = c1` 改成 `let c2 = c1`，则编译会报错，例如：

<!-- compile.error -->

```cangjie
struct Copy {
    var data = 2012
}

main() {
    let c1 = Copy()
    let c2 = c1
    c2.data = 2023 // Error, cannot assign to immutable value
}
```