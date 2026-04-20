## interface ArbitraryRange\<T>

```cangjie
public interface ArbitraryRange<T> where T <: Arbitrary<T> & Comparable<T> {
    static func min(): T
    static func max(): T
    static func arbitraryRange(random: RandomSource, min: T, max: T): Generator<T>
}
```

功能：接口为不同类型提供可以在一定范围内生成值的方法。

### func arbitraryRange(RandomSource, T, T)

```cangjie
func arbitraryRange(random: RandomSource, min: T, max: T): Generator<T>
```

功能：返回在范围内生成的值。

参数：

- random: [RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: T - 可生成范围的最小值。
- max: T - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成器。

### func max()

```cangjie
func max(): T
```

功能：返回最大值。

返回值：

- T - 最大值。

### func min()

```cangjie
func min(): T
```

功能：返回最小值。

返回值：

- T - 最小值。

### extend Float16 <: ArbitraryRange\<Float16>

```cangjie
extend Float16 <: ArbitraryRange<Float16> {
    public static func min(): Float16
    public static func max(): Float16
    public static func arbitraryRange(random: RandomSource, min: Float16, max: Float16): Generator<Float16>
}
```

功能：为 Float16 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, Float16, Float16)

```cangjie
func arbitraryRange(random: RandomSource, min: Float16, max: Float16): Generator<Float16>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: Float16 - 可生成范围的最小值。
- max: Float16 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Float16> - 生成器。

#### func max()

```cangjie
func max(): Float16
```

功能：返回最大值。

返回值：

- Float16 - 最大值。

#### func min()

```cangjie
func min(): Float16
```

功能：返回最小值。

返回值：

- Float16 - 最小值。

### extend Float32 <: ArbitraryRange\<Float32>

```cangjie
extend Float32 <: ArbitraryRange<Float32> {
    public static func min(): Float32 
    public static func max(): Float32 
    public static func arbitraryRange(random: RandomSource, min: Float32, max: Float32): Generator<Float32> 
}
```

功能：为 Float32 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, Float32, Float32)

```cangjie
func arbitraryRange(random: RandomSource, min: Float32, max: Float32): c<Float32>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: Float32 - 可生成范围的最小值。
- max: Float32 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Float32> - 生成器。

#### func max()

```cangjie
func max(): Float32
```

功能：返回最大值。

返回值：

- Float32 - 最大值。

#### func min()

```cangjie
func min(): Float32
```

功能：返回最小值。

返回值：

- Float32 - 最小值。