## while 表达式

`while` 表达式的基本形式为：

```text
while (条件) {
  循环体
}
```

其中“条件”同 `if` 表达式的“条件”，“循环体”是一个代码块。`while` 表达式将按如下规则执行：

1. 计算“条件”表达式，如果值为 `true` 则转第 2 步，值为 `false` 转第 3 步。
2. 执行“循环体”，转第 1 步。
3. 结束循环，继续执行 `while` 表达式后面的代码。

例如，以下程序使用 `while` 表达式，基于二分法，近似计算数字 2 的平方根：

<!-- verify -->

```cangjie
main() {
    var root = 0.0
    var min = 1.0
    var max = 2.0
    var error = 1.0
    let tolerance = 0.1 ** 10

    while (error ** 2 > tolerance) {
        root = (min + max) / 2.0
        error = root ** 2 - 2.0
        if (error > 0.0) {
            max = root
        } else {
            min = root
        }
    }
    println("2 的平方根约等于：${root}")
}
```

运行以上程序，将输出：

```text
2 的平方根约等于：1.414215
```

## do-while 表达式

`do-while` 表达式的基本形式为：

```text
do {
  循环体
} while (条件)
```

其中“条件”是布尔类型表达式，“循环体”是一个代码块。`do-while` 表达式将按如下规则执行：

1. 执行“循环体”，转第 2 步。
2. 计算“条件”表达式，如果值为 `true` 则转第 1 步，值为 `false` 转第 3 步。
3. 结束循环，继续执行 `do-while` 表达式后面的代码。

例如，以下程序使用 `do-while` 表达式，基于蒙特卡洛算法，近似计算圆周率的值：

<!-- run -->

```cangjie
import std.random.Random

main() {
    let random = Random()
    var totalPoints = 0
    var hitPoints = 0

    do {
        // 在 ((0, 0), (1, 1)) 这个正方形中随机取点
        let x = random.nextFloat64()
        let y = random.nextFloat64()
        // 判断是否落在正方形内接圆里
        if ((x - 0.5) ** 2 + (y - 0.5) ** 2 < 0.25) {
            hitPoints++
        }
        totalPoints++
    } while (totalPoints < 1000000)

    let pi = 4.0 * Float64(hitPoints) / Float64(totalPoints)
    println("圆周率近似值为：${pi}")
}
```

运行以上程序，将输出：

```text
圆周率近似值为：3.141872
```

> **说明：**
>
> 由于算法涉及随机数，所以每次运行程序输出的数值可能都不同，但都会约等于 3.14。