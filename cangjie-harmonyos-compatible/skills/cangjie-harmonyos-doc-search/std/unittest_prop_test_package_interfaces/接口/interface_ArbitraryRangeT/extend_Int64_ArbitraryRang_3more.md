### extend Int64 <: ArbitraryRange\<Int64>

```cangjie
extend Int64 <: ArbitraryRange<Int64> {
    public static func min(): Int64 
    public static func max(): Int64 
    public static func arbitraryRange(random: RandomSource, min: Int64, max: Int64): Generator<Int64> 
}
```

功能：为 Int64 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, Int64, Int64)

```cangjie
func arbitraryRange(random: RandomSource, min: Int64, max: Int64): Generator<Int64>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: Int64 - 可生成范围的最小值。
- max: Int64 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Int64> - 生成器。

#### func max()

```cangjie
func max(): Int64
```

功能：返回最大值。

返回值：

- Int64 - 最大值。

#### func min()

```cangjie
func min(): Int64
```

功能：返回最小值。

返回值：

- Int64 - 最小值。

### extend Int8 <: ArbitraryRange\<Int8>

```cangjie
extend Int8 <: ArbitraryRange<Int8> {
    public static func min(): Int8 
    public static func max(): Int8 
    public static func arbitraryRange(random: RandomSource, min: Int8, max: Int8): Generator<Int8> 
}
```

功能：为 Int8 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, Int8, Int8)

```cangjie
func arbitraryRange(random: RandomSource, min: Int8, max: Int8): Generator<Int8>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: Int8 - 可生成范围的最小值。
- max: Int8 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Int8> - 生成器。

#### func max()

```cangjie
func max(): Int8
```

功能：返回最大值。

返回值：

- Int8 - 最大值。

#### func min()

```cangjie
func min(): Int8
```

功能：返回最小值。

返回值：

- Int8 - 最小值。

### extend IntNative <: ArbitraryRange\<IntNative>

```cangjie
extend IntNative <: ArbitraryRange<IntNative> {
    public static func min(): IntNative 
    public static func max(): IntNative 
    public static func arbitraryRange(random: RandomSource, min: IntNative, max: IntNative): Generator<IntNative> 
}
```

功能：为 IntNative 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, IntNative, IntNative)

```cangjie
func arbitraryRange(random: RandomSource, min: IntNative, max: IntNative): Generator<IntNative>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: IntNative - 可生成范围的最小值。
- max: IntNative - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<IntNative> - 生成器。

#### func max()

```cangjie
func max(): IntNative
```

功能：返回最大值。

返回值：

- IntNative - 最大值。

#### func min()

```cangjie
func min(): IntNative
```

功能：返回最小值。

返回值：

- IntNative - 最小值。