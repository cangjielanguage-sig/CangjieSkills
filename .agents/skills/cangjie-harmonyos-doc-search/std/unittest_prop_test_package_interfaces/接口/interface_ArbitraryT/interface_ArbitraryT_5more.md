## interface Arbitrary\<T>

```cangjie
public interface Arbitrary<T> {
    static func arbitrary(random: RandomSource): Generator<T>
}
```

功能：生成 T 类型随机值的接口。

### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<T>
```

功能：获取生成 T 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成 T 类型随机值生成器。

### extend Bool <: Arbitrary\<Bool>

```cangjie
extend Bool <: Arbitrary<Bool>
```

功能：为 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Bool>
```

功能：获取生成 T 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Bool> - 生成 Bool 类型随机值生成器。

### extend Float16 <: Arbitrary\<Float16>

```cangjie
extend Float16 <: Arbitrary<Float16>
```

功能：为 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Float16>
```

功能：获取生成 T 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Float16> - 生成 Float16 类型随机值生成器。

### extend Float32 <: Arbitrary\<Float32>

```cangjie
extend Float32 <: Arbitrary<Float32>
```

功能：为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 实现了 [Arbitrary](#interface-arbitraryt)\<T> 接口。

父类型：

- [Arbitrary](#interface-arbitraryt)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)>

#### static func arbitrary(RandomSource)

```cangjie
static func arbitrary(random: RandomSource): Generator<Float32>
```

功能：获取生成 T 类型随机值生成器。

参数：

- random: [RandomSource](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<Float32> - 生成 Float32 类型随机值生成器。