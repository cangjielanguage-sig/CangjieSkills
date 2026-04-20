### operator func |(BigInt)

```cangjie
public operator func |(that: BigInt): BigInt
```

功能：按位或。其功能是参与运算的两数各对应的二进位相或。只有对应的两个二进位都为 0 时，结果位才为 0。

参数：

- that: [BigInt](math_numeric_package_structs.md#struct-bigint) - 按位或运算的另外一个 [BigInt](math_numeric_package_structs.md#struct-bigint)。

返回值：

- [BigInt](math_numeric_package_structs.md#struct-bigint) - 返回与另一个 [BigInt](math_numeric_package_structs.md#struct-bigint) 的按位或的结果。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.BigInt

main() {
    let bigInt = BigInt.parse("8")
    let that = BigInt.parse("7")
    let or = bigInt | that
    println(or)
}
```

运行结果：

```text
15
```

### extend BigInt <: Formattable

```cangjie
extend BigInt <: Formattable
```

功能：为 [BigInt](#struct-bigint) 扩展 [Formattable](../../convert/convert_package_api/convert_package_interfaces.md#interface-formattable) 接口，以实现将 [BigInt](#struct-bigint) 实例转换为格式化字符串。

父类型：

- [Formattable](../../convert/convert_package_api/convert_package_interfaces.md#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [BigInt](#struct-bigint) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [BigInt](#struct-bigint) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。

### extend BigInt <: Integer\<BigInt>

```cangjie
extend BigInt <: Integer<BigInt>
```

功能：为 [BigInt](#struct-bigint) 类型扩展 [Integer\<T>](../../math/math_package_api/math_package_interfaces.md#interface-integert) 接口。

父类型：

- [Integer](../../math/math_package_api/math_package_interfaces.md#interface-integert)\<[BigInt](#struct-bigint)>

#### static func isSigned()

```cangjie
public static func isSigned(): Bool
```

功能：判断 [BigInt](#struct-bigint) 类型是否是有符号类型。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 总是返回 `true`。

### extend BigInt <: Number\<BigInt>

```cangjie
extend BigInt <: Number<BigInt> {}
```

功能：为 [BigInt](#struct-bigint) 类型扩展 [Number\<T>](../../math/math_package_api/math_package_interfaces.md#interface-numbert) 接口。

父类型：

- [Number](../../math/math_package_api/math_package_interfaces.md#interface-numbert)\<[BigInt](#struct-bigint)>