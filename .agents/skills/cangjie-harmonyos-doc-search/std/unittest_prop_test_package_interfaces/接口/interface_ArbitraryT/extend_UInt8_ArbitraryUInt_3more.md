### extend UInt8 <: Arbitrary\<UInt8>

```cangjie
extend UInt8 <: Arbitrary<UInt8>
```

功能：为 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<UInt8>
```

功能：获取生成 UInt8 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UInt8> - 生成 UInt8 类型随机值生成器。

### extend UIntNative <: Arbitrary\<UIntNative>

```cangjie
extend UIntNative <: Arbitrary<UIntNative>
```

功能：为 [UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[UIntNative](../../core/core_package_api/core_package_intrinsics.md#uintnative)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<UIntNative>
```

功能：获取生成 UIntNative 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<UIntNative> - 生成 UIntNative 类型随机值生成器。

### extend Unit <: Arbitrary\<Unit>

```cangjie
extend Unit <: Arbitrary<Unit>
```

功能：为 [Unit](../../core/core_package_api/core_package_intrinsics.md#unit) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Unit](../../core/core_package_api/core_package_intrinsics.md#unit)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Unit>
```

功能：获取生成 Unit 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Unit> - 生成 Unit 类型随机值生成器。