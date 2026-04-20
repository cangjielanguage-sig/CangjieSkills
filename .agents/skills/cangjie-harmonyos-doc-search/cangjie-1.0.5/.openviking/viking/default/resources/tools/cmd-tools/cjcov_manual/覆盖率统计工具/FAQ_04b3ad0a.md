## FAQ

### 报错找不到 `llvm-cov` 命令

**解决方法：**

方法 1：设置 `CANGJIE_HOME` 环境变量，`cjcov` 可通过 `CANGJIE_HOME` 环境变量找到 `llvm-cov` 命令，设置方法如下：
假设 `which cjc` 显示 `/work/cangjie/bin/cjc`, 并且 `/work/cangjie/third_party/llvm/bin` 和 `/work/cangjie/third_party/llvm/lib` 目录都存在，则可设置：

```shell
export CANGJIE_HOME=/work/cangjie
```

方法 2：在 `/root/.bashrc` 里面直接设置环境变量，如 `cjc` 放在 `/work/cangjie/bin/cjc` 目录下，则设置方法如下：

```shell
export PATH=/work/cangjie/third_party/llvm/bin:$PATH
export LIBRARY_PATH=/work/cangjie/third_party/llvm/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=/work/cangjie/third_party/llvm/lib:$LD_LIBRARY_PATH
```

方法 3：手动安装 `llvm-cov` 命令，如 `ubuntu` 上可执行命令：

```shell
apt install llvm-cov
```

### 出现 VirtualMachineError OutOfMemoryError

**问题现象：**

```text
An exception has occurred:
Error VirtualMachineError OutOfMemoryError
```

**解决方法：** 仓颉默认规格  stack 1MB，heap 256 MB，建议根据文件数量大小将堆内存调到合适的大小。通常 2GB 的内存能够满足大多数情况，如果不够用则根据具体情况再增加内存大小。

示例：

```text
把堆内存扩大到2GB：
export cjHeapSize=2GB
```