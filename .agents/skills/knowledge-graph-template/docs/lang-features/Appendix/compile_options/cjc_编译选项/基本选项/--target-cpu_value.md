### `--target-cpu <value>`

> **注意：**
>
> 该选项为实验性功能，使用该功能生成的二进制可能存在潜在的运行时问题，请注意使用该选项的风险。此选项必须配合 `--experimental` 选项一同使用。

指定编译目标的 CPU 类型。

指定编译目标的 CPU 类型时，编译器在生成二进制时会尝试使用该 CPU 类型特有的扩展指令集，并尝试应用适用于该 CPU 类型的优化。为某个特定 CPU 类型生成的二进制通常会失去可移植性，该二进制可能无法在其他（拥有相同架构指令集的）CPU 上运行。

该选项支持以下经过测试的 CPU 类型：

**x86-64 架构：**

- generic

**aarch64 架构：**

- generic
- tsv110

`generic` 为通用 CPU 类型，指定 `generic` 时编译器会生成适用于该架构的通用指令，这样生成的二进制在操作系统和二进制本身的动态依赖一致的前提下，可以在基于该架构的各种 CPU 上运行，无关于具体的 CPU 类型。`--target-cpu` 选项的默认值为 `generic`。

该选项还支持以下 CPU 类型，但以下 CPU 类型未经过测试验证，请注意使用以下 CPU 类型生成的二进制可能会存在运行时问题。

**x86-64 架构：**

- alderlake
- amdfam10
- athlon
- athlon-4
- athlon-fx
- athlon-mp
- athlon-tbird
- athlon-xp
- athlon64
- athlon64-sse3
- atom
- barcelona
- bdver1
- bdver2
- bdver3
- bdver4
- bonnell
- broadwell
- btver1
- btver2
- c3
- c3-2
- cannonlake
- cascadelake
- cooperlake
- core-avx-i
- core-avx2
- core2
- corei7
- corei7-avx
- geode
- goldmont
- goldmont-plus
- haswell
- i386
- i486
- i586
- i686
- icelake-client
- icelake-server
- ivybridge
- k6
- k6-2
- k6-3
- k8
- k8-sse3
- knl
- knm
- lakemont
- nehalem
- nocona
- opteron
- opteron-sse3
- penryn
- pentium
- pentium-m
- pentium-mmx
- pentium2
- pentium3
- pentium3m
- pentium4
- pentium4m
- pentiumpro
- prescott
- rocketlake
- sandybridge
- sapphirerapids
- silvermont
- skx
- skylake
- skylake-avx512
- slm
- tigerlake
- tremont
- westmere
- winchip-c6
- winchip2
- x86-64
- x86-64-v2
- x86-64-v3
- x86-64-v4
- yonah
- znver1
- znver2
- znver3

**aarch64 架构：**

- a64fx
- ampere1
- apple-a10
- apple-a11
- apple-a12
- apple-a13
- apple-a14
- apple-a7
- apple-a8
- apple-a9
- apple-latest
- apple-m1
- apple-s4
- apple-s5
- carmel
- cortex-a34
- cortex-a35
- cortex-a510
- cortex-a53
- cortex-a55
- cortex-a57
- cortex-a65
- cortex-a65ae
- cortex-a710
- cortex-a72
- cortex-a73
- cortex-a75
- cortex-a76
- cortex-a76ae
- cortex-a77
- cortex-a78
- cortex-a78c
- cortex-r82
- cortex-x1
- cortex-x1c
- cortex-x2
- cyclone
- exynos-m3
- exynos-m4
- exynos-m5
- falkor
- kryo
- neoverse-512tvb
- neoverse-e1
- neoverse-n1
- neoverse-n2
- neoverse-v1
- saphira
- thunderx
- thunderx2t99
- thunderx3t110
- thunderxt81
- thunderxt83
- thunderxt88

除以上可选 CPU 类型外，该选项还可以使用 `native` 作为当前 CPU 类型。编译器会尝试识别当前机器的 CPU 类型，并使用该 CPU 类型作为目标类型生成二进制文件。