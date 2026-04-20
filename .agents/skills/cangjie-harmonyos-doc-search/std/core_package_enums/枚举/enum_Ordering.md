## enum Ordering

```cangjie
public enum Ordering {
    | LT
    | GT
    | EQ
}
```

功能：[Ordering](core_package_enums.md#enum-ordering) 表示比较大小的结果，它包含三种情况：小于，大于和等于。

### EQ

```cangjie
EQ
```

功能：构造一个 [Ordering](core_package_enums.md#enum-ordering) 实例，表示等于。

### GT

```cangjie
GT
```

功能：构造一个 [Ordering](core_package_enums.md#enum-ordering) 实例，表示大于。

### LT

```cangjie
LT
```

功能：构造一个 [Ordering](core_package_enums.md#enum-ordering) 实例，表示小于。

### extend Ordering <: Comparable

```cangjie
extend Ordering <: Comparable<Ordering>
```

功能：为 [Ordering](core_package_enums.md#enum-ordering) 类型其扩展 [Comparable](core_package_interfaces.md#interface-comparablet)\<[Ordering](core_package_enums.md#enum-ordering)> 接口，支持比较操作。

父类型：

- [Comparable](core_package_interfaces.md#interface-comparablet)\<[Ordering](#enum-ordering)>

#### func compare(Ordering)

```cangjie
public func compare(that: Ordering): Ordering
```

功能：判断当前 [Ordering](core_package_enums.md#enum-ordering) 实例与参数指定的 [Ordering](core_package_enums.md#enum-ordering) 实例的大小关系。

[Ordering](core_package_enums.md#enum-ordering) 枚举的大小关系为：GT > EQ > LT。

参数：

- that: [Ordering](core_package_enums.md#enum-ordering) - 待比较的 [Ordering](core_package_enums.md#enum-ordering) 实例。

返回值：

- [Ordering](core_package_enums.md#enum-ordering) - 如果大于，返回 GT；如果等于，返回 EQ；如果小于，返回 LT。

### extend Ordering <: Hashable

```cangjie
extend Ordering <: Hashable
```

功能：为 [Ordering](core_package_enums.md#enum-ordering) 类型其扩展 [Hashable](core_package_interfaces.md#interface-hashable) 接口，支持计算哈希值。

父类型：

- [Hashable](core_package_interfaces.md#interface-hashable)

#### func hashCode()

```cangjie
public func hashCode(): Int64
```

功能：获取哈希值，GT 的哈希值是 3，EQ 的哈希值是 2，LT 的哈希值是 1。

返回值：

- [Int64](core_package_intrinsics.md#int64) - 哈希值。

### extend Ordering <: ToString

```cangjie
extend Ordering <: ToString
```

功能：为 [Ordering](core_package_enums.md#enum-ordering) 类型其扩展 [ToString](core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将 [Ordering](core_package_enums.md#enum-ordering) 转换为可输出的字符串。

转换结果如下：

- GT: "[Ordering](core_package_enums.md#enum-ordering).GT"。
- LT: "[Ordering](core_package_enums.md#enum-ordering).ET"。
- EQ: "[Ordering](core_package_enums.md#enum-ordering).EQ"。

返回值：

- [String](core_package_structs.md#struct-string) - 转化后的字符串。