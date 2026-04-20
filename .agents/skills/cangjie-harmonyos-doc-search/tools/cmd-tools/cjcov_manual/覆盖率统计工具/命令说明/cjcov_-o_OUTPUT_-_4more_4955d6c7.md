### cjcov -o OUTPUT |  --output=OUTPUT

该参数指定的 `OUTPUT` 参数，表示 `html` 覆盖率报告的输出路径。

如果 `OUTPUT` 目录及其父目录均不存在，`cjcov` 工具将显示错误提示。若 `OUTPUT` 目录不存在但其父目录存在，`cjcov` 工具将自动创建 `OUTPUT` 目录。

不指定该参数，默认会以当前目录为 `OUTPUT` 目录来存放 `html` 文件。

### -s SOURCE | --source=SOURCE

该参数指定的 `SOURCE` 参数，表示仓颉源文件的代码路径，`html` 总覆盖率报告 `index.html` 会有各个源文件的索引，这些文件路径记录的是一个相对路径。如果指定 `-s SOURCE |--source SOURCE` 参数，优先以 `SOURCE` 路径列表中的路径作为相对路径的参考路径，如果没有指定该参数，则以 `-r ROOT | --root=ROOT` 作为相对路径的参考路径，如果都没有指定，则以当前路径作为相对路径的参考路径。

示例：

仓颉代码目录结构如下：

```text
/work/cangjie/tests/API/test01/src/1.cj
/work/cangjie/tests/API/test01/src/2.cj
/work/cangjie/tests/cjnative/test02/src/3.cj
/work/cangjie-tools/tests/cjnative/test01/src/4.cj
/work/cangjie-tools/tests/cjnative/test02/src/5.cj
```

1. 在 `/work` 目录执行命令：

    ```shell
    cjcov --root=./ -s "/work/cangjie /work/cangjie-tools/tests" --html-details --output=html_output
    ```

    最后 html 中呈现的源文件相对路径是：

    ```text
    tests/API/test01/src/1.cj
    tests/API/test01/src/2.cj
    tests/cjnative/test02/src/3.cj
    cjnative/test01/src/4.cj
    cjnative/test02/src/5.cj
    ```

2. 在 `/work` 目录执行命令, 没有指定 `--root` 参数和 `--source` 参数，默认当前所在路径为相对路径的参考路径，执行命令如下：

    ```shell
    cjcov --html-details --output=html_output
    ```

    最后 html 中呈现的源文件相对路径是：

    ```text
    cangjie/tests/API/test01/src/1.cj
    cangjie/tests/API/test01/src/2.cj
    cangjie/tests/cjnative/test02/src/3.cj
    cangjie-tools/tests/cjnative/test01/src/4.cj
    cangjie-tools/tests/cjnative/test02/src/5.cj
    ```

### -e EXCLUDE | --exclude=EXCLUDE

该参数指定的 `EXCLUDE` 参数，表示不需要生成覆盖率信息的源文件列表，支持指定目录和文件。

示例：

仓颉代码目录结构如下：

```text
/usr1/cangjie/tests/API/test01/src/1.cj
/usr1/cangjie/tests/API/test01/src/2.cj
/usr1/cangjie/tests/cjnative/test02/src/3.cj
/usr1/cangjie-tools/tests/cjnative/test01/src/4.cj
/usr1/cangjie-tools/tests/cjnative/test02/src/5.cj
```

在 `/usr1` 目录执行命令：

```shell
cjcov --root=./ -s "/usr1/cangjie" -e "/usr1/cangjie-tools/tests/cjnative" --html-details --output=html_output
```

在生成的 HTML 报告中，源文件的相对路径会被呈现，但以 `/usr1/cangjie-tools/tests/cjnative` 开头的路径不会出现在文件列表中。

```text
tests/API/test01/src/1.cj
tests/API/test01/src/2.cj
tests/cjnative/test02/src/3.cj
```

### -i INCLUDE | --include=INCLUDE

该参数指定的 `INCLUDE` 参数，表示以 `INCLUDE` 开头的文件会显示在 `index.html` 的文件列表中，支持指定目录和文件。如果 `-e | --exclude` 和 `-i | --include` 指定的参数有路径重复，会有报错提示。

示例：

仓颉代码目录 `/usr1/cangjie/tests` 结构如下：

```text
├── API
│   └── test01
│       └── src
│           ├── 1.cj
│           └── 2.cj
└── cjnative
    └── test02
        └── src
            └── 3.cj
```

在 `/usr1` 目录执行命令, 其中 `-i` 参数表示需要体现在覆盖率报告 `index.html` 的文件，命令如下：

```shell
cjcov --root=./ -s "/usr1/cangjie" -i "/usr1/cangjie/tests/API/test01/src/1.cj /usr1/cangjie/tests/cjnative/test02" --html-details --output=html_output
```

上面命令执行后, 在 `index.html` 中文件路径列表如下(`tests/API/test01/src/2.cj` 不在 `-i` 参数指定的列表里面，所以不会出现在 `html` 的文件列表中):

```text
tests/API/test01/src/1.cj
tests/cjnative/test02/src/3.cj
```