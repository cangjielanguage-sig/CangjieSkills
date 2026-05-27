### "workspace"

该字段可管理多个模块作为一个工作空间，支持以下配置项：

- `members = ["aoo", "path/to/boo"]`：列举包含在此工作空间的本地源码模块，支持绝对路径和相对路径。该字段的成员必须是一个模块，不允许是另一个工作空间
- `build-members = []`：本次编译的模块，不指定时默认编译该工作空间内的所有模块。该字段的成员必须被包含在 `members` 字段中
- `test-members = []`：本次测试的模块，不指定时默认单元测试该工作空间内的所有模块。该字段的成员必须被包含在 `build-members` 字段中
- `compile-option = ""`：工作空间的公共编译选项，非必需
- `override-compile-option = ""`：工作空间的公共全局编译选项，非必需
- `link-option = ""`：工作空间的公共链接选项，非必需
- `target-dir = ""`：工作空间的产物存放路径，非必需，默认为 `target`

工作空间内的公共配置项，对所有成员模块生效。例如：配置了 `[dependencies] xoo = { path = "path_xoo" }` 的源码依赖，则所有成员模块可以直接使用 `xoo` 模块，无需在每个子模块的 `cjpm.toml` 中再配置。

> **注意：**
>
> `package` 字段用于配置模块的通用信息，不允许和 `workspace` 字段出现在同一个 `cjpm.toml` 中，除 `package` 外的其它字段均可在工作空间中使用。

工作空间目录举例：

```text
root_path
├── aoo
│    ├── src
│    └── cjpm.toml
├── boo
│    ├── src
│    └── cjpm.toml
├── coo
│    ├── src
│    └── cjpm.toml
└── cjpm.toml
```

工作空间的配置文件使用举例：

```text
[workspace]
members = ["aoo", "boo", "coo"]
build-members = ["aoo", "boo"]
test-members = ["aoo"]
compile-option = "-Woff all"
override-compile-option = "-O2"

[dependencies]
xoo = { path = "path_xoo" }

[ffi.c]
abc = { path = "libs" }
```