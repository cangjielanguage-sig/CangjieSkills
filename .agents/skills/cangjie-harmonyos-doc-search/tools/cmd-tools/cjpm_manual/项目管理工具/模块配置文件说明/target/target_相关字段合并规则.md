#### "target" 相关字段合并规则

`target` 配置项中的内容可能同时存在于 `cjpm.toml` 的其他选项中，例如 `compile-option` 字段在 `package` 字段中也可以存在，区别在于 `package` 中的该字段会应用于全部 `target`。`cjpm` 对这些重复的字段会按照特定的方式将所有可应用的配置合并。以 `x86_64-unknown-linux-gnu` 的 `debug` 编译模式为例，有如下的 `target` 配置：

```text
[package]
  compile-option = "compile-0"
  override-compile-option = "override-compile-0"
  link-option = "link-0"

[dependencies]
  dep0 = { path = "./dep0" }

[test-dependencies]
  devDep0 = { path = "./devDep0" }

[target.x86_64-unknown-linux-gnu]
  compile-option = "compile-1"
  override-compile-option = "override-compile-1"
  link-option = "link-1"
  [target.x86_64-unknown-linux-gnu.dependencies]
    dep1 = { path = "./dep1" }
  [target.x86_64-unknown-linux-gnu.test-dependencies]
    devDep1 = { path = "./devDep1" }
  [target.x86_64-unknown-linux-gnu.bin-dependencies]
    path-option = ["./test/pro1"]
  [target.x86_64-unknown-linux-gnu.bin-dependencies.package-option]
    "pro1.xoo" = "./test/pro1/pro1.xoo.cjo"

[target.x86_64-unknown-linux-gnu.debug]
  compile-option = "compile-2"
  override-compile-option = "override-compile-2"
  link-option = "link-2"
  [target.x86_64-unknown-linux-gnu.debug.dependencies]
    dep2 = { path = "./dep2" }
  [target.x86_64-unknown-linux-gnu.debug.test-dependencies]
    devDep2 = { path = "./devDep2" }
  [target.x86_64-unknown-linux-gnu.debug.bin-dependencies]
    path-option = ["./test/pro2"]
  [target.x86_64-unknown-linux-gnu.debug.bin-dependencies.package-option]
    "pro2.xoo" = "./test/pro2/pro2.xoo.cjo"
```

`target` 配置项在与 `cjpm.toml` 公共配置项或者相同 `target` 的其他级别的配置项共存时，按照如下的优先级合并：

1. `debug/release` 模式下对应 `target` 的配置
2. `debug/release` 无关的对应 `target` 的配置
3. 公共配置项

以上述的 `target` 配置为例，`target` 各个配置项按照以下规则合并：

- `compile-option`：将所有适用的同名配置项按照优先级拼接，优先级更高的配置拼接在后方。在本例中，在 `x86_64-unknown-linux-gnu` 的 `debug` 编译模式下，最终生效的 `compile-option` 值为 `compile-0 compile-1 compile-2`，在 `release` 编译模式下为 `compile-0 compile-1`，在其他 `target` 中为 `compile-0`。
- `override-compile-option`：同上。由于 `override-compile-option` 优先级高于 `compile-option`，在最后的编译命令中，拼接完成的 `override-compile-option` 会整体置于拼接完成的 `compile-option` 之后。
- `link-option`：同上。
- `dependencies`：源码依赖将被直接合并，如果其中存在依赖冲突则会报错。在本例中，在 `x86_64-unknown-linux-gnu` 的 `debug` 编译模式下，最终生效的 `dependencies` 为 `dep0`, `dep1` 和 `dep2`，而在 `release` 编译模式下仅有 `dep0` 和 `dep1` 生效。在其他 `target` 中，仅有 `dep0` 生效。
- `test-dependencies`：同上。
- `bin-dependencies`：二进制依赖将按照优先级合并，如果有冲突则仅有优先级更高的依赖将会被加入，同优先级的配置先加入 `package-option` 配置。在本例中，在 `x86_64-unknown-linux-gnu` 的 `debug` 编译模式下，`./test/pro1` 和 `./test/pro2` 内的二进制依赖将被加入，而在 `release` 模式下仅会加入 `./test/pro1`。由于 `bin-dependencies` 没有公共配置，因此在其他 `target` 中不会有二进制依赖生效。

在本例的交叉编译场景中，若在其他平台中指定了 `x86_64-unknown-linux-gnu` 作为目标 `target`，则 `target.x86_64-unknown-linux-gnu` 的配置也会按照上述规则与公共配置项合并并应用；如果处于 `debug` 编译模式，也将应用 `target.x86_64-unknown-linux-gnu.debug` 的配置项。