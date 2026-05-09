# `cjpm` 介绍

`CJPM（Cangjie Project Manager）` 是仓颉语言的官方项目管理工具，用来管理、维护仓颉项目的模块系统，并且提供更简易统一的编译入口，支持自定义编译命令。通过自动依赖管理，实现对引入的多版本三方依赖软件进行分析合并，无需开发者担心多版本依赖冲突问题，大大减轻开发者的负担。同时提供基于仓颉语言原生的自定义构建机制，允许开发者在构建的不同阶段增加预处理和后处理流程，实现构建流程可灵活定制，能够满足开发者不同业务场景下的编译构建需求。

## `cjpm` 基本使用方法

通过 `cjpm -h` 即可查看主界面，由几个板块组成，从上到下分别是： 当前命令说明、使用示例（Usage）、支持的可用命令（Available subcommands）、支持的配置项（Available options）、更多提示内容。

```text
Cangjie Project Manager

Usage:
  cjpm [subcommand] [option]

Available subcommands:
  init             Init a new cangjie module
  check            Check the dependencies
  update           Update cjpm.lock
  tree             Display the package dependencies in the source code
  build            Compile the current module
  run              Compile and run an executable product
  test             Unittest a local package or module
  bench            Run benchmarks in a local package or module
  clean            Clean up the target directory
  install          Install a cangjie binary
  uninstall        Uninstall a cangjie binary

Available options:
  -h, --help       help for cjpm
  -v, --version    version for cjpm

Use "cjpm [subcommand] --help" for more information about a command.
```

`cjpm init` 用来初始化一个新的仓颉模块或工作空间。初始化模块时会默认在当前文件夹创建 `cjpm.toml` 文件，并且新建 `src` 源码文件夹，在 `src` 下生成默认的 `main.cj` 文件。自定义参数初始化功能支持可以通过 `cjpm init -h` 查看。

例如：

```text
输入: cjpm init
输出: cjpm init success
```

`cjpm build` 用来构建当前仓颉项目，执行该命令前会先检查依赖项，检查通过后调用 `cjc` 进行构建。支持全量编译、增量编译、交叉编译、并行编译等，更多编译功能支持可以通过 `cjpm build -h` 查看。通过 `cjpm build -V` 命令可以打印所有的编译过程命令。

例如：

```text
输入: cjpm build -V
输出:
compile package module1.package1: cjc --import-path target -p "src/package1" --output-type=staticlib -o target/release/module1/libmodule1.package1.a
compile package module1: cjc --import-path target -L target/release/module1 -lmodule1.package1 -p "src" --output-type=exe --output-dir target/release/bin -o main

cjpm build success
```