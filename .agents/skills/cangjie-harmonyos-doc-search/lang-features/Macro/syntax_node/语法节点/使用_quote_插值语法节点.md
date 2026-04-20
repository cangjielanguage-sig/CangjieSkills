## 使用 quote 插值语法节点

任何语法节点都可以在 `quote` 语句中插值，部分语法节点的 `ArrayList` 列表也可以被插值（主要对应实际情况中会出现这类节点列表的情况）。插值直接通过 `$(node)` 表达即可，其中 `node` 是任意节点类型的实例。

下面，通过一些案例展示节点的插值。

<!-- verify -->

```cangjie
var binExpr = BinaryExpr(quote(1 + 2))
let a = quote($(binExpr))
let b = quote($binExpr)
let c = quote($(binExpr.leftExpr))
let d = quote($binExpr.leftExpr)
println("a: ${a.toTokens()}")
println("b: ${b.toTokens()}")
println("c: ${c.toTokens()}")
println("d: ${d.toTokens()}")
```

输出结果是：

```text
a: 1 + 2
b: 1 + 2
c: 1
d: 1 + 2.leftExpr
```

一般来说，插值运算符后面的表达式使用小括号限定作用域，例如 `$(binExpr)`。但是当后面只跟单个标识符的时候，小括号可省略，即可写为 `$binExpr`。因此，在案例中 `a` 和 `b` 都在 `quote` 中插入了 `binExpr`节点，结果为 `1 + 2`。然而，如果插值运算符后面的表达式更复杂，不加小括号可能造成作用域出错。例如，表达式 `binExpr.leftExpr` 求值为 `1 + 2` 的左表达式，即 `1`，因此 `c` 正确赋值为 `1`。但 `d` 中的插值被解释为 `($binExpr).leftExpr`，因此结果是 `1 + 2.leftExpr`。为了明确插值的作用域，推荐在插值运算符中使用小括号。

下面的案例展示节点列表（`ArrayList`）的插值。

<!-- verify -->

```cangjie
var incrs = ArrayList<Node>()
for (i in 1..=5) {
    incrs.add(parseExpr(quote(x += $(i))))
}
var foo = quote(
    func foo(n: Int64) {
        let x = n
        $(incrs)
        x
    })
println(foo)
```

输出结果是：

```text
func foo(n: Int64) {
    let x = n
    x += 1
    x += 2
    x += 3
    x += 4
    x += 5
    x
}
```

在这个案例中，创建了一个节点列表 `incrs`，包含表达式 `x += 1`，...，`x += 5`。对 `incrs` 的插值将节点依次列出，在每个节点后换行。这适用于插入需要依次执行的表达式和声明的情况。

下面的案例展示在某些情况下，需要在插值周围添加括号，以保证正确性。

<!-- verify -->

```cangjie
var binExpr1 = BinaryExpr(quote(x + y))
var binExpr2 = BinaryExpr(quote($(binExpr1) * z))       // 错误：得到 x + y * z
println("binExpr2: ${binExpr2.toTokens()}")
println("binExpr2.leftExpr: ${binExpr2.leftExpr.toTokens()}")
println("binExpr2.rightExpr: ${binExpr2.rightExpr.toTokens()}")
var binExpr3 = BinaryExpr(quote(($(binExpr1)) * z))     // 正确：得到 (x + y) * z
println("binExpr3: ${binExpr3.toTokens()}")
```

输出结果是：

```text
binExpr2: x + y * z
binExpr2.leftExpr: x
binExpr2.rightExpr: y * z
binExpr3: (x + y) * z
```

首先，构建表达式 `x + y`，然后将该表达式插入到模板 `$(binExpr1) * z` 中。这里的意图是得到一个先计算 `x + y` 再乘 `z` 的表达式，但是，插值的结果是 `x + y * z`，即先计算 `y * z` 再加 `x`。这是因为插值不会自动添加括号以保证被插入的表达式的原子性（这和前一节介绍的 `leftExpr` 的替换不同）。因此，需要在 `$(binExpr1)` 周围添加小括号，保证得到正确的结果。