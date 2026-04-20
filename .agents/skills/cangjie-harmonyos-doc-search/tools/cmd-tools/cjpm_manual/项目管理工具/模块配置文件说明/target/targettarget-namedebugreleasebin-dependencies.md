#### "target.target-name[.debug/release].bin-dependencies"

该字段用于导入已编译好的、适用于指定 `target` 的仓颉库产物文件，以导入下述的 `pro0` 模块和 `pro1` 模块的三个包来举例说明。

> **注意：**
>
> 非特殊需求场景，不建议使用该字段，请使用上文介绍的 `dependencies` 字段导入模块源码。

```text
├── test
│    ├── pro0
│    │    ├── libpro0.xoo.so
│    │    ├── pro0.xoo.cjo
│    │    ├── libpro0.yoo.so
│    │    └── pro0.yoo.cjo
│    └── pro1
│         ├── libpro1.zoo.so
│         └── pro1.zoo.cjo
├── src
│    └── main.cj
└── cjpm.toml
```

方式一，通过 `path-option` 导入：

```text
[target.x86_64-unknown-linux-gnu.bin-dependencies]
  path-option = ["./test/pro0", "./test/pro1"]
```

`path-option` 选项为字符串数组结构，每个元素代表待导入的路径名称。`cjpm` 会自动导入该路径下所有符合规则的仓颉库包，这里的合规性是指库名称的格式为 `完整包名`。例如，上述例子中的 `pro0.xoo.cjo` 对应的库名称应为 `libpro0.xoo.so` 或 `libpro0.xoo.a`。库名称不满足该规则的包只能通过 `package-option` 选项进行导入。

方式二，通过 `package-option` 导入：

```text
[target.x86_64-unknown-linux-gnu.bin-dependencies.package-option]
  "pro0.xoo" = "./test/pro0/pro0.xoo.cjo"
  "pro0.yoo" = "./test/pro0/pro0.yoo.cjo"
  "pro1.zoo" = "./test/pro1/pro1.zoo.cjo"
```

`package-option` 选项为 `map` 结构，`pro0.xoo` 名称作为 `key` (`toml` 配置文件中含有 `.` 的字符串作为整体时，需要用 `""` 包含)，所以 `key` 的值为 `libpro0.xoo.so` 。前端文件 `cjo` 的路径作为 `value`，对应于该 `cjo` 的 `.a` 或 `.so` 需放置在相同路径下。

> **注意：**
>
> 如果同时通过 `package-option` 和 `path-option` 导入了相同的包，则 `package-option` 字段的优先级更高。

其中，源码 `main.cj` 调用 `pro0.xoo`、`pro0.yoo`、`pro1.zoo` 包的代码示例如下所示。

```cangjie
import pro0.xoo.*
import pro0.yoo.*
import pro1.zoo.*

main(): Int64 {
    var res = x + y + z // x, y, z 分别为 pro0.xoo, pro0.yoo, pro1.zoo 中定义的值
    println(res)
    return 0
}
```

> **注意：**
>
> 依赖的仓颉动态库文件可能是其他模块通过配置 `profile.build.combined` 生成的 `root` 包编译产物，包含其所有子包的符号。因此，在依赖检查时，如果找不到某个包对应的仓颉库，会使用该包对应的 `root` 包作为依赖，并打印告警提示。开发者需要保证以此方式导入的 `root` 包是通过对应方式生成的仓颉库文件，否则该库文件可能不会包含子包的符号，导致编译报错。
> 例如，源码中通过 `import demo.aoo` 导入了 `demo.aoo` 包，在二进制依赖中没有找到该包对应的仓颉库，`cjpm` 会尝试寻找该包对应的 `root` 包的动态库，即 `libdemo.so`，如果找到则使用该库作为依赖。