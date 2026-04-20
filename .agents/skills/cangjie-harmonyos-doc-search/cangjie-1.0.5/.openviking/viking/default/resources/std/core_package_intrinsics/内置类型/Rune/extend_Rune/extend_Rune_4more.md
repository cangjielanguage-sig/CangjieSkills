### extend Rune

```cangjie
extend Rune
```

功能：为 [Rune](core_package_intrinsics.md#rune) 类型实现一系列扩展方法，主要为在 Ascii 字符集范围内的一些字符判断、转换等操作。

#### static func fromUtf8(Array\<UInt8>, Int64)

```cangjie
public static func fromUtf8(arr: Array<UInt8>, index: Int64): (Rune, Int64)
```

功能：将字节数组中的指定元素，根据 UTF-8 编码规则转换成字符，并告知字符占用字节长度。

参数：

- arr: [Array](core_package_structs.md#struct-arrayt)\<[UInt8](core_package_intrinsics.md#uint8)> - 待转换字节所在的字节数组。
- index: [Int64](core_package_intrinsics.md#int64) - 待转换字节在数组中的下标。

返回值：

- ([Rune](core_package_intrinsics.md#rune), [Int64](core_package_intrinsics.md#int64)) - 转换得到的字符，以及该字符占用的字节长度。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 不合法的 UTF-8 字节序列。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<UInt8> = [4u8, 8u8, 65u8] // A <=> 65
    var tuple = Rune.fromUtf8(arr, 2)
    println(tuple[0]) // Rune
    println(tuple[1]) // len
}
```

运行结果：

```text
A
1
```

#### static func getPreviousFromUtf8(Array\<UInt8>, Int64)

```cangjie
public static func getPreviousFromUtf8(arr: Array<UInt8>, index: Int64): (Rune, Int64)
```

功能：获取字节数组中指定索引对应的字节所在的 UTF-8 编码字符，同时返回该字符首位字节码在数组中的索引。

当指定了一个索引，那么函数会找到数组对应索引位置并且根据 UTF-8 规则，查看该字节码是否是字符的首位字节码，如果不是就继续向前遍历，直到该字节码是首位字节码，然后利用字节码序列找到对应的字符。

参数：

- arr: [Array](core_package_structs.md#struct-arrayt)\<[UInt8](core_package_intrinsics.md#uint8)> - 待从中获取字符的字节数组。
- index: [Int64](core_package_intrinsics.md#int64) - 待查找字符在数组中的索引。

返回值：

- ([Rune](core_package_intrinsics.md#rune), [Int64](core_package_intrinsics.md#int64)) - 找到的字符，以及该字符首位字节码在数组中的索引。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 如果找不到对应首位字节码，即指定字节所在位置的字节不符合 UTF-8 编码，抛出异常。

#### static func intoUtf8Array(Rune, Array\<UInt8>, Int64)

```cangjie
public static func intoUtf8Array(c: Rune, arr: Array<UInt8>, index: Int64): Int64
```

功能：该函数会把字符转成字节码序列然后覆盖 [Array](core_package_structs.md#struct-arrayt) 数组内指定位置的字节码。

参数：

- c: [Rune](core_package_intrinsics.md#rune) - 待转换的字符。
- arr: [Array](core_package_structs.md#struct-arrayt)\<[UInt8](core_package_intrinsics.md#uint8)> - 待覆盖的 [Array](core_package_structs.md#struct-arrayt) 数组。
- index: [Int64](core_package_intrinsics.md#int64) - 目标位置的起始索引。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 字符的字节码长度，例如中文是三个字节码长度。

示例：

<!-- verify -->
```cangjie
main() {
    var arr: Array<UInt8> = [1u8, 2u8, 3u8, 230u8, 136u8, 145u8]
    var len: Int64 = Rune.intoUtf8Array(r'爱', arr, 2)
    println(len)
    println(arr[2]) // 字符爱的utf-8编码的第一个字节
}
```

运行结果：

```text
3
231
```