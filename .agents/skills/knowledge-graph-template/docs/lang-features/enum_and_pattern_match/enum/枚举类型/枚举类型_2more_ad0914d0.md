# 枚举类型

本节介绍仓颉中的 `enum` 类型。`enum` 类型提供了通过列举一个类型的所有可能取值来定义此类型的方式。

在很多语言中都有 `enum` 类型（或者称枚举类型），但是不同语言中的 `enum` 类型的使用方式和表达能力均有所差异，仓颉中的 `enum` 类型可以理解为函数式编程语言中的代数数据类型（Algebraic Data Types）。

## enum 的定义

定义 `enum` 时需要把它所有可能的取值一一列出，称这些值为 `enum` 的构造器（或者 `constructor`）。

`enum` 类型的定义以关键字 `enum` 开头，接着是 `enum` 的名字，之后是定义在一对花括号中的 `enum` 体，`enum` 体中定义了若干构造器，多个构造器之间使用 `|` 进行分隔（第一个构造器之前的 `|` 是可选的）。构造器可以是有名字的，也可以是没有名字的 `...`。

每个 `enum` 中至少存在一个有名字的构造器。有名字的构造器可以没有参数（即“无参构造器”），也可以携带若干个参数（即“有参构造器”）。如下示例代码定义了一个名为 `RGBColor` 的 `enum` 类型，它有 3 个构造器：`Red`、`Green` 和 `Blue`，分别表示 RGB 色彩模式中的红色、绿色和蓝色。每个构造器有一个 `UInt8` 类型的参数，用来表示每个颜色的亮度级别。

<!-- compile -->

```cangjie
enum RGBColor {
    | Red(UInt8) | Green(UInt8) | Blue(UInt8)
}
```

仓颉支持同一个 `enum` 中定义多个同名构造器，但是要求这些构造器的参数个数不同（认为没有参数的构造器的参数个数等于 `0`），例如：

<!-- compile -->

```cangjie
enum RGBColor {
    | Red | Green | Blue
    | Red(UInt8) | Green(UInt8) | Blue(UInt8)
}
```

每个 `enum` 中最多只有一个没有名字的 `...` 构造器，且 `...` 只能是最后一个构造器。拥有 `...` 构造器的 `enum` 称为 `non-exhaustive enum`。由于没有名字，这个构造器不能被直接匹配，在解构时，需要使用可匹配所有构造器的模式，如通配符模式 `_` 或绑定模式，具体可参见[match 表达式的定义](./match.md#match-表达式的定义) 。例如：

<!-- compile -->

```cangjie
enum T {
    | Red | Green | Blue | ...
}
```

`enum` 支持递归定义，例如，下面的例子中使用 `enum` 定义了一种表达式（即 `Expr`），此表达式只能有 3 种形式：单独的一个数字 `Num`（携带一个 `Int64` 类型的参数）、加法表达式 `Add`（携带两个 `Expr` 类型的参数）、减法表达式 `Sub`（携带两个 `Expr` 类型的参数）。对于 `Add` 和 `Sub` 这两个构造器，其参数中递归地使用到了 `Expr` 自身。

<!-- compile -->

```cangjie
enum Expr {
    | Num(Int64)
    | Add(Expr, Expr)
    | Sub(Expr, Expr)
}
```

另外，在 `enum` 体中还可以定义一系列成员函数、操作符函数（详见[操作符重载](../function/operator_overloading.md)）和成员属性（详见[属性](../class_and_interface/prop.md)），但是要求构造器、成员函数、成员属性之间不能重名。例如，下面的例子在 `RGBColor` 中定义了一个名为 `printType` 的函数，它会输出字符串 `RGBColor`：

<!-- compile -->

```cangjie
enum RGBColor {
    | Red | Green | Blue

    public static func printType() {
        print("RGBColor")
    }
}
```

> **注意：**
>
> `enum` 只能定义在源文件的顶层作用域。