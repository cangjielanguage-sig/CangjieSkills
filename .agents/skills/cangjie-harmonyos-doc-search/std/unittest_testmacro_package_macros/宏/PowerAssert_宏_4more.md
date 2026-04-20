## `@PowerAssert` 宏

1. `@PowerAssert(leftExpr, rightExpr)` ，比较 `leftExpr` 和 `rightExpr` 值是否相同。
2. `@PowerAssert(condition: Bool)` ，比较 `condition` 是否为 `true` ，即 `@PowerAssert(condition: Bool)` 等同于 `@PowerAssert(condition: Bool, true)` 。
3. `@PowerAssert(leftExpr, rightExpr, delta: deltaExpr)` 使用 delta 参数使能近似相等功能。
4. `@PowerAssert(leftExpr <comparison_operator> rightExpr, delta: deltaExpr)` 使用 delta 参数使能近似相等功能。

`@PowerAssert` 宏对比 `@Assert` ，可显示表达式各个可被计算的子表达式的值的详细图表，包括步骤中的异常。

其打印的详细信息如下：

```text
Assert Failed: `(foo(10, y: "test" + s) == foo(s.size, y: s) + bar(a))`
                |          |        |_||  |   |_|    |   |_|| |   |_||
                |          |       "123"  |  "123"   |  "123" |    1 |
                |          |__________||  |   |______|      | |______|
                |            "test123" |  |       3         |    33  |
                |______________________|  |_________________|        |
                            0             |        1                 |
                                          |__________________________|
                                                        34
--------------------------------------------------------------------------------------------------
```

请注意，返回的 [Tokens](../../ast/ast_package_api/ast_package_classes.md#class-tokens) 是初始表达式，但包装到一些内部包装器中，这些包装器允许进一步打印中间值和异常。

## `@Skip` 宏

功能：`@Skip` 修饰已经被 `@TestCase` / `@Bench` 修饰的函数，使该测试用例被跳过。

语法规则为 `@Skip[expr]` 。

1. `expr` 暂只支持 `true` ，表达式为 `true` 时，跳过该测试，其他均为 `false` 。
2. 默认 `expr` 为 `true` 即 `@Skip[true]` == `@Skip` 。

## `@Strategy` 宏

功能：在函数上使用 `@Strategy` 可从该函数创建新的 [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 。它是一个用于组合、映射和重用策略的便捷 API。

标记为 `@Strategy` 的函数必须满足以下条件：

1. 必须显式指定返回类型。
2. 参数必须与宏参数中指定的 DSL 相对应。
3. 可以在 `@Test` 标记的类的外部和内部使用。

> 实现说明：宏展开的结果是一个具有函数名称和 [DataStrategyProcessor](../../unittest/unittest_package_api/unittest_package_classes.md#class-datastrategyprocessort) 类型的变量。 该变量可以在任何可以使用  [DataStrategy](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-datastrategy) 的地方使用。

## `@Tag` 宏

`@Tag` 宏可以应用于 `@Test` 类和 `@Test` 或 `@TestCase` 或 `@Bench` 函数，提供测试实体的元信息。后续可以通过 [`--include-tags`](../../unittest/unittest_samples/unittest_basics.md#--include-tags) 和 [`--exclude-tags`](../../unittest/unittest_samples/unittest_basics.md#--exclude-tags) 运行选项过滤带有这些标签的测试实体。

### 支持的语法

1. 单个 `@Tag` 在测试函数上。

    ```cangjie
    @Tag[Unittest]
    func test() {}
    ```

2. 单个 `@Tag` 包含多个标签名，用逗号分隔。

    ```cangjie
    @Tag[Unittest, TestAuthor]
    func test() {}
    ```

3. 多个 `@Tag` 在测试函数上。

    ```cangjie
    @Tag[Smoke]
    @Tag[Backend, JiraTask3271]
    func test() {}
    ```

### 规则与约束

- 标签应为有效的仓颉语言标识符。
- `@Tag` 内的标签列表不应为空。
- 如果 `@Tag` 放在 `@Test` 类的顶部，它会将其标签传播到其中的 `@TestCase` 函数上。

例如：

```cangjie
@Test
@Tag[Unittest]
public class UnittestClass {
    @TestCase[x in [1, 2, 3, 4, 5]]
    @Tag[JiraTask3271]
    func caseA(x: Int64) {}

    @TestCase
    func caseB() {}
}
```

等同于：

```cangjie
@Test
@Tag[Unittest]
public class UnittestClass {
    @TestCase[x in [1, 2, 3, 4, 5]]
    @Tag[Unittest]
    @Tag[JiraTask3271]
    func caseA(x: Int64) {}

    @TestCase
    @Tag[Unittest]
    func caseB() {}
}
```