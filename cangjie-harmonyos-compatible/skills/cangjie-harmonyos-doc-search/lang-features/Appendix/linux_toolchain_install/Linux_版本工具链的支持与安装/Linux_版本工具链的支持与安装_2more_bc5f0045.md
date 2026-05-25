# Linux 版本工具链的支持与安装

仓颉工具链当前基于以下 Linux 发行版进行了完整功能测试：

- Ubuntu 18.04
- Ubuntu 20.04
- UnionTech OS Server 20
- Kylin Linux Advanced Server Release V10

## 适用于各 Linux 发行版的仓颉工具链依赖安装命令

> **注意：**
>
> 当前仓颉工具链依赖的某些工具在一些 Linux 发行版上可能无法通过系统默认软件源直接安装。可参考下一节[编译安装依赖工具](./linux_toolchain_install.md#编译安装依赖工具)进行手动安装。

### Ubuntu 18.04

```shell
$ apt-get install \
          binutils \
          libc-dev \
          libc++-dev \
          libgcc-7-dev
```

此外，还需要安装 OpenSSL 3，安装方法请参见[编译安装依赖工具](./linux_toolchain_install.md#编译安装依赖工具)。

### Ubuntu 20.04

```shell
$ apt-get install \
          binutils \
          libc-dev \
          libc++-dev \
          libgcc-9-dev
```

此外，还需要安装 OpenSSL 3，安装方法请参见[编译安装依赖工具](./linux_toolchain_install.md#编译安装依赖工具)。

### UnionTech OS Server 20

```shell
$ yum install \
      binutils \
      glibc-devel \
      libstdc++-devel \
      gcc \
```

此外，还需要安装 OpenSSL 3，安装方法请参见[编译安装依赖工具](./linux_toolchain_install.md#编译安装依赖工具)。

### Kylin Linux Advanced Server release V10

```shell
$ yum install \
      binutils \
      glibc-devel \
      libstdc++-devel \
      gcc \
```

此外，还需要安装 OpenSSL 3，安装方法请参见[编译安装依赖工具](./linux_toolchain_install.md#编译安装依赖工具)。

### 其他 Linux 发行版

根据使用的 Linux 发行版的不同，可能需要参考以上系统的依赖安装命令，使用系统包管理工具安装对应依赖。若使用的系统没有提供相关软件包，可能需要自行安装链接工具、C 语言开发工具、C++ 开发工具、GCC 编译器、以及 OpenSSL 3 以正常使用仓颉工具链。