### operator func \[](Int64)

```cangjie
public operator const func [](index: Int64): Byte
```

功能：返回指定索引 index 处的 UTF-8 编码字节。

参数：

- index: [Int64](core_package_intrinsics.md#int64) - 要获取 UTF-8 编码字节的下标。

返回值：

- [Byte](core_package_types.md#type-byte) - 获取得到下标对应的 UTF-8 编码字节。

异常：

- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果 index 小于 0 或大于等于字符串长度，抛出异常。

### operator func \[](Range\<Int64>)

```cangjie
public operator const func [](range: Range<Int64>): String
```

功能：根据给定区间获取当前字符串的切片。

> **注意：**
>
> 1. 如果参数 range 是使用 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 构造函数构造的 [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet) 实例，有如下行为：
>    - start 的值就是构造函数传入的值本身，不受构造时传入的 hasStart 的值的影响。
>    - hasEnd 为 false 时，end 值不生效，且不受构造时传入的 isClosed 的值的影响，该字符串切片取到原字符串最后一个元素。
> 2. range 的步长只能为 1。

参数：

- range: [Range](core_package_structs.md#struct-ranget-where-t--countablet--comparablet--equatablet)\<[Int64](core_package_intrinsics.md#int64)> - 切片的区间。

返回值：

- [String](core_package_structs.md#struct-string) - 字符串切片。

异常：

- [IndexOutOfBoundsException](core_package_exceptions.md#class-indexoutofboundsexception) - 如果切片范围超过原字符串边界，抛出异常。
- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 如果 range.[step](#let-step) 不等于 1 或者范围起止点不是字符边界，抛出异常。