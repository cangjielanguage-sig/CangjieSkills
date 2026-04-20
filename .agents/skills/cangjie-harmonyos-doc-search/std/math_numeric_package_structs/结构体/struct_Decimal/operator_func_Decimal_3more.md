### operator func \/(Decimal)

```cangjie
public operator func /(d: Decimal): Decimal
```

功能：除法运算，除法运算符重载，除以入参 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，返回结果值。

> **注意：**
>
> 结果为无限小数场景时，默认采用 IEEE 754-2019 decimal128 对结果进行舍入。

参数：

- d: [Decimal](math_numeric_package_structs.md#struct-decimal) - [Decimal](math_numeric_package_structs.md#struct-decimal) 除数对象。

返回值：

- [Decimal](math_numeric_package_structs.md#struct-decimal) - 生成一个新的 [Decimal](math_numeric_package_structs.md#struct-decimal) 对象，用于存储除法运算结果值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当除数为 0 时，抛出此异常。
- [OverflowException](../../core/core_package_api/core_package_exceptions.md#class-overflowexception) - 当除法结果值范围超过 [-(maxValue(precision) * (10 <sup>[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).MAX</sup>)), maxValue(precision) * (10 <sup>[Int32](../../core/core_package_api/core_package_intrinsics.md#int32).MAX</sup>)] 时，抛出此异常。

示例：
<!-- verify -->
```cangjie
import std.math.numeric.Decimal

main(): Unit {
    let A = Decimal(2)
    let B = Decimal(3)
    let C = A / B
    println("C = ${C}")
}
```

运行结果：

```text
C = 0.6666666666666666666666666666666667
```

### extend Decimal <: Formattable

```cangjie
extend Decimal <: Formattable
```

功能：为 [Decimal](#struct-decimal) 扩展 [Formattable](../../convert/convert_package_api/convert_package_interfaces.md#interface-formattable) 接口，以实现将 [Decimal](#struct-decimal) 实例转换为格式化字符串。

父类型：

- [Formattable](../../convert/convert_package_api/convert_package_interfaces.md#interface-formattable)

#### func format(String)

```cangjie
public func format(fmt: String): String
```

功能：根据格式化参数将当前 [Decimal](#struct-decimal) 类型实例格式化为对应格式的字符串。

参数：

- fmt: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 格式化参数。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 将当前 [Decimal](#struct-decimal) 类型实例格式化后得到的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当 fmt 不合法时抛出异常。

### extend Decimal <: Number\<Decimal>

```cangjie
extend Decimal <: Number<Decimal> {}
```

功能：为 [Decimal](#struct-decimal) 类型扩展 [Number\<T>](../../math/math_package_api/math_package_interfaces.md#interface-numbert) 接口。

父类型：

- [Number](../../math/math_package_api/math_package_interfaces.md#interface-numbert)\<[Decimal](#struct-decimal)>