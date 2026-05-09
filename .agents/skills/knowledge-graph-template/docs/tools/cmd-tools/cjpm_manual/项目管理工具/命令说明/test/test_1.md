### test

`test` 用于编译并运行仓颉文件的单元测试用例，运行后打印测试结果，编译产物默认存放在 `target/release/unittest_bin` 文件夹。单元测试用例代码的写法可参考《仓颉编程语言标准库 API》中 `std.unittest` 库的说明。

该命令可以指定待测试的单包路径（支持指定多个单包，形如 `cjpm test path1 path2`），不指定路径时默认执行模块级别的单元测试。执行模块级别的单元测试时，默认只进行当前模块的单元测试，直接或间接依赖的其他所有模块内的测试均不会被执行。`test` 执行前提是当前项目能够 `build` 编译成功。

模块的单元测试代码结构如下所示，其中 `xxx.cj` 存放该包的源码，`xxx_test.cj` 存放单元测试代码：

```text
└── src
│    ├── koo
│    │    ├── koo.cj
│    │    └── koo_test.cj
│    ├── zoo
│    │    ├── zoo.cj
│    │    └── zoo_test.cj
│    ├── main.cj
│    └── main_test.cj
└── cjpm.toml
```

1. 单模块测试场景

    ```text
    输入: cjpm test
    进度报告：
    group test.koo                                    100% [||||||||||||||||||||||||||||] ✓    (00:00:01)
    group test.zoo                                      0% [----------------------------]      (00:00:00)
    test TestZ.sayhi                                                                           (00:00:00)

    passed: 1, failed: 0                                  33% [|||||||||-------------------]  1/3 (00:00:01)

    输出:
    --------------------------------------------------------------------------------------------------
    TP: test, time elapsed: 177921 ns, RESULT:
        TCS: TestM, time elapsed: 177921 ns, RESULT:
        [ PASSED ] CASE: sayhi (177921 ns)
        Summary: TOTAL: 1
        PASSED: 1, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    TP: test.koo, time elapsed: 134904 ns, RESULT:
        TCS: TestK, time elapsed: 134904 ns, RESULT:
        [ PASSED ] CASE: sayhi (134904 ns)
        Summary: TOTAL: 1
        PASSED: 1, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    TP: test.zoo, time elapsed: 132013 ns, RESULT:
        TCS: TestZ, time elapsed: 132013 ns, RESULT:
        [ PASSED ] CASE: sayhi (132013 ns)
        Summary: TOTAL: 1
        PASSED: 1, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    Project tests finished, time elapsed: 444838 ns, RESULT:
    TP: test.*, time elapsed: 312825 ns, RESULT:
        PASSED:
        TP: test.zoo, time elapsed: 132013 ns
        TP: test.koo, time elapsed: 312825 ns
        TP: test, time elapsed: 312825 ns
    Summary: TOTAL: 3
        PASSED: 3, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    cjpm test success
    ```

2. 单包测试场景

    ```text
    输入: cjpm test src/koo
    输出:
    --------------------------------------------------------------------------------------------------
    TP: test.koo, time elapsed: 160133 ns, RESULT:
        TCS: TestK, time elapsed: 160133 ns, RESULT:
        [ PASSED ] CASE: sayhi (160133 ns)
        Summary: TOTAL: 1
        PASSED: 1, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    Project tests finished, time elapsed: 160133 ns, RESULT:
    TP: test.*, time elapsed: 160133 ns, RESULT:
        PASSED:
        TP: test.koo, time elapsed: 160133 ns
    Summary: TOTAL: 1
        PASSED: 1, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    cjpm test success
    ```

3. 多包测试场景