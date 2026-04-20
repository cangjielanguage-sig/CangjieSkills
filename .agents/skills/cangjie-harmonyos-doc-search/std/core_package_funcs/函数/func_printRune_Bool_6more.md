## func print(Rune, Bool)

```cangjie
public func print(c: Rune, flush!: Bool = false): Unit
```

功能：向控制台输出 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型数据的字符串表达。

参数：

- c: [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 待输出的 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var char: Rune = r'a'
    print(char)
}
```

运行结果：

```text
a
```

## func print(String, Bool)

```cangjie
public func print(str: String, flush!: Bool = false): Unit
```

功能：向控制台输出指定字符串。

参数：

- str: [String](core_package_structs.md#struct-string) - 待输出的字符串。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var str: String = "I like Cangjie"
    print(str)
}
```

运行结果：

```text
I like Cangjie
```

## func print(UInt16, Bool)

```cangjie
public func print(i: UInt16, flush!: Bool = false): Unit
```

功能：向控制台输出 [UInt16](core_package_intrinsics.md#uint16) 类型数据的字符串表达。

参数：

- i: [UInt16](core_package_intrinsics.md#uint16) - 待输出的 [UInt16](core_package_intrinsics.md#uint16) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt16 = 8
    var num2: UInt16 = 32
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
8
32
```

## func print(UInt32, Bool)

```cangjie
public func print(i: UInt32, flush!: Bool = false): Unit
```

功能：向控制台输出 [UInt32](core_package_intrinsics.md#uint32) 类型数据的字符串表达。

参数：

- i: [UInt32](core_package_intrinsics.md#uint32) - 待输出的 [UInt32](core_package_intrinsics.md#uint32) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt16 = 8
    var num2: UInt16 = 32
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
8
32
```

## func print(UInt64, Bool)

```cangjie
public func print(i: UInt64, flush!: Bool = false): Unit
```

功能：向控制台输出 [UInt64](core_package_intrinsics.md#uint64) 类型数据的字符串表达。

参数：

- i: [UInt64](core_package_intrinsics.md#uint64) - 待输出的 [UInt64](core_package_intrinsics.md#uint64) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt64 = 8
    var num2: UInt64 = 32
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
8
32
```

## func print(UInt8, Bool)

```cangjie
public func print(i: UInt8, flush!: Bool = false): Unit
```

功能：向控制台输出 [UInt8](core_package_intrinsics.md#uint8) 类型数据的字符串表达。

参数：

- i: [UInt8](core_package_intrinsics.md#uint8) - 待输出的 [UInt8](core_package_intrinsics.md#uint8) 类型数据。
- flush!: [Bool](core_package_intrinsics.md#bool) - 是否清空缓存，true 清空，false 不清空，默认 false。

示例：

<!-- verify -->
```cangjie
main() {
    var num1: UInt8 = 8
    var num2: UInt8 = 32
    print(num1)
    println()
    print(num2)
}
```

运行结果：

```text
8
32
```