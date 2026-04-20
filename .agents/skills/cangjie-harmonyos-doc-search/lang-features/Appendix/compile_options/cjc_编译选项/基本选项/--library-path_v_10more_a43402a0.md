### `--library-path <value>`, `-L <value>`, `-L<value>`

指定要链接的库文件所在的目录。

使用 `--library <value>` 选项时，通常也需要使用此选项来指定要链接的库文件所在的目录。

`--library-path <value>` 指定的路径会被加入链接器的库文件搜索路径。此外，环境变量 `LIBRARY_PATH` 中指定的路径也会被加入链接器的库文件搜索路径中，通过 `--library-path` 指定的路径会比 `LIBRARY_PATH` 中的路径拥有更高的优先级。

假设有从以下 C 语言源文件通过 C 语言编译器编译得到的动态库文件 `libcProg.so`，

```c
#include <stdio.h>

void printHello() {
    printf("Hello World\n");
}
```

仓颉文件 `main.cj`：

```cangjie
foreign func printHello(): Unit

main(): Int64 {
  unsafe {
    printHello()
  }
  return 0
}
```

可以使用

```shell
cjc main.cj -L . -l cProg
```

来编译 `main.cj` 并指定要链接的 `cProg` 库，这里 `cjc` 会输出一个可执行文件 `main`。

执行 `main` 会有如下输出：

```shell
$ LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH ./main
Hello World
```

**值得注意的是**，由于使用了动态库文件，这里需要将库文件所在目录加入 `$LD_LIBRARY_PATH` 以保证 `main` 能够在执行时进行动态链接。

### `-g` <sup>[frontend]</sup>

生成带有调试信息的可执行文件或库文件。

> **注意：**
>
> `-g` 只能配合 `-O0` 使用，如果使用更高的优化级别可能会导致调试功能出现异常。

### `--trimpath <value>` <sup>[frontend]</sup>

移除调试信息中源文件路径信息的前缀。

编译仓颉代码时，`cjc` 会保存源文件（`.cj` 文件）的绝对路径信息以在运行时提供调试与异常信息。

使用此选项可以将指定的路径前缀从源文件路径信息中移除，`cjc` 的输出文件中的源文件路径信息不会包含用户指定的部分。

可以多次使用 `--trimpath` 指定多个不同的路径前缀；对于每个源文件路径，编译器会将第一个匹配到的前缀从路径中移除。

### `--coverage` <sup>[frontend]</sup>

生成支持统计代码覆盖率的可执行程序。编译器会为每一个编译单元生成一个后缀名为 `gcno` 的代码信息文件。在执行程序后，每一个编译单元都会生成一个后缀名为 `gcda` 的执行统计文件。根据这两个文件，配合使用 `cjcov` 工具可以生成本次执行下的代码覆盖率报表。

> **注意：**
>
> `--coverage` 只能配合 `-O0` 使用，如果使用更高的优化级别，编译器将告警并强制使用 `-O0`。`--coverage` 用于编译生成可执行程序，如果用于生成静态库或者动态库，那么在最终使用该库时可能出现链接错误。

### `--int-overflow=[throwing|wrapping|saturating]` <sup>[frontend]</sup>

指定固定精度整数运算的溢出策略，默认为 `throwing`。

- `throwing` 策略下，整数运算溢出时会抛出异常。
- `wrapping` 策略下，整数运算溢出时会回转至对应固定精度整数的另一端。
- `saturating` 策略下，整数运算溢出时会选择对应固定精度的极值作为结果。

### `--diagnostic-format=[default|noColor|json]` <sup>[frontend]</sup>

> **注意：**
>
> Windows 版本暂不支持输出带颜色渲染的错误信息。

指定错误信息的输出格式，默认为 `default` 。

- `default` 错误信息默认格式输出（带颜色）
- `noColor` 错误信息默认格式输出（无颜色）
- `json` 错误信息`json`格式输出

### `--verbose`, `-V` <sup>[frontend]</sup>

`cjc` 会打印出编译器版本信息、工具链依赖的相关信息以及编译过程中执行的命令。

### `--help`, `-h` <sup>[frontend]</sup>

打印可用的编译选项。

使用此选项时，编译器仅会打印编译选项相关信息，不会对任何输入文件进行编译。

### `--version`, `-v` <sup>[frontend]</sup>

打印编译器版本信息。

使用此选项时，编译器仅会打印版本信息，不会对任何输入文件进行编译。

### `--save-temps <value>`

保留编译过程中生成的中间文件并保存至 `<value>` 路径下。

编译器会保留编译过程中生成的 `.bc`、`.o` 等中间文件。