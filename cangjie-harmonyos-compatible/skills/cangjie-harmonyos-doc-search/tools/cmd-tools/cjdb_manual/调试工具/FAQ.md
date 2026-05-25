## FAQ

1. `docker` 环境下 cjdb 报 `error: process launch failed: 'A' packet returned an error: 8`。

    ```text
    root@xxx:/home/cj/cangjie-example#cjdb ./hello
    (cjdb) target create "./hello"
    Current executable set to '/home/cj/cangjie-example/hello' (x86_64).
    (cjdb) b main
    Breakpoint 1: 2 locations.
    (cjdb) r
    error: process launch failed: 'A' packet returned an error: 8
    (cjdb)
    ```

    问题原因：`docker` 创建容器时，未开启 SYS_PTRACE 权限。

    解决方案：创建新容器时加上如下选项，并且删除已存在的容器。

    ```shell
    docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --security-opt apparmor=unconfined
    ```

2. cjdb 报 `stop reason = signal XXX`。

    ```text
    Process 32491 stopped
    * thread #2, name = 'PoolGC_1', stop reason = signal SIGABRT
        frame #0: 0x00007ffff450bfb7 lib.so.6`__GI_raise(sig=2) at raise.c:51
    ```

    问题原因：程序持续产生 `SIGABRT` 信号触发调试器暂停。

    解决方案：可执行如下命令屏蔽此类信号。

    ```text
    (cjdb) process handle --pass true --stop false --notify true SIGBUS
    NAME         PASS   STOP   NOTIFY
    ===========  =====  =====  ======
    SIGBUS       true   false  true
    (cjdb)
    ```

3. cjdb 没有捕获 `SIGSEGV` 信号。

    问题原因：cjdb 在启动时会默认不捕获 `SIGSEGV` 信号。

    解决方案：开发者如果需要在调试时捕获此信号，可使用如下命令重新设置。

    ```text
    (cjdb)process handle -p true -s true -n true SIGSEGV
    NAME         PASS   STOP   NOTIFY
    ===========  =====  =====  ======
    SIGSEGV      true   true   true
    (cjdb)
    ```

4. cjdb 无法通过 `next/s` 等调试指令进入 `catch` 块。

    问题原因：仓颉使用 `LandingPad` 机制来实现异常处理，而该机制无法通过控制流明确 `try` 语句块中抛出的异常会由哪一个 `catch` 语句块捕获，所以无法明确执行的代码。类似问题在 `clang++` 中也存在。

    解决方案：开发者如果需要调试 `catch` 块中的代码，可以在 `catch` 中打上断点。

    ```text
    (cjdb) b 31
    Breakpoint 2: where = main`default::test(Int64) + 299 at a.cj:31:18, address = 0x000055555557caff
    (cjdb) n
    Process 1761640 stopped
    * thread #1, name = 'schmon', stop reason = breakpoint 2.1
        frame #0: 0x000055555557caff main`default::test(a=0) at a.cj:31:18
      28      s = 12/a
      29    } catch (e:Exception) {
      30
    ->31     error_result = e.toString()
      32     println(error_result)
      33    }
      34    s
    (cjdb)
    ```

5. `macOS` 平台表达式计算报错 `Expression can't be run, because there is no JIT compiled function`。

    问题原因：表达式暂不支持在 `macOS` 平台使用。

6. `macOS` 平台表达式计算 `aarch64` 架构有一部分环境调试时报 `Connection shut down by remote side while waiting for reply to initial handshake packet`。

    问题原因：部分系统会导致调试服务异常退出。

    解决方案：删除 `third_party/llvm/bin/debugserver` 文件，重新启动调试。

7. 在打断点调试时，如果该断点处有泛型变元，则泛型变元的名字为 T0, T1, ... Tn。举例如下：

    ```cangjie
    func global_func_02<K, G>() { 0 }
    public struct Pair<T, U> {
        let x: T
        let y: U
        public init(a: T, b: U) {
            x = a
            y = b
        }
    }
    main() {
        var a: Pair<String, Int64> = Pair<String, Int64>("hello", 0)
        global_func_02<Int64, String>()
        0
    }

    ========================================
    (cjdb) b 1
    Breakpoint 1: where = main`default::global_func_02<T0,T1>() + 9 at test.cj:1:33, address = 0x0000000000019989
    (cjdb) b 6
    Breakpoint 2: where = main`default::Pair<T0,T1>::init(T0, T1) + 150 at test.cj:6:9, address = 0x000000000001982a
    ```

  问题原因：仓颉为了满足泛型变元的 ABI 兼容，即开发者侧泛型变元改变，仓颉侧二进制符号表中的符号名不变。

  解决方案：将开发者编写的泛型变元的名称修改为 T0, T1, ... Tn。