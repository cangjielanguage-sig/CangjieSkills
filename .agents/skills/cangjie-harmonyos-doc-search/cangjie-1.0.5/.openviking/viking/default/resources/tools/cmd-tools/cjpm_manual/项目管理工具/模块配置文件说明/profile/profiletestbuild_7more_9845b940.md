#### "profile.test.build"

用于指定支持的编译选项，其列表如下:

- `compile-option` 是一个包含附加 `cjc` 编译选项的字符串。为顶级 `compile-option` 字段做补充
- `lto` 指定是否开启 `LTO` 优化编译模式，该值可为 `thin` 或 `full` ，仅 `Linux` 平台支持该功能
- `mock` 显式设置 `mock` 模式，可能的选项：`on`、`off`、`runtime-error` 。对 `test` / `build` 子命令默认值为 `on`，对于 `bench` 子命令默认值为 `runtime-error`

#### "profile.test.env"

用于在 `test` 命令时运行可执行文件时配置临时环境变量，`key` 值为需要配置的环境变量的名称，有如下配置项:

- `value` 指定配置的环境变量值
- `splice-type` 指定环境变量的拼接方式，非必填，不配置时默认为 `absent`，共有以下四种取值：
    - `absent`: 该配置仅在环境内不存在同名环境变量时生效，若存在同名环境变量则忽略该配置
    - `replace`: 该配置会替代环境中已有的同名环境变量
    - `prepend`: 该配置会拼接在环境中已有的同名环境变量之前
    - `append`: 该配置会拼接在环境中已有的同名环境变量之后

#### "profile.bench"

```text
[profile.bench] # 使用举例
no-color = true
random-seed = 10
report-path = "bench_report"
baseline-path = ""
report-format = "csv"
verbose = true
```

测试配置支持指定编译和运行测试用例时的选项，所有字段均可缺省，不配置时不生效，顶层模块设置的 `profile.bench` 项才会生效。选项列表与 `cjpm bench` 提供的控制台执行选项一致。如果选项在配置文件和控制台中同时被配置，则控制台中的选项优先级高于配置文件中的选项。`profile.bench` 支持的运行时选项:

- `filter` 指定用例过滤器，参数值类型为字符串, 格式与 [bench 命令说明](#bench)中 `--filter` 的值格式一致
- `option:<value>` 与 `@Configure` 协同定义运行选项。例如，如下选项：
    - `random-seed` 用来指定随机种子的值, 参数值类型为正整数
    - `no-color` 指定执行结果在控制台中是否无颜色显示，值为 `true` 或 `false`
    - `report-path` 指定测试执行后的报告生成路径（不能通过 `@Configure` 配置）
    - `report-format` 指定报告输出格式，当前单元测试报告仅支持 `xml` 格式（可忽略大小写），使用其它值将会抛出异常（不能通过 `@Configure` 配置）, 性能测试报告仅支持 `csv` 和 `csv-raw` 格式
    - `verbose` 指定显示编译过程详细信息，参数值类型为 `BOOL`, 即值可为 `true` 或 `false`
    - `baseline-path` 与当前性能结果进行比较的现有报告的路径。默认情况下它使用 `--report-path` 值。

#### "profile.bench.build"

用于指定为 `cjpm bench` 构建可执行文件时使用的附加编译选项。配置与 `profile.test.build` 相同。

#### "profile.bench.env"

支持配置在 `bench` 命令时运行可执行文件时的环境变量配置，配置方式同 `profile.test.env`。

#### "profile.run"

运行可执行文件时的选项，支持配置在 `run` 命令时运行可执行文件时的环境变量配置 `env`，配置方式同 `profile.test.env`。

#### "profile.customized-option"

```text
[profile.customized-option]
cfg1 = "--cfg=\"feature1=lion, feature2=cat\""
cfg2 = "--cfg=\"feature1=tiger, feature2=dog\""
cfg3 = "-O2"
```

自定义透传给 `cjc` 的选项，通过 `--cfg1 --cfg3` 使能，每个模块设置的 `customized-option` 对该模块内的所有包生效。例如，执行 `cjpm build --cfg1 --cfg3` 命令时，透传给 `cjc` 的命令则为 `--cfg="feature1=lion, feature2=cat" -O2`。

> **注意：**
>
> 这里的条件值必须是一个合法的标识符。