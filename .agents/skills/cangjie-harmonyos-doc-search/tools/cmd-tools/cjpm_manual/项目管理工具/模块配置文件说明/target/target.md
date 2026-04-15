### "target"

多后端、多平台隔离选项，用于配置不同后端、不同平台情况下的一系列不同配置项。以 `Linux` 系统为例，`target` 配置方式如下：

```text
[target.x86_64-unknown-linux-gnu] # Linux 系统的配置项
  compile-option = "value1" # 额外编译命令选项
  override-compile-option = "value2" # 额外全局编译命令选项
  link-option = "value3" # 链接器透传选项
  [target.x86_64-unknown-linux-gnu.dependencies] # 源码依赖配置项
  [target.x86_64-unknown-linux-gnu.test-dependencies] # 测试阶段依赖配置项
  [target.x86_64-unknown-linux-gnu.bin-dependencies] # 仓颉二进制库依赖
    path-option = ["./test/pro0", "./test/pro1"]
  [target.x86_64-unknown-linux-gnu.bin-dependencies.package-option]
    "pro0.xoo" = "./test/pro0/pro0.xoo.cjo"
    "pro0.yoo" = "./test/pro0/pro0.yoo.cjo"
    "pro1.zoo" = "./test/pro1/pro1.zoo.cjo"

[target.x86_64-unknown-linux-gnu.debug] # Linux 系统的 debug 配置项
  [target.x86_64-unknown-linux-gnu.debug.test-dependencies]

[target.x86_64-unknown-linux-gnu.release] # Linux 系统的 release 配置项
  [target.x86_64-unknown-linux-gnu.release.bin-dependencies]
```

开发者可以通过配置 `target.target-name` 字段为某个 `target` 添加一系列配置项。`target` 的名称可以在相应的仓颉环境下通过命令 `cjc -v` 获取，命令输出中的 `Target` 项目即为该环境对应的 `target` 名称。上述用例应用于 `Linux` 系统，其他平台也适用，同样可以通过命令 `cjc -v` 获取 `target` 名称。

为特定 `target` 配置的专用配置项，将作用于该 `target` 的编译流程，也能被其他以该 `target` 为目标平台的交叉编译流程使用。配置项列表如下：

- `compile-option`：额外编译命令选项
- `override-compile-option`：额外全局编译命令选项
- `link-option`：链接器透传选项
- `dependencies`：源码依赖配置项，结构同 `dependencies` 字段
- `test-dependencies`：测试阶段依赖配置项，结构同 `test-dependencies` 字段
- `bin-dependencies`：仓颉二进制库依赖，结构在下文中介绍
- `compile-macros-for-target`：交叉编译时的宏包控制项，该选项不支持区分下述的 `debug` 和 `release` 编译模式

开发者可以通过配置 `target.target-name.debug` 和 `target.target-name.release` 字段为该 `target` 额外配置在 `debug` 和 `release` 编译模式下特有的配置，可配置的配置项同上。配置于此类字段的配置项将仅应用于该 `target` 的对应编译模式。