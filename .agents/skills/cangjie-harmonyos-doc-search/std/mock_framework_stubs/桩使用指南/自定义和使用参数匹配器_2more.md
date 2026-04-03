## 自定义和使用参数匹配器

为了避免重复使用相同的**参数匹配器**，可以自定义参数匹配器。

如下示例为在测试用例之间共享匹配器：

<!--compile.onlyformat-->
```cangjie
@On(foo.bar(oddNumbers())).returns("Odd")
@On(foo.bar(evenNumbers())).returns("Even")
foo.bar(0) // "Even"
foo.bar(1) // "Odd"
```

由于每个匹配器都只是 `Matchers` 类的静态函数，因此可以使用**扩展**来自定义参数匹配器。新参数匹配器需要调用现有的（实例）。

<!-- 链接至Matchers类 （自动生成的 API 手册） -->
<!--compile-->
```cangjie
import std.unittest.mock.*

extend Matchers {
    static func evenNumbers(): TypedMatcher<Int> {
        argThat {arg: Int => arg % 2 == 0}
    }

    static func oddNumbers(): TypedMatcher<Int> {
        argThat {arg: Int => arg % 2 == 1}
    }
}
```

函数参数匹配器可以包含参数。
<!--compile-->
```cangjie
import std.unittest.mock.*

extend Matchers {
    // 只接受Int参数。
    static func isDivisibleBy(n: Int): TypedMatcher<Int> {
        argThat {arg: Int => arg % n == 0}
    }
}
```

大多数匹配器函数都指定了返回类型 `TypedMatcher<T>` 。这样的匹配器只接受类型为 `T` 。在桩声明中使用参数匹配器调用时，类型为 `T` 的值应该是被打桩函数或属性 setter 的有效参数。换句话说，类型 `T` 应该是参数子类型或与参数实际类型相同。

## 设置属性和字段和顶层变量

字段和属性和顶层变量打桩的方式与函数相同，可以依[相同操作](./mock_framework_basics.md#操作-api)来配置返回值。

setter 类似于返回 `Unit` 的函数。特殊操作 `doesNothing()` 可用于 setter。

可变属性打桩的常用模式如下：

```cangjie
@On(foo.prop).returns("value")  // 配置getter
@On(foo.prop = _).doesNothing() // 忽略setter调用
```

极少场景下，我们期望可变属性的行为与字段的行为相同。要创建**合成字段**（框架生成的字段），请使用 `SyntheticField.create` 静态函数。合成字段存储由 mock 框架来管理。适用于 mock 含有可变属性和字段的接口或抽象类的场景。

<!-- 链接至SyntheticField类 （自动生成的 API 手册）-->

执行 `getsField` 和 `setsField` 桩操作将字段或顶层变量绑定到特定的调用，这些操作可以将预期配置为任何其他操作。

<!-- 待办：链接至字段操作 -->

<!--compile-->
```cangjie
import std.unittest.mock.*
import std.unittest.mock.mockmacro.*

interface Foo {
    mut prop bar: String
}

@Test
func test() {
    let foo = mock<Foo>()
    let syntheticField = SyntheticField.create(initialValue: "initial")
    @On(foo.bar).getsField(syntheticField) // 对属性的读取访问即为读取合成字段
    @On(foo.bar = _).setsField(syntheticField) // 为属性写入新值

    // 此时'bar'属性表现为字段
}
```

> **注意:**
>
> 如果多个测试用例之间共享 `SyntheticField` 对象，则该字段本身的值会在每个测试用例之前重置为 `initialValue` ，避免在测试之间共享可变状态。