## struct 成员函数

`struct` 成员函数分为实例成员函数和静态成员函数（使用 `static` 修饰符修饰），二者的区别在于：实例成员函数只能通过 `struct` 实例访问，静态成员函数只能通过 `struct` 类型名访问；静态成员函数中不能访问实例成员变量，也不能调用实例成员函数，但在实例成员函数中可以访问静态成员变量以及静态成员函数。

下例中，`area` 是实例成员函数，`typeName` 是静态成员函数。

<!-- compile -->

```cangjie
struct Rectangle {
    let width: Int64 = 10
    let height: Int64 = 20

    public func area() {
        this.width * this.height
    }

    public static func typeName(): String {
        "Rectangle"
    }
}
```

实例成员函数中可以通过 `this` 访问实例成员变量，例如：

<!-- compile -->

```cangjie
struct Rectangle {
    let width: Int64 = 1
    let height: Int64 = 1

    public func area() {
        this.width * this.height
    }
}
```

## struct 成员的访问修饰符

`struct` 的成员包括成员变量、成员属性、构造函数、成员函数、操作符函数（详见[操作符重载](../function/operator_overloading.md)），这些成员可使用四种访问修饰符：`private`、`internal`、`protected` 和 `public`，缺省的修饰符是 `internal`。

- `private` 表示在 `struct` 定义内可见。
- `internal` 表示仅当前包及子包（包括子包的子包，详见[包](../package/toplevel_access.md)章节）内可见。
- `protected` 表示当前模块（详见[包](../package/toplevel_access.md)章节）可见。
- `public` 表示模块内外均可见。

下面的例子中，`width` 是 `public` 修饰的成员，在类外可以访问，`height` 是缺省访问修饰符的成员，仅在当前包及子包可见，其他包无法访问。

<!-- compile.error -->

```cangjie
package a
public struct Rectangle {
    public var width: Int64
    var height: Int64
    private var area: Int64

    public init(width: Int64, height: Int64, area: Int64) {
        this.width = width
        this.height = height
        this.area = area
    }
}

func samePkgFunc() {
    var r = Rectangle(10, 20, 40)
    r.width = 8               // OK: public 'width' can be accessed here
    r.height = 24             // OK: 'height' has no modifier and can be accessed here
    r.area = 30               // Error, private 'area' can't be accessed here
}
```

<!-- compile.error -->
<!-- cfg="-p b --output-type=staticlib" -->
<!-- cfg="liba.a" -->

```cangjie
package b
import a.*

main() {
    r.width = 8     // OK: public 'width' can be accessed here
    r.height = 24   // Error, no modifier 'height' can't be accessed here
    r.area = 30     // Error, private 'area' can't be accessed here
}
```

## 禁止递归 struct

递归和互递归定义的 `struct` 均是非法的。例如：

<!-- compile.error -->

```cangjie
struct R1 { // Error, 'R1' recursively references itself
    let other: R1
}
struct R2 { // Error, 'R2' and 'R3' are mutually recursive
    let other: R3
}
struct R3 { // Error, 'R2' and 'R3' are mutually recursive
    let other: R2
}
```