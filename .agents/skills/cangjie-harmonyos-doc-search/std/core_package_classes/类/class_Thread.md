## class Thread

```cangjie
public class Thread {}
```

功能：获取线程 ID 及名字、查询线程是否存在取消请求、注册线程未处理异常的处理函数等。

该类型实例无法通过构造得到，仅能通过 [Future](core_package_classes.md#class-futuret) 对象的 `thread` 属性或是 [Thread](core_package_classes.md#class-thread) 类的 `currentThread` 静态属性获取。

### static prop currentThread

```cangjie
public static prop currentThread: Thread
```

功能：获取当前执行线程的 [Thread](core_package_classes.md#class-thread) 对象。

类型：[Thread](core_package_classes.md#class-thread)

### prop hasPendingCancellation

```cangjie
public prop hasPendingCancellation: Bool
```

功能：线程是否存在取消请求，即是否通过 future.cancel() 发送过取消请求，常见使用方为 [Thread](core_package_classes.md#class-thread).currentThread.hasPendingCancellation。

类型：[Bool](core_package_intrinsics.md#bool)

### prop id

```cangjie
public prop id: Int64
```

功能：获取当前执行线程的标识，以 [Int64](core_package_intrinsics.md#int64) 表示，所有存活的线程都有不同标识，但不保证当线程执行结束后复用它的标识。

类型：[Int64](core_package_intrinsics.md#int64)

### prop name

```cangjie
public mut prop name: String
```

功能：获取或设置线程的名称，获取设置都具有原子性。

类型：[String](core_package_structs.md#struct-string)

### static func handleUncaughtExceptionBy((Thread, Exception) -> Unit)

```cangjie
public static func handleUncaughtExceptionBy(exHandler: (Thread, Exception) -> Unit): Unit
```

功能：注册线程未处理异常的处理函数。

当某一线程因异常而提前终止后，如果全局的未处理异常函数被注册，那么将调用该函数并结束线程，在该函数内抛出异常时，将向终端打印提示信息并结束线程，但不会打印异常调用栈信息；如果没有注册全局异常处理函数，那么默认会向终端打印异常调用栈信息。

多次注册处理函数时，后续的注册函数将覆盖之前的处理函数。

当有多个线程同时因异常而终止时，处理函数将被并发执行，因而开发者需要在处理函数中确保并发正确性。

处理函数的参数第一个参数类型为 [Thread](core_package_classes.md#class-thread)，是发生异常的线程，第二个参数类型为 [Exception](core_package_exceptions.md#class-exception)，是线程未处理的异常。

参数：

- exHandler: ([Thread](core_package_classes.md#class-thread), [Exception](core_package_exceptions.md#class-exception)) -> [Unit](core_package_intrinsics.md#unit) - 注册的处理函数。