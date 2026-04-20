#### "profile.test"

```text
[profile.test] # 使用举例
parallel=true
filter=*.*
no-color = true
timeout-each = "4m"
random-seed = 10
bench = false
report-path = "reports"
report-format = "xml"
verbose = true
[profile.test.build]
  compile-option = ""
  lto = "thin"
  mock = "on"
[profile.test.env]
MY_ENV = { value = "abc" }
cjHeapSize = { value = "32GB", splice-type = "replace" }
PATH = { value = "/usr/bin", splice-type = "prepend" }
```

测试配置支持指定编译和运行测试用例时的选项，所有字段均可缺省，不配置时不生效，顶层模块设置的 `profile.test` 项才会生效。选项列表与 `cjpm test` 提供的控制台执行选项一致。如果选项在配置文件和控制台中同时被配置，则控制台中的选项优先级高于配置文件中的选项。`profile.test` 支持的运行时选项：

- `filter` 指定用例过滤器，参数值类型为字符串，格式与 [test 命令说明](#test)中 `--filter` 的值格式一致
- `timeout-each <value>` 中 `value` 的格式为 `%d[millis|s|m|h]`，为每个测试用例指定默认的超时时间
- `parallel` 指定测试用例并行执行的方案，`value` 的形式如下所示：
    - `<BOOL>` 值为 `true` 或 `false`，指定为 `true` 时，测试类可被并行运行，并行进程个数将受运行系统上的 CPU 核数控制
    - `nCores` 指定并行的测试进程个数应该等于可用的 CPU 核数
    - `NUMBER` 指定并行的测试进程个数值。该数值应该为正整数
    - `NUMBERnCores` 指定并行的测试进程个数值为可用的 CPU 核数的指定数值倍。该数值应该为正数（支持浮点数或整数）
- `option:<value>` 与 `@Configure` 协同定义运行选项。例如，如下选项：
    - `random-seed` 用来指定随机种子的值，参数值类型为正整数
    - `no-color` 指定执行结果在控制台中是否无颜色显示，值为 `true` 或 `false`
    - `report-path` 指定测试执行后的报告生成路径（不能通过 `@Configure` 配置）
    - `report-format` 指定报告输出格式，当前单元测试报告仅支持 `xml` 格式（可忽略大小写），使用其它值将会抛出异常（不能通过 `@Configure` 配置），性能测试报告仅支持 `csv` 和 `csv-raw` 格式
    - `verbose` 指定显示编译过程详细信息，参数值类型为 `BOOL`，即值可为 `true` 或 `false`