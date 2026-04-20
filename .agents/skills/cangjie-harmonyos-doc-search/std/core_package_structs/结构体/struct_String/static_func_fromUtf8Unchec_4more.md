### static func fromUtf8Unchecked(Array\<UInt8>)

```cangjie
public unsafe static  func fromUtf8Unchecked(utf8Data: Array<UInt8>): String
```

功能：根据字节数组构造一个字符串。

相较于 [fromUtf8](core_package_structs.md#static-func-fromutf8arrayuint8) 函数，fromUtf8Unchecked 并没有针对于字节数组进行 UTF-8 相关规则的检查，所以它所构建的字符串并不一定保证是合法的，甚至出现非预期的异常，如果不是某些场景下的性能考虑，请优先使用安全的 fromUtf8 函数。

参数：

- utf8Data: [Array](core_package_structs.md#struct-arrayt)\<[UInt8](core_package_intrinsics.md#uint8)> - 根据该字节数组构造字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 构造的字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当试图构造长度超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32) 的字符串时，抛出异常。

### static func join(Array\<String>, String)

```cangjie
public static func join(strArray: Array<String>, delimiter!: String = String.empty): String
```

功能：连接字符串列表中的所有字符串，以指定分隔符分隔。

参数：

- strArray: [Array](core_package_structs.md#struct-arrayt)\<[String](core_package_structs.md#struct-string)> - 需要被连接的字符串数组，当数组为空时，返回空字符串。
- delimiter!: [String](core_package_structs.md#struct-string) - 用于连接的中间字符串，其默认值为 [String](core_package_structs.md#struct-string).empty。

返回值：

- [String](core_package_structs.md#struct-string) - 连接后的新字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当试图构造长度超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32) 的字符串时，抛出异常。

示例：

<!-- verify -->
```cangjie
main() {
    var arr = ["I", "like", "Cangjie"]
    var str = String.join(arr, delimiter: " ")
    println(str)
}
```

运行结果：

```text
I like Cangjie
```

### static func withRawData(Array\<UInt8>)

```cangjie
public static unsafe func withRawData(rawData: Array<UInt8>): String
```

功能：根据字节数组构造一个字符串。

相较于 [fromUtf8Unchecked](core_package_structs.md#static-func-fromutf8uncheckedarrayuint8) 函数，withRawData 没有做数组的拷贝，直接用传入的数组构造了字符串。

> **注意：**
>
> 用户应该保证：
>
> 1. rawData 在字符串构造后永远不会被修改。
> 2. rawData 符合 UTF-8 编码。
>
> 否则程序行为是未定义的。
>
> 如果不是某些场景下的性能考虑，请优先使用安全的 fromUtf8 函数。

参数：

- rawData: [Array](core_package_structs.md#struct-arrayt)\<[UInt8](core_package_intrinsics.md#uint8)> - 根据该字节数组构造字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 构造的字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当试图构造长度超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32) 的字符串时，抛出异常。

### func clone()

```cangjie
public func clone(): String
```

功能：返回原字符串的拷贝。

返回值：

- [String](core_package_structs.md#struct-string) - 拷贝得到的新字符串。