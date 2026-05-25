## `const` 函数

`const` 函数是一类特殊的函数，这些函数具备了可以在编译时求值的能力。在 `const` 上下文中调用这种函数时，这些函数会在编译时执行计算。而在其他非 `const` 上下文，`const` 函数会和普通函数一样在运行时执行。

下例是一个计算平面上两点距离的 `const` 函数，`distance` 中使用 `let` 定义了两个局部变量 `dx` 和 `dy`：

<!-- verify -->

```cangjie
struct Point {
    const Point(let x: Float64, let y: Float64) {}
}

const func distance(a: Point, b: Point) {
    let dx = a.x - b.x
    let dy = a.y - b.y
    (dx ** 2 + dy ** 2) ** 0.5
}

main() {
    const a = Point(3.0, 0.0)
    const b = Point(0.0, 4.0)
    const d = distance(a, b)
    println(d)
}
```

编译运行输出：

```text
5.000000
```

需要注意：

1. `const` 函数声明必须使用 `const` 修饰。
2. 全局 `const` 函数和 `static const` 函数中只能访问 `const` 声明的外部变量，包含 `const` 全局变量、`const` 静态成员变量，其他外部变量都不可访问。`const init` 函数和 `const` 实例成员函数除了能访问 `const` 声明的外部变量，还可以访问当前类型的实例成员变量。
3. `const` 函数中的表达式都必须是 `const` 表达式，`const init` 函数除外。
4. `const` 函数中可以使用 `let`、`const` 声明新的局部变量。但不支持 `var`。
5. `const` 函数中的参数类型和返回类型没有特殊规定。如果该函数调用的实参不符合 `const` 表达式要求，那这个函数调用不能作为 `const` 表达式使用，但仍然可以作为普通表达式使用。
6. `const` 函数不一定都会在编译时执行，例如可以在非 `const` 函数中运行时调用。
7. `const` 函数与非 `const` 函数重载规则一致。
8. 数值类型、`Bool`、`Unit`、`Rune`、`String` 类型 和 `enum` 支持定义 `const` 实例成员函数。
9. 对于 `struct` 和 `class`，只有定义了 `const init` 才能定义 `const` 实例成员函数。`class` 中的 `const` 实例成员函数不能是 `open` 的。`struct` 中的 `const` 实例成员函数不能是 `mut` 的。

另外，接口中也可以定义 `const` 函数，但会受到以下规则限制：

1. 接口中的 `const` 函数，实现类型必须也用 `const` 函数才算实现接口。
2. 接口中的非 `const` 函数，实现类型使用 `const` 或非 `const` 函数都算实现接口。
3. 接口中的 `const` 函数与接口的 `static` 函数一样，只有在该接口作为泛型约束的时候，受约束的泛型变元或变量才能使用这些 `const` 函数。

在下面的例子中，在接口 `I` 里定义了两个 `const` 函数，类 `A` 实现了接口 `I`，泛型函数 `g` 的形参类型上界是 `I`。

<!-- verify -->

```cangjie
interface I {
    const func f(): Int64
    const static func f2(): Int64
}

class A <: I {
    public const func f() { 0 }
    public const static func f2() { 1 }
    const init() {}
}

const func g<T>(i: T) where T <: I {
    return i.f() + T.f2()
}

main() {
    println(g(A()))
}
```

编译执行上述代码，输出结果为：

```text
1
```