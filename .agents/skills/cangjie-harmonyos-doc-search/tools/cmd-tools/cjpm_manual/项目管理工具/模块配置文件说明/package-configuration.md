### "package-configuration"

每个模块的单包可配置项。该选项是个 `map` 结构，需要配置的包名作为 `key`，单包配置信息作为 `value`。当前可配置的信息包含：

- `output-type`：包编译产物类型，取值同 [`output-type`](#output-type)
- `compile-option`：仅用于该包的额外编译选项
- `combine-all-deps`：工程级编译产物合并开关，取值为 `true/false`，仅可配置于 `root` 包

上述选项均可按需配置。

如下所示，`demo` 模块中的 `demo.aoo` 包的输出类型会被指定为动态库类型，`-g` 命令会在编译时透传给 `demo.aoo` 包。

```text
[package.package-configuration."demo.aoo"]
  output-type = "dynamic"
  compile-option = "-g"
```

如果在不同字段配置了相互兼容的编译选项，生成命令的优先级如下所示。

```text
[package]
  compile-option = "-O1"
[package.package-configuration.demo]
  compile-option = "-O2"

# profile字段会在下文介绍
[profile.customized-option]
  cfg1 = "-O0"

输入: cjpm build --cfg1 -V
输出: cjc --import-path build -O0 -O1 -O2 ...
```

通过配置这个字段，可以同时生成多个二进制产物（生成多个二进制产物时，`-o, --output <value>` 选项将会失效），示例如下：

源码结构的示例，模块名为 `demo`：

```text
src
├── aoo
│    └── aoo.cj
├── boo
│    └── boo.cj
├── coo
│    └── coo.cj
└──  main.cj
```

配置方式的示例：

```text
[package.package-configuration."demo.aoo"]
  output-type = "executable"
[package.package-configuration."demo.boo"]
  output-type = "executable"
```

多个二进制产物的示例：

```text
输入：cjpm build
输出：cjpm build success

输入：tree target/release/bin
输出：target/release/bin
|-- demo.aoo
|-- demo.boo
`-- demo
```

`combine-all-deps = true` 配置后，可以开启工程级别的编译产物合并。该配置仅在以下条件下生效：

- 开启模块级动态库合并 `profile.build.combined` 和 `LTO` 编译优化 `profile.build.lto` （参考 `profile.build` 字段）；
- 配置的模块为当前执行的 `cjpm build` 命令对应的模块，并且配置的包为该模块的 `root` 包。配置在当前模块的非 `root` 包中，或配置在被依赖的模块中的该字段将被忽略。

在满足上述配置条件后，该模块会按照如下方式编译：

- 除该模块 `root` 包以外的所有包（该模块下的所有子包，以及该模块直接、间接依赖的其他模块的包含 `root` 包的所有包），会以 `LTO` 优化编译模式编译成 `.bc` 文件；
- 该模块的 `root` 包会被编译成动态库，并且链入上述所有 `.bc` 文件，无论对应的包是否被该 `root` 包导入。