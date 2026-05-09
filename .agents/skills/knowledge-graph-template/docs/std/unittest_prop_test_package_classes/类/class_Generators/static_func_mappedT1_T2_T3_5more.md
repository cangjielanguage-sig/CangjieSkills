### static func mapped\<T1, T2, T3, R>(RandomSource, (T1, T2, T3) -> R)

```cangjie
public static func mapped<T1, T2, T3, R>(random: RandomSource, body: (T1, T2, T3) -> R): Generator<R>
            where T1 <: Arbitrary<T1>, T2 <: Arbitrary<T2>, T3 <: Arbitrary<T3>
```

功能：获取 T1,T2,T3 的 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实例提供的生成器，并使用函数体生成 R 类型的值。

参数：

- random: [RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。
- body: (T1, T2,T3) -> R - 生成 R 类型的值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<R> - 生成器。

### static func mapped\<T1, T2, T3, T4, R>(RandomSource, (T1, T2, T3, T4) -> R)

```cangjie
public static func mapped<T1, T2, T3, T4, R>(random: RandomSource, body: (T1, T2, T3, T4) -> R): Generator<R>
            where T1 <: Arbitrary<T1>, T2 <: Arbitrary<T2>, T3 <: Arbitrary<T3>, T4 <: Arbitrary<T4>
```

功能：获取 T1,T2,T3,T4 的 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实例提供的生成器，并使用函数体生成 R 类型的值。

参数：

- random: [RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。
- body: (T1, T2,T3,T4) -> R - 生成 R 类型的值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<R> - 生成器。

### static func pick\<T>(RandomSource, Array\<Generator\<T>>)

```cangjie
public static func pick<T>(random: RandomSource, variants: Array<Generator<T>>): Generator<T>
```

功能：通过从生成器数组中随机选取来生成值的生成器。

参数：

- random: [RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。
- variants: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T>> - 生成器数组。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成器。

### static func single\<T>(T)

```cangjie
public static func single<T>(value: T): Generator<T>
```

功能：生成器始终返回同一个值。

参数：

- value: T - 生成器返回的值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成器。

### static func weighted\<T>(RandomSource, Array\<(UInt64, Generator\<T>)>)

```cangjie
public static func weighted<T>(random: RandomSource, variants: Array<(UInt64, Generator<T>)>): Generator<T>
```

功能：通过从成对数组（权重、生成器）中随机选取来生成值的生成器。

参数：

- random: [RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。
- variants: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<(UInt64, Generator\<T>)> - 数组（权重、生成器）。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成器。