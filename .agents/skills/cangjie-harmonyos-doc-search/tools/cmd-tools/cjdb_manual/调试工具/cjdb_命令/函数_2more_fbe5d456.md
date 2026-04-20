### 函数

#### 是否进入带调试信息的函数

可以使用`thread step-over <cmd-options> [<thread-id>]`（`thread step-over` 可简写为 `next` 或`n`）跳过当前函数调用，直接执行函数调用后的下一行代码。

```text
(cjdb) n
Process 2884 stopped
* thread #1, name = 'test', stop reason = step over
    frame #0: 0x0000000000401498 test`default.main() at test.cj:5:7
   2    main(): Int64 {
   3
   4       var a : Int32 = 12
-> 5       a = a + 23
   6       a = test(10, 34)
   7       return 1
   8    }
(cjdb)
```

使用 `cjdb` 调试遇到函数时，用`thread step-in <cmd-options> [<thread-id>]`（`thread step-in`可简写为`step`或`s`）命令可以进入函数（函数必须有调试信息）。

```text
(cjdb) n
Process 5240 stopped
* thread #1, name = 'test', stop reason = step over
    frame #0: 0x00000000004014d8 test`default.main() at test.cj:6:7
   3
   4      var a : Int32 = 12
   5      a = a + 23
-> 6      a = test(10, 34)
   7      return 1
   8    }
   9
(cjdb) s
Process 5240 stopped
* thread #1, name = 'test', stop reason = step in
    frame #0: 0x0000000000401547 test`default.test(a=10, b=34) at test.cj:12:10
   9
   10   func test(a : Int32, b : Int32) : Int32 {
   11
-> 12     return a + b
   13   }
   14
(cjdb)
```

#### 退出正在调试的函数

执行 `finish` 命令，退出当前函数，返回到上一个调用栈函数。

```text
(cjdb) s
Process 5240 stopped
* thread #1, name = 'test', stop reason = step in
    frame #0: 0x0000000000401547 test`default.test(a=10, b=34) at test.cj:12:10
   9
   10   func test(a : Int32, b : Int32) : Int32 {
   11
-> 12     return a + b
   13   }
   14
(cjdb) finish
Process 5240 stopped
* thread #1, name = 'test', stop reason = step out

Return value: (int) $0 = 44

    frame #0: 0x00000000004014dd test`default.main() at test.cj:6:7
   3
   4      var a : Int32 = 12
   5      a = a + 23
-> 6      a = test(10, 34)
   7      return 1
   8    }
   9
(cjdb)
```

### 断点

#### 设置源码断点

```text
breakpoint set --file test.cj --line line_number
```

`--line` 指定行号。

`--file` 指定文件。

当调试单个文件时，只需要输入行号即可；当调试涉及多个文件时，需要同时指定文件名和行号。

`b test.cj:4` 是 `breakpoint set --file test.cj --line 4` 的缩写。

例：**breakpoint set --line 2**

```text
(cjdb) b 2
Breakpoint 1: where = test`default.main() + 13 at test.cj:4:3, address = 0x0000000000401491
(cjdb) b test.cj : 4
Breakpoint 2: where = test`default.main() + 13 at test.cj:4:3, address = 0x0000000000401491
(cjdb)
```

#### 设置函数断点

```text
breakpoint set --name function_name
```

`--name` 指定要设置函数断点的函数名。

`b test` 是 `breakpoint set --name test` 的缩写。

例：**breakpoint set --name test**

```text
(cjdb) b test
Breakpoint 3: where = test`default.test(int, int) + 19 at test.cj:12:10, address = 0x0000000000401547
(cjdb)
```

#### 设置条件断点

```text
breakpoint set --file xx.cj --line line_number --condition expression
```

`--file` 指定文件。

`--line` 指定行号。

`--condition` 指定条件。

例：**breakpoint set --file test.cj --line 4 --condition a==12**

```text
(cjdb) breakpoint set --file test.cj --line 4 --condition a==12
Breakpoint 2: where = main`default::main() + 60 at test.cj:4:9, address = 0x00005555555b62d0
(cjdb) c
Process 3128551 resuming
Process 3128551 stopped
* thread #1, name = 'schmon', stop reason = breakpoint 2.1
    frame #0: 0x00005555555b62d0 main`default::main() at test.cj:4:9
   1    main(): Int64 {
   2
   3        var a : Int32 = 12
-> 4        a = a + 23
   5        return 1
   6    }
```

#### 执行到下一个断点停止

```text
(cjdb) c
Process 2884 resuming
Process 2884 stopped
* thread #1, name = 'test', stop reason = breakpoint 3.1
    frame #0: 0x0000000000401547 test`default.test(a=10, b=34) at test.cj:12:10
   9
   10   func test(a : Int32, b : Int32) : Int32 {
   11
-> 12     return a + b
   13   }
   14
(cjdb)
```