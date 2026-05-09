## 功能简介

`CJLint(Cangjie Lint)`是一款静态检查工具，该工具是基于仓颉语言编程规范开发。通过它可以识别代码中不符合编程规范的问题，帮助开发者发现代码中的漏洞，写出满足 Clean Source 要求的仓颉代码。

## 使用说明

`cjlint -h` 帮助信息，选项介绍。

```text
Options:
   -h                      Show usage
                               eg: ./cjlint -h
   -v                      Show version
                               eg: ./cjlint -v
   -f <value>              Detected file directory, it can be absolute paths or relative paths, if it is directory, default file name is cjReport
                               eg: ./cjlint -f fileDir -c . -m .
                               eg: ./cjlint -f "fileDir1 fileDir2" -c . -m .
   -e <v1:v2:...>          Excluded files, directories or configurations, splitted by ':'. Regular expressions are supported
                               eg: ./cjlint -f fileDir -e fileDir/a/:fileDir/b/*.cj
   -o <value>              Output file path, it can be absolute path or relative path
                               eg: ./cjlint -f fileDir -o ./out
   -r [csv|json]           Report file format, it can be csv or json, default is json
                               eg: ./cjlint -f fileDir -r csv -o ./out
   -c <value>              Directory path where the config directory is located, it can be absolute path or relative path to the executable file
                               eg: ./cjlint -f fileDir -c .
   -m <value>              Directory path where the modules directory is located, it can be absolute path or relative path to the executable file
                               eg: ./cjlint -f fileDir -m .
   --import-path <value>   Add .cjo search path
```

`cjlint -f` 指定检查目录。

```bash
cjlint -f fileDir [option] fileDir...

# 若需要指定多个路径，则在 "" 中以空格相隔
cjlint -f "fileDir1 fileDir2" [option] fileDir...
```

> **注意：**
>
> `-f` 后面指定的是*.cj 文件所在`src`目录。

正例：

```bash
cjlint -f xxx/xxx/src
```

反例：

```bash
cjlint -f xxx/xxx/src/xxx.cj
```

> **说明：**
>
> 当前工具支持目录扫描，暂不支持对单源码文件的独立检查，建议开发者提供单包路径作为输入。

`-r` 指定生成扫描报告的格式，目前支持`json`格式和`csv`格式。

`-r`需要与`-o`选项配合使用，如果没有`-o`指定输出到文件，即使指定了`-r`也不会生成扫描报告。如果指定了`-o`没有指定`-r`，那么默认生成`json`格式的扫描报告。

```bash
cjlint -f ./src -r csv -o ./report         # 生成report.csv文件
cjlint -f ./src -r csv -o ./output/report  # 在output目录下生成report.csv文件
```

`-c`, `-m` 在开发者需要时用以指定`config`和`modules`所在的目录路径。

`cjlint`默认使用其所在目录下的`config`和`modules`作为配置和依赖目录。开发者可通过命令行选项 `-c` 和 `-m` 指定其他目录路径。

例：指定的 config 和 modules 的路径分别为：`./tools/cjlint/config` 和 `./tools/cjlint/modules`。则`config`和`modules`所在的目录路径同为`./tools/cjlint`, 所以命令应为：

```bash
cjlint -f ./src -c ./tools/cjlint -m ./tools/cjlint
```

`--import-path` 在开发者需要时用以指定 `cjo` 所在的目录路径，且支持多个路径。

```bash
cjlint --import-path fileDir

# 若需要指定多个路径，则在 "" 中以空格相隔
cjlint --import-path "fileDir1 fileDir2"
```