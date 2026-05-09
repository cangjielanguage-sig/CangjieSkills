# 内置编译标记

仓颉语言提供了一些预定义的编译标记，可以通过这些编译标记控制仓颉编译器的编译行为。

## 源码位置

仓颉提供了几个内置编译标记，用于在编译时获取源码的位置。

- `@sourcePackage()` 展开后是一个 `String` 类型的字面量，内容为该标记所在的源码的包名。
- `@sourceFile()` 展开后是一个 `String` 类型的字面量，内容为该标记所在的源码的文件名。
- `@sourceLine()` 展开后是一个 `Int64` 类型的字面量，内容为该标记所在的源码的代码行。

这几个编译标记可以在任意表达式内部使用，只要能符合类型检查规则即可。示例如下：

<!-- run -->

```cangjie
func test1() {
    let s: String = @sourceFile()  // The value of `s` is the current source file name
}

func test2(n!: Int64 = @sourceLine()) { /* at line 5 */
    // The default value of `n` is the source file line number of the definition of `test2`
    println(n) // print 5
}
```

## 条件编译

条件编译使用 `@When` 标记，是一种在程序代码中根据特定条件选择性地编译不同代码段的技术。条件编译的作用主要体现在以下几个方面：

- 平台适应：支持根据当前的编译环境选择性地编译代码，用于实现跨平台的兼容性。
- 功能选择：支持根据不同的需求选择性地编译代码，用于实现功能的灵活配置。
- 调试支持：支持调试模式下编译相关代码，用于提高程序的性能和安全性。例如，在调试模式下编译调试信息或记录日志相关的代码，而在发布版本中将其排除。
- 性能优化：支持根据预定义的条件选择性地编译代码，用于提高程序的性能。

关于条件编译的具体内容，请参见[条件编译](../compile_and_build/conditional_compilation.md)章节，这里不再额外展开。

## @FastNative

为了提升与 `C` 语言互操作的性能，仓颉提供 `@FastNative` 标记用于优化对 `C` 函数的调用。值得注意的是 `@FastNative` 只能用于 `foreign` 声明的函数。

首先编译以下 C 语言程序得到动态库文件 `libcProg.so`，示例如下：

```c
#include <stdio.h>

char* foo()
{
    static char str[] = "this is an example";
    return str;
}
```

仓颉文件 `main.cj`：

<!-- code_no_check -->

```cangjie
@FastNative
foreign func foo(): CPointer<Int32>

@FastNative
foreign func printf(fmt: CPointer<Int32>, ...): Int32

main(): Int32 {
    unsafe{
        let str = foo()
        printf(str)
    }
}
```

具体的编译介绍，详情请参见[附录](../Appendix/compile_options.md)。下面为该用例对应的编译命令：

```shell
cjc -L . -lcProg ./main.cj
```

执行上述命令编译 `main.cj` 之后生成一个可执行文件 `main`，其执行结果如下：

```text
this is an example
```

开发者在使用 `@FastNative` 修饰 `foreign` 函数时，应确保对应的 `C` 函数满足以下两点要求：

1. 函数的整体执行时间不宜太长。例如：不允许函数内部存在很大的循环；不允许函数内部产生阻塞行为，例如：调用 `sleep`、`wait` 等函数。
2. 函数内部不能调用仓颉方法。

## @Frozen

`@Frozen` 标记可用于修饰函数和属性。如果确定某个函数、属性在将来的版本更新中不会去修改它的内部实现，那么可以使用 `@Frozen` 对其进行标记，该标记代表开发者对该函数/属性在未来版本演进的一种承诺。被 `@Frozen` 修饰的函数和属性，在后续的升级版本中，签名和函数体都不能发生任何变化。这意味着，前后两个代码版本，在相同编译器、相同编译选项的情况下，该函数或属性的生成产物完全一致。

`@Frozen` 标记可被用于修饰：

- 全局函数
- 类、结构、接口、扩展、枚举中的函数
- 类、接口、扩展中的属性

`@Frozen` 标记不可被用于修饰：

- 除了函数和属性以外的其他类型声明
- 嵌套函数
- 表达式

使用示例如下：

<!-- run -->

```cangjie
@Frozen
public func test(): Unit {}

public class testClass {
    @Frozen
    public func testFunc(): Unit {}

    @Frozen
    public prop testProp: Unit {
        get() {}
    }
}
```