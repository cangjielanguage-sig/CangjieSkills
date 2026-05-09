### bench

`bench` 用于执行测试文件的性能用例并直接打印测试结果。编译产物默认存放在 `target/release/unittest_bin` 文件夹中。性能用例由 `@Bench` 宏标注。更多关于如何编写性能用例代码的详细信息，请参见《仓颉编程语言标准库 API》中对 `std.unittest` 库的描述。

该命令可以指定待测试的单包路径（支持指定多个单包，形如 `cjpm bench path1 path2`），不指定路径时默认执行模块级别的单元测试。与 `test` 一样，执行模块级别的单元测试时，默认只进行当前模块的单元测试。`bench` 执行前提是当前项目能够 `build` 编译成功。

与 `test` 子命令类似，如果您有 `xxx.cj` 文件，则 `xxx_test.cj` 也可以包含性能测试用例。

```text
输入: cjpm bench
输出:
TP: bench, time elapsed: 8107939844 ns, RESULT:
    TCS: Test_UT, time elapsed: 8107939844 ns, RESULT:
    | Case       |   Median |         Err |   Err% |     Mean |
    |:-----------|---------:|------------:|-------:|---------:|
    | Benchmark1 | 5.438 ns | ±0.00439 ns |  ±0.1% | 5.420 ns |
Summary: TOTAL: 1
    PASSED: 1, SKIPPED: 0, ERROR: 0
    FAILED: 0
--------------------------------------------------------------------------------------------------
Project tests finished, time elapsed: 8107939844 ns, RESULT:
TP: bench.*, time elapsed: 8107939844 ns, RESULT:
    PASSED:
    TP: bench, time elapsed: 8107939844 ns, RESULT:
Summary: TOTAL: 1
    PASSED: 1, SKIPPED: 0, ERROR: 0
    FAILED: 0
```

`bench` 有多个可配置项：