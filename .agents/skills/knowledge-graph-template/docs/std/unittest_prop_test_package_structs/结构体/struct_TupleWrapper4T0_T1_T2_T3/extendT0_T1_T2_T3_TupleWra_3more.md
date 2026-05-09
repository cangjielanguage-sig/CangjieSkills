### extend\<T0, T1, T2, T3> TupleWrapper4\<T0, T1, T2, T3><: Arbitrary\<TupleWrapper4\<T0, T1, T2, T3>> where where T0 <: Arbitrary\<T0>,T1 <: Arbitrary\<T1>,T2 <: Arbitrary\<T2>,T3 <: Arbitrary\<T3>

```cangjie
extend<T0, T1, T2, T3> TupleWrapper4<T0, T1, T2, T3><: Arbitrary<TupleWrapper4<T0, T1, T2, T3>> where where T0 <: Arbitrary<T0>,T1 <: Arbitrary<T1>,T2 <: Arbitrary<T2>,T3 <: Arbitrary<T3>
```

功能：为 [TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3) 扩展 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实现。

父类型：

- [Arbitrary](unittest_prop_test_package_interfaces.md#interface-arbitraryt)\<[TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3)\<T0, T1, T2, T3>>

#### static func arbitrary(RandomSource)

```cangjie
public static func arbitrary(random: RandomSource): Generator<TupleWrapper2<T0, T1, T2, T3>>
```

功能：获取生成 [TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3)\<T0, T1, T2, T3> 类型随机值生成器。

返回值：

- [Generator](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<[TupleWrapper4](#struct-tuplewrapper4t0-t1-t2-t3)\<T0, T1, T2, T3>> - 生成器。

### extend\<T0, T1, T2, T3> TupleWrapper4\<T0, T1, T2, T3> <: Shrink\<TupleWrapper4\<T0, T1, T2, T3>> where T0 <: Shrink\<T0>,T1 <: Shrink\<T1>,T2 <: Shrink\<T2>, T3 <: Shrink\<T3>

```cangjie
extend<T0, T1, T2, T3> TupleWrapper4<T0, T1, T2, T3> <: Shrink<TupleWrapper4<T0, T1, T2, T3>>
        where T0 <: Shrink<T0>,
              T1 <: Shrink<T1>,
              T2 <: Shrink<T2>,
              T3 <: Shrink<T3> {
    public func shrink(): Iterable<TupleWrapper4<T0, T1, T2, T3>>
}
```

### func shrink()

```cangjie
override func shrink(): Iterable<TupleWrapper4<T0, T1, T2, T3>>
```

功能：缩减元组。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<TupleWrapper4<T0, T1, T2, T3>> -  数据迭代器。