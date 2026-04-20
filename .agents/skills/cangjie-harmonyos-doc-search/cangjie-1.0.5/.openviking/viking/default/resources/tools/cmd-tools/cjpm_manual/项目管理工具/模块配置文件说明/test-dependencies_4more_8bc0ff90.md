### "test-dependencies"

具有与 `dependencies` 字段相同的格式。它用于指定仅在测试过程中使用的依赖项，而不是构建主项目所需的依赖项。模块开发者应将此字段用于此模块的下游用户不需要感知的依赖项。

`test-dependencies` 内的依赖仅可用于文件名形如 `xxx_test.cj` 的测试文件，在编译时这些依赖将不会被编译。`test-dependencies` 在 `cjpm.toml` 中的配置格式与 `dependencies` 相同。

### "script-dependencies"

具有与 `dependencies` 字段相同的格式。它用于指定仅在编译构建脚本中使用的依赖项，而不是构建主项目所需的依赖项。构建脚本相关功能将在[其他-构建脚本](#构建脚本)章节中详述。

### "replace"

具有与 `dependencies` 字段相同的格式。它用于指定间接依赖的同名替换项，配置的依赖项会作为编译该模块时最终使用的依赖版本。

例如，如下模块 `aaa` 依赖了一个本地模块 `bbb`：

```text
[package]
  name = "aaa"

[dependencies]
  bbb = { path = "path/to/bbb" }
```

主模块 `demo` 依赖 `aaa` 的情况下，`bbb` 即成为 `demo` 的间接依赖模块。在这种情况下，主模块 `demo` 若想替换 `bbb` 为另一个同名模块，例如在另一个路径 `new/path/to/bbb` 下的 `bbb` 模块，则可以进行如下配置：

```text
[package]
  name = "demo"

[dependencies]
  aaa = { path = "path/to/aaa" }

[replace]
  bbb = { path = "new/path/to/bbb" }
```

配置后，编译 `demo` 模块时，实际使用的间接依赖 `bbb` 为 `new/path/to/bbb` 下的 `bbb` 模块。`aaa` 中配置的 `path/to/bbb` 下的 `bbb` 模块不会被编译。

> **注意：**
>
> 仅入口模块的 `replace` 字段会在编译时生效。

### "ffi.c"

当前仓颉模块外部依赖 `c` 库的配置。该字段配置了依赖该库所需要的信息，包含库名和路径。

开发者需要自行编出动态库或静态库放到设置的 `path` 下，可参考下面的例子。

仓颉调用外部 `c` 动态库的方法说明：

- 自行将相应的 `hello.c` 文件编成 `.so`库（在该文件路径执行 `clang -shared -fPIC hello.c -o libhello.so`）
- 修改该项目的 `cjpm.toml` 文件，配置 `ffi.c` 字段，如下面的例子所示。其中，`./src/` 是编出的 `libhello.so` 相对当前目录的地址，`hello` 为库名。
- 执行 `cjpm build`，即可编译成功。

```text
[ffi.c]
hello = { path = "./src/" }
```