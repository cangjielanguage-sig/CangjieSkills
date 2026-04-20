### `--sanitizer-coverage-inline-bool-flag`

开启该选项后，会在每个 Edge 插入布尔值，经历过的 Edge 对应的布尔值会被设置为 True，受 `sanitizer-coverage-level` 影响。

**值得注意的是**，该功能存在与 gcc/llvm 实现不一致的地方：不会在 constructor 插入 `void __sanitizer_cov_bool_flag_init(bool *start, bool *stop)`，而是在 package 初始化阶段插入函数调用 `bool *__cj_sancov_bool_flag_ctor(uint64_t edgeCount)`。

`__cj_sancov_bool_flag_ctor` 回调函数需要开发者自行实现，开启 SanCov 的 package 会尽可能早地调用该回调函数，入参是该 Package 的 Edge 个数，返回值是通常是 calloc 创建的内存区域。

如果需要调用 `__sanitizer_cov_bool_flag_init`，建议在 `__cj_sancov_bool_flag_ctor` 中调用，使用动态创建的缓冲区计算该函数的入参和返回值。

一个标准的 `__cj_sancov_bool_flag_ctor` 参考实现如下：

```cpp
bool *__cj_sancov_bool_flag_ctor(uint64_t edgeCount) {
    bool *p = (bool *) calloc(edgeCount, sizeof(bool));
    __sanitizer_cov_bool_flag_init(p, p + edgeCount);
    return p;
}
```

### `--sanitizer-coverage-pc-table`

该编译选项用于提供插桩点和源码之间的对应关系，当前只提供精确到函数级的对应关系。需要与 `--sanitizer-coverage-trace-pc-guard`、`--sanitizer-coverage-inline-8bit-counters`、`--sanitizer-coverage-inline-bool-flag` 共用，至少需要开启其中一项，可以同时开启多项。

**值得注意的是**，该功能存在与 gcc/llvm 实现不一致的地方：不会在 constructor 插入 `void __sanitizer_cov_pcs_init(const uintptr_t *pcs_beg, const uintptr_t *pcs_end);`，而是在 package 初始化阶段插入函数调用 `void __cj_sancov_pcs_init(int8_t *packageName, uint64_t n, int8_t **funcNameTable, int8_t **fileNameTable, uint64_t *lineNumberTable)`，各入参含义如下：

- `int8_t *packageName`: 字符串，表示包名（插桩用 c 风格的 int8 数组作为入参来表达字符串，下同）。
- `uint64_t n`: 共有 n 个函数被插桩。
- `int8_t **funcNameTable`: 长度为 n 的字符串数组，第 i 个插桩点对应的函数名为 funcNameTable\[i\]。
- `int8_t **fileNameTable`: 长度为 n 的字符串数组，第 i 个插桩点对应的文件名为 fileNameTable\[i\]。
- `uint64_t *lineNumberTable`: 长度为 n 的 uint64 数组，第 i 个插桩点对应的行号为 lineNumberTable\[i\]。

如果需要调用 `__sanitizer_cov_pcs_init`，需要自行完成仓颉 pc-table 到 C 语言 pc-table 的转化。

### `--sanitizer-coverage-stack-depth`

开启该编译选项后，由于仓颉无法获取 SP 指针的值，因此只能在每个函数入口处插入调用 `__updateSancovStackDepth`，在 C 侧实现该函数即可获得 SP 指针。

一个标准的 `updateSancovStackDepth` 实现如下：

```cpp
thread_local void* __sancov_lowest_stack;

void __updateSancovStackDepth()
{
    register void* sp = __builtin_frame_address(0);
    if (sp < __sancov_lowest_stack) {
        __sancov_lowest_stack = sp;
    }
}
```

### `--sanitizer-coverage-trace-compares`

开启该选项后，会在所有的 compare 指令和 match 指令调用前插入函数回调函数，具体列表如下，与 LLVM 系的 API 功能一致。参考 Tracing data flow。

```cpp
void __sanitizer_cov_trace_cmp1(uint8_t Arg1, uint8_t Arg2);
void __sanitizer_cov_trace_const_cmp1(uint8_t Arg1, uint8_t Arg2);
void __sanitizer_cov_trace_cmp2(uint16_t Arg1, uint16_t Arg2);
void __sanitizer_cov_trace_const_cmp2(uint16_t Arg1, uint16_t Arg2);
void __sanitizer_cov_trace_cmp4(uint32_t Arg1, uint32_t Arg2);
void __sanitizer_cov_trace_const_cmp4(uint32_t Arg1, uint32_t Arg2);
void __sanitizer_cov_trace_cmp8(uint64_t Arg1, uint64_t Arg2);
void __sanitizer_cov_trace_const_cmp8(uint64_t Arg1, uint64_t Arg2);
void __sanitizer_cov_trace_switch(uint64_t Val, uint64_t *Cases);
```