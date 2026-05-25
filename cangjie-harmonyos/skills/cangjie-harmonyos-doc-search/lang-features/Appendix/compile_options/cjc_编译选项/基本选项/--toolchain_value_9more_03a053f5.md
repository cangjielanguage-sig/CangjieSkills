### `--toolchain <value>`, `-B <value>`, `-B<value>`

指定编译工具链中，二进制文件存放的路径。

这些二进制文件包括编译器、链接器、工具链提供的 C 运行时目标文件（如 `crt0.o`、 `crti.o` 等）。

在准备好编译工具链后，可以在将其存放在一个自定义路径，然后通过 `--toolchain <value>` 向编译器传入该路径，即可让编译器调用到该路径下的二进制文件进行交叉编译。

### `--sysroot <value>`

指定编译工具链的根目录路径。

对于目录结构固定的交叉编译工具链，如果没有指定该目录以外的二进制和动态库、静态库文件路径的需求，可以直接使用 `--sysroot <value>` 向编译器传入工具链的根目录路径，编译器会根据目标平台种类分析对应的目录结构，自动搜索所需的二进制文件和动态库、静态库文件。使用该选项后，无需再指定 `--toolchain`、`--library-path` 参数。

如果向 `triple` 为 `arch-os-env` 的平台进行交叉编译，且交叉编译工具链有以下目录结构：

```text
/usr/sdk/arch-os-env
├── bin
|   ├── arch-os-env-gcc (交叉编译器)
|   ├── arch-os-env-ld  (链接器)
|   └── ...
├── lib
|   ├── crt1.o          (C 运行时目标文件)
|   ├── crti.o
|   ├── crtn.o
|   ├── libc.so         (动态库)
|   ├── libm.so
|   └── ...
└── ...
```

对于仓颉源文件 `hello.cj` ，可以使用以下命令，将 `hello.cj` 交叉编译至 `arch-os-env` 平台：

```shell
cjc --target=arch-os-env --toolchain /usr/sdk/arch-os-env/bin --toolchain /usr/sdk/arch-os-env/lib --library-path /usr/sdk/arch-os-env/lib hello.cj -o hello
```

也可以使用简写的参数：

```shell
cjc --target=arch-os-env -B/usr/sdk/arch-os-env/bin -B/usr/sdk/arch-os-env/lib -L/usr/sdk/arch-os-env/lib hello.cj -o hello
```

如果该工具链的目录符合惯例的目录结构，可以不使用 `--toolchain`、`--library-path` 参数，直接使用以下命令：

```shell
cjc --target=arch-os-env --sysroot /usr/sdk/arch-os-env hello.cj -o hello
```

### `--strip-all`, `-s`

编译可执行文件或动态库时，指定该选项以删除输出文件中的符号表。

### `--discard-eh-frame`

编译可执行文件或动态库时，指定该选项可以删除 eh_frame 段以及 eh_frame_hdr 段中的部分信息（涉及到 crt 的相关信息不作处理），减少可执行文件或动态库的大小，但会影响调试信息。

编译 macOS 目标时暂不支持使用该功能。

### `--set-runtime-rpath`

将仓颉运行时库所在目录的绝对路径写入到二进制的 RPATH/RUNPATH 段中，使用该选项后在构建所在环境中运行该仓颉程序时无需再使用 LD_LIBRARY_PATH (适用于 Linux 平台) 或 DYLD_LIBRARY_PATH (适用于 macOS 平台) 设置仓颉运行时库目录。

编译 Windows 目标时不支持使用该功能。

### `--link-options <value>`<sup>1</sup>

指定链接器选项。

`cjc` 会将该选项的多个参数透传给链接器, 参数之间用空格分隔。可用的参数会因（系统或指定的）链接器的不同而不同。可以多次使用 `--link-options` 指定多个链接器选项。

<sup>1</sup> 上标表示链接器透传选项可能会因为链接器的不同而不同，具体支持的选项请查阅链接器文档。

### `--disable-reflection`

关闭反射选项，即编译过程中不生成相关反射信息。

> **注意：**
>
> 交叉编译至 aarch64-linux-ohos 目标时，默认关闭反射信息，该选项不生效。

### `--profile-compile-time` <sup>[frontend]</sup>

打印各编译阶段的时间消耗数据。

### `--profile-compile-memory` <sup>[frontend]</sup>

打印各编译阶段的内存消耗数据。