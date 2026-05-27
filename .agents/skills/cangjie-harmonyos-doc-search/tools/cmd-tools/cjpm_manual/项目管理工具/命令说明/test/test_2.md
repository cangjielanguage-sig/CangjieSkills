```text
    输入: cjpm test src/koo src
    输出:
    --------------------------------------------------------------------------------------------------
    TP: test.koo, time elapsed: 168204 ns, RESULT:
        TCS: TestK, time elapsed: 168204 ns, RESULT:
        [ PASSED ] CASE: sayhi (168204 ns)
        Summary: TOTAL: 1
        PASSED: 1, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    TP: test, time elapsed: 171541 ns, RESULT:
        TCS: TestM, time elapsed: 171541 ns, RESULT:
        [ PASSED ] CASE: sayhi (171541 ns)
        Summary: TOTAL: 1
        PASSED: 1, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    Project tests finished, time elapsed: 339745 ns, RESULT:
    TP: test.*, time elapsed: 339745 ns, RESULT:
        PASSED:
        TP: test.koo, time elapsed: 339745 ns
        TP: test, time elapsed: 339745 ns
    Summary: TOTAL: 2
        PASSED: 2, SKIPPED: 0, ERROR: 0
        FAILED: 0
    --------------------------------------------------------------------------------------------------
    cjpm test success
    ```

`test` 有多个可配置项：