# I/O 节点流

节点流是指直接提供数据源的流，节点流的构造方式通常是依赖某种直接的外部资源（如文件、网络等）。

仓颉编程语言中常见的节点流包含标准流（ConsoleReader、ConsoleWriter）、文件流（File）、网络流（Socket）等。

本章介绍标准流和文件流。

## 标准流

标准流包含标准输入流、标准输出流和标准错误输出流。

标准流是程序与外部数据交互的标准接口。程序运行的时候从输入流读取数据，作为程序的输入，程序运行过程中输出的信息被传送到输出流，类似的，错误信息被传送到错误流。

在仓颉编程语言中可以使用 `getStdIn`、`getStdOut`、`getStdErr` 全局函数来分别获取这三个标准流。

使用上面的函数需要导入 `env` 包：

导入 env 包示例：

<!-- run -->

```cangjie
import std.env.*
```

`env` 包内的 `ConsoleReader` 和 `ConsoleWriter` 类型对这三个标准流都进行了易用性封装（标准错误输出流也是输出流，所以一共是两个类型），提供了更方便的基于 `String` 的扩展操作，并且对于很多常见类型都提供了丰富的重载来优化性能。

其中最重要的是 `ConsoleReader` 和 `ConsoleWriter` 类型提供了并发安全的保证，可以在任意线程中安全地通过该类型提供的接口来读写内容。

默认情况下标准输入流来源于键盘输入的信息，例如在命令行界面中输入的文本。

当需要从标准输入流中获取数据时，可以通过 `getStdIn` 全局函数获取 `ConsoleReader` 类型，再通过该类型的 `readln` 函数获取命令行的输入。

标准输入流读取示例：

<!-- run -->

```cangjie
import std.env.getStdIn

main() {
    let consoleReader = getStdIn()
    let txt = consoleReader.readln()
    println(txt ?? "")
}
```

运行上面的代码，在命令行上输入一些文字，然后换行结束，即可看到输入的内容。

输出流分为标准输出流和标准错误流，默认情况下，它们都会输出到屏幕，例如在命令行界面中看到的文本。

当需要往标准输出流中写入数据时，可以通过 `getStdOut`/`getStdErr` 全局函数获取 `ConsoleWriter` 来写入，例如通过 `write` 函数来向控制台打印内容。

使用 `ConsoleWriter` 和直接使用 `print` 函数的差别是，`ConsoleWriter` 是并发安全的，并且由于 `ConsoleWriter` 使用了缓存技术，在输入内容较多时拥有更好的性能表现。

需要注意的是，写完数据后需要对 `ConsoleWriter` 调用 `flush` 才能保证内容被完整写到标准流中。

标准输出流写入示例：

<!-- run -->

```cangjie
import std.env.getStdOut

main() {
    let consoleWriter = getStdOut()
    for (_ in 0..1000) {
        consoleWriter.writeln("hello, world!")
    }
    consoleWriter.flush()
}
```