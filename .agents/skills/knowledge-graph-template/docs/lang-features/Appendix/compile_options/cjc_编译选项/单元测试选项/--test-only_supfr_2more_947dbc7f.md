### `--test-only` <sup>[frontend]</sup>

`--test-only` 选项用于单独编译包的测试部分。

如果启用此选项，编译器将仅编译包中的测试文件（以 `_test.cj` 结尾）。

> **注意：**
>
> 使用此选项时，应单独以常规模式编译相同的包，然后通过 `-L`/`-l` 链接选项添加依赖，或在使用 `LTO` 选项时添加依赖的 `.bc` 文件。否则，编译器将报缺少依赖的符号的错误。

示例:

```cangjie
/*main.cj*/
package my_pkg

func concatM(s1: String, s2: String): String {
    return s1 + s2
}

main() {
    println(concatM("a", "b"))
    0
}
```

```cangjie
/*main_test.cj*/
package my_pkg

@Test
class Tests {
    @TestCase
    public func case1(): Unit {
        @Expect("ac", concatM("a", "c"))
    }
}
```

使用编译器编译的命令如下：

```shell
# Compile the production part of the package first, only `main.cj` file would be compiled here
cjc -p my_pkg --output-type=static -o=output/libmain.a
# Compile the test part of the package, Only `main_test.cj` file would be compiled here
cjc -p my_pkg --test-only -L output -lmain
```

### `--mock <on|off|runtime-error>` <sup>[frontend]</sup>

如果传递了 `on` ，则该包将使能 mock 编译，该选项允许在测试用例中 mock 该包中的类。`off` 是一种显式禁用 mock 的方法。

> **注意：**
>
> 在测试模式下（当使能 `--test` ）自动启用对此包的 mock 支持，不需要显式传递 `--mock` 选项。

`runtime-error` 仅在测试模式下可用（当使能 `--test` 时），它允许编译带有 mock 代码的包，但不在编译器中做任何 mock 相关的处理（这些处理可能会造成一些开销并影响测试的运行时性能）。这对于带有 mock 代码用例进行基准测试时可能是有用的。使用此编译选项时，避免编译带有 mock 代码的用例并运行测试，否则将抛出运行时异常。