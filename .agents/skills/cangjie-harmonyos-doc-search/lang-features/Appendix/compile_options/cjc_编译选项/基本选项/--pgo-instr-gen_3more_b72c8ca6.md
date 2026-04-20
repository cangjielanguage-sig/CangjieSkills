### `--pgo-instr-gen`

使能插桩编译，生成携带插桩信息的可执行程序。

编译 macOS 与 Windows 目标时暂不支持使用该功能。

`PGO`（全称 `Profile-Guided Optimization`）是一种常用的编译优化技术，通过使用运行时 profiling 信息进一步提升程序性能。`Instrumentation-based PGO` 是使用插桩信息的一种 `PGO` 优化手段，它通常包含三个步骤：

1. 编译器对源码插桩编译，生成插桩后的可执行程序（instrumented program）；
2. 运行插桩后的可执行程序，生成配置文件；
3. 编译器使用配置文件，再次对源码进行编译。

```shell
# 生成支持源码执行信息统计（携带插桩信息）的可执行程序 test
$ cjc test.cj --pgo-instr-gen -o test
# 运行可执行程序 test 结束后，生成 default.profraw 配置文件
$ ./test
```

### `--pgo-instr-use=<.profdata>`

使用指定 `profdata` 配置文件指导编译并生成优化后的可执行程序。

编译 macOS 目标时暂不支持使用该功能。

> **注意：**
>
> `--pgo-instr-use` 编译选项仅支持格式为 `profdata` 的配置文件。可使用 `llvm-profdata` 工具可将 `profraw` 配置文件转换为 `profdata` 配置文件。

```shell
# 将 `profraw` 文件转换为 `profdata` 文件。
$ LD_LIBRARY_PATH=$CANGJIE_HOME/third_party/llvm/lib:$LD_LIBRARY_PATH $CANGJIE_HOME/third_party/llvm/bin/llvm-profdata merge default.profraw -o default.profdata
# 使用指定 `default.profdata` 配置文件指导编译并生成优化后的可执行程序 `testOptimized`
$ cjc test.cj --pgo-instr-use=default.profdata -o testOptimized
```

### `--target <value>` <sup>[frontend]</sup>

指定编译的目标平台的 triple。

参数 `<value>` 一般为符合以下格式的字符串：`<arch>(-<vendor>)-<os>(-<env>)`。其中：

- `<arch>` 表示目标平台的系统架构，例如 `aarch64`，`x86_64` 等；
- `<vendor>` 表示开发目标平台的厂商，常见的例如 `apple` 等，在没有明确平台厂商或厂商不重要的情况下也经常写作 `unknown` 或直接省略；
- `<os>` 表示目标平台的操作系统，例如 `Linux`，`Win32` 等；
- `<env>` 表示目标平台的 ABI 或标准规范，用于更细粒度地区分同一操作系统的不同运行环境，例如 `gnu`，`musl` 等。在操作系统不需要根据 `<env>` 进行更细地区分的时候，此项也可以省略。

目前，`cjc` 已支持交叉编译的本地平台和目标平台如下表所示：

| 本地平台 (host)    | 目标平台 (target)   |
| ------------------ | ------------------ |
| x86_64-linux-gnu   | x86_64-windows-gnu     |
| aarch64-linux-gnu   | x86_64-windows-gnu     |

在使用 `--target` 指定目标平台进行交叉编译之前，请准备好对应目标平台的交叉编译工具链，以及可以在本地平台上运行的、向该目标平台编译的对应 Cangjie SDK 版本。