### extend Rune <: Comparable\<Rune>

```cangjie
extend Rune <: Comparable<Rune>
```

功能：为 [Rune](core_package_intrinsics.md#rune) 类型扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[Rune](core_package_intrinsics.md#rune)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[Rune](#rune)>

#### func compare(Rune)

```cangjie
public func compare(rhs: Rune): Ordering
```

功能：判断当前 [Rune](core_package_intrinsics.md#rune) 实例与指定 [Rune](core_package_intrinsics.md#rune) 实例的大小关系。

[Rune](core_package_intrinsics.md#rune) 的大小关系指的是它们对应的 unicode 码点的大小关系。

参数：

- rhs: [Rune](core_package_intrinsics.md#rune) - 待比较的另一个 [Rune](core_package_intrinsics.md#rune) 实例。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 [Ordering](core_package_enums.md#enum-ordering).GT；如果等于，返回 [Ordering](core_package_enums.md#enum-ordering).EQ；如果小于，返回 [Ordering](core_package_enums.md#enum-ordering).LT。

示例：

<!-- verify -->
```cangjie
main() {
    var char1: Rune = r'i'
    var char2: Rune = r'j'
    println(char1.compare(char2))
}
```

运行结果：

```text
Ordering.LT
```

### extend Rune <: Countable\<Rune>

```cangjie
extend Rune <: Countable<Rune>
```

功能：为 [Rune](core_package_intrinsics.md#rune) 类型扩展 [Countable](core_package_interfaces.md#interface-countablet)\<[Rune](core_package_intrinsics.md#rune)> 接口，支持计数操作。

父类型：

- [Countable](core_package_interfaces.md#interface-countablet)\<[Rune](#rune)>

#### func next(Int64)

```cangjie
public func next(right: Int64): Rune
```

功能：获取当前 [Rune](core_package_intrinsics.md#rune) 值往右数 `right` 后所到位置的 [Rune](core_package_intrinsics.md#rune) 值。

参数：

- right: [Int64](core_package_intrinsics.md#int64) - 往右数的个数。

返回值：

- [Rune](core_package_intrinsics.md#rune) - 往右数 `right` 后所到位置的 [Rune](core_package_intrinsics.md#rune) 值。

异常：

- [OverflowException](core_package_exceptions.md#class-overflowexception) - 如果与 [Int64](core_package_intrinsics.md#int64) 数进行加法运算后为不合法的 Unicode 值，抛出异常。

#### func position()

```cangjie
public func position(): Int64
```

功能：获取当前 [Rune](core_package_intrinsics.md#rune) 值的位置信息，即将该 [Rune](core_package_intrinsics.md#rune) 转换为 [Int64](core_package_intrinsics.md#int64) 值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 当前 [Rune](core_package_intrinsics.md#rune) 值的位置信息。

### extend Rune <: Hashable

```cangjie
extend Rune <: Hashable
```

功能：为 [Rune](core_package_intrinsics.md#rune) 类型扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。

### extend Rune <: ToString

```cangjie
extend Rune <: ToString
```

功能：这里为 [Rune](core_package_intrinsics.md#rune) 类型扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，实现向 [String](core_package_structs.md#struct-string) 类型的转换。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [Rune](core_package_intrinsics.md#rune) 值转换为可输出的字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。