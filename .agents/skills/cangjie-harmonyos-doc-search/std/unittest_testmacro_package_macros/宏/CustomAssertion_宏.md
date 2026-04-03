## `@CustomAssertion` 宏

功能：`@CustomAssertions` 将函数指定为用户自定义断言。

该宏修饰的函数应满足两个要求：

1. 顶层函数
2. 首个入参为 [`AssertionCtx`](../../unittest/unittest_package_api/unittest_package_classes.md#class-assertionctx) 类型。

示例如下：

```cangjie
@CustomAssertion
public func checkNotNone<T>(ctx: AssertionCtx, value: ?T): T {
    if (let Some(res) <- value) {
        return res
    }
    ctx.fail("Expected ${ctx.arg("value")} to be Some(_) but got None")
}
```

`@CustomAssertion` 的输出为树状结构，以提高 [嵌套断言](#嵌套断言) 的可读性。

例如：

```cangjie
@Test
func customTest() {
    @Assert[checkNotNone](Option<Bool>.None)
}
```

```text
[ FAILED ] CASE: customTest (120812 ns)
Assert Failed: @Assert[checkNotNone](Option < Bool >.None)
└── Assert Failed: `('Option < Bool >.None' was expected to be Some(_) but got None)`
```

### 返回值

`@CustomAssertion` 修饰的函数存在返回值时，它将被 `@Assert` 宏返回。

示例如下：

```cangjie
@Test
func testfunc() {
    let maybeValue: Option<SomeObject> = maybeReturnsSomeObject()
    let value = @Assert[checkNotNone](maybeValue)

    @Assert[otherAssertion](value)
}
```

> 注意：自定义 `@Expect` 将总是返回 `Unit` ，不论 `@CustomAssertion` 修饰的函数返回值为什么类型。

### 嵌套断言

在 `@CustomAssertion` 定义中， [`@Assert`](#assert-宏)/[`@Expect`](#expect-宏)（包括自定义断言），[`@AssertThrows`](#assertthrows-宏)/[`@ExpectThrows`](#expectthrows-宏), [`@Fail`](#fail-宏)/[`@FailExpect`](#failexpect-宏)宏均可被调用，形成嵌套。

例如：

```cangjie
@CustomAssertion
func iterableWithoutNone<T>(ctx: AssertionCtx, iter: Interable<?T>): Array<T> {
    iter |> map { it: ?T => @Assert[checkNotNone](it)} |> collectArray
}
```

```cangjie
@Test
func customTest() {
    @Assert[iterWithoutNone]([true, false, Option<Bool>.None])
}
```

```text
[ FAILED ] CASE: customTest
Assert Failed: @Assert[iterWithoutNone]([true, false, Option < Bool >.None])
└── @Assert[checkNotNone](it):
    └── Assert Failed: `('it' was expected to be Some(_) but got None)`
```

如果用户自定义的断言在被 [`@Expect`](#expect-宏) 宏调用时抛出 [`AssertException`](../../unittest/unittest_package_api/unittest_package_exceptions.md#class-assertexception) 。它会被捕获，不会往外传递。
同样，如果用户自定义的断言失败在被 [`@Assert`](#assert-宏) 宏调用时不引发异常，异常将被创建并抛出。

### 指定泛型类型

当指定泛型类型参数时，可使用与常规语法来完成。

例如：

```cangjie
@CustomAssertion
public func doesThrow<E>(ctx: AssertionCtx, codeblock: () -> Any): E where E <: Excepiton {
    ...
}

@Test
func customTest() {
    let e = @Assert[doesThrow<NoneValueException>]({ => Option<Bool>.None.getOrThrow()})
}
```