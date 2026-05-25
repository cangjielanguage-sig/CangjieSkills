### 使用方法

运行 cjc 编译的可执行文件 test ，添加参数选项

```shell
./test --bench --filter=MyTest.*Test,-stringTest
```

### `--bench`

默认情况下，只有被 `@TestCase` 修饰的函数会被执行。在使用 `--bench` 的情况下只执行 `@Bench` 宏修饰的用例。

### `--filter`

如果您希望以测试类和测试用例过滤出测试的子集，可以使用 `--filter=测试类名.测试用例名` 的形式来筛选匹配的用例，例如：

1. `--filter=*` 匹配所有测试类
2. `--filter=*.*` 匹配所有测试类所有测试用例（结果和*相同）
3. `--filter=*.*Test,*.*case*` 匹配所有测试类中以 Test 结尾的用例，或者所有测试类中名字中带有 case 的测试用例
4. `--filter=MyTest*.*Test,*.*case*,-*.*myTest` 匹配所有 MyTest 开头测试类中以 Test 结尾的用例，或者名字中带有 case 的用例，或者名字中不带有 myTest 的测试用例

### `--dry-run`

执行单元测试框架而不实际运行测试。可用于查看测试用例列表。

### `--include-tags`

若需按 [`@Tag`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#tag-宏) 宏中指定的类别选择测试的子集，则可使用 `--include-tags` 或 `--exclude-tags` 运行选项。例如：

1. `--include-tags=Unittest` 运行所有的带有 `@Tag[Unittest]` 的测试用例。
2. `--include-tags=Unittest,Smoke` 运行所有的带有 `@Tag[Unittest]`和/或`@Tag[Smoke]` 的测试用例。
3. `--include-tags=Unittest+Smoke` 运行所有的带有 `@Tag[Unittest]`和`@Tag[Smoke]` 的测试用例。
4. `--include-tags=Unittest+Smoke+JiraTask3271,Backend` 运行所有的带有 `@Tag[Backend]`和/或`@Tag[Unittest, Smoke, JiraTask3271]` 的测试用例。

> **注意：**
>
> 如果没有符合指定标签类别的测试用例。框架将不运行任何内容。
> 可以与 `exclude-tags` 结合。详见 [`--exclude-tags`](./unittest_basics.md#--exclude-tags)。

### `--exclude-tags`

若需按 [`@Tag`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#tag-宏) 宏中指定的类别选择测试的子集，则可使用 `--include-tags` 或 `--exclude-tags` 运行选项。例如：

1. `--exclude-tags=Unittest` 运行所有的**未**带有 `@Tag[Unittest]` 的测试用例。
2. `--exclude-tags=Unittest,Smoke` 运行所有的**未**带有 `@Tag[Unittest]`和/或`@Tag[Smoke]` 的测试用例。
3. `--exclude-tags=Unittest+Smoke` 运行所有的**未**同时带有 `@Tag[Unittest]`、`@Tag[Smoke]` 的测试用例。
4. `--include-tags=Unittest --exclude-tags=Smoke` 运行所有带有 `@Tag[Unittest]` 但不带有 `@Tag[Smoke]` 的测试用例。

> **注意：**
>
> `exclude-tags` 的优先级高于 `include-tags`，如果用例被排除，则必定不会被执行，例如 `--include-tags=Unittest+Smoke --exclude-tags=Smoke` 则带有 `@Tag[Smoke]` 的用例不会被执行。

### `--show-tags`

若需要在测试报告中显示测试用例中 [`@Tag`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#tag-宏) 的信息，可使用 `--show-tags` 运行选项。

在 `--dry-run` 模式下，并且测试报告为 `xml` 格式时，将始终包含 `Tag` 信息。

### `--timeout-each=timeout`

使用 `--timeout-each=timeout` 选项等同于对所有的测试类使用 `@Timeout[timeout]` 修饰。若代码中已有 `@Timeout[timeout]` ，则将被代码中的超时时间覆盖，即选项的超时时间配置优先级低于代码中超时时间配置。

`timeout` 的值应符合以下语法：
    `number ('millis' | 's' | 'm' | 'h')`
例如： `10s`, `9millis` 等。

- millis: 毫秒
- s: 秒
- m: 分钟
- h: 小时