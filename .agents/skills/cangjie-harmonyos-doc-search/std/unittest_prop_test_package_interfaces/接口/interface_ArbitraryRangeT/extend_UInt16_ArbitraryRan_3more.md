### extend UInt16 <: ArbitraryRange\<UInt16>

```cangjie
extend UInt16 <: ArbitraryRange<UInt16> {
    public static func min(): UInt16 
    public static func max(): UInt16 
    public static func arbitraryRange(random: RandomSource, min: UInt16, max: UInt16): Generator<UInt16> 
}
```

功能：为 UInt16 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, UInt16, UInt16)

```cangjie
func arbitraryRange(random: RandomSource, min: UInt16, max: UInt16): Generator<UInt16>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: UInt16 - 可生成范围的最小值。
- max: UInt16 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UInt16> - 生成器。

#### func max()

```cangjie
func max(): UInt16
```

功能：返回最大值。

返回值：

- UInt16 - 最大值。

#### func min()

```cangjie
func min(): UInt16
```

功能：返回最小值。

返回值：

- UInt16 - 最小值。

### extend UInt32 <: ArbitraryRange\<UInt32>

```cangjie
extend UInt32 <: ArbitraryRange<UInt32> {
    public static func min(): UInt32 
    public static func max(): UInt32 
    public static func arbitraryRange(random: RandomSource, min: UInt32, max: UInt32): Generator<UInt32> 
}
```

功能：为 UInt32 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, UInt32, UInt32)

```cangjie
func arbitraryRange(random: RandomSource, min: UInt32, max: UInt32): Generator<UInt32>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: UInt32 - 可生成范围的最小值。
- max: UInt32 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UInt32> - 生成器。

#### func max()

```cangjie
func max(): UInt32
```

功能：返回最大值。

返回值：

- UInt32 - 最大值。

#### func min()

```cangjie
func min(): UInt32
```

功能：返回最小值。

返回值：

- UInt32 - 最小值。

### extend UInt64 <: ArbitraryRange\<UInt64>

```cangjie
extend UInt64 <: ArbitraryRange<UInt64> {
    public static func min(): UInt64 
    public static func max(): UInt64 
    public static func arbitraryRange(random: RandomSource, min: UInt64, max: UInt64): Generator<UInt64> 
}
```

功能：为 UInt64 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, UInt64, UInt64)

```cangjie
func arbitraryRange(random: RandomSource, min: UInt64, max: UInt64): Generator<UInt64>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: UInt64 - 可生成范围的最小值。
- max: UInt64 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UInt64> - 生成器。

#### func max()

```cangjie
func max(): UInt64
```

功能：返回最大值。

返回值：

- UInt64 - 最大值。

#### func min()

```cangjie
func min(): UInt64
```

功能：返回最小值。

返回值：

- UInt64 - 最小值。