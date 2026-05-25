### `--import-path <value>` <sup>[frontend]</sup>

指定导入模块的 AST 文件的搜索路径。

假设已有以下目录结构，`libs/myModule` 目录中包含 `myModule` 模块的库文件和 `log` 包的 AST 导出文件：

```text
.
├── libs
|   └── myModule
|       ├── log.cjo
|       └── libmyModule.a
└── main.cj
```

且有如下 `main.cj` 文件：

```cangjie
import myModule.log.printLog

main() {
    printLog("Everything is great")
}
```

可以通过使用 `--import-path ./libs` 来将 `./libs` 加入导入模块的 AST 文件搜索路径，`cjc` 会使用 `./libs/myModule/log.cjo` 文件来对 `main.cj` 文件进行语义检查与编译。

`--import-path` 提供与 `CANGJIE_PATH` 环境变量相同的功能，但通过 `--import-path` 设置的路径拥有更高的优先级。

### `--scan-dependency` <sup>[frontend]</sup>

通过 `--scan-dependency` 指令可以获得指定包源码或者一个包的 `cjo` 文件对于其他包的直接依赖以及其他信息，以 `json` 格式输出。

```cangjie
// this file is placed under directory pkgA
macro package pkgA
import pkgB.*
import std.io.*
import pkgB.subB.*
```

```shell
cjc --scan-dependency --package pkgA
```

或

```shell
cjc --scan-dependency pkgA.cjo
```

```json
{
  "package": "pkgA",
  "isMacro": true,
  "dependencies": [
    {
      "package": "pkgB",
      "isStd": false,
      "imports": [
        {
          "file": "pkgA/pkgA.cj",
          "begin": {
            "line": 2,
            "column": 1
          },
          "end": {
            "line": 2,
            "column": 14
          }
        }
      ]
    },
    {
      "package": "pkgB.subB",
      "isStd": false,
      "imports": [
        {
          "file": "pkgA/pkgA.cj",
          "begin": {
            "line": 4,
            "column": 1
          },
          "end": {
            "line": 4,
            "column": 19
          }
        }
      ]
    },
    {
      "package": "std.io",
      "isStd": true,
      "imports": [
        {
          "file": "pkgA/pkgA.cj",
          "begin": {
            "line": 3,
            "column": 1
          },
          "end": {
            "line": 3,
            "column": 16
          }
        }
      ]
    }
  ]
}
```

### `--no-sub-pkg` <sup>[frontend]</sup>

表明当前编译包没有子包。

开启该选项后，编译器可以进一步缩减 code size 大小。

### `--warn-off`, `-Woff <value>` <sup>[frontend]</sup>

关闭编译期出现的全部或部分警告。

`<value>` 可以为 `all` 或者一个设定好的警告组别。当参数为 `all` 时，对于编译过程中生成的所有警告，编译器都不会打印；当参数为其他设定好的组别时，编译器将不会打印编译过程中生成的该组别警告。

在打印每个警告时，会有一行 `#note` 提示该警告属于什么组别并如何关闭它，可以通过 `--help` 打印所有可用的编译选项参数，来查阅具体的组别名称。

### `--warn-on`, `-Won <value>` <sup>[frontend]</sup>

开启编译期出现的全部或部分警告。

`--warn-on` 的 `<value>` 与 `--warn-off` 的 `<value>` 取值范围相同，`--warn-on` 通常与 `--warn-off` 组合使用；比如，可以通过设定 `-Woff all -Won <value>` 来仅允许组别为 `<value>` 的警告被打印。

**特别要注意的是**，`--warn-on` 与 `--warn-off` 在使用上顺序敏感；针对同一组别，后设定的选项会覆盖之前选项的设定，比如，调换上例中两个编译选项的位置，使其变为 `-Won <value> -Woff all`，其效果将变为关闭所有警告。

### `--error-count-limit <value>` <sup>[frontend]</sup>

限制编译器打印错误个数的上限。

参数 `<value>` 可以为 `all` 或一个非负整数。当参数为 `all` 时，编译器会打印编译过程中生成的所有错误；当参数为非负整数 `N` 时，编译器最多会打印 `N` 个错误。此选项默认值为 8。

### `--output-dir <value>` <sup>[frontend]</sup>

控制编译器生成的中间文件与最终文件的保存目录。

控制编译器生成的中间文件的保存目录，例如 `.cjo` 文件。当指定 `--output-dir <path1>` 时也指定了 `--output <path2>`，则中间文件会被保存至 `<path1>`，最终输出会被保存至 `<path1>/<path2>` 。

> **注意：**
>
> 同时指定此选项与 `--output` 选项时，`--output` 选项的参数必须是一个相对路径。

### `--static`

静态链接仓颉库。

此选项仅在编译可执行文件时生效。

**值得注意的是：**

`--static` 选项仅适用于 Linux 平台，在其他平台不生效。