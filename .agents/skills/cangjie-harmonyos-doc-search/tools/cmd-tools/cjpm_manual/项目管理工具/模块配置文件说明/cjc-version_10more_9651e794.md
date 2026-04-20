### "cjc-version"

仓颉编译器最低版本要求，必须和当前环境版本兼容才可以执行。一个合法的仓颉版本号是由三段数字组成，中间使用 `.` 隔开，每个数字均为自然数，且没有多余的前缀 `0`。例如：

- `1.0.0` 是一个有效的版本号；
- `1.00.0` 不是一个有效的版本号，因为 `00` 中含有多余的前缀 `0`；
- `1.2e.0` 不是一个有效的版本号，因为 `2e` 不是自然数。

### "name"

当前仓颉模块名称，同时也是模块 `root` 包名。

一个合法的仓颉模块名称必须是一个合法的标识符。标识符可由字母、数字、下划线组成，标识符的开头必须是字母，例如 `cjDemo` 或者 `cj_demo_1`。

> **注意：**
>
> 当前仓颉模块名暂不支持使用 Unicode 字符，仓颉模块名必须是一个仅含 ASCII 字符的合法的标识符。

### "description"

当前仓颉模块描述信息，仅作说明用，不限制格式。

### "version"

当前仓颉模块版本号，由模块所有者管理，主要供模块校验使用。模块版本号的格式同 `cjc-version`。

### "compile-option"

传给 `cjc` 的额外编译选项。多模块编译时，每个模块设置的 `compile-option` 对该模块内的所有包生效。

例如：

```text
compile-option = "-O1 -V"
```

这里填入的命令会在 `build` 执行时插入到编译命令中间，多个命令可以用空格隔开。可用的命令参考《仓颉编程语言开发指南》的[编译选项](../../../dev-guide/source_zh_cn/Appendix/compile_options.md)章节内容。

### "override-compile-option"

传给 `cjc` 的额外全局编译选项。多模块编译时，编译入口模块设置的 `override-compile-option` 对该模块及依赖的所有其他模块的包生效。

例如：

```text
override-compile-option = "-O1 -V"
```

这里填入的命令会在 `build` 执行时插入到编译命令中间，并且拼接于模块配置的 `compile-option` 内容之后，优先级高于 `compile-option`。可用的命令参考《仓颉编程语言开发指南》的[编译选项](../../../dev-guide/source_zh_cn/Appendix/compile_options.md)章节内容。

> **注意：**
>
> - `override-compile-option` 会生效于依赖模块内的包，开发者需保证配置的 `cjc` 编译选项与依赖模块内配置的 `compile-option` 没有冲突，否则编译过程中执行 `cjc` 将出现相应报错。对于不冲突的同类 `cjc` 编译选项，`override-compile-option` 内的选项优先级高于 `compile-option`。
> - 在工作空间编译场景下，仅 `workspace` 内配置的 `override-compile-option` 选项会应用于工作空间内所有模块所有包的编译；即使使用 `-m` 指定以单模块为入口模块进行编译，也不会使用入口模块的 `override-compile-option`。

### "link-option"

传给链接器的编译选项，可用于透传安全编译命令，如下所示:

```text
link-option = "-z noexecstack -z relro -z now --strip-all"
```

> **注意：**
>
> `link-option` 中配置的命令在编译时只会自动透传给动态库和可执行产物对应的包。

### "output-type"

编译输出产物的类型，包含可执行程序和库两种形式，相关的输入如下表格所示。如果想生成 `cjpm.toml` 时该字段自动填充为 `static`，可使用命令 `cjpm init --type=static --name=modName`，不指定类型时默认生成为 `executable`。只有主模块的该字段可以为 `executable`。

|     输入     |                 说明 |
| :----------: | :------------------: |
| "executable" |           可执行程序 |
|   "static"   | 静态库 |
|  "dynamic"   | 动态库 |
|     其它     |                 报错 |

### "src-dir"

该字段可以指定源码的存放路径，不指定时默认为 `src` 文件夹。

### "target-dir"

该字段可以指定编译产物的存放路径，不指定时默认为 `target` 文件夹。若该字段不为空，执行 `cjpm clean` 时会删除该字段所指向的文件夹，开发者需自身保证清理该目录行为的安全性。

> **注意：**
>
> 若在编译时同时指定了 `--target-dir` 选项，则该选项的优先级会更高。

```text
target-dir = "temp"
```