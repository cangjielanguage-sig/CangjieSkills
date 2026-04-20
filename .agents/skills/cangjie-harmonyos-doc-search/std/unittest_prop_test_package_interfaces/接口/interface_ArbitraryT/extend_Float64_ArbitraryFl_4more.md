### extend Float64 <: Arbitrary\<Float64>

```cangjie
extend Float64 <: Arbitrary<Float64>
```

功能：为 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Float64](../../core/core_package_api/core_package_intrinsics.md#float64)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Float64>
```

功能：获取生成 T 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Float64> - 生成 Float64 类型随机值生成器。

### extend Int16 <: Arbitrary\<Int16>

```cangjie
extend Int16 <: Arbitrary<Int16>
```

功能：为 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Int16>
```

功能：获取生成 T 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Int16> - 生成 Int16 类型随机值生成器。

### extend Int32 <: Arbitrary\<Int32>

```cangjie
extend Int32 <: Arbitrary<Int32>
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Int32>
```

功能：获取生成 T 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Int32> - 生成 Int32 类型随机值生成器。

### extend Int64 <: Arbitrary\<Int64>

```cangjie
extend Int64 <: Arbitrary<Int64>
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Int64>
```

功能：获取生成 Int64 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Int64> - 生成 Int64 类型随机值生成器。