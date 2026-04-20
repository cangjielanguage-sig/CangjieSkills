## if 表达式

`if` 表达式的基本形式为：

```text
if (条件) {
  分支 1
} else {
  分支 2
}
```

其中“条件”可以是一个布尔类型的表达式，或者一个 “let pattern” （语法糖），或者多个 “let pattern” 和布尔类型的表达式之间通过逻辑与或逻辑或直接连接形成的表达式，涉及 “let pattern” 的介绍和示例，参照[涉及 “let pattern” 的“条件”示例](#涉及-let-pattern-的条件示例)。

当表达式和模式匹配成功时，该模式匹配的值为 true，此时执行 `if` 分支对应的代码块；反之，为 false，执行 `else` 分支代码块，`else` 分支可以不存在。

“分支 1”和“分支 2”是两个代码块。`if` 表达式将按如下规则执行：

1. 计算“条件”表达式，如果值为 `true` 则转到第 2 步，值为 `false` 则转到第 3 步。
2. 执行“分支 1”，转到第 4 步。
3. 执行“分支 2”，转到第 4 步。
4. 继续执行 `if` 表达式后面的代码。

在一些场景中，可能只关注条件成立时该做些什么，所以 `else` 和对应的代码块是允许省略的。

如下程序演示了 `if` 表达式的基本用法：

<!-- run -->

```cangjie
import std.random.Random

main() {
    let number: Int8 = Random().nextInt8()
    println(number)
    if (number % 2 == 0) {
        println("偶数")
    } else {
        println("奇数")
    }
}
```

在这段程序中，使用仓颉标准库的 `random` 包生成了一个随机整数，然后使用 `if` 表达式判断这个整数是否能被 2 整除，并在不同的条件分支中打印“偶数”或“奇数”。

仓颉编程语言是强类型的，`if` 表达式的条件只能是布尔类型，不能使用整数或浮点数等类型，和 C 语言等不同，仓颉不以条件取值是否为 0 作为分支选择依据，例如以下程序将编译报错（此外，后文的[错误的表达式示例](#错误的表达式示例)补充了更多错误的表达式用例场景，可对比参照）：

<!-- compile.error -->

```cangjie
main() {
    let number = 1
    if (number) { // 编译错误，类型不匹配
        println("非零数")
    }
}
```

在许多场景中，当一个条件不成立时，可能还要判断另一个或多个条件，再执行对应的动作。仓颉允许在 `else` 之后跟随新的 `if` 表达式，由此支持多级条件判断和分支执行，例如：

<!-- run -->

```cangjie
import std.random.Random

main() {
    let speed = Random().nextFloat64() * 20.0
    println("${speed} km/s")
    if (speed > 16.7) {
        println("第三宇宙速度，鹊桥相会")
    } else if (speed > 11.2) {
        println("第二宇宙速度，嫦娥奔月")
    } else if (speed > 7.9) {
        println("第一宇宙速度，腾云驾雾")
    } else {
        println("脚踏实地，仰望星空")
    }
}
```

`if` 表达式的值与类型，需要根据使用形式与场景来确定：

- 当含 `else` 分支的 `if` 表达式被求值时，需要根据求值上下文确定 `if` 表达式的类型：

    - 如果上下文明确要求值类型为 `T`，则 `if` 表达式各分支代码块的类型必须是 `T` 的子类型，这时 `if` 表达式的类型被确定为 `T`，如果不满足子类型约束，编译会报错。具体示例如下，由于变量 `b` 的类型 Int64 与各分支代码块的类型不满足子类型约束，因此编译报错：

        <!-- compile.error -->

        ```cangjie
        var a = 10
        var b: Int64 = if(a == 10) { // Error, mismatched types
            "this is 10"
        }else {
            "this is not 10"
        }
        ```

    - 如果上下文没有明确的类型要求，则 `if` 表达式的类型是其各分支代码块类型的最小公共父类型，如果最小公共父类型不存在，编译会报错。具体示例如下，由于字符串和数值类型不存在最小公共父类型，因此编译报错：

        <!-- compile.error -->

        ```cangjie
        var a = 10
        var b = if(a == 10) { // Error, types Struct-String and Int64 of the two branches of this 'if' expression mismatch
            "this is 10"
        }else {
            20
        }
        ```

  如果编译通过，则 `if` 表达式的值就是所执行分支代码块的值。