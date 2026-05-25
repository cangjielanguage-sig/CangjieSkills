## class 定义

`class` 类型的定义以关键字 `class` 开头，后跟 `class` 的名字，接着是定义在一对花括号中的 `class` 定义体。`class` 定义体中可以定义一系列的成员变量、成员属性（参见[属性](prop.md)）、静态初始化器、构造函数、成员函数和操作符函数（详见[操作符重载](../function/operator_overloading.md)）。

<!-- compile -->

```cangjie
class Rectangle {
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

上例中定义了名为 `Rectangle` 的 `class` 类型，它有两个 `Int64` 类型的成员变量 `width` 和 `height`，一个有两个 `Int64` 类型参数的构造函数，以及一个成员函数 `area`（返回 `width` 和 `height` 的乘积）。

> **注意：**
>
> `class` 只能定义在源文件的顶层作用域。

使用 `abstract` 修饰的类为抽象类，与普通类不同的是，在抽象类中除了可以定义普通的函数，还允许声明抽象函数（没有函数体）。抽象类定义时的 `open` 修饰符是可选的，也可以使用 `sealed` 修饰符修饰抽象类。`sealed` 修饰符表示该抽象类只能在本包被继承，详见 [class 的继承小节](#class-的继承)。下例中在抽象类 `AbRectangle` 中定义了抽象函数 `foo`。

<!-- compile -->

```cangjie
abstract class AbRectangle {
    public func foo(): Unit
}
```

> **注意：**
>
> - 抽象类中禁止定义 `private` 的抽象函数；
> - 不能为抽象类创建实例；
> - 抽象类的非抽象子类必须实现父类中的所有抽象函数。

### class 成员变量

`class` 成员变量分为实例成员变量和静态成员变量，静态成员变量使用 `static` 修饰符修饰，没有静态初始化器时必须有初值，只能通过类型名访问，参考如下示例：

<!-- compile -->

```cangjie
class Rectangle {
    let width = 10
    static let height = 20
}

let l = Rectangle.height // l = 20
```

实例成员变量定义时可以不设置初值（但必须标注类型），也可以设置初值，只能通过对象（即类的实例）访问，参考如下示例：

<!-- compile -->

```cangjie
class Rectangle {
    let width = 10
    let height: Int64
    init(h: Int64) {
        height = h
    }
}
let rec = Rectangle(20)
let l = rec.height // l = 20
```

### class 静态初始化器

`class` 支持定义静态初始化器，并在静态初始化器中通过赋值表达式来对静态成员变量进行初始化。

静态初始化器以关键字组合 `static init` 开头，后跟无参参数列表和函数体，且不能被访问修饰符修饰。函数体中必须完成对所有未初始化的静态成员变量的初始化，否则编译报错。

<!-- compile -->

```cangjie
class Rectangle {
    static let degree: Int64
    static init() {
        degree = 180
    }
}
```

一个 `class` 中最多允许定义一个静态初始化器，否则报重定义错误。

<!-- compile.error -->

```cangjie
class Rectangle {
    static let degree: Int64
    static init() {
        degree = 180
    }
    static init() { // Error, redefinition with the previous static init function
        degree = 180
    }
}
```