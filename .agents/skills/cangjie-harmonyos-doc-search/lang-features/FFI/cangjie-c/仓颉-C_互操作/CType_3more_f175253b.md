## CType

除类型映射一节提供的与 C 侧类型进行映射的类型外，仓颉还提供了一个 `CType` 接口，接口本身不包含任何方法，它可以作为所有 C 互操作支持的类型的父类型，便于在泛型约束中使用。

需要注意的是：

1. `CType` 接口是仓颉中的一个接口类型，它本身不满足 `CType` 约束；
2. `CType` 接口不允许被继承、扩展；
3. `CType` 接口不会突破子类型的使用限制。

`CType` 的使用示例如下：

<!-- verify -->

```cangjie
func foo<T>(x: T): Unit where T <: CType {
    match (x) {
        case i32: Int32 => println(i32)
        case ptr: CPointer<Int8> => println(ptr.isNull())
        case f: CFunc<() -> Unit> => unsafe { f() }
        case _ => println("match failed")
    }
}

main() {
    var i32: Int32 = 1
    var ptr = CPointer<Int8>()
    var f: CFunc<() -> Unit> = { => println("Hello") }
    var f64 = 1.0
    foo(i32)
    foo(ptr)
    foo(f)
    foo(f64)
}
```

执行结果如下：

```text
1
true
Hello
match failed
```

## C 调用仓颉的函数

仓颉提供 `CFunc` 类型来对应 C 侧的函数指针类型。C 侧的函数指针可以传递到仓颉，仓颉也可以构造出对应 C 的函数指针的变量传递到 C 侧。

假设一个 C 的库 API 如下：

```c
typedef void (*callback)(int);
void set_callback(callback cb);
```

对应的，在仓颉里面这个函数可以声明为：

```cangjie
foreign func set_callback(cb: CFunc<(Int32) -> Unit>): Unit
```

CFunc 类型的变量可以从 C 侧传递过来，也可以在仓颉侧构造出来。在仓颉侧构造 CFunc 类型有两种办法，一个是用 `@C` 修饰的函数，另外一个是标记为 CFunc 类型的闭包。

`@C` 修饰的函数，表明它的函数签名是满足 C 的调用规则的，定义还是写在仓颉这边。`foreign` 修饰的函数定义是在 C 侧的。

> **注意：**
>
> `foreign` 修饰的函数与 `@C` 修饰的函数，这两种 `CFunc` 的命名不建议使用 `CJ_`（不区分大小写）作为前缀，否则可能与标准库及运行时等编译器内部符号出现冲突，导致未定义行为。

示例如下：

```cangjie
@C
func myCallback(s: Int32): Unit {
    println("handle ${s} in callback")
}

main() {
    // the argument is a function qualified by `@C`
    unsafe { set_callback(myCallback) }

    // the argument is a lambda with `CFunc` type
    let f: CFunc<(Int32) -> Unit> = { i => println("handle ${i} in callback") }
    unsafe { set_callback(f) }
}
```

假设 C 函数编译出来的库是 "libmyfunc.so"，那么需要使用 `cjc -L. -lmyfunc test.cj -o test.out` 编译命令，使仓颉编译器去链接这个库。最终就能生成想要的可执行程序。

另外，在编译 C 代码时，请打开 `-fstack-protector-all/-fstack-protector-strong` 栈保护选项，仓颉侧代码默认拥有溢出检查与栈保护功能。在引入 C 代码后，需要同步保证 unsafe 块中的溢出的安全性。

## 编译选项

使用 C 互操作通常需要手动链接 C 的库，仓颉编译器提供了相应的编译选项。

- `--library-path <value>`, `-L <value>`, `-L<value>`：指定要链接的库文件所在的目录。

  `--library-path <value>` 指定的路径会被加入链接器的库文件搜索路径。另外环境变量 `LIBRARY_PATH` 中指定的路径也会被加入链接器的库文件搜索路径中，通过 `--library-path` 指定的路径会比 `LIBRARY_PATH` 中的路径拥有更高的优先级。

- `--library <value>`, `-l <value>`, `-l<value>`：指定要链接的库文件。

  给定的库文件会被直接传给链接器，库文件名的格式应为 `lib[arg].[extension]`。

关于仓颉编译器支持的所有编译选项，详情请参见 "附录 > cjc 编译选项"。