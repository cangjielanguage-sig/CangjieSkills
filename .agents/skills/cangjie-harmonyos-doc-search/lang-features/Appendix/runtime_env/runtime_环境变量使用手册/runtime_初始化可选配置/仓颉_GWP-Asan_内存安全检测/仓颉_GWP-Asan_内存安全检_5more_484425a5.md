### 仓颉 GWP-Asan 内存安全检测

在仓颉与 C 代码互操作的过程中，可能出现一些仓颉堆内存安全问题。仓颉 GWP-Asan 提供了一种内存安全检测功能。它可以在仓颉程序运行过程中检测代码是否存在仓颉堆内存安全问题。GWP-Asan 通过对仓颉语言标准库提供的 acquireArrayRawData 和 releaseArrayRawData 接口（参见《仓颉编程语言库 API 文档》std.core 包一节）进行采样，并记录对比采样对象前后内存的 Canary 数据，从而检测仓颉与 C 语言互操作过程中是否出现了仓颉堆内存安全问题。

仓颉 GWP-Asan 是一种基于采样的检测工具，可以通过设置不同的值来调整采样频率，以平衡性能影响和检测覆盖率。在默认或更低采样频率下，CPU 性能损失和额外的内存占用极低。

> **说明：**
>
> 仓颉 GWP-Asan 内存安全检测仅支持 Linux 和 HarmonyOS 操作系统。

#### cjEnableGwpAsan

仓颉 GWP-Asan 内存安全检测功能默认关闭。通过将环境变量 `cjEnableGwpAsan` 设置为 `1`、`true` 或 `TRUE` 可以开启该功能。Linux 下设置参考如下：

```shell
export cjEnableGwpAsan=true
```

#### cjGwpAsanSampleRate

在仓颉 GWP-Asan 内存安全检测功能开启状态下，通过环境变量 `cjGwpAsanSampleRate` 设置采样频率。`cjGwpAsanSampleRate` 支持设置为 32 位整形数值范围内的正整数，即 $(0, 2^{31} - 1]$ 。默认值为 5000，即每 5000 次 acquireArrayRawData 接口调用，进行一次采样。Linux 设置参考如下：

```shell
export cjGwpAsanSampleRate=1000
```

> **说明：**
>
> 仓颉 GWP-Asan 内存安全检测中，采样会影响性能。采样率越高，对性能影响越大，能检出更多的问题；采样率越低，其对性能影响越小，能检出更少的问题。请根据实际情况设置采样率。

#### cjGwpAsanHelp

通过环境变量 `cjGwpAsanHelp` 可以设置是否在控制台输出 GWP-Asan 帮助信息。默认不开启。`cjGwpAsanHelp` 设置为`1`、`true` 或 `TRUE` 时，表示在控制台输出帮助信息。Linux 设置参考如下：

```shell
export cjGwpAsanHelp=true
```

#### 约束限制

- 仓颉 GWP-Asan 是一种基于采样的内存检查工具，内存越界问题可能无法完全检出。
- 仓颉 GWP-Asan 对仓颉堆内存的越界检测范围有限，无法检测内存读越界访问，仅能检测部分写越界访问：向前写越界 8 字节以内；向后写越界到尾部的填充区域（根据数组对象长度的不同，填充区域可能为 0-7 字节）。