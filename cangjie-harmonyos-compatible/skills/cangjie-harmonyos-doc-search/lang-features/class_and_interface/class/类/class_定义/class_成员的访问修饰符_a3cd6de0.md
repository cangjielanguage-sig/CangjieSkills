### class 成员的访问修饰符

对于 `class` 的成员（包括成员变量、成员属性、构造函数、成员函数），可以使用的访问修饰符有 4 种访问修饰符修饰：`private`、`internal`、`protected` 和 `public`，缺省的含义是 `internal`。

- `private` 表示在 `class` 定义内可见。
- `internal` 表示仅当前包及子包（包括子包的子包，详见[包](../package/toplevel_access.md)）内可见。
- `protected` 表示当前模块（详见[包](../package/toplevel_access.md)）及当前类的子类可见。
- `public` 表示模块内外均可见。

<!-- compile.error -error-->

```cangjie
package a

public open class Rectangle {
    public var width: Int64
    protected var height: Int64
    private var area: Int64
    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
        this.area = this.width * this.height
    }
    init(width: Int64, height: Int64, multiple: Int64) {
        this.width = width
        this.height = height
        this.area = width * height * multiple
    }
}

func samePkgFunc() {
    var r = Rectangle(10, 20) // OK: constructor 'Rectangle' can be accessed here
    r.width = 8               // OK: public 'width' can be accessed here
    r.height = 24             // OK: protected 'height' can be accessed here
    r.area = 30               // Error, private 'area' cannot be accessed here
}
```

<!-- compile.error -error-->

```cangjie
package b
import a.*

public class Cuboid <: Rectangle {
    private var length: Int64
    public init(width: Int64, height: Int64, length: Int64) {
        super(width, height)
        this.length = length
    }
    public func volume() {
        this.width * this.height * this.length // OK: protected 'height' can be accessed here
    }
}

main() {
    var r = Rectangle(10, 20, 2) // Error, Rectangle has no `public` constructor with three parameters
    var c = Cuboid(20, 20, 20)
    c.width = 8               // OK: public 'width' can be accessed here
    c.height = 24             // Error, protected 'height' cannot be accessed here
    c.area = 30               // Error, private 'area' cannot be accessed here
}
```