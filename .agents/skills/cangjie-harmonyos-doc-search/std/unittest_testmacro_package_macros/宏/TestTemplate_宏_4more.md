## `@TestTemplate` 宏

功能：`@TestTemplate` 宏可修饰抽象类，使得它成为一个[测试模版](../../unittest/unittest_samples/unittest_test_templates.md)。

## `@Timeout` 宏

功能：`@Timeout` 指示测试应在指定时间后终止。它有助于测试可能运行很长时间或陷入无限循环的复杂算法。

语法规则为 `@Timeout[expr]`

 `expr` 的类型应为 std.time.[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) 。
其修饰测试类时为每个相应的测试用例提供超时时间。

## `@Types` 宏

功能：`@Types` 宏为测试类或测试函数提供类型参数。它可以放置在测试类或测试函数上。

语法规则为 `@Types[Id1 in <Type1, Type2, Type3>, Id2 in <Type4, Type5> ...]`
其中 `Id1`、`Id2`... 是有效类型参数标识符，`Type1`、`Type2`、`Type3`... 是有效的仓颉类型。

`@Types` 宏有以下限制：

- 必须与 `@Test`， `@TestCase` 或 `@Bench` 宏共同使用。
- 一个声明只能有一个 `@Types` 宏修饰。
- 该声明必须是具有与 `@Types` 宏中列出的相同类型参数的泛型类或函数。
- 类型列表中列出的类型不能相互依赖，例如 `@Types[A in <Int64, String>, B in <List<A>>]` 将无法正确编译。但是，在为该类内的测试函数提供类型时，可以使用为测试类提供的类型。例如：

```cangjie
@Test
@Types[T in <...>]
class TestClass<T> {
    @TestCase
    @Types[U in <Array<T>>]
    func testfunc<U>() {}
}
```

该机制可以与其他测试框架功能一起使用，例如 `@Configure` 等。

## `@UnittestOption` 宏

该宏可用于注册自定义配置项。只有已注册的配置项才能与单元测试框架一起使用。宏的参数是**类型**、**选项名称**、可选的**验证器回调**和**可选的描述**。
对所有单元测试配置项的严格检查保证了控制台输入和源代码的正确性。它可以防止笔误和使用错误类型的值。

示例：

```cangjie
@UnittestOption[String, Int](optionName)
@UnittestOption[String](opt, /*validator*/ { str: String => str.size < 5 })
@UnittestOption[A, B](option3, { x: Any => ... })
@UnittestOption[Bool](needLog, /*description*/ "The option do ...")
@UnittestOption[Int](public myOpt)
```

具体规则如下：

- `@UnittestOption` 对同一个配置项不能重复使用。
- `@UnittestOption` 必须在顶层。
- 如果配置项有多种类型，则验证器回调参数应为 Any，如果只有一种类型对该选项有效，则验证器回调参数应为该具体类型。
- 验证器回调返回类型为 Bool 或 ?String。
- `true` 表示选项有效，`false` 表示选项值无效。
- ·`Some<String>` 包含选项无效原因的描述，`None<String>` 表示选项值有效。

与 `Configuration` 配合使用的示例如下：

配置项的键名称是通过首字母大写并以 `Key` 字符串开头构建的成员。例如，对于名为 `zxc` 的配置项，有效键名称将为 `KeyZxc.zxc`

```cangjie
@UnittestOption[String](opt)

@Test
func test_that_derived_type_overwrite_parent_type_value_in_configuration() {
    let conf = Configuration()

    conf.set(KeyOpt.opt, "a")
    let value = conf.get(KeyOpt.opt).getOrThrow()
    @PowerAssert(value == "a")
}
```

[Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 类正确处理继承的情况。示例如下：

```cangjie
open class Base {
    public open func str() {
        "Base"
    }
}

class Derived <: Base {
    public func str() {
        "Derived"
    }
}

@UnittestOption[Base](opt)

@Test
func test_that_derived_type_overwrite_parent_type_value_in_configuration() {
    let conf = Configuration()

    conf.set(KeyOpt.opt, Base())
    let first = conf.get(KeyOpt.opt).getOrThrow()
    @PowerAssert(first.str() == "Base")

    conf.set(KeyOpt.opt, Derived())
    let second = conf.get(KeyOpt.opt).getOrThrow()
    @PowerAssert(second.str() == "Derived")
}
```