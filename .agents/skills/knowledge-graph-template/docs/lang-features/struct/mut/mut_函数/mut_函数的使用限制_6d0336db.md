## mut 函数的使用限制

因为 `struct` 是值类型，所以如果一个变量是 `struct` 类型且使用 `let` 声明，那么不能通过这个变量访问该类型的 `mut` 函数。

示例：

<!-- compile.error -->

```cangjie
interface I {
    mut func f(): Unit
}
struct Foo <: I {
    public var i = 0
    public mut func f(): Unit {
        i += 1
    }
}
main() {
    let a = Foo()
    a.f() // Error, 'a' is of type struct and is declared with 'let', the 'mut' function cannot be accessed via 'a'
    var b = Foo()
    b.f() // OK
    let c: I = Foo()
    c.f() // OK, 变量 c 为接口 I 类型，非 struct 类型，此处允许访问。
}
```

为避免逃逸，如果一个变量的类型是 `struct` 类型，那么这个变量不能将该类型使用 `mut` 修饰的函数作为一等公民来使用，只能调用这些 `mut` 函数。

示例：

<!-- compile.error -->

```cangjie
interface I {
    mut func f(): Unit
}

struct Foo <: I {
    var i = 0

    public mut func f(): Unit {
        i += 1
    }
}

main() {
    var a = Foo()
    var fn = a.f // Error, mut function 'f' of 'a' cannot be used as a first class citizen.
    var b: I = Foo()
    fn = b.f // OK
}
```

为避免逃逸，非 `mut` 的实例成员函数（包括 `lambda` 表达式）不能直接访问所在类型的 `mut` 函数，反之可以。

示例：

<!-- compile.error -->

```cangjie
struct Foo {
    var i = 0

    public mut func f(): Unit {
        i += 1
        g() // OK
    }

    public func g(): Unit {
        f() // Error, mut functions cannot be invoked in non-mut functions
    }
}

interface I {
    mut func f(): Unit {
        g() // OK
    }

    func g(): Unit {
        f() // Error, mut functions cannot be invoked in non-mut functions
    }
}
```