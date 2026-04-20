### "dependencies"

该字段通过源码方式导入依赖的其它仓颉模块，里面配置了当前构建所需要的其它模块的信息。目前，该字段支持本地路径依赖和远程 `git` 依赖。

要指定本地依赖项，请使用 `path` 字段，并且它必须包含有效的本地路径。例如，下面的两个子模块 `pro0` 和 `pro1` 和主模块的代码结构如下：

```text
├── pro0
│    ├── cjpm.toml
│    └── src
│         └── zoo
│              └── zoo.cj
├── pro1
│    ├── cjpm.toml
│    └── src
│         ├── xoo
│         │    └── xoo.cj
│         └── yoo
│              └── yoo.cj
├── cjpm.toml
└── src
     ├── aoo
     │    └── aoo.cj
     ├── boo
     │    └── boo.cj
     └── main.cj
```

在主模块的 `cjpm.toml` 中进行如下配置后，即可在源码中使用 `pro0` 和 `pro1` 模块：

```text
[dependencies]
  pro0 = { path = "./pro0" }
  pro1 = { path = "./pro1" }
```

要指定远程 `git` 依赖项，请使用 `git` 字段，并且它必须包含 `git` 支持的任何格式的有效 `url`。要配置 `git` 依赖关系，最多可以有一个 `branch`、`tag` 和 `commitId` 字段，这些字段允许分别选择特定的分支、标记或提交哈希，若配置多个此类字段则仅会生效优先级最高的配置，优先级顺序为 `commitId` > `branch` > `tag`。例如，进行如下配置后，即可在源码中使用特定 `git` 仓库地址的 `pro0` 和 `pro1` 模块：

```text
[dependencies]
  pro0 = { git = "https://github.com/example", tag = "v1.0.0"}
  pro1 = { git = "https://gitee.com/example", branch = "dev"}
```

在这种情况下，`cjpm` 将下载对应存储库的最新版本，并将当前 `commit-hash` 保存在 `cjpm.lock` 文件中。所有后续的 `cjpm` 调用都将使用保存的版本，直到使用 `cjpm update`。

通常需要一些身份验证才能访问 `git` 存储库。`cjpm` 不要求提供所需的凭据，因此应使用现有的 `git` 身份验证支持。如果用于 `git` 的协议是 `https`，则需要使用一些现有的 git 凭据帮助程序。在 `Windows` 上，可在安装 `git` 时一起安装凭据帮助程序，默认使用。在 `Linux/macOS` 上，请参见 `git` 官方文档中 `git-config` 的配置说明，了解有关设置凭据帮助程序的详细信息。如果协议是 `ssh` 或 `git`，则应使用基于密钥的身份验证。如果密钥受密码短语保护，则开发者应确保 `ssh-agent` 正在运行，并且在使用 `cjpm` 之前通过 `ssh-add` 添加密钥。

`dependencies` 字段可以通过 `output-type` 属性指定编译产物类型，指定的类型可以与源码依赖自身的编译产物类型不一致，且仅能为 `static` 或者 `dynamic`，如下所示：

```text
[dependencies]
  pro0 = { path = "./pro0", output-type = "static" }
  pro1 = { git = "https://gitee.com/example", output-type = "dynamic" }
```

进行如上配置后，将会忽略 `pro0` 和 `pro1` 的 `cjpm.toml` 中的 `output-type` 配置，将这两个模块的产物分别编译成 `static` 和 `dynamic` 类型。