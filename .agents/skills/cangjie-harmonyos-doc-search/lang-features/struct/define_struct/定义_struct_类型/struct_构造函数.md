## struct 构造函数

`struct` 支持两类构造函数：普通构造函数和主构造函数。

普通构造函数以关键字 `init` 开头，后跟参数列表和函数体，函数体中必须完成对所有未初始化的实例成员变量的初始化（如果参数名和成员变量名无法区分，可以在成员变量前使用 `this` 加以区分，`this` 表示 `struct` 的当前实例），否则编译报错。

<!-- compile.error -->

```cangjie
struct Rectangle {
    let width: Int64
    let height: Int64

    public init(width: Int64, height: Int64) { // Error, 'height' is not initialized in the constructor
        this.width = width
    }
}
```

一个 `struct` 中可以定义多个普通构造函数，但它们必须构成重载（参见[函数重载](../function/function_overloading.md)），否则报重定义错误。

<!-- compile.error -->

```cangjie
struct Rectangle {
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

除了可以定义若干普通的以 `init` 为名字的构造函数外，`struct` 内还可以定义（最多）一个主构造函数。主构造函数的名字和 `struct` 类型名相同，它的参数列表中可以有两种形式的形参：普通形参和成员变量形参（需要在参数名前加上 `let` 或 `var`），成员变量形参同时扮演定义成员变量和构造函数参数的功能。

使用主构造函数通常可以简化 `struct` 的定义，例如，上述包含一个 `init` 构造函数的 `Rectangle` 可以简化为如下定义：

<!-- compile -->

```cangjie
struct Rectangle {
    public Rectangle(let width: Int64, let height: Int64) {}
}
```

主构造函数的参数列表中也可以定义普通形参，例如：

<!-- compile -->

```cangjie
struct Rectangle {
    public Rectangle(name: String, let width: Int64, let height: Int64) {}
}
```

如果 `struct` 定义中不存在自定义构造函数（包括主构造函数），并且所有实例成员变量都有初始值，则会自动为其生成一个无参构造函数（调用此无参构造函数会创建一个所有实例成员变量的值均等于其初值的对象）；否则，不会自动生成此无参构造函数。例如，对于如下 `struct` 定义，注释中给出了自动生成的无参构造函数：

<!-- compile -->

```cangjie
struct Rectangle {
    let width: Int64 = 10
    let height: Int64 = 10
    /* Auto-generated memberwise constructor:
    public init() {
    }
    */
}
```