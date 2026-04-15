## Linux / macOS

### 环境准备

#### Linux

Linux 版仓颉工具链的系统环境要求如下：

| 架构    | 环境要求                                                     |
| ------- | ------------------------------------------------------------ |
| x86_64  | glibc 2.27，Linux Kernel 4.15 或更高版本，系统安装 libstdc++ 6.0.24 或更高版本 |
| aarch64 | glibc 2.27，Linux Kernel 4.15 或更高版本，系统安装 libstdc++ 6.0.24 或更高版本 |

除此之外，对于 Ubuntu 18.04，还需要安装相应的依赖软件包：

```bash
$ apt-get install binutils libc-dev libc++-dev libgcc-7-dev
```

更多 Linux 发行版的依赖安装命令可以参见附录[Linux 版本工具链的支持与安装](../Appendix/linux_toolchain_install.md)章节。

此外，仓颉工具链还依赖 OpenSSL 3 组件，由于该组件可能无法从以上发行版的默认软件源直接安装，因此需要自行手动安装，安装方式请参考附录[Linux 版本工具链的支持与安装](../Appendix/linux_toolchain_install.md)章节。

#### macOS

macOS 版仓颉工具链支持在 macOS 12.0 及以上版本运行。

使用 macOS 版本前需要安装相应的依赖软件包，可以通过执行以下命令安装：

```bash
$ brew install libffi
```

### 安装指导

首先请前往仓颉官方发布渠道，下载适配平台架构的安装包：

- `cangjie-sdk-linux-x64-x.y.z.tar.gz`：适用于 x86_64 架构 Linux 系统的仓颉工具链
- `cangjie-sdk-linux-aarch64-x.y.z.tar.gz`：适用于 aarch64 架构 Linux 系统的仓颉工具链
- `cangjie-sdk-mac-aarch64-x.y.z.tar.gz`：适用于 aarch64/arm64 架构 macOS 系统的仓颉工具链

假设这里选择了 `cangjie-sdk-linux-x64-x.y.z.tar.gz`，下载到本地后，请执行如下命令解压：

```bash
tar xvf cangjie-sdk-linux-x64-x.y.z.tar.gz
```

解压完成，可以在当前工作路径下看到一个名为 `cangjie` 的目录，其中存放了仓颉工具链的全部内容，请执行如下命令完成仓颉工具链的安装配置：

```bash
source cangjie/envsetup.sh
```

为了验证是否安装成功，可以执行如下命令：

```bash
cjc -v
```

其中 `cjc` 是仓颉编译器的可执行文件名，如果在命令行中看到了仓颉编译器版本信息，表示已经成功安装了仓颉工具链。值得说明的是，`envsetup.sh` 脚本只是在当前 shell 环境中配置了工具链相关的环境变量，所以仓颉工具链仅在当前 shell 环境中可用，在新的 shell 环境中，需要重新执行 `envsetup.sh` 脚本配置环境。

若想使仓颉工具链的环境变量配置在 `shell` 启动时自动生效，可以在 `$HOME/.bashrc` 或 `$HOME/.zshrc`（依 `shell` 种类而定）等 `shell` 初始化配置文件的最后加入以下命令：

```shell
# 假设仓颉安装包解压在 /home/user/cangjie 中
source /home/user/cangjie/envsetup.sh  # 即 envsetup.sh 的绝对路径
```

配置完成后 shell 启动即可直接使用仓颉编译工具链。

### 卸载与更新

在 Linux 和 macOS 平台，删除上述仓颉工具链的安装包目录，同时移除上述环境变量（最简单的，可以新开一个 shell 环境），即可完成卸载。

```bash
$ rm -rf <path>/<to>/cangjie
```

若需要更新仓颉工具链，需要先卸载当前版本，然后按上述指导重新安装最新版本的仓颉工具链。