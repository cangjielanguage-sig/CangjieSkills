## unsafe

在引入与 C 语言的互操作过程中，同时也引入了 C 的许多不安全因素，因此在仓颉中使用 `unsafe` 关键字，用于对跨 C 调用的不安全行为进行标识。

关于 unsafe 关键字，有以下几点说明：

- `unsafe` 可以修饰函数、表达式，也可以修饰一段作用域。
- 被 `@C` 修饰的函数，被调用处需要在 `unsafe` 上下文中。
- 在调用 `CFunc` 时，使用处需要在 `unsafe` 上下文中。
- `foreign` 函数在仓颉中进行调用，被调用处需要在 `unsafe` 上下文中。
- 当被调用函数被 `unsafe` 修饰时，被调用处需要在 `unsafe` 上下文中。

使用方式如下：

<!-- run -->

```cangjie
foreign func rand(): Int32

@C
func foo(): Unit {
    println("foo")
}

var foo1: CFunc<() -> Unit> = { =>
    println("foo1")
}

main(): Int64 {
    unsafe {
        rand()           // Call foreign func.
        foo()            // Call @C func.
        foo1()           // Call CFunc var.
    }
    0
}
```

需要注意的是，普通 `lambda` 无法传递 `unsafe` 属性，当 `unsafe` 的 `lambda` 逃逸后，可以不在 `unsafe` 上下文中直接调用而未产生任何编译错误。当需要在 `lambda` 中调用 `unsafe` 函数时，建议在 `unsafe` 块中进行调用，参考如下用例：

<!-- run -->

```cangjie
unsafe func A(){}
unsafe func B(){
    var f = { =>
        unsafe { A() } // Avoid calling A() directly without unsafe in a normal lambda.
    }
    return f
}
main() {
    var f = unsafe{ B() }
    f()
    println("Hello World")
}
```

## 调用约定

函数调用约定描述调用者和被调用者双方如何进行函数调用（如参数如何传递、栈由谁清理等），函数调用和被调用双方必须使用相同的调用约定才能正常运行。仓颉编程语言通过 `@CallingConv` 来表示各种调用约定，支持的调用约定如下：

- **CDECL**：`CDECL` 表示 clang 的 C 编译器在不同平台上默认使用的调用约定。
- **STDCALL**：`STDCALL` 表示 Win32 API 使用的调用约定。

通过 C 语言互操作机制调用的 C 函数，未指定调用约定时将采用默认的 `CDECL` 调用约定。如下调用 C 标准库函数 `rand` 示例：

<!-- run -->

```cangjie
@CallingConv[CDECL]   // Can be omitted in default.
foreign func rand(): Int32

main() {
    println(unsafe { rand() })
}
```

`@CallingConv` 只能用于修饰 `foreign` 块、单个 `foreign` 函数和顶层作用域中的 `CFunc` 函数。当 `@CallingConv` 修饰 `foreign` 块时，会为 `foreign` 块中的每个函数分别加上相同的 `@CallingConv` 修饰。

## 使用说明

- 操作系统线程局部变量使用约束

  仓颉和 C 语言互操作时，使用操作系统线程的局部变量存在风险，说明如下：

  1. 线程局部变量包括 C 语言提供的 `thread_local` 定义的变量和使用 `pthread_key_create` 创建的变量。
  2. 仓颉具备仓颉线程调度能力，支持仓颉线程的切换和恢复，仓颉线程被调度到哪个操作系统线程是随机的，从而在仓颉线程上调用其他语言的线程局部变量是有风险的。

  如下示例中，仓颉调用 C 语言的线程局部变量存在风险：

  ```c
  // C language logic using thread_local
  static thread_local int64_t count = 0;
  int64_t getCount() {
      count++;
      return count;
  }
  ```

  ```cangjie
  foreign func getCount(): Int64
  // Cangjie invokes the preceding C language logic
  spawn {
      let r1 = unsafe { getCount() }  // r1 equals 1
      sleep(Duration.second * 10)
      let r2 = unsafe { getCount() }  // r2 may not be equal to 2
  }
  ```

- 线程绑定使用约束

  仓颉调用 C 语言执行互操作逻辑时，仓颉线程调度到哪个操作系统线程是随机的，线程优先级和线程亲和性等与线程绑定的行为不建议使用。

- 同步原语使用说明

  仓颉调用 C 语言执行互操作逻辑时，当前这个仓颉线程会等待互操作逻辑执行结束，不建议在其他语言中出现可能导致长时间等待的阻塞性行为。

- 对进程 fork 场景的支持说明

  仓颉调用 C 语言执行互操作逻辑时，如果在 C 语言中以 `fork()` 方式创建子进程，子进程中不支持执行仓颉逻辑。同一进程中其他操作系统线程不受影响。

- 进程退出时的说明

  仓颉调用 C 语言执行互操作逻辑时，如果在 C 语言中退出进程，进程内共享的资源已经释放，可能导致非法访问等错误。