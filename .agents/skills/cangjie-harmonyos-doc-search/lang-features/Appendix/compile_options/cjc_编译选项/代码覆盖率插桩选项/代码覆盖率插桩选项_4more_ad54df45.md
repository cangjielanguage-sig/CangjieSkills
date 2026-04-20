## 代码覆盖率插桩选项

> **注意：**
>
> Windows 和 macOS 版本目前不支持代码覆盖率插桩选项。

仓颉支持对代码覆盖率插桩（SanitizerCoverage，以下简称 SanCov），提供与 LLVM 的 SanitizerCoverage 一致的接口，编译器在函数级或 BasicBlock 级插入覆盖率反馈函数，用户只需要实现约定好的回调函数即可在运行过程中感知程序运行状态。

仓颉提供的 SanCov 功能以 package 为单位，即整个 package 只有全部插桩和全部不插桩两种情况。

### `--sanitizer-coverage-level=0/1/2`

插桩级别：

- 0 表示不插桩；
- 1 表示函数级插桩，仅在函数入口处插入回调函数；
- 2 表示 BasicBlock 级插桩，在各个 BasicBlock 处插入回调函数。

如果不指定，默认值为 2。

该编译选项仅影响 `--sanitizer-coverage-trace-pc-guard`、`--sanitizer-coverage-inline-8bit-counters` 和 `--sanitizer-coverage-inline-bool-flag` 的插桩级别。

### `--sanitizer-coverage-trace-pc-guard`

开启该选项，会在每个 Edge 插入函数调用 `__sanitizer_cov_trace_pc_guard(uint32_t *guard_variable)`，受 `sanitizer-coverage-level` 影响。

**值得注意的是**，该功能存在与 gcc/llvm 实现不一致的地方：不会在 constructor 插入 `void __sanitizer_cov_trace_pc_guard_init(uint32_t *start, uint32_t *stop)`，而是在 package 初始化阶段插入函数调用 `uint32_t *__cj_sancov_pc_guard_ctor(uint64_t edgeCount)`。

`__cj_sancov_pc_guard_ctor` 回调函数需要开发者自行实现，开启 SanCov 的 package 会尽可能早地调用该回调函数，入参是该 Package 的 Edge 个数，返回值是通常是 calloc 创建的内存区域。

如果需要调用 `__sanitizer_cov_trace_pc_guard_init`，建议在 `__cj_sancov_pc_guard_ctor` 中调用，使用动态创建的缓冲区计算该函数的入参和返回值。

一个标准的 `__cj_sancov_pc_guard_ctor` 参考实现如下：

```cpp
uint32_t *__cj_sancov_pc_guard_ctor(uint64_t edgeCount) {
    uint32_t *p = (uint32_t *) calloc(edgeCount, sizeof(uint32_t));
    __sanitizer_cov_trace_pc_guard_init(p, p + edgeCount);
    return p;
}
```

### `--sanitizer-coverage-inline-8bit-counters`

开启该选项后，会在每个 Edge 插入一个累加器，每经历过一次，该累加器加一，受 `sanitizer-coverage-level` 影响。

**值得注意的是**，该功能存在与 gcc/llvm 实现不一致的地方：不会在 constructor 插入 `void __sanitizer_cov_8bit_counters_init(char *start, char *stop)`，而是在 package 初始化阶段插入函数调用 `uint8_t *__cj_sancov_8bit_counters_ctor(uint64_t edgeCount)`。

`__cj_sancov_pc_guard_ctor` 回调函数需要开发者自行实现，开启 SanCov 的 package 会尽可能早地调用该回调函数，入参是该 Package 的 Edge 个数，返回值是通常是 calloc 创建的内存区域。

如果需要调用 `__sanitizer_cov_8bit_counters_init`，建议在 `__cj_sancov_8bit_counters_ctor` 中调用，使用动态创建的缓冲区计算该函数的入参和返回值。

一个标准的 `__cj_sancov_8bit_counters_ctor` 参考实现如下：

```cpp
uint8_t *__cj_sancov_8bit_counters_ctor(uint64_t edgeCount) {
    uint8_t *p = (uint8_t *) calloc(edgeCount, sizeof(uint8_t));
    __sanitizer_cov_8bit_counters_init(p, p + edgeCount);
    return p;
}
```