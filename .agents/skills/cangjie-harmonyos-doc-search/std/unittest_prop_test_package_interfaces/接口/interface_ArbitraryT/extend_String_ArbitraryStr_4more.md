### extend String <: Arbitrary\<String>

```cangjie
extend String <: Arbitrary<String>
```

功能：为 [String](../../core/core_package_api/core_package_structs.md#struct-string) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<String>
```

功能：获取生成 String 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<String> - 生成 String 类型随机值生成器。

### extend UInt16 <: Arbitrary\<UInt16>

```cangjie
extend UInt16 <: Arbitrary<UInt16>
```

功能：为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<UInt16>
```

功能：获取生成 UInt16 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UInt16> - 生成 UInt16 类型随机值生成器。

### extend UInt32 <: Arbitrary\<UInt32>

```cangjie
extend UInt32 <: Arbitrary<UInt32>
```

功能：为 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<UInt32>
```

功能：获取生成 UInt32 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UInt32> - 生成 UInt32 类型随机值生成器。

### extend UInt64 <: Arbitrary\<UInt64>

```cangjie
extend UInt64 <: Arbitrary<UInt64>
```

功能：为 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<UInt64>
```

功能：获取生成 UInt64 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UInt64> - 生成 UInt64 类型随机值生成器。