### 操作 API

mock 框架提供 API 来指定桩操作。触发桩后，打桩声明会执行指定的操作。如果调用与相应的 `@On` 宏调用指定的签名匹配，则会触发桩。

每个桩函数**必须**指定一个操作。
`@On` 宏调用返回的 `ActionSelector` 子类型会定义可用操作。操作列表取决于所打桩的实体。

<!-- 链接至操作文档 -->

#### 通用（操作）

适用于所有桩的操作。

* `throws(exception: Exception)`：抛出 `exception` 。
* `throws(exceptionFactory: () -> Exception)`：调用 `exceptionFactory` 去构造桩触发时抛出的异常。
* `fails()`：如果触发了桩，则测试失败。

> **注意：**
>
> `throws` 用于测试桩声明抛出异常时的系统行为。`fails` 用于测试桩声明是否未被调用。

<!--compile.onlyformat-->
```cangjie
@On(service.request()).throws(TimeoutException())
```

#### 函数和属性/字段 Getter 和顶层变量读操作

**R** 表示对应成员的返回类型。

* `returns()`：不做任何操作并返回 `()`，仅当 `R` 为 `Unit` 时可用。
* `returns(value: R)`：返回 `value` 。
* `returns(valueFactory: () -> R)`：调用 `valueFactory` 去构造桩触发时抛出的异常。
* `returnsConsecutively(values: Array<R>)`, `returnsConsecutively(values: ArrayList<R>)`：触发桩时，返回 `values` 中的下一个元素。

```cangjie
@On(foo.bar()).returns(2) // 返回 0
@On(foo.bar()).returnsConsecutively(1, 2, 3) // 依次返回 1，2，3
```

#### 属性/字段 Setter 和顶层变量写操作

* `doesNothing()`：忽略调用，不做任何操作。类似于返回 Unit 的函数的 `returns()`。
更多信息详见[这里](./mock_framework_stubs.md#设置属性和字段和顶层变量)。

#### spy 操作

对于 spy 对象，可以使用其他操作来委托监控实例。

* `callsOriginal()` ：调用原始方法。
* `getsOriginal()` ：调用原始属性 getter 或获取原始实例中的字段值。
* `setsOriginal()` ：调用原始属性 setter 或设置原始实例中的字段值。

### 预期

定义桩时会隐式或显式地向桩附加预期。桩**可以**定义期望的基数。**操作**（ `fails` 和 `returnsConcesecutively` 除外）返回`CardinalitySelector` 的实例，该实例可以使用**基数说明符**自定义预期。

**CardinalitySelector** 定义了如下函数：

* `once()`
* `atLeastOnce()`
* `anyTimes()`
* `times(expectedTimes: Int64)`
* `times(min!: Int64, max!: Int64)`
* `atLeastTimes(minTimesExpected: Int64)`

`anyTimes` 说明符用于提升预期，即如果桩从未被触发，测试也不会失败。其他说明符都暗示了测试代码中特定桩的调用次数上下限。只要桩被触发的次数比预期的多，测试就会立即失败。下限在测试代码执行完毕后进行检查。

示例：

<!--run -->
```cangjie
import std.unittest.mock.*
import std.unittest.mock.mockmacro.*

class Foo {
    func bar() { }
}

@Test
func tooFewInvocations() {
    let foo = mock<Foo>()
    @On(foo.bar()).returns().times(2)
    foo.bar()
}
```

输出：

```text
Expectation failed
    Too few invocations for stub foo.bar() declared at example_test.cj:9.
        Required: exactly 2 times
        Actual: 1
        Invocations handled by this stub occured at:
            example_test.cj:6
```

如果没有自定义预期，mock 框架使用默认预期：

| 操作| 默认期望基数| 允许自定义基数|
| ----   |  ---                |  ---                      |
| fails | 不可调用| 否                      |
| returns | atLeastOnce        | 是                      |
| returnsConsecutively | times(values.size)        | 否          |
| throws | atLeastOnce        | 是                       |
| doesNothing | atLeastOnce        | 是                  |
| (calls/gets/sets)Original | atLeastOnce        | 是    |