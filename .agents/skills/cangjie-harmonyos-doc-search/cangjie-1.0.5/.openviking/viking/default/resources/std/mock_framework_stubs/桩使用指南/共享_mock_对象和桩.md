## 共享 mock 对象和桩

测试需要大量使用 mock 对象时可以多个测试用例共享 mock 对象和/或桩。
可以在任何位置创建 mock 或 spy 对象。然而，如果误将 mock 对象从一个测试用例泄漏到另一个测试用例，可能导致顺序依赖问题或测试不稳定。因此，不建议这样操作，mock 框架也会检测这类情况。
在同一测试类下的测试用例之间共享 mock 或 spy 对象时，可以将它们放在该类的实例变量中。

桩声明中隐含了预期，因此更难处理共享桩。测试用例之间不能共享预期。
可以声明桩的位置：

* 测试用例主体（无论是 `@Test` 函数还是`@Test`类中的`@TestCase`）：检查预期。
* 在 `@Test` 类的 `BeforeAll` 宏修饰的函数或者 `beforeAll` 函数中：在测试用例之间共享桩。这样的桩不能声明预期，预期也不会被检查。不允许使用基数说明符。只允许 `returns(value)`、`throws(exception)`、`fails()`、`callsOriginal()` 等*无状态*操作。可以将这些桩视为具有隐式 `anyTimes()` 基数。
* 如果测试用例的预期相同，则可以在测试用例主体中提取和调用函数（测试类中非测试用例的成员函数）。

> **说明：**
>
> 不要在测试类构造函数中声明桩。否则可能导致框架运行内部错误。

在测试用例主体（`@Test`类中的`@TestCase`）中声明桩的示例：

<!--compile-testBar0-->
```cangjie
import std.unittest.mock.*
import std.unittest.mock.mockmacro.*

class Foo {
    public func bar(x: Int64): String {
        match (x) {
            case 0 => "zero"
            case 1 => "one"
            case _ => "default"
        }
    }
}

@Test
class TestFoo {
    let foo = mock<Foo>()

    func setupDefaultStubs() {
        @On(foo.bar(_)).returns("default")
    }

    @TestCase
    func testZero() {
        setupDefaultStubs()
        @On(foo.bar(0)).returns("zero")

        foo.bar(0) // 返回"zero"
        foo.bar(1) // 返回"default"
    }

    @TestCase
    func testOne() {
        setupDefaultStubs()
        @On(foo.bar(0)).returns("zero")
        foo.bar(0) // 返回"zero"

        // 预期失败，桩已声明但从未使用
    }
}
```

在 `@Test` 类的 `beforeAll` 函数中使用的示例：

<!--compile-testBar1-->
```cangjie
import std.unittest.mock.*
import std.unittest.mock.mockmacro.*

@Test
class TestFoo2 {
    let foo = mock<Foo>()

    // 单元测试框架会在执行测试用例之前调用以下内容
    @BeforeAll
    public func beforeAll(): Unit {
        // 在所有测试用例之间共享默认行为
        // 此桩无需在每个测试用例中使用
        @On(foo.bar(_)).returns("default")
    }

    @TestCase
    func testZero() {
        @On(foo.bar(0)).returns("zero") // 本测试用例中需要使用此桩
        foo.bar(0) // 返回 "zero"
        foo.bar(1) // 返回 "default"
    }

    @TestCase
    func testOne() {
        @On(foo.bar(0)).returns("one")
        foo.bar(0) // 返回 "one"
    }
}
```