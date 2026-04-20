### `--output-type=[exe|staticlib|dylib]` <sup>[frontend]</sup>

指定输出文件的类型。`exe` 模式下会生成可执行文件，`staticlib` 模式下会生成静态库文件（ `.a` 文件），`dylib` 模式下会生成动态库文件（Linux 平台为 `.so` 文件、Windows 平台为 `.dll` 文件，macOS 平台为 `.dylib` 文件）。

`cjc` 默认为 `exe` 模式。

除了可以将 `.cj` 文件编译成一个可执行文件以外，也可以将其编译成一个静态或者是动态的链接库，例如使用：

```shell
$ cjc tool.cj --output-type=dylib
```

可以将 `tool.cj` 编译成一个动态链接库，在 Linux 平台上，`cjc` 会生成一个名为 `libtool.so` 的动态链接库文件。

**值得注意的是**，若编译可执行程序时链接了仓颉的动态库文件，必须同时指定 `--dy-std` 与 `--dy-libs` 选项，详情请见 [`--dy-std` 选项说明](#--dy-std)。

<sup>[frontend]</sup> 在 `cjc-frontend` 中，编译流程仅进行至 `LLVM IR`，因此输出总是 `.bc` 文件，但不同的 `--output-type` 类型仍会影响前端编译的策略。

### `--package`, `-p` <sup>[frontend]</sup>

编译包，使用此选项时需要指定一个目录作为输入，目录中的源码文件需要属于同一个包。

假设有文件 `log/printer.cj`：

```cangjie
package log

public func printLog(message: String) {
    println("[Log]: ${message}")
}
```

与文件 `main.cj`:

```cangjie
import log.*

main() {
    printLog("Everything is great")
}
```

可以使用

```shell
$ cjc -p log --output-type=staticlib
```

来编译 `log` 包，`cjc` 会在当前目录下生成一个 `liblog.a` 文件。

可以使用 `liblog.a` 文件来编译 `main.cj` ，编译命令如下：

```shell
$ cjc main.cj liblog.a
```

`cjc` 会将 `main.cj` 与 `liblog.a` 一同编译成一个可执行文件 `main` 。

### `--module-name <value>` <sup>[frontend]</sup>

指定要编译的模块的名称。

假设有文件 `my_module/src/log/printer.cj`：

```cangjie
package log

public func printLog(message: String) {
    println("[Log]: ${message}")
}
```

与文件 `main.cj`:

```cangjie
import my_module.log.*

main() {
    printLog("Everything is great")
}
```

可以使用

```shell
$ cjc -p my_module/src/log --module-name my_module --output-type=staticlib -o my_module/liblog.a
```

来编译 `log` 包并指定其模块名为 `my_module`，`cjc` 会在 `my_module` 目录下生成一个 `my_module/liblog.a` 文件。

然后可以使用 `liblog.a` 文件来编译导入了 `log` 包的 `main.cj` ，编译命令如下：

```shell
$ cjc main.cj my_module/liblog.a
```

`cjc` 会将 `main.cj` 与 `liblog.a` 一同编译成一个可执行文件 `main` 。

### `--output <value>`, `-o <value>`, `-o<value>` <sup>[frontend]</sup>

指定输出文件的路径，编译器的输出将被写入指定文件。

例如，以下命令会将输出的可执行文件名称指定为 `a.out`。

```shell
cjc main.cj -o a.out
```

### `--library <value>`, `-l <value>`, `-l<value>`

指定要链接的库文件。

给定的库文件会被直接传给链接器，此编译选项一般需要和 `--library-path <value>` 配合使用。

文件名的格式应为 `lib[arg].[extension]`。当需要链接库 `a` 时，可以使用选项 `-l a`，库文件搜索目录下的 `liba.a`、`liba.so`（或链接 Windows 目标程序时会搜索 `liba.dll`）等文件会被链接器搜索到并根据需要被链接至最终输出中。