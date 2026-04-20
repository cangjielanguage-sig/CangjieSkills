## 优化选项

### `--fchir-constant-propagation` <sup>[frontend]</sup>

开启 chir 常量传播优化。

### `--fno-chir-constant-propagation` <sup>[frontend]</sup>

关闭 chir 常量传播优化。

### `--fchir-function-inlining` <sup>[frontend]</sup>

开启 chir 函数内联优化。

### `--fno-chir-function-inlining` <sup>[frontend]</sup>

关闭 chir 函数内联优化。

### `--fchir-devirtualization` <sup>[frontend]</sup>

开启 chir 去虚函数调用优化。

### `--fno-chir-devirtualization` <sup>[frontend]</sup>

关闭 chir 去虚函数调用优化。

### `--fast-math` <sup>[frontend]</sup>

开启此选项后，编译器会对浮点数作一些激进且有可能损失精度的假设，以便优化浮点数运算。

### `-O<N>` <sup>[frontend]</sup>

使用参数指定的代码优化级别。

指定越高的优化级别，编译器会越多地进行代码优化以生成更高效的程序，同时也可能会需要更长的编译时间。

`cjc` 默认使用 O0 级别的代码优化。当前 `cjc` 支持如下优化级别：O0、O1、O2、Os、Oz。

当优化等级等于 2 时，`cjc` 除了进行对应的优化外，还会开启以下选项：

- `--fchir-constant-propagation`
- `--fchir-function-inlining`
- `--fchir-devirtualization`

当优化等级等于 s 时， `cjc`除了进行 O2 级别优化外，将针对 code size 进行优化。

当优化等级等于 z 时， `cjc`除了进行 Os 级别优化外，还将进一步缩减 code size 大小。

> **注意：**
>
> 当优化等级等于 s 或 z 时，不允许同时使用链接时优化编译选项 `--lto=[full|thin]`。

### `-O` <sup>[frontend]</sup>

使用 O1 级别的代码优化，等价于 `-O1`。