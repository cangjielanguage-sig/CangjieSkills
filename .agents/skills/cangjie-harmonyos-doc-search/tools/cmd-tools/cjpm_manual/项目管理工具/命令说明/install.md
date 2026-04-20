### install

`install` 用于安装仓颉项目，执行该命令前会先进行编译，然后将编译产物安装到指定路径，安装产物以仓颉项目名命名（`Windows` 系统上会有 `.exe` 后缀）。`install` 安装的项目产物类型需要是 `executable`。

`install` 有多个可配置项：

- `-V, --verbose` 用于展示安装日志。
- `-m, --member <value>` 仅可在工作空间下使用，可用于指定单个模块作为编译入口以安装单一模块。
- `-g` 用于生成 `debug` 版本的安装产物。
- `--path <value>` 用于指定本地安装项目的路径，默认为当前路径下的项目。
- `--root <value>` 用于指定可执行文件的安装路径。不配置时 `Linux` / `macOS` 系统下默认为 `$HOME/.cjpm`，`Windows` 系统下默认为 `%USERPROFILE%/.cjpm`；配置时将会安装于 `value`。
- `--git <value>` 用于指定 `git` 安装的项目 `url`。
- `--branch <value>` 用于指定 `git` 安装的项目分支。
- `--tag <value>` 用于指定 `git` 安装的项目 `tag`。
- `--commit <value>` 用于指定 `git` 安装的项目 `commit ID`。
- `-j, --jobs <N>` 用于指定并行编译的最大并发数，最终的最大并发数取 `N` 和 `2倍 CPU 核数` 的最小值。
- `--cfg` 指定后，能够透传 `cjpm.toml` 中的自定义 `cfg` 选项。
- `--target-dir <value>` 用于指定编译产物的存放路径。
- `--name <value>` 用于指定最终安装的产物名。
- `--skip-build` 用于跳过编译阶段以直接安装产物，需要项目处于编译完成状态，且仅在本地安装场景下生效。
- `--list` 用于打印已安装产物列表。
- `--skip-script` 配置后，将会跳过待安装模块的构建脚本的编译运行。

`install` 功能有如下注意事项：

- `install` 共有两种安装方式：安装本地项目（通过 `--path` 配置项目路径）和安装 `git` 项目（通过 `--git` 配置项目 `url`）。这两种安装方式至多只能配置一种，否则 `install` 将报错。任意一种均未配置时，默认安装当前目录下的本地项目。
- `install` 编译项目时，默认开启增量编译。
- `git` 相关配置仅在配置 `--git` 后生效，否则会被忽略，包括 `--branch`, `--tag` 和 `--commit`。当配置多个 `git` 相关配置时，仅会生效优先级更高的配置，优先级排序为 `--commit` > `--branch` > `--tag`。
- 若已存在同名可执行文件被安装，则原来的文件将被替换。
- 假设安装路径为 `root`（`root` 为配置的安装路径，不配置则为默认路径），则可执行文件将被安装于 `root/bin`。
- 若项目存在动态库依赖，可执行程序所需动态库会被安装到 `root/libs`，按程序名分隔为若干目录，开发者需要将对应目录加入相应路径（`Linux` 中为 `LD_LIBRARY_PATH`，`Windows` 中为 `PATH`，`macOS` 中为 `DYLD_LIBRARY_PATH`）方可使用。
- 默认安装路径（`Linux` / `macOS` 系统下默认为 `$HOME/.cjpm`，`Windows` 系统下默认为 `%USERPROFILE%/.cjpm`）会在 `envsetup` 中被加入 `PATH`。
- `install` 在安装 `git` 项目后，对应的编译产物目录会被清除。
- 在待安装项目仅存在一个可执行文件产物时，指定 `--name` 会将其更名后安装；若存在多个可执行文件产物，指定 `--name` 会仅安装对应名称的产物。
- 配置 `--list` 时，`install` 会打印已安装产物列表，此时除 `--root` 以外的所有配置项均会被忽略。配置 `--root` 后，`--list` 会打印配置路径下已安装的产物列表，否则会打印默认路径下的列表。

例如：

```text
cjpm install --path path/to/project # 从本地路径 path/to/project 中安装
cjpm install --git url              # 从 git 对应地址安装
```