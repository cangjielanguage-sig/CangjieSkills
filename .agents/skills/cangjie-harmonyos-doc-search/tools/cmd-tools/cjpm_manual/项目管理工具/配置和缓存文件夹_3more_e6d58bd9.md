## 配置和缓存文件夹

`cjpm` 通过 `git` 下载文件的存储路径可以通过 `CJPM_CONFIG` 环境变量指定。如果未指定，则 `Linux/macOS` 上的默认位置为 `$HOME/.cjpm`，`Windows` 上的默认位置为 `%USERPROFILE%/.cjpm` 。

## 仓颉包管理规格说明

在仓颉包管理规格中，对于一个文件目录，被识别为一个有效源码包的要求如下：

1. 必须直接包含至少一个仓颉代码文件；
2. 其父包（包括父包的父包，直至 `root` 包）也为有效源码包。其中，模块 `root` 包不存在父包，因此仅需满足条件 1。

例如，有如下名为 `demo` 的 `cjpm` 项目：

```text
demo
├──src
│   ├── main.cj
│   └── pkg0
│        ├── aoo
│        │    └── aoo.cj
│        └── boo
│             └── boo.cj
└── cjpm.toml
```

其中，`demo.pkg0` 对应目录内没有直接包含仓颉代码，因此 `demo.pkg0` 不是一个有效源码包；`demo.pkg0.aoo` 和 `demo.pkg0.boo` 包虽然直接包含仓颉代码文件 `aoo.cj` 和 `boo.cj`，但由于其上游包 `demo.pkg0` 不是有效源码包，因此这两个包也不是有效源码包。

当 `cjpm` 识别到 `demo.pkg0` 这样的不直接包含仓颉文件的包时，会将其视为非源码包，忽略其所有子包，并打印如下告警：

```text
Warning: there is no '.cj' file in directory 'demo/src/pkg0', and its subdirectories will not be scanned as source code
```

因此，如果开发者需要配置一个有效的源码包，则该包内必须直接包含至少一个仓颉代码文件，并且其上游包都需要是有效源码包。以上述项目 `demo` 为例，如果想要让 `demo.pkg0`,`demo.pkg0.aoo` 和 `demo.pkg0.boo` 均被识别为有效源码包，则可以在 `demo/src/pkg0` 内添加一个仓颉代码文件，如下所示：

```text
demo
├── src
│    ├── main.cj
│    └── pkg0
│         ├── pkg0.cj
│         ├── aoo
│         │    └── aoo.cj
│         └── boo
│              └── boo.cj
└── cjpm.toml
```

`demo/src/pkg0/pkg0.cj` 需要是一个符合包管理规格的仓颉代码文件，可以不包含功能代码，例如如下形式：

```cangjie
package demo.pkg0
```

## 命令扩展

`cjpm` 提供命令扩展机制，开发者可以通过文件名形如 `cjpm-xxx(.exe)` 的可执行文件扩展 `cjpm` 的命令。

针对可执行文件 `cjpm-xxx`（`Windows` 系统中为 `cjpm-xxx.exe`），若系统环境变量 `PATH` 中配置了该文件所在的路径，则可以使用如下的命令运行该可执行文件：

```shell
cjpm xxx [args]
```

其中 `args` 为可能需要的输入给 `cjpm-xxx(.exe)` 的参数列表。上述命令等价于：

```shell
cjpm-xxx(.exe) [args]
```

运行 `cjpm-xxx(.exe)` 可能会依赖某些动态库，在这种情况下，开发者需要手动将需要使用的动态库所在的目录添加到环境变量中。

下面以 `cjpm-demo` 为例，该可执行文件由以下仓颉代码编译得到：

```cangjie
import std.process.*
import std.collection.*

main(): Int64 {
    var args = ArrayList<String>(Process.current.arguments)

    if (args.size < 1) {
        eprintln("Error: failed to get parameters")
        return 1
    }

    println("Output: ${args[0]}")

    return 0
}
```

则在将其目录添加到 `PATH` 之后，运行对应命令，会运行该可执行文件并获得对应的输出。

```text
输入：cjpm demo hello,world
输出：Output: hello,world
```

`cjpm` 内部已有的命令优先级更高，因此无法用此方式扩展这些命令。例如，即使系统环境变量中存在名为 `cjpm-build` 的可执行文件，`cjpm build` 也不会运行该文件，而是运行 `cjpm` 并将 `build` 作为参数输入 `cjpm`。