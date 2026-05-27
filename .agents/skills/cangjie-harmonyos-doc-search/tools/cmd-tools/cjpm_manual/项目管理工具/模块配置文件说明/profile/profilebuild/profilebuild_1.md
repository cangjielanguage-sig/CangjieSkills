#### "profile.build"

```text
[profile.build]
lto = "full"  # 是否开启 `LTO` （Link Time Optimization 链接时优化）优化编译模式，仅 `Linux` 平台支持该功能
performance_analysis = true # 开启编译性能分析功能
incremental = true # 是否默认开启增量编译
[profile.build.combined]
demo = "dynamic" # 将模块整体编译成一个动态库文件，key 值为模块名
```

编译流程的控制项，所有字段均可缺省，不配置时不生效，顶层模块设置的 `profile.build` 项才会生效。

`lto` 配置项的取值为 `full` 或 `thin`，对应 `LTO` 优化支持的两种编译模式：`full LTO` 将所有编译模块合并到一起，在全局上进行优化，这种方式可以获得最大的优化潜力，同时也需要更长的编译时间；`thin LTO` 在多模块上使用并行优化，同时默认支持链接时增量编译，编译时间比 `full LTO` 短，但是因为失去了更多的全局信息，所以优化效果不如 `full LTO`。

`performance_analysis` 配置项的取值为 `true` 或 `false`，代表是否开启编译性能分析功能。当开启此功能时，`cjpm` 会在编译产物目录下的 `performance_analysis` 目录中生成 `.prof` 和 `.json` 文件，这些文件记录了编译过程中的时间和内存消耗。例如，编译产物目录默认为 `target` 目录，且编译模式为 `debug`，则产物目录结构如下：

```text
demo
├── cjpm.toml
├── src
|   └── demo.cj
└── target
    └── debug
        └── performance_analysis
            ├── xxx1.prof
            ├── ...
            ├── xxxN.prof
            ├── xxx1.json
            ├── ...
            └── xxxN.json
```

`combined` 配置项是一个键值对，其中键为模块名，即 `package.name`，值为 `dynamic`。配置该配置项之前，该模块会根据 `package.output-type` 配置将各个包编译成独立的动态库或静态库文件；配置后，该模块的编译方式改为：

- 模块内除 `root` 包以外的子包以静态库形式编译；
- `root` 包以动态库形式编译，并且链接所有子包的静态库，无论子包是否被 `root` 包依赖。其他模块以二进制依赖形式依赖该动态库时，可以使用所有子包内的符号。

例如，假设模块 `demo` 的结构如下：

```text
demo
├── cjpm.toml
└── src
     ├── aoo
     |    └── aoo.cj
     ├── boo
     |    └── boo.cj
     └── demo.cj
```

模块配置文件 `cjpm.toml` 内配置如下：

```text
[package]
name = "demo"

[profile.build.combined]
demo = "dynamic"
```

在编译之后，最终的编译产物目录 `target/release/demo` 中的产物列表如下（以 `Linux` 为例）：

```text
|-- libdemo.so
|-- libdemo.aoo.a
|-- libdemo.boo.a
|-- demo.cjo
|-- demo.aoo.cjo
|-- demo.boo.cjo
```

模块开发者可以将上述产物列表中的所有 `cjo` 文件和 `root` 包动态库 `libdemo.so` 提供给其他模块作为二进制依赖，无需提供子包的静态库文件。其他模块依赖该动态库之后，可以在代码中依赖其所有子包，例如可以通过 `import demo.aoo` 的方式依赖 `demo.aoo` 包。

> **注意：**
>
> - 在应用此配置时，编译 `root` 包动态库需要使用其所有子包的静态库，因此需要保证 `root` 包不被其子包直接或间接导入。
> - 目前 `profile.build.combined` 配置项为实验特性，暂不稳定，开发者若想启用该配置，需要注意如下限制：
>     - 如果配置了该字段的模块直接或间接依赖了其他源码模块，那么这些依赖模块也需要配置该字段；
>     - 构建脚本依赖的源码模块中，若配置了 `profile.build.combined`，不会生效；
>     - `profile.build.combined` 选项仅支持 `Linux/OpenHarmonyOS/Windows` 平台。

若启用了 `combined` 配置，可能会出现无法通过导入关系识别的循环依赖，导致出现 `cyclic dependency` 循环依赖报错，解决方式如下：