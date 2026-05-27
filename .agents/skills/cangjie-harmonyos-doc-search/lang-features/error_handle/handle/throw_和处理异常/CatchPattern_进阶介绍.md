## CatchPattern 进阶介绍

大多数时候，只想捕获某一类型和其子类型的异常，这时候使用 CatchPattern 的**类型模式**来处理；但有时也需要所有异常做统一处理（如此处不该出现异常，出现了就统一报错），这时可以使用 CatchPattern 的**通配符模式**来处理。

类型模式在语法上有两种格式：

- `Identifier: ExceptionClass`。此格式可以捕获类型为 `ExceptionClass` 及其子类的异常，并将捕获到的异常实例转换成 `ExceptionClass`，然后与 `Identifier` 定义的变量进行绑定，接着就可以在 catch 块中通过 Identifier 定义的变量访问捕获到的异常实例。
- `Identifier: ExceptionClass_1 | ExceptionClass_2 | ... | ExceptionClass_n`。此格式可以通过连接符 `|` 将多个异常类进行拼接，连接符 `|` 表示“或”的关系：可以捕获类型为 `ExceptionClass_1` 及其子类的异常，或者捕获类型为 `ExceptionClass_2` 及其子类的异常，依次类推，或捕获类型为 `ExceptionClass_n` 及其子类的异常（假设 n 大于 1）。当待捕获异常的类型属于上述“或”关系中的任一类型或其子类型时，此异常将被捕获。但是由于无法静态地确定被捕获异常的类型，所以被捕获异常的类型会被转换成由 `|` 连接的所有类型的最小公共父类，并将异常实例与 `Identifier` 定义的变量进行绑定。因此在此类模式下，catch 块内只能通过 `Identifier` 定义的变量访问 `ExceptionClass_i（1 <= i <= n）` 的最小公共父类中的成员变量和成员函数。当然，也可以使用通配符代替类型模式中的 `Identifier`，差别仅在于通配符不会进行绑定操作。

示例如下：

<!-- verify -->

```cangjie
main(): Int64 {
    try {
        throw IllegalArgumentException("This is an Exception!")
    } catch (e: OverflowException) {
        println(e.message)
        println("OverflowException is caught!")
    } catch (e: IllegalArgumentException | NegativeArraySizeException) {
        println(e.message)
        println("IllegalArgumentException or NegativeArraySizeException is caught!")
    } finally {
        println("finally is executed!")
    }
    return 0
}
```

执行结果：

```text
This is an Exception!
IllegalArgumentException or NegativeArraySizeException is caught!
finally is executed!
```

关于“被捕获异常的类型是由 `|` 连接的所有类型的最小公共父类”的示例：

<!-- verify -->

```cangjie
open class Father <: Exception {
    var father: Int32 = 0
}

class ChildOne <: Father {
    var childOne: Int32 = 1
}

class ChildTwo <: Father {
    var childTwo: Int32 = 2
}

main() {
    try {
        throw ChildOne()
    } catch (e: ChildTwo | ChildOne) {
        println("${e is Father}")
    }
}
```

执行结果：

```text
true
```

**通配符模式**的语法是 `_`，它可以捕获同级 try 块内抛出的任意类型的异常，等价于类型模式中的 `e: Exception`，即捕获 Exception 子类所定义的异常。示例如下：

<!-- compile -->

```cangjie
// Catch with wildcardPattern.
try {
    throw OverflowException()
} catch (_) {
    println("catch an exception!")
}
```