### class 构造函数

和 `struct` 一样，`class` 中也支持定义普通构造函数和主构造函数。

普通构造函数以关键字 `init` 开头，后跟参数列表和函数体，函数体中必须完成所有未初始化实例成员变量的初始化，否则编译报错。

<!-- compile.error -->

```cangjie
class Rectangle {
    let width: Int64
    let height: Int64

    public init(width: Int64, height: Int64) { // Error, 'height' is not initialized in the constructor
        this.width = width
    }
}
```

一个类中可以定义多个普通构造函数，但它们必须构成重载（参见[函数重载](../function/function_overloading.md)），否则报重定义错误。

<!-- compile.error -->

```cangjie
class Rectangle {
    let width: Int64
    let height: Int64

    public init(width: Int64) {
        this.width = width
        this.height = width
    }

    public init(width: Int64, height: Int64) { // OK: overloading with the first init function
        this.width = width
        this.height = height
    }

    public init(height: Int64) { // Error, redefinition with the first init function
        this.width = height
        this.height = height
    }
}
```

除了可以定义若干普通的以 `init` 为名字的构造函数外，`class` 内还可以定义（最多）一个主构造函数。主构造函数的名字和 `class` 类型名相同，它的参数列表中可以有两种形式的形参：普通形参和成员变量形参（需要在参数名前加上 `let` 或 `var`），成员变量形参同时具有定义成员变量和构造函数参数的功能。

使用主构造函数通常可以简化 `class` 的定义，例如，上述包含一个 `init` 构造函数的 `Rectangle` 可以简化为如下定义：

<!-- compile -->

```cangjie
class Rectangle {
    public Rectangle(let width: Int64, let height: Int64) {}
}
```

主构造函数的参数列表中也可以定义普通形参，例如：

<!-- compile -->

```cangjie
class Rectangle {
    public Rectangle(name: String, let width: Int64, let height: Int64) {}
}
```

创建类的实例时调用的构造函数，将根据以下顺序执行类中的表达式：

1. 先初始化主构造函数之外定义的有缺省值的变量；
2. 如果构造函数体内未显式调用父类构造函数或本类其他构造函数，则调用父类的无参构造函数 `super()`，如果父类没有无参构造函数，则报错；
3. 执行构造函数体内的代码。

<!-- verify -->

```cangjie
func foo(x: Int64): Int64 {
    println("I'm foo, got ${x}")
    x
}

open class A {
    init() {
        println("I'm A")
    }
}

class B <: A {
    var x = foo(0)
    init() {
        x = foo(1)
        println("init B finished")
    }
}

main() {
    B()
    0
}
```

上述例子中，调用 `B` 的构造函数时，首先初始化有缺省值的变量 `x`，此时 `foo(0)` 被调用；之后调用父类的无参构造函数，此时 `A` 的构造函数被调用；接下来执行构造函数体内的代码，此时 `foo(1)` 被调用，并打印字符串。因此上例的输出为：

```text
I'm foo, got 0
I'm A
I'm foo, got 1
init B finished
```

如果 `class` 定义中不存在自定义构造函数（包括主构造函数），并且所有实例成员变量都有初始值，则会自动为其生成一个无参构造函数（调用此无参构造函数会创建一个所有实例成员变量的值均等于其初值的对象）；否则，不会自动生成此无参构造函数。例如，对于如下 `class` 定义，编译器会为其自动生成一个无参构造函数：

<!-- compile -->

```cangjie
class Rectangle {
    let width = 10
    let height = 20

    /* Auto-generated parameterless constructor:
    public init() {

    }
    */
}

// Invoke the auto-generated parameterless constructor
let r = Rectangle() // r.width = 10，r.height = 20
```