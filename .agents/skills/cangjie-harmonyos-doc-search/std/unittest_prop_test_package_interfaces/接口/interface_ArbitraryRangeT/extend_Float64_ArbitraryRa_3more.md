### extend Float64 <: ArbitraryRange\<Float64>

```cangjie
extend Float64 <: ArbitraryRange<Float64> {
    public static func min(): Float64 
    public static func max(): Float64 
    public static func arbitraryRange(random: RandomSource, min: Float64, max: Float64): Generator<Float64> 
}
```

功能：为 Float64 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, Float64, Float64)

```cangjie
func arbitraryRange(random: RandomSource, min: Float64, max: Float64): Generator<Float64>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: Float64 - 可生成范围的最小值。
- max: Float64 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Float64> - 生成器。

#### func max()

```cangjie
func max(): Float64
```

功能：返回最大值。

返回值：

- Float64 - 最大值。

#### func min()

```cangjie
func min(): Float64
```

功能：返回最小值。

返回值：

- Float64 - 最小值。

### extend Int16 <: ArbitraryRange\<Int16>

```cangjie
extend Int16 <: ArbitraryRange<Int16> {
    public static func min(): Int16 
    public static func max(): Int16 
    public static func arbitraryRange(random: RandomSource, min: Int16, max: Int16): Generator<Int16> 
}
```

功能：为 Int16 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, Int16, Int16)

```cangjie
func arbitraryRange(random: RandomSource, min: Int16, max: Int16): Generator<Int16>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: Int16 - 可生成范围的最小值。
- max: Int16 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Int16> - 生成器。

#### func max()

```cangjie
func max(): Int16
```

功能：返回最大值。

返回值：

- Int16 - 最大值。

#### func min()

```cangjie
func min(): Int16
```

功能：返回最小值。

返回值：

- Int16 - 最小值。

### extend Int32 <: ArbitraryRange\<Int32>

```cangjie
extend Int32 <: ArbitraryRange<Int32> {
    public static func min(): Int32 
    public static func max(): Int32 
    public static func arbitraryRange(random: RandomSource, min: Int32, max: Int32): Generator<Int32> 
}
```

功能：为 UInt32 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, Int32, Int32)

```cangjie
func arbitraryRange(random: RandomSource, min: Int32, max: Int32): Generator<Int32>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: Int32 - 可生成范围的最小值。
- max: Int32 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Int32> - 生成器。

#### func max()

```cangjie
func max(): Int32
```

功能：返回最大值。

返回值：

- Int32 - 最大值。

#### func min()

```cangjie
func min(): Int32
```

功能：返回最小值。

返回值：

- Int32 - 最小值。