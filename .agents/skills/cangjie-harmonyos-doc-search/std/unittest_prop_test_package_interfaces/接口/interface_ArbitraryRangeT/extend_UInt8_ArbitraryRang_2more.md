### extend UInt8 <: ArbitraryRange\<UInt8>

```cangjie
extend UInt8 <: ArbitraryRange<UInt8> {
    public static func min(): UInt8 
    public static func max(): UInt8 
    public static func arbitraryRange(random: RandomSource, min: UInt8, max: UInt8): Generator<UInt8> 
}
```

功能：为 UInt8 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, UInt8, UInt8)

```cangjie
func arbitraryRange(random: RandomSource, min: UInt8, max: UInt8): Generator<UInt8>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: UInt8 - 可生成范围的最小值。
- max: UInt8 - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UInt8> - 生成器。

#### func max()

```cangjie
func max(): UInt8
```

功能：返回最大值。

返回值：

- UInt8 - 最大值。

#### func min()

```cangjie
func min(): UInt8
```

功能：返回最小值。

返回值：

- UInt8 - 最小值。

### extend UIntNative <: ArbitraryRange\<UIntNative>

```cangjie
extend UIntNative <: ArbitraryRange<UIntNative> {
    public static func min(): UIntNative 
    public static func max(): UIntNative 
    public static func arbitraryRange(random: RandomSource, min: UIntNative, max: UIntNative): Generator<UIntNative> 
}
```

功能：为 UIntNative 类型实现的可以在一定范围内生成值的方法。

#### func arbitraryRange(RandomSource, UIntNative, UIntNative)

```cangjie
func arbitraryRange(random: RandomSource, min: UIntNative, max: UIntNative): Generator<UIntNative>
```

功能：返回在范围内生成的值。

参数：

- random:[RandomSource](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数源。
- min: UIntNative - 可生成范围的最小值。
- max: UIntNative - 可生成范围的最大值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UIntNative> - 生成器。

#### func max()

```cangjie
func max(): UIntNative
```

功能：返回最大值。

返回值：

- UIntNative - 最大值。

#### func min()

```cangjie
func min(): UIntNative
```

功能：返回最小值。

返回值：

- UIntNative - 最小值。