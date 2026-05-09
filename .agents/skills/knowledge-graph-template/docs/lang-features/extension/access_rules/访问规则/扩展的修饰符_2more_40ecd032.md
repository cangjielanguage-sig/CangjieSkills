## 扩展的修饰符

扩展本身不能使用修饰符修饰。

例如，下面的例子中对 A 的直接扩展前使用了 `public` 修饰，将编译报错。

<!-- compile.error -->

```cangjie
public class A {}

public extend A {}  // Error, expected no modifier before extend
```

扩展成员可使用的修饰符有：`static`、`public`、`protected`、`internal`、`private`、`mut`。

- 使用 `private` 修饰的成员只能在本扩展内使用，外部不可见。
- 使用 `internal` 修饰的成员可以在当前包及子包（包括子包的子包）内使用，这是默认行为。
- 使用 `protected` 修饰的成员在本模块内可以被访问（受导出规则限制）。当被扩展类型是 class 时，该 class 的子类定义体也能访问。
- 使用 `static` 修饰的成员，只能通过类型名访问，不能通过实例对象访问。
- 对 `struct` 类型的扩展可以定义 `mut` 函数。

<!-- compile -->

```cangjie
package p1

public open class A {}

extend A {
    public func f1() {}
    protected func f2() {}
    private func f3() {}
    static func f4() {}
}

main() {
    A.f4()
    var a = A()
    a.f1()
    a.f2()
}
```

扩展内的成员定义不支持使用 `open`、`override`、`redef` 修饰。

<!-- compile.error -->

```cangjie
class Foo {
    public open func f() {}
    static func h() {}
}

extend Foo {
    public override func f() {} // Error
    public open func g() {} // Error
    redef static func h() {} // Error
}
```

## 扩展的孤儿规则

为一个其他 `package` 的类型实现另一个 `package` 的接口，可能造成理解上的困扰。

为了防止一个类型被意外实现不合适的接口，仓颉不允许定义孤儿扩展，即既不与接口（包含接口继承链上的所有接口）定义在同一个包中，也不与被扩展类型定义在同一个包中的接口扩展。

如下代码所示，不能在 `package c` 中，为 `package a` 里的 `Foo` 实现 `package b` 里的 `Bar`。

只能在 `package a` 或者在 `package b` 中为 `Foo` 实现 `Bar`。

<!-- compile.error -->

```cangjie
// package a
public class Foo {}

// package b
public interface Bar {}

// package c
import a.Foo
import b.Bar

extend Foo <: Bar {} // Error
```