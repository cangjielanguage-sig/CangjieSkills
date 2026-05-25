# 调试工具

CJDB 是一款基于 `lldb` 开发的仓颉程序命令行调试工具。当前 `cjdb` 工具是在[llvm15.0.4](https://github.com/llvm/llvm-project/releases/tag/llvmorg-15.0.4)基础上适配演进出来的工具。为仓颉开发者提供程序调试的能力。

## `cjdb` 工具获取

### 获取方式

通过 `Cangjie` 的 `SDK` 获取，获取路径：每日构建。

`cjdb` 工具在 `SDK` 中的路径：`cangjie\tools\bin` 。

### 使用举例

下面以 `Windows` 平台使用方式举例

  解压，直接在 `cjdb` 工具所在路径 `cangjie\tools\bin` 运行 `cjdb.exe` 即可。

> **说明：**
>
> 表 `system` 参数取值说明
>
> | system 参数取值| 说明                    |
> | -------------- | ----------------------- |
> | windows        | 适用于 Windows 平台的工具 |
> | linux          | 适用于 Linux 平台的工具   |
> | darwin         | 适用于 macOS 平台的工具     |
>
> **注意**
>
> 尽可能保证待调试的 ELF 文件或应用编译时使用的编译器和获取的 `cjdb` 调试器工具来源同一版本的工具链。