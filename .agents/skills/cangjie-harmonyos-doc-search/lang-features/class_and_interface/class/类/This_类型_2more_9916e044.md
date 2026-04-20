## This 类型

在类内部，支持 `This` 类型占位符，代指当前类的类型。它只能被作为实例成员函数的返回类型来使用，当使用子类对象调用在父类中定义的返回 `This` 类型的函数时，该函数调用的类型会被识别为子类类型，而非定义所在的父类类型。

如果实例成员函数没有声明返回类型，并且只存在返回 `This` 类型表达式时，当前函数的返回类型会推断为 `This`。示例如下：

<!-- compile -->

```cangjie
open class C1 {
    func f(): This {  // its type is `() -> C1`
        return this
    }

    func f2() { // its type is `() -> C1`
        return this
    }

    public open func f3(): C1 {
        return this
    }
}
class C2 <: C1 {
    // member function f is inherited from C1, and its type is `() -> C2` now
    public override func f3(): This { // OK
        return this
    }
}

main() {
    var obj1: C2 = C2()
    var obj2: C1 = C2()

    var x = obj1.f()    // During compilation, the type of x is C2
    var y = obj2.f()    // During compilation, the type of y is C1
}
```

## 创建对象

定义了 `class` 类型后，即可通过调用其构造函数来创建对象（通过 `class` 类型名调用构造函数）。例如，下例中通过 `Rectangle(10, 20)` 创建 `Rectangle` 类型的对象并赋值给变量 `r`。创建对象之后，可以通过对象访问（`public` 修饰的）实例成员变量和实例成员函数。例如，下例中通过 `r.width` 和 `r.height` 可分别访问 `r` 中 `width` 和 `height` 的值，通过 `r.area()` 可以调用成员函数 `area`。

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
        this.width * this.height
    }
}

main() {
    let r = Rectangle(10, 20) // r.width = 10, r.height = 20
    let width = r.width       // width = 10
    let height = r.height     // height = 20
    let a = r.area()          // a = 200
}
```

如果希望通过对象去修改成员变量的值（不鼓励这种方式，最好还是通过成员函数去修改），需要将 `class` 类型中的成员变量定义为可变成员变量（即使用 `var` 定义）。举例如下：

<!-- run -->

```cangjie
class Rectangle {
   public var width: Int64
   public var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }
    public func area() {
        width * height
    }
}

main() {
    let r = Rectangle(10, 20) // r.width = 10, r.height = 20
    r.width = 8               // r.width = 8
    r.height = 24             // r.height = 24
    let a = r.area()          // a = 192
}
```

不同于 `struct`，对象在赋值或传参时，不会将对象进行复制，多个变量指向的是同一个对象，通过一个变量去修改对象中成员的值，其他变量中对应的成员变量也会被修改。以赋值为例，下面的例子中，将 `r1` 赋值给 `r2` 之后，修改 `r1` 的 `width` 和 `height` 的值，`r2` 的 `width` 和 `height` 值也同样会被修改。

<!-- run -->

```cangjie
class Rectangle {
    var width: Int64
    var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }
     public func area() {
        this.width * this.height
    }
}
main() {
    var r1 = Rectangle(10, 20) // r1.width = 10, r1.height = 20
    var r2 = r1                // r2.width = 10, r2.height = 20
    r1.width = 8               // r1.width = 8
    r1.height = 24             // r1.height = 24
    let a1 = r1.area()         // a1 = 192
    let a2 = r2.area()         // a2 = 192
}
```