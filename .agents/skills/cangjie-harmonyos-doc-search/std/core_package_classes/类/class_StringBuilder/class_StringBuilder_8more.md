## class StringBuilder

```cangjie
public class StringBuilder <: ToString {
    public init()
    public init(str: String)
    public init(r: Rune, n: Int64)
    public init(value: Array<Rune>)
    public init(capacity: Int64)
}
```

功能：该类主要用于字符串的构建。

[StringBuilder](core_package_classes.md#class-stringbuilder) 在字符串的构建上效率高于 [String](core_package_structs.md#struct-string)：

- 在功能上支持传入多个类型的值，该类将自动将其转换为 [String](core_package_structs.md#struct-string) 类型对象，并追加到构造的字符串中。
- 在性能上使用动态扩容算法，减少内存申请频率，构造字符串的速度更快，占用内存资源通常更少。

> **注意：**
>
> [StringBuilder](core_package_classes.md#class-stringbuilder) 仅支持 UTF-8 编码的字符数据。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

### prop capacity

```cangjie
public prop capacity: Int64
```

功能：获取 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例此时能容纳字符串的长度，该值会随扩容的发生而变大。

类型：[Int64](core_package_intrinsics.md#int64)

### prop size

```cangjie
public prop size: Int64
```

功能：获取 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例中字符串长度。

类型：[Int64](core_package_intrinsics.md#int64)

### init()

```cangjie
public init()
```

功能：构造一个初始容量为 32 的空 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例。

### init(Array\<Rune>)

```cangjie
public init(value: Array<Rune>)
```

功能：使用参数 `value` 指定的字符数组初始化一个 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例，该实例的初始容量为 `value` 大小，初始内容为 `value` 包含的字符内容。

参数：

- value: [Array](core_package_structs.md#struct-arrayt)\<Rune> - 初始化 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例的字符数组。

### init(Int64)

```cangjie
public init(capacity: Int64)
```

功能：使用参数 `capacity` 指定的容量初始化一个空 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例，该实例的初始容量为 `value` 大小，初始内容为若干 `\0` 字符。

参数：

- capacity: [Int64](core_package_intrinsics.md#int64) - 初始化 [StringBuilder](core_package_classes.md#class-stringbuilder) 的字节容量，取值范围为 (0, [Int64.Max](./core_package_intrinsics.md)]。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当参数 `capacity` 的值小于等于 0 时，抛出异常。

### init(Rune, Int64)

```cangjie
public init(r: Rune, n: Int64)
```

功能：使用 `n` 个 `r` 字符初始化 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例，该实例的初始容量为 `n`，初始内容为 `n` 个 `r` 字符。

参数：

- r: Rune - 初始化 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例的字符。
- n: [Int64](core_package_intrinsics.md#int64) - 字符 `r` 的数量，取值范围为 [0, [Int64.Max](./core_package_intrinsics.md)]。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当参数 `n` 小于 0 时，抛出异常。

### init(String)

```cangjie
public init(str: String)
```

功能：根据指定初始字符串构造 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例，该实例的初始容量为指定字符串的大小，初始内容为指定字符串。

参数：

- str: [String](core_package_structs.md#struct-string) - 初始化 [StringBuilder](core_package_classes.md#class-stringbuilder) 实例的字符串。