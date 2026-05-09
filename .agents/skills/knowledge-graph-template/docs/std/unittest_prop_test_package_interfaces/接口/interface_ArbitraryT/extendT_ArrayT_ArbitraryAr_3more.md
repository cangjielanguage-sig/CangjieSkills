### extend\<T> Array\<T> <: Arbitrary\<Array\<T>> where T <: Arbitrary\<T>

```cangjie
extend<T> Array<T> <: Arbitrary<Array<T>> where T <: Arbitrary<T>
```

功能：为 [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> 实现了 [Arbitrary](#interface-arbitraryt)\<[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T>> 接口，且 T 需实现 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T>>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Array<T>>
```

功能：获取生成 Array\<T> 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Array\<T>> - 生成 Array\<T> 类型随机值生成器。

### extend\<T> Option\<T> <: Arbitrary\<Option\<T>> where T <: Arbitrary\<T>

```cangjie
extend<T> option<T> <: Arbitrary<Option<T>> where T <: Arbitrary<T>
```

功能：为 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>  实现了 [Arbitrary](#interface-arbitraryt)\<[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>> 接口，且 T 需实现 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Option<T>>
```

功能：获取生成 option\<T> 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Option\<T>> - 生成 option\<T> 类型随机值生成器。

### extend\<T> ArrayList\<T> <: Arbitrary\<ArrayList\<T>> where T <: Arbitrary\<T>

```cangjie
extend<T> ArrayList<T> <: Arbitrary<ArrayList<T>> where T <: Arbitrary<T> 
```

功能：为 [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T>  实现了 [Arbitrary](#interface-arbitraryt) 接口，且 T 需实现 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T>>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<ArrayList<T>>
```

功能：获取生成 ArrayList\<T> 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<ArrayList\<T>> - 生成 ArrayList\<T> 类型随机值生成器。