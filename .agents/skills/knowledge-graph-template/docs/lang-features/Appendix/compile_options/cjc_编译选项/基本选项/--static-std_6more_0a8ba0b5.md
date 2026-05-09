### `--static-std`

静态链接仓颉库的 std 模块。

此选项仅在编译动态链接库或可执行文件时生效。

当编译可执行程序时（即指定了 `--output-type=exe` 时），`cjc` 默认静态链接仓颉库的 std 模块。

### `--dy-std`

动态链接仓颉库的 std 模块。

此选项仅在编译动态链接库或可执行文件时生效。

当编译动态库时（即指定了 `--output-type=dylib` 时），`cjc` 默认动态链接仓颉库的 std 模块。

**值得注意的是：**

1. `--static-std` 和 `--dy-std` 选项一起使用时，仅最后一个选项生效。
2. `--dy-std` 与 `--static-libs` 选项不可一起使用，否则会报错。
3. 当编译可执行程序时链接了仓颉动态库（即通过 `--output-type=dylib` 选项编译的产物），必须显式指定 `--dy-std` 选项动态链接标准库，否则可能导致程序集中出现多份标准库，最终可能会导致运行时问题。

### `--static-libs`

静态链接仓颉库中除 std 及运行时模块外的其他模块。

此选项仅在编译动态链接库或可执行文件时生效。`cjc` 默认静态链接仓颉库中除 std 及运行时模块外的其他模块。

### `--dy-libs`

动态链接仓颉库非 std 的其他模块。

此选项仅在编译动态链接库或可执行文件时生效。

**值得注意的是：**

1. `--static-libs` 和 `--dy-libs` 选项一起使用时，仅最后一个选项生效；
2. `--static-std` 与 `--dy-libs` 选项不可一起使用，否则会报错；
3. `--dy-std` 单独使用时，会默认生效 `--dy-libs` 选项，并有相关告警信息提示；
4. `--dy-libs` 单独使用时，会默认生效 `--dy-std` 选项，并有相关告警信息提示。

### `--stack-trace-format=[default|simple|all]`

指定异常调用栈打印格式，用来控制异常抛出时的栈帧信息显示，默认为 `default` 格式。

异常调用栈的格式说明如下：

- `default` 格式：`省略泛型参数的函数名 (文件名:行号)`
- `simple` 格式： `文件名:行号`
- `all` 格式：`完整的函数名 (文件名:行号)`

### `--lto=[full|thin]`

使能且指定 `LTO` （`Link Time Optimization` 链接时优化）优化编译模式。

**值得注意的是：**

1. `Windows` 以及 `macOS` 平台不支持该功能；
2. 当使能且指定 `LTO` （`Link Time Optimization` 链接时优化）优化编译模式时，不允许同时使用如下优化编译选项：`-Os`、`-Oz`。

`LTO` 优化支持两种编译模式：

- `--lto=full`：`full LTO` 将所有编译模块合并到一起，在全局上进行优化，这种方式可以获得最大的优化潜力，同时也需要更长的编译时间。
- `--lto=thin`：相比于 `full LTO`，`thin LTO` 在多模块上使用并行优化，同时默认支持链接时增量编译，编译时间比 `full LTO` 短，因为失去了更多的全局信息，所以优化效果不如 `full LTO`。

    - 通常情况下优化效果对比：`full LTO` **>** `thin LTO` **>** 常规静态链接编译。
    - 通常情况下编译时间对比：`full LTO` **>** `thin LTO` **>** 常规静态链接编译。

`LTO` 优化使用场景：

1. 使用以下命令编译可执行文件。

    ```shell
    $ cjc test.cj --lto=full
    or
    $ cjc test.cj --lto=thin
    ```

2. 使用以下命令编译 `LTO` 模式下需要的静态库（`.bc` 文件），并且使用该库文件参与可执行文件编译。

    ```shell
    # 生成的静态库为 .bc 文件
    $ cjc pkg.cj --lto=full --output-type=staticlib -o libpkg.bc
    # .bc 文件和源文件一起输入给仓颉编译器编译可执行文件
    $ cjc test.cj libpkg.bc --lto=full
    ```

    > **注意：**
    >
    > `LTO` 模式下的静态库（`.bc` 文件）输入时需要将该文件的路径输入仓颉编译器。

3. 在 `LTO` 模式下，静态链接标准库（`--static-std` & `--static-libs`）时，标准库的代码也会参与 `LTO` 优化，并静态链接到可执行文件；动态链接标准库（`--dy-std` & `--dy-libs`）时，在 `LTO` 模式下依旧使用标准库中的动态库参与链接。

    ```shell
    # 静态链接，标准库代码也参与 LTO 优化
    $ cjc test.cj --lto=full --static-std
    # 动态链接，依旧使用动态库参与链接，标准库代码不会参与 LTO 优化
    $ cjc test.cj --lto=full --dy-std
    ```