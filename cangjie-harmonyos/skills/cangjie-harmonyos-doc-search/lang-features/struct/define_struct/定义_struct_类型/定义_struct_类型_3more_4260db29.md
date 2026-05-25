# 定义 struct 类型

`struct` 类型的定义以关键字 `struct` 开头，后跟 `struct` 的名字，接着是定义在一对花括号中的 `struct` 定义体。`struct` 定义体中可以定义一系列的成员变量、成员属性（参见[属性](../class_and_interface/prop.md)）、静态初始化器、构造函数和成员函数。

<!-- compile -->

```cangjie
struct Rectangle {
    let width: Int64
    let height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }

    public func area() {
        width * height
    }
}
```

上例中定义了名为 `Rectangle` 的 `struct` 类型，它有两个 `Int64` 类型的成员变量 `width` 和 `height`，一个有两个 `Int64` 类型参数的构造函数（使用关键字 `init` 定义，函数体中通常是对成员变量的初始化），以及一个成员函数 `area`（返回 `width` 和 `height` 的乘积）。

> **注意：**
>
> `struct` 只能定义在源文件的顶层作用域。

## struct 成员变量

`struct` 成员变量分为实例成员变量和静态成员变量（使用 `static` 修饰符修饰），二者访问上的区别在于实例成员变量只能通过 `struct` 实例（说 `a` 是 `T` 类型的实例，指的是 `a` 是一个 `T` 类型的值）访问，静态成员变量只能通过 `struct` 类型名访问。

实例成员变量定义时可以不设置初值（但必须标注类型，如上例中的 `width` 和 `height`），也可以设置初值，例如：

<!-- compile -->

```cangjie
struct Rectangle {
    let width = 10
    let height = 20
}
```

## struct 静态初始化器

`struct` 支持定义静态初始化器，并在静态初始化器中通过赋值表达式来对静态成员变量进行初始化。

静态初始化器以关键字组合 `static init` 开头，后跟无参参数列表和函数体，且不能被访问修饰符修饰。函数体中必须完成对所有未初始化的静态成员变量的初始化，否则编译报错。

<!-- compile -->

```cangjie
struct Rectangle {
    static let degree: Int64
    static init() {
        degree = 180
    }
}
```

一个 `struct` 中最多允许定义一个静态初始化器，否则报重定义错误。

<!-- compile.error -->

```cangjie
struct Rectangle {
    static let degree: Int64
    static init() {
        degree = 180
    }
    static init() { // Error, redefinition with the previous static init function
        degree = 180
    }
}
```