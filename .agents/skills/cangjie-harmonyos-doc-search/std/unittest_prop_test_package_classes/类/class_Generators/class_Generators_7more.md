## class Generators

```cangjie
public class Generators {}
```

功能：包含辅助函数的类，可帮助开发人员编写自己的生成器。

### static func generate\<T>(T, T, (T, T) -> T)

```cangjie
public static func generate<T>(l: T, r: T, body: (T, T) -> T): Generator<T>
```

功能：通过重复调用函数生成值的生成器，范围为 [l, r]。

参数：

- l: T - 最小值。
- r: T - 最大值。
- body: () -> T - 被调用的生成器闭包。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成器。

### static func generate\<T>(() -> T)

```cangjie
public static func generate<T>(body: () -> T): Generator<T>
```

功能：通过重复调用函数生成值的生成器。

参数：

- body: () -> T - 被调用的生成器闭包。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成器。

### static func iterable\<T>(RandomSource, Array\<T>)

```cangjie
public static func iterable<T>(random: RandomSource, collection: Array<T>): Generator<T>
```

功能：通过从数组中随机选取来生成值的生成器。

参数：

- random: [RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。
- collection: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 被选取数字的数组。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成器。

### static func lookup\<T>(RandomSource)

```cangjie
public static func lookup<T>(random: RandomSource): Generator<T> where T <: Arbitrary<T>
```

功能：通过 T 的 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实例提供的生成器。

参数：

- random: [RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<T> - 生成器。

### static func mapped\<T, R>(RandomSource,(T) -> R)

```cangjie
public static func mapped<T, R>(random: RandomSource, body: (T) -> R): Generator<R> where T <: Arbitrary<T>
```

功能：获取 T 的 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实例提供的生成器，并使用函数体生成 R 类型的值。

参数：

- random: [RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。
- body: (T) -> R - 生成 R 类型的值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<R> - 生成器。

### static func mapped\<T1, T2, R>(RandomSource, (T1, T2) -> R)

```cangjie
 public static func mapped<T1, T2, R>(random: RandomSource, body: (T1, T2) -> R): Generator<R> where T1 <: Arbitrary<T1>, T2 <: Arbitrary<T2>
```

功能：获取 T1，T2 的 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实例提供的生成器，并使用函数体生成 R 类型的值。

参数：

- random: [RandomSource](./unittest_prop_test_package_interfaces.md#interface-randomsource) - 随机数。
- body: (T1, T2) -> R - 生成 R 类型的值。

返回值：

- [Generator](../../unittest_prop_test/unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<R> - 生成器。