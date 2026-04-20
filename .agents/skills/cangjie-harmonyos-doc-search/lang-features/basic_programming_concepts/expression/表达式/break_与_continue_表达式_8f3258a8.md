## break 与 continue 表达式

在循环结构的程序中，有时需要根据特定条件提前结束循环或跳过本轮循环，为此仓颉引入了 `break` 与 `continue` 表达式，它们可以出现在循环表达式的循环体中，`break` 用于终止当前循环表达式的执行、转去执行循环表达式之后的代码，`continue` 用于提前结束本轮循环、进入下一轮循环。`break` 与 `continue` 表达式的类型都是 [`Nothing`](../basic_data_type/nothing.md)。

例如，以下程序使用 `for-in` 表达式和 `break` 表达式，在给定的整数数组中，找到第一个能被 5 整除的数字：

<!-- verify -->

```cangjie
main() {
    let numbers = [12, 18, 25, 36, 49, 55]
    for (number in numbers) {
        if (number % 5 == 0) {
            println(number)
            break
        }
    }
}
```

当 `for-in` 迭代至 `numbers` 数组的第三个数 25 时，由于 25 可以被 5 整除，所以将执行 `if` 分支中的 `println` 和 `break`，`break` 将终止 `for-in` 循环，`numbers`中的后续数字不会被遍历到。因此运行以上程序，将输出：

```text
25
```

以下程序使用 `for-in` 表达式和 `continue` 表达式，将给定整数数组中的奇数打印出来：

<!-- verify -->

```cangjie
main() {
    let numbers = [12, 18, 25, 36, 49, 55]
    for (number in numbers) {
        if (number % 2 == 0) {
            continue
        }
        println(number)
    }
}
```

在循环迭代中，当 `number` 是偶数时，`continue` 将被执行，这会提前结束本轮循环，进入下一轮循环，`println` 不会被执行。因此运行以上程序，将输出：

```text
25
49
55
```