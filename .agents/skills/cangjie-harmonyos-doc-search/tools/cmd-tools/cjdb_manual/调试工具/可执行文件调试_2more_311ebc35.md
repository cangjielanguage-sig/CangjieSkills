## 可执行文件调试

### launch 方式

launch 方式有两种加载方式，如下：

1. 启动调试器的同时加载被调程序。

    ```text
    ~/0901/cangjie_test$ cjdb test
    (cjdb) target create "test"
    Current executable set to '/0901/cangjie-linux-x86_64-release/bin/test' (x86_64).
    (cjdb)
    ```

2. 先启动调试器，然后通过 `file` 命令加载被调程序。

    ```text
    ~/0901/cangjie_test$ cjdb
    (cjdb) file test
    Current executable set to '/0901/cangjie/test' (x86_64).
    (cjdb)
    ```

### attach 方式

使用 attach 方式调试目标程序。

针对正在运行的程序，支持 attach 方式进行调试，如下：

```text
~/0901/cangjie-linux-x86_64-release/bin$ cjdb
(cjdb) attach 15325
Process 15325 stopped
* thread #1, name = 'test', stop reason = signal SIGSTOP
    frame #0: 0x00000000004014cd test`default.main() at test.cj:7:9
   4      var a : Int32 = 12
   5      a = a + 23
   6      while (true) {
-> 7        a = 1
   8      }
   9      a = test(10, 34)
   10     return 1
  thread #2, name = 'FinalProcessor', stop reason = signal SIGSTOP
    frame #0: 0x00007f48c12fc065 libpthread.so.0`__pthread_cond_timedwait at futex-internal.h:205
  thread #3, name = 'PoolGC_1', stop reason = signal SIGSTOP
    frame #0: 0x00007f48c12fbad3 libpthread.so.0`__pthread_cond_wait at futex-internal.h:88
  thread #4, name = 'MainGC', stop reason = signal SIGSTOP
    frame #0: 0x00007f48c12fc065 libpthread.so.0`__pthread_cond_timedwait at futex-internal.h:205
  thread #5, name = 'schmon', stop reason = signal SIGSTOP
    frame #0: 0x00007f48c0fe17a0 libc.so.6`__GI___nanosleep(requested_time=0x00007f48a8ffcb70, remaining=0x0000000000000000) at nanosleep.c:28

Executable module set to "/0901/cangjie-linux-x86_64-release/bin/test".
Architecture set to: x86_64-unknown-linux-gnu.
```

## 注意事项

1. 进行调试的程序必须是已经经过编译的 `debug` 版本，如使用下述命令编译的程序文件：

    ```shell
    cjc -g test.cj -o test
    ```

2. 开发者定义了一个泛型对象后，调试单步进入该对象的 `init` 函数时，栈信息显示的函数名称会包含两个包名，一个是实例化该泛型对象所在的包名，另外一个是泛型定义所在的包名。

    ```text
    * thread #1, name = 'main', stop reason = step in
        frame #0: 0x0000000000404057 main`default.p1.Pair<String, Int64>.init(a="hello", b=0) at a.cj:21:9
       18       let x: T
       19       let y: U
       20       public init(a: T, b: U) {
    -> 21           x = a
       22           y = b
       23       }
    ```

3. 对于 `Enum` 类型的显示，当 `Enum` 构造器有参数时，会显示成如下样式：

    ```cangjie
    enum E {
        Ctor(Int64, String) | Ctor
    }

    main() {
        var temp = E.Ctor(10, "String")
        0
    }

    ========================================
    (cjdb) p temp
    (E) $0 = Ctor {
      arg_1 = 10
      arg_2 = "String"
    }
    ```

    其中 `arg_x` 并非是一个可打印的成员变量，`Enum` 内实际并没有命名为 `arg_x` 的成员变量。

4. 仓颉 `cjdb` 基于 `lldb` 构建，所以支持 `lldb` 原生基础功能，详情见 [lldb 官方文档](https://lldb.llvm.org)。

5. 如果开发者在高于该版本的系统环境上运行，可能会遇到不兼容的问题和风险，如 `C` 语言互操作场景，cjdb 无法正常解析 `C` 代码的文件和行号信息。

    ```c
    int32_t cfoo()
    {
        printf("cfoo\n");
        return 0;
    }
    ```

    ```cangjie
    foreign func cfoo(): Int32
    unsafe main() {
        cfoo()
    }
    ```

    ```shell
    # step 1: 使用系统自带 clang 版本编译 c 文件，生成 dylib
    clang -g -shared cffi.c -o libcffi.dylib
    # step 2: 使用 cjc 版本编译 cj 文件并连接 c 语言动态库
    cjc -g test.cj -L. -lcffi -o test
    # step 3: 使用 cjdb 调试 test 文件，由于调试信息不兼容导致无法调试 c 代码
    cjdb test
    ```

    ```text
    (cjdb) target create "test"
    Current executable set to 'test' (x86_64).
    (cjdb) b cfoo
    Breakpoint 1: where = libcffi.dylib`cfoo + 4, address = 0x0000000000000f84
    (cjdb) r
    Process 3133 launched: 'test' (x86_64)
    Process 3133 stopped
    * thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
        frame #0: 0x00000001000a6f84 libcffi.dylib`cfoo
      1    foreign func cfoo(): Int32
      2    unsafe main() {
      3        cfoo()
    -> 4    }
    ```