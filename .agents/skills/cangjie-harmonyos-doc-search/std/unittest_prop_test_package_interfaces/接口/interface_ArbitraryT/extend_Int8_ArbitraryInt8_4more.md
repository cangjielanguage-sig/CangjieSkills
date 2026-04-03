### extend Int8 <: Arbitrary\<Int8>

```cangjie
extend Int8 <: Arbitrary<Int8>
```

功能：为 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Int8>
```

功能：获取生成 Int8 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Int8> - 生成 Int8 类型随机值生成器。

### extend IntNative <: Arbitrary\<IntNative>

```cangjie
extend IntNative <: Arbitrary<IntNative>
```

功能：为 [IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[IntNative](../../core/core_package_api/core_package_intrinsics.md#intnative)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<IntNative>
```

功能：获取生成 IntNative 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<IntNative> - 生成 IntNative 类型随机值生成器。

### extend Ordering <: Arbitrary\<Ordering>

```cangjie
extend Ordering <: Arbitrary<Ordering>
```

功能：为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Ordering>
```

功能：获取生成 Ordering 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Ordering> - 生成 Ordering 类型随机值生成器。

### extend Rune <: Arbitrary\<Rune>

```cangjie
extend Rune <: Arbitrary<Rune>
```

功能：为 [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Rune>
```

功能：获取生成 Rune 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Rune> - 生成 Rune 类型随机值生成器。