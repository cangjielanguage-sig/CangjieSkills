## 普通 try 表达式

普通 try 表达式包括三个部分：try 块，catch 块和 finally 块。

- try 块，以关键字 `try` 开始，后面紧跟一个由表达式与声明组成的块（用一对花括号括起来，定义了新的局部作用域，可以包含任意表达式和声明，后简称“块”），try 后面的块内可以抛出异常，并被紧随的 catch 块所捕获并处理（如果不存在 catch 块或未被捕获，则在执行完 finally 块后，该异常继续被抛出）。

- catch 块，一个普通 try 表达式可以包含零个或多个 catch 块（当没有 catch 块时必须有 finally 块）。每个 catch 块以关键字 `catch` 开头，后跟一条 `catchPattern` 和一个块，`catchPattern` 通过模式匹配的方式匹配待捕获的异常。一旦匹配成功，则交由其后跟随的块进行处理，并且忽略它后面的其他 catch 块。当某个 catch 块可捕获的异常类型均可被定义在它前面的某个 catch 块所捕获时，会在此 catch 块处报“catch 块不可达”的 warning。

- finally 块，以关键字 `finally` 开始，后面紧跟一个块。原则上，finally 块中主要实现一些“善后”的工作，如释放资源等，且要尽量避免在 finally 块中再抛异常。并且无论异常是否发生（即无论 try 块中是否抛出异常），finally 块内的内容都会被执行（若异常未被处理，执行完 finally 块后，继续向外抛出异常）。一个 try 表达式在包含 catch 块时可以不包含 finally 块，否则必须包含 finally 块。

`try` 后面紧跟的块以及每个 `catch` 块的作用域互相独立。

下面是一个只有 try 块和 catch 块的简单示例：

<!-- verify -->

```cangjie
main() {
    try {
        throw NegativeArraySizeException("I am an Exception!")
    } catch (e: NegativeArraySizeException) {
        println(e)
        println("NegativeArraySizeException is caught!")
    }
    println("This will also be printed!")
}
```

执行结果为：

```text
NegativeArraySizeException: I am an Exception!
NegativeArraySizeException is caught!
This will also be printed!
```

`catchPattern` 中引入的变量作用域级别与 `catch` 后面的块中变量作用域级别相同，在 catch 块中再次引入相同名字会触发重定义错误。例如：

<!-- compile.error -->

```cangjie
main() {
    try {
        throw NegativeArraySizeException("I am an Exception!")
    } catch (e: NegativeArraySizeException) {
        println(e)
        let e = 0 // Error, redefinition
        println(e)
        println("NegativeArraySizeException is caught!")
    }
    println("This will also be printed!")
}
```

下面是带有 finally 块的 try 表达式的简单示例：

<!-- verify -->

```cangjie
main() {
    try {
        throw NegativeArraySizeException("NegativeArraySizeException")
    } catch (e: NegativeArraySizeException) {
        println("Exception info: ${e}.")
    } finally {
        println("The finally block is executed.")
    }
}
```

执行结果为：

```text
Exception info: NegativeArraySizeException: NegativeArraySizeException.
The finally block is executed.
```

try 表达式可以出现在任何允许使用表达式的地方。try 表达式的类型的确定方式，与 `if`、`match` 表达式等多分支语法结构的类型的确定方式相似，为 finally 分支除外的所有分支的类型的最小公共父类型。例如下面代码中的 try 表达式和变量 `x` 的类型均为 E 和 D 的最小公共父类型 D；finally 分支中的 `C()` 并不参与公共父类型的计算（若参与，则最小公共父类型会变为 `C`）。

另外，当 `try` 表达式的值没有被使用时，其类型为 `Unit`，不要求各分支的类型有最小公共父类型。

<!-- compile -->

```cangjie
open class C { }
open class D <: C { }
class E <: D { }
main () {
    let x = try {
        E()
    } catch (e: Exception) {
        D()
    } finally {
        C()
    }
    0
}
```