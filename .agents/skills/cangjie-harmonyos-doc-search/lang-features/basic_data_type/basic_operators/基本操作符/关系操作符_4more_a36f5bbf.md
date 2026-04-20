## 关系操作符

关系操作符包括六种：相等（`==`）、不等（`!=`）、小于（`<`）、小于等于（`<=`）、大于（`>`）、大于等于（`>=`）。关系操作符都是二元操作符，并且要求两个操作数的类型是一样的。关系表达式的类型是 Bool 类型，即值只可能是 true 或 false。

关系表达式举例：

<!-- compile -->

```cangjie
main(): Int64 {
    3 < 4        // true
    3 <= 3       // true
    3 > 4        // false
    3 >= 3       // true
    3.14 == 3.15 // false
    3.14 != 3.15 // true
    return 0
}
```

对于元组类型，当且仅当所有元素均支持使用 `==` 进行值判等（使用 `!=` 进行值判不等）时，此元组类型才支持使用 `==` 进行值判等（使用 `!=` 进行值判不等）；否则，此元组类型不支持 `==` 和 `!=`（如果使用 `==` 和 `!=`，编译报错）。两个同类型的元组实例相等，当且仅当相同位置（index）的元素全部相等（意味着它们的长度相等）。

<!-- compile.error -->

```cangjie
    var isTrue: Bool = (1, 3) == (0, 2) // false
    isTrue = (1, "123") == (1.0, 2)      // 编译错误，两个操作数的类型不一致
    isTrue = (1, _) == (1.0, _)          // 编译错误，通配符不可作为元组中元素进行匹配
```

## coalescing 操作符

coalescing 操作符使用 `??` 表示，`??` 是二元中缀操作符。coalescing 操作符用于 [Option 类型](../enum_and_pattern_match/option_type.md)的解构。

`e1 ?? e2` 表达式，在 e1 的值等于 `Option<T>.Some(v)` 时，`e1 ?? e2` 的值等于 v 的值（此时，不会再去对 e2 求值，即满足 “短路求值”）；在 e1 的值等于 `Option<T>.None` 时，`e1 ?? e2` 的值等于 e2 的值。

coalescing 表达式使用举例：

<!-- run -->

```cangjie
main(): Int64 {
    let v1 = Option<Int64>.Some(100)
    let v2 = Option<Int64>.None
    let r1 = v1 ?? 0
    let r2 = v2 ?? 0
    print("${r1}") // 100
    print("${r2}") // 0
    return 0
}
```

## 区间操作符

区间操作符有两种：`..` 和 `..=`，分别用于创建 “左闭右开” 和 “左闭右闭” 的区间实例。关于它们的介绍，请参见 [区间类型](./range.md)。

## 逻辑操作符

仓颉编程语言支持三种逻辑操作符：逻辑非（`!`）、逻辑与（`&&`）、逻辑或（`||`）。

逻辑非（`!`）是一元操作符，它的作用是对其操作数的布尔值取反：`!false` 的值等于 `true`，`!true` 的值等于 `false`。

<!-- compile -->

```cangjie
    var a: Bool = true     // a = true
    var b: Bool = !a       // b = false
    var c: Bool = !false   // c = true
```

逻辑与（`&&`）和逻辑或（`||`）均是二元操作符。对于表达式 `expr1 && expr2`，只有当 `expr1` 和 `expr2` 的值均等于 `true` 时，它的值才等于 `true`；对于表达式 `expr1 || expr2`，只有当 `expr1` 和 `expr2` 的值均等于 `false` 时，它的值才等于 `false`。

<!-- compile -->

```cangjie
    var a: Bool = true && true    // a = true
    var b: Bool = true && false   // b = false
    var c: Bool = false && false  // c = false
    var d: Bool = false && true   // d = false

    a = true || true              // a = true
    b = true || false             // b = true
    c = false || false            // c = false
    d = false || true             // d = true
```

逻辑与（`&&`）和逻辑或（`||`）采用短路求值策略：计算 `expr1 && expr2` 时，当 `expr1=false` 则无需对 `expr2` 求值，整个表达式的值为 `false`；计算 `expr1 || expr2` 时，当 `expr1=true` 则无需对 `expr2` 求值，整个表达式的值为 `true`。

<!-- run -->

```cangjie
func isEven(a: Int64): Bool {
    if((a % 2) == 0) {
         println("${a} is an even number")
         true
    } else {
        println("${a} is not an even number")
        false
    }
}


main() {
    var a: Bool = isEven(2) && isEven(20)
    var b: Bool = isEven(3) && isEven(30) // isEven(3)返回值是false, b 值为false，无需对isEven(30)求值

    a = isEven(4) || isEven(40)  // isEven(4)返回值是true, a 值为true，无需对isEven(40)求值
    b = isEven(5) || isEven(50)
}
```