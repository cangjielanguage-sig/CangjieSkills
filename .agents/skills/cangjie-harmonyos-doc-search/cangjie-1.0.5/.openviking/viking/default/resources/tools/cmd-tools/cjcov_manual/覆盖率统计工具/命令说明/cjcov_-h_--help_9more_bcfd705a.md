### cjcov -h | --help

显示 `cjcov` 基本使用方法。

### cjcov -v | --version

显示 `cjcov` 的版本号。指定 `-v` 或者 `--version` 参数后，输入其他任何选项参数都不生效，只会显示版本号。如 `--version` 和 `--help` 同时使用，则显示版本号信息后退出。

### cjcov --verbose

指定该选项后会将一些日志信息生成到 `cjcov_logs` 目录中，该参数默认不生效，即默认不会打印中间信息。`gcov` 文件是 `cjcov` 工具生成的中间文件，`cjcov` 解析 `gcov` 文件的格式如下：

```text
==================== start: main.cj.gcov =====================

noncode line numbers:
[0, 0, 0, 0, 1, 2, 6, 7, 9, 10, 11, 15, 17, 18]

uncovered line numbers:
[5]

covered data:
[(16, 1), (3, 1), (4, 1), (8, 1), (12, 1), (13, 1), (14, 1)]

branches data:
line number:    4  ==>  data: [(0, 0), (1, 1)]

===================== end: main.cj.gcov =======================

```

指定该选项参数，会显示每个 `gcov` 文件的详细覆盖率数据。

具体字段解释如下：

- `start: xxx.gcov, end: xxx.gcov`：两行中间的文本是对应 `xxx.gcov` 文件解析到的覆盖率数据。
- `noncode line numbers`：显示的是不统计到总代码行的行号，在 `html` 中是以白色底呈现，对应 `gcov` 中的以 `-` 开头的行数。
- `uncovered line numbers`：显示的是没有覆盖到的数据，在 `html` 中是以红色底呈现，对应 `gcov` 文件中以 `#####` 开头的行数。
- `covered data`：显示的是覆盖到的数据，以（代码行数, 覆盖次数）呈现，在对应 `html` 中以绿色呈现，只要覆盖次数大于 0，在 `html` 中的 `Exec` 一列中显示为 `Y`，对应于 `gcov` 文件以数字开头的行数。
- `branches data`：显示的分支覆盖数据，以（代码行数, 分支覆盖次数）呈现，在对应 `html` 中的 `Branch` 一列中，有一个倒三角形，显示的是分支覆盖数/总分支数。该数据对应于 `gcov` 文件中以 `branch` 开头的数据。

### cjcov --html-details

如果指定该参数，表示会生成源代码文件对应的 `html` 覆盖报告。在总的 `index` 文件里面会有每个子 `html` 的索引。子 `html` 文件和 `index.html` 放在同一个目录。

子 `html` 文件名由目录名和文件名通过下划线拼接而成。例如，源文件为 `src/main.cj` 时，生成的 `html` 文件名为 `src_main.cj.html`。如果源文件路径包含特殊字符，这些字符将被替换为 `=`。有关详细信息，请参见[文件名包含特殊字符](#文件名包含特殊字符)章节。

如果没有指定该参数，表示不会生成子 `html`。在总的 `index` 文件里面会显示每个子 `html` 的覆盖率数据，但是不能跳转到对应的子 `html` 文件。

该参数默认不生效。即默认只会生成一个 `index.html`, 不会生成子 `html` 文件。

### cjcov -x | --xml

如果指定该参数，则会在指定输出路径生成 `coverage.xml` 文件，`coverage.xml` 记录的是所有文件的覆盖率数据。

### cjcov -j | --json

如果指定该参数，则会在指定输出路径生成 `coverage.json` 文件，`coverage.json` 记录的是所有文件的覆盖率数据。

### cjcov -k |  --keep

指定该参数后则会保留生成的 `gcov` 中间文件。如果保留这些文件，后续测试运行时会重复计算覆盖率数据，可能导致最终覆盖率结果不准确。

默认该参数不生效，即默认会删除 `gcov` 中间文件。

### cjcov -b | --branches

指定该参数后则会生成分支覆盖率信息。

默认该参数不生效，即默认不生成分支的覆盖率信息，此时在 `html` 报告中的分支覆盖率数据百分比显示为 `-`。

### cjcov -r ROOT | --root=ROOT

该参数指定的 `ROOT` 参数表示在 `ROOT` 目录或其递归子目录中查找 `gcda` 文件。`gcda` 和 `gcno` 文件默认会生成在一起，请不要手动将 `gcda` 文件和 `gcno` 文件分开存放，否则可能导致程序无法运行。

参数指定的 `ROOT` 目录如果不存在，`cjcov` 工具会有报错提示。

不指定该参数，默认会以当前目录为 `ROOT` 目录。