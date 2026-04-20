## `@AfterAll` 宏

功能：声明测试类中的函数为[测试生命周期](../../unittest/unittest_samples/unittest_basics.md#测试生命周期)函数。被该宏修饰的函数在所有测试用例之后运行一次。

## `@AfterEach` 宏

功能：声明测试类中的函数为[测试生命周期](../../unittest/unittest_samples/unittest_basics.md#测试生命周期)函数。被该宏修饰的函数在每个测试用例之后运行一次。

## `@Assert` 宏

功能：`@Assert` 声明 Assert 断言，测试函数内部使用，断言失败停止用例。

1. `@Assert(leftExpr, rightExpr)` ，比较 `leftExpr` 和 `rightExpr` 值是否相同。
2. `@Assert(condition: Bool)` ，比较 `condition` 是否为 `true` ，即 `@Assert(condition: Bool)` 等同于 `@Assert(condition: Bool, true)` 。
3. `@Assert[customAssertion](arguments...)`, 使用指定的参数 `arguments` 调用 `customAssertion` 函数，详见 [`@CustomAssertion`](#customassertion-宏)。
4. `@Assert(leftExpr, rightExpr, delta: deltaExpr)` 使用 delta 参数使能近似相等功能。
5. `@Assert(leftExpr <comparison_operator> rightExpr, delta: deltaExpr)` 使用 delta 参数使能近似相等功能。

## `@AssertThrows` 宏

功能：声明[预期异常的断言](../../unittest/unittest_samples/unittest_basics.md#预期异常的断言)，测试函数内部使用，断言失败停止用例。

## `@BeforeAll` 宏

功能：声明测试类中的函数为[测试生命周期](../../unittest/unittest_samples/unittest_basics.md#测试生命周期)函数。被该宏修饰的函数在所有测试用例之前运行一次。

## `@BeforeEach` 宏

功能：声明测试类中的函数为[测试生命周期](../../unittest/unittest_samples/unittest_basics.md#测试生命周期)函数。被该宏修饰的函数在每个测试用例之前运行一次。