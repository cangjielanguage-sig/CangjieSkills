### build

`build` 用于构建当前仓颉项目，执行该命令前会先检查依赖项，检查通过后调用 `cjc` 进行构建。

`build` 有多个可配置项：

- `-i, --incremental` 用于指定增量编译，默认情况下是全量编译
- `-j, --jobs <N>` 用于指定并行编译的最大并发数，最终的最大并发数取 `N` 和 `2倍 CPU 核数` 的最小值
- `-V, --verbose` 用于展示编译日志
- `-g` 用于生成 `debug` 版本的输出产物
- `--coverage` 用于生成覆盖率信息，默认情况下不开启覆盖率功能
- `--cfg` 指定后，能够透传 `cjpm.toml` 中的自定义 `cfg` 选项，`cjpm.toml` 中的配置可参考 profile.customized-option 章节
- `-m, --member <value>` 仅可在工作空间下使用，可用于指定单个模块作为编译入口
- `--target <value>` 指定后，可交叉编译代码到目标平台，`cjpm.toml` 中的配置可参考 [target](#target) 章节
- `--target-dir <value>` 用于指定输出产物的存放路径
- `-o, --output <value>` 用于指定输出可执行文件的名称，默认名称为 `main`（`Windows` 系统下则默认为 `main.exe`）。注意，当前不支持编译名称为 `cjc` 的可执行文件
- `-l, --lint` 用于在编译时调用仓颉语言静态检查工具进行代码检查
- `--mock` 带有此选项的构建版本中的类可用于在测试中进行 `mock` 测试
- `--skip-script` 配置后，将会跳过构建脚本的编译运行

> **注意：**
>
> - `-i, --incremental` 选项仅会开启 `cjpm` 包级别的增量编译。开发者可以在配置文件的 `compile-option` 字段自行透传 `--incremental-compile` 和 `--experimental` 编译选项，从而开启 `cjc` 编译器提供的函数粒度增量功能。
> - `-i, --incremental` 选项目前仅支持基于源码的增量分析。如果导入的库内容有变更，需要开发者重新使用全量方式构建。

编译生成的中间文件默认会存放在 `target` 文件夹，而可执行文件会根据编译模式存放到 `target/release/bin` 或 `target/debug/bin` 文件夹。运行可执行文件的方式可参考 `run`。

为了提供可复制的构建，此命令会创建 `cjpm.lock` 文件，该文件包含所有可传递依赖项的确切版本，这些依赖项将用于所有后续构建，需要更新该文件时请使用 `update` 命令。如果有必要保证每个项目参与者都有可复制的构建，那么此文件应提交到版本控制系统中。

例如：

```text
输入: cjpm build -V
输出:
compile package module1.package1: cjc --import-path "target/release" --output-dir "target/release/module1" -p "src/package1" --output-type=staticlib -o libmodule1.package1.a
compile package module1: cjc --import-path "target/release" --output-dir "target/release/bin" -p "src" --output-type=exe -o main
cjpm build success
```

```text
输入: cjpm build
输出: cjpm build success
```

> **注意：**
>
> 根据仓颉包管理规格，只有符合要求的有效源码包才能被正确纳入编译范围。如果编译时出现 `no '.cj' file` 相关的告警，很可能是因为对应包不符合规范导致源码文件不被编译。如果出现这种情况，请参考[仓颉包管理规格说明](#仓颉包管理规格说明)修改代码目录结构。

在执行 `cjpm build` 之前，`cjpm` 会对当前模块或工作空间进行包依赖关系检查。若发现包之间存在相互导入关系形成依赖闭环，构建将被中止并返回错误信息，提示循环依赖路径。

例如，模块 `demo` 的源代码目录结构如下：

```text
src
├── main.cj
├── aoo
│   └── a.cj
├── boo
│   └── b.cj
└── coo
    └── c.cj
```

依赖关系为：包 `demo.aoo` 导入包 `demo.boo`，包 `demo.boo` 导入包 `demo.coo`，包 `demo.coo` 导入包 `demo.aoo`，三个包之间的依赖导入形成闭环，导致循环依赖：

```text
输入: cjpm build
输出:
cyclic dependency:
demo.boo -> demo.coo
demo.coo -> demo.aoo
demo.aoo -> demo.boo

Error: cjpm build failed
```