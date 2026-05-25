# 模式概述

对于包含匹配值的 `match` 表达式，`case` 之后支持哪些模式决定了 `match` 表达式的表达能力。本节中将依次介绍仓颉支持的模式，包括：常量模式、通配符模式、绑定模式、tuple 模式、类型模式和 enum 模式。

## 常量模式

常量模式可以是整数字面量、浮点数字面量、字符字面量、布尔字面量、字符串字面量（不支持字符串插值）、Unit 字面量。

在包含匹配值的 `match` 表达式（参见[match 表达式](./match.md)）中使用常量模式时，要求常量模式表示的值的类型与待匹配值的类型相同，匹配成功的条件是待匹配的值与常量模式表示的值相等。

下面的例子中，根据 `score` 的值（假设 `score` 只能取 `0` 到 `100` 间被 `10` 整除的值），输出考试成绩的等级：

<!-- verify -->

```cangjie
main() {
    let score = 90
    let level = match (score) {
        case 0 | 10 | 20 | 30 | 40 | 50 => "D"
        case 60 => "C"
        case 70 | 80 => "B"
        case 90 | 100 => "A" // Matched.
        case _ => "Not a valid score"
    }
    println(level)
}
```

编译执行上述代码，输出结果为：

```text
A
```

- 在模式匹配的目标是静态类型为 `Rune` 的值时，`Rune` 字面量和单字符字符串字面量都可用于表示 `Rune` 类型字面量的常量 pattern。

  <!-- verify -->

  ```cangjie
  func translate(n: Rune) {
      match (n) {
          case "A" => 1
          case "B" => 2
          case "C" => 3
          case _ => -1
      }
  }

  main() {
      println(translate(r"C"))
  }
  ```

  编译执行上述代码，输出结果为：

  ```text
  3
  ```

- 在模式匹配的目标是静态类型为 `Byte` 的值时，一个表示 ASCII 字符的字符串字面量可用于表示 `Byte` 类型字面量的常量 pattern。

  <!-- verify -->

  ```cangjie
  func translate(n: Byte) {
      match (n) {
          case "1" => 1
          case "2" => 2
          case "3" => 3
          case _ => -1
      }
  }

  main() {
      println(translate(51)) // UInt32(r'3') == 51
  }
  ```

  编译执行上述代码，输出结果为：

  ```text
  3
  ```

## 通配符模式

通配符模式使用下划线 `_` 表示，可以匹配任意值。通配符模式通常作为最后一个 `case` 中的模式，用来匹配其他 `case` 未覆盖到的情况，如[常量模式](./pattern_overview.md#常量模式)中匹配 `score` 值的示例中，最后一个 `case` 中使用 `_` 来匹配无效的 `score` 值。