# 仓颉标准库类型转换 Skill

> 导入：`import std.convert.*`
>
> `std.convert.*` 不会自动导入；使用本专题 API 前必须确认顶层 import。

---

## 1. Parsable\<T> — 字符串解析为指定类型

```cangjie
public interface Parsable<T> {
    static func parse(value: String): T           // 失败抛 IllegalArgumentException
    static func tryParse(value: String): Option<T> // 失败返回 None
}
```

### 1.1 解析路径选择

- 输入无效属于契约违例、并且调用栈已有异常处理时，使用 `parse`；其结果是普通 `T`。
- 输入来自用户、文件或网络，解析失败是预期分支时，使用 `tryParse`；其结果是 `Option<T>`，由调用方匹配、解包或提供默认值。
- `??` 只适用于 `tryParse` 等 Option 结果，不能用于 `parse` 的普通返回值。两条路径的区别是失败语义，不是语法偏好。

### 1.2 已实现类型

Bool, Rune, Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64, Float16, Float32, Float64

### 1.3 用法示例

```cangjie
import std.convert.*

main() {
    // parse — 失败抛异常
    let n = Int64.parse("12345")          // 12345
    let f = Float64.parse("3.14")         // 3.140000
    let b = Bool.parse("true")            // true
    let c = Rune.parse("'a'")             // a

    // tryParse — 失败返回 None，安全转换
    let r1 = Int32.tryParse("abc")        // None
    let r2 = Int32.tryParse("42")         // Some(42)

    // 配合模式匹配使用
    let userInput = "999"
    match (Int64.tryParse(userInput)) {
        case Some(v) => println("解析成功: ${v}")
        case None => println("无效输入")
    }
}
```

> **注意**：浮点数解析暂不支持二进制和八进制格式。Rune 解析需要带引号，如 `"'a'"`。

---

## 2. RadixConvertible\<T> — 指定进制的解析与转换

```cangjie
public interface RadixConvertible<T> {
    static func parse(value: String, radix!: Int64): T
    static func tryParse(value: String, radix!: Int64): Option<T>
    func toString(radix!: Int64): String
}
```

### 2.1 已实现类型

Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64

### 2.2 进制规则

- `radix` 范围：2 ~ 36（10 个数字 + 26 个字母）
- Int 系列支持 `+`/`-` 前缀；UInt 系列不允许 `-` 前缀
- `toString` 输出使用小写字母
- 无法使用 `std.convert.*` 时，本专题的进制 API 不可用；若契约必须完成指定进制转换，可选择经过验证的 digit 表与循环实现，否则说明依赖缺口。

### 2.3 用法示例

```cangjie
import std.convert.*

main() {
    // 从指定进制字符串解析
    let hex = Int64.parse("FF", radix: 16)     // 255
    let bin = Int64.parse("1010", radix: 2)    // 10
    let oct = UInt32.parse("77", radix: 8)     // 63

    // 安全解析
    let r = Int64.tryParse("GG", radix: 16)    // None

    // 转换为指定进制字符串
    let n: Int64 = 255
    println(n.toString(radix: 16))   // "ff"
    println(n.toString(radix: 2))    // "11111111"
    println(n.toString(radix: 8))    // "377"

    // 36 进制
    println(Int64.parse("z", radix: 36))       // 35
    let big: Int64 = 35
    println(big.toString(radix: 36))            // "z"
}
```

---

## 3. 常见用法总结

```cangjie
import std.convert.*

main() {
    // 1. 安全解析用户输入
    let input = "100"
    if (let Some(v) <- Int64.tryParse(input)) {
        println("数值: ${v}")
    }

    // 2. 十六进制字符串 <-> 整数互转
    let addr = UInt64.parse("DEADBEEF", radix: 16)
    println(addr.toString(radix: 16))  // "deadbeef"

    // 3. 二进制位表示
    let flags: Int32 = 13
    println(flags.toString(radix: 2))  // "1101"

    // 4. 字符串转浮点
    let pi = Float64.parse("3.14159265358979")
    println(pi)  // 3.141593
}
```
