### init

`init` 用于初始化一个新的仓颉模块或者工作空间。初始化模块时，默认在当前文件夹创建配置文件 `cjpm.toml`，并新建 `src` 源码文件夹。如果该模块的产物为可执行类型，则会在 `src` 下生成默认的 `main.cj` 文件，并在编译后打印输出 `hello world`。初始化工作空间时仅会创建 `cjpm.toml` 文件，默认会扫描该路径下已有的仓颉模块并添加到 `members` 字段中。若已存在 `cjpm.toml` 文件，或源码文件夹内已存在 `main.cj`，则会跳过对应的文件创建步骤。

`init` 有多个可配置项：

- `--workspace` 新建一个工作空间配置文件，指定该选项时以上其它选项无效会自动忽略
- `--name <value>` 指定新建模块的 `root` 包名，不指定时默认为上一级子文件夹名称
- `--path <value>` 指定新建模块的路径，不指定时默认为当前文件夹
- `--type=<executable|static|dynamic>` 指定新建模块的产物类型，缺省时默认为 `executable`

例如：

```text
输入: cjpm init
输出: cjpm init success
```

```text
输入: cjpm init --name demo --path project
输出: cjpm init success
```

```text
输入: cjpm init --type=static
输出: cjpm init success
```

### check

`check` 命令用于检查项目中所需的依赖项，执行成功将会打印有效的包编译顺序。

`check` 有多个可配置项：

- `-m, --member <value>` 仅可在工作空间下使用，可用于指定单个模块作为检查入口
- `--no-tests` 配置后，测试相关的依赖将不会被打印
- `--skip-script` 配置后，将会跳过构建脚本的编译运行

例如：

```text
输入: cjpm check
输出:
The valid serial compilation order is:
    b.pkgA -> b
cjpm check success
```

```text
输入: cjpm check
输出:
Error: cyclic dependency
b.B -> c.C
c.C -> d.D
d.D -> b.B
输出说明：上述输出中，b.B 代表以 b 为 root 包的模块中的一个名为 b.B 的子包
```

```text
输入: cjpm check
输出:
Error: can not find the following dependencies
    pro1.xoo
    pro1.yoo
    pro2.zoo
```

### update

`update` 用于将 `cjpm.toml` 里的内容更新到 `cjpm.lock`。当 `cjpm.lock` 不存在时，将会生成该文件。`cjpm.lock` 文件记录着 `git` 依赖的版本号等元信息，用于下次构建使用。

`update` 有以下可配置项：

- `--skip-script` 配置后，将会跳过构建脚本的编译运行

```text
输入: cjpm update
输出: cjpm update success
```

### tree

`tree` 命令用于可视化地展示仓颉源码中的包依赖关系。

`tree` 有多个可配置项：

- `-V, --verbose` 增加包节点的详细信息，包括包名、版本号和包路径
- `--depth <N>` 指定依赖树的最大深度，可选值是非负整数。指定该选项时，默认会以所有包作为根节点。其中，N 的值代表每个依赖树的子节点最大深度
- `-p, --package <value>` 指定某个包为根节点，从而展示它的子依赖包，需要配置的值是包名
- `--invert <value>` 指定某个包为根节点并反转依赖树，从而展示它被哪些包所依赖，需要配置的值是包名
- `--target <value>` 将指定目标平台的依赖项加入分析，并展示依赖关系
- `--no-tests` 排除 `test-dependencies` 字段的依赖项
- `--skip-script` 配置后，将会跳过构建脚本的编译运行

例如，模块 `a` 的源代码目录结构如下：

```text
src
├── main.cj
├── aoo
│   └── a.cj
├── boo
│   └── b.cj
├── coo
│   └── c.cj
├── doo
│   └── d.cj
└── eoo
    └── e.cj
```

依赖关系为：包 `a` 导入包 `a.aoo`、`a.boo`，子包 `aoo` 导入包 `a.coo`，子包 `boo` 导入包 `coo`，子包 `doo` 导入包 `coo`。

```text
输入: cjpm tree
输出:
|-- a
    └── a.aoo
        └── a.coo
    └── a.boo
        └── a.coo
|-- a.doo
    └── a.coo
|-- a.eoo
cjpm tree success
```

```text
输入: cjpm tree --depth 2 -p a
输出:
|-- a
    └── a.aoo
        └── a.coo
    └── a.boo
        └── a.coo
cjpm tree success
```

```text
输入: cjpm tree --depth 0
输出:
|-- a
|-- a.eoo
|-- a.aoo
|-- a.boo
|-- a.doo
|-- a.coo
cjpm tree success
```

```text
输入: cjpm tree --invert a.coo --verbose
输出:
|-- a.coo 1.2.0 （.../src/coo）
    └── a.aoo 1.1.0 （.../src/aoo）
            └── a 1.0.0 （.../src）
    └── a.boo 1.1.0 （.../src/boo）
            └── a 1.0.0 （.../src）
    └── a.doo 1.3.0 （.../src/doo）
cjpm tree success
```