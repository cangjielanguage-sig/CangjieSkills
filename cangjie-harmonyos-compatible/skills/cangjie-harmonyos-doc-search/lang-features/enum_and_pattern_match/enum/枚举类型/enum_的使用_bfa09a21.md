## enum 的使用

定义了 `enum` 类型之后，就可以创建此类型的实例（即 `enum` 值），`enum` 值只能取 `enum` 类型定义中的一个构造器。`enum` 没有构造函数，可以通过 `类型名.构造器`，或者直接使用构造器的方式来构造一个 `enum` 值（对于有参构造器，需要传实参）。

下例中，`RGBColor` 中定义了三个构造器，其中有两个无参构造器（`Red` 和 `Green`）和一个有参构造器（`Blue(UInt8)`），`main` 中定义了三个 `RGBColor` 类型的变量 `r`，`g` 和 `b`，其中，`r` 的值使用 `RGBColor.Red` 进行初始化，`g` 的值直接使用 `Green` 进行初始化，`b` 的值使用 `Blue(100)` 进行初始化：

<!-- compile -->

```cangjie
enum RGBColor {
    | Red | Green | Blue(UInt8)
}

main() {
    let r = RGBColor.Red
    let g = Green
    let b = Blue(100)
}
```

当省略类型名时，`enum` 构造器的名字可能和类型名、变量名、函数名发生冲突。此时必须加上 `enum` 类型名来使用 `enum` 构造器，否则只会选择同名的类型、变量、函数定义。

下面的例子中，只有构造器 `Blue(UInt8)` 可以不带类型名使用，`Red` 和 `Green(UInt8)` 皆会因为名字冲突而不能直接使用，必须加上类型名 `RGBColor`。

<!-- compile -->

```cangjie
let Red = 1

func Green(g: UInt8) {
    return g
}

enum RGBColor {
    | Red | Green(UInt8) | Blue(UInt8)
}

let r1 = Red                 // Will choose 'let Red'
let r2 = RGBColor.Red        // OK: constructed by enum type name

let g1 = Green(100)          // Will choose 'func Green'
let g2 = RGBColor.Green(100) // OK: constructed by enum type name

let b = Blue(100)            // OK: can be uniquely identified as an enum constructor
```

如下的例子中，只有构造器 `Blue` 会因为名称冲突而不能直接使用，必须加上类型名 `RGBColor`。

<!-- compile.error -->

```cangjie
class Blue {}

enum RGBColor {
    | Red | Green(UInt8) | Blue(UInt8)
}

let r = Red                 // OK: constructed by enum type name

let g = Green(100)          // OK: constructed by enum type name

let b = Blue(100)           // Will choose constructor of 'class Blue' and report an error
```