# throw 和处理异常

上文介绍了如何自定义异常，接下来学习如何抛出和处理异常。

- 由于异常是 `class` 类型，只需要按 class 对象的构建方式去创建异常即可。如表达式 `FatherException()` 即创建了一个类型为 `FatherException` 的异常。
- 仓颉语言提供 `throw` 关键字，用于抛出异常。用 `throw` 来抛出异常时，`throw` 之后的表达式必须是 `Exception` 的子类型（同为异常的 `Error` 不可以手动 `throw` ），如 `throw ArithmeticException("I am an Exception!")` （被执行到时）会抛出一个算术运算异常。
- `throw` 关键字抛出的异常需要被捕获处理。若异常没有被捕获，则由系统调用默认的异常处理函数。

  > **注意：**
  >
  > 开发者可以调用如下 `Thread` 类的静态函数，对未捕获的 `Exception` 注册自定义的异常处理函数：
  >
  > - `public static func handleUncaughtExceptionBy(exHandler: (Thread, Exception) -> Unit): Unit`

异常处理由 `try` 表达式完成，可分为：

- 不涉及资源自动管理的普通 try 表达式。
- 会进行资源自动管理 try-with-resources 表达式。