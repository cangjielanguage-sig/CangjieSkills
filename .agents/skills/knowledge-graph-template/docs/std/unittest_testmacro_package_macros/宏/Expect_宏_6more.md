## `@Expect` 宏

功能：`@Expect` 声明 Expect 断言，测试函数内部使用，断言失败继续执行用例。

1. `@Expect(leftExpr, rightExpr)` ，比较 `leftExpr` 和 `rightExpr` 是否相同。
2. `@Expect(condition: Bool)` ，比较 `condition` 是否为 `true` ，即 `@Expect(condition: Bool)` 等同于 `@Expect(condition: Bool, true)` 。
3. `@Expect[customAssertion](arguments...)`, 使用指定的参数 `arguments` 调用 `customAssertion` 函数。详见 [`@CustomAssertion`](#customassertion-宏)。
4. `@Expect(leftExpr, rightExpr, delta: deltaExpr)` 使用 delta 参数使能近似相等功能。
5. `@Expect(leftExpr <comparison_operator> rightExpr, delta: deltaExpr)` 使用 delta 参数使能近似相等功能。

## `@ExpectThrows` 宏

功能：声明[预期异常的断言](../../unittest/unittest_samples/unittest_basics.md#预期异常的断言)，测试函数内部使用，断言失败继续执行用例。

## `@Fail` 宏

功能：声明[预期失败的断言](../../unittest/unittest_samples/unittest_basics.md#失败断言)，测试函数内部使用，断言失败停止用例。

## `@FailExpect` 宏

功能：声明[预期失败的断言](../../unittest/unittest_samples/unittest_basics.md#失败断言)，测试函数内部使用，断言失败继续执行用例。

## `@Measure` 宏

功能：用于为性能测试指定 [Measurement](../../unittest/unittest_package_api/unittest_package_interfaces.md#interface-measurement) 实例。只能应用于标有 `@Test` 宏的类或顶级函数的范围内。
对于每个 `Measurement`，都会进行不同的测量。因此，指定更多 `Measurement` 实例，将花费更多时间进行性能测试。
默认值为 [TimeNow](../../unittest/unittest_package_api/unittest_package_structs.md#struct-timenow)() ，它在内部使用 [DateTime](../../time/time_package_api/time_package_structs.md#struct-datetime).now() 进行测量。

例如：

```cangjie
@Test
@Measure[TimeNow(), TimeNow(Nanos)]
class BenchClass {
    @Bench
    func someBench() {
        for (i in 0..1000) {
            1e3 * Float64(i)
        }
    }
}
```

输出的测试报告如下：

```text
| Case      | Measurement  |   Median |         Err |   Err% |     Mean |
|:----------|:-------------|---------:|------------:|-------:|---------:|
| someBench | Duration     | 6.319 us | ±0.00019 us |  ±0.0% | 6.319 us |
|           |              |          |             |        |          |
| someBench | Duration(ns) |  6308 ns |   ±0.147 ns |  ±0.0% |  6308 ns |
```

`CSV` 报告如下：

```csv
Case,Args,Median,Err,Err%,Mean,Unit,Measurement
"someBench",,"6319","0.185632","0.0","6319","ns","Duration"
"someBench",,"6308","0.146873","0.0","6308","ns","Duration(ns)"
```

## `@Parallel` 宏

功能：`@Parallel` 宏可以修饰测试类。被 `@Parallel` 修饰的测试类中的测试用例可并行执行。该配置仅在 `--parallel` 运行模式下生效。

1. 所有相关的测试用例应该各自独立，不依赖于任何可变的共享的状态值。
2. `beforeAll()` 和 `afterAll()` 应该是可重入的，以便可以在不同的进程中多次运行。
3. 需要并行化的测试用例本身应耗时较长。否则并行化引入的多次 `beforeAll()` 和 `afterAll()` 可能会超过并行化的收益。
4. 不允许与 `@Bench` 同时使用。由于性能用例对底层资源敏感，用例是否并行执行，将影响性能用例的结果，因此禁止与 `@Bench` 同时使用。