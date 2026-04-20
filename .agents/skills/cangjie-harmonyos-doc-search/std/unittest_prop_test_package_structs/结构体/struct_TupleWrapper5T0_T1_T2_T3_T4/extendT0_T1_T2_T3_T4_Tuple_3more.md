### extend\<T0, T1, T2, T3, T4> TupleWrapper5\<T0, T1, T2, T3, T4> <: Arbitrary\<TupleWrapper2\<T0, T1, T2, T3, T4>> where T0 <: Arbitrary\<T0>,T1 <: Arbitrary\<T1>,T2 <: Arbitrary\<T2>,T3 <: Arbitrary\<T3>,T4 <: Arbitrary\<T4>

```cangjie
extend<T0, T1, T2, T3, T4> TupleWrapper5<T0, T1, T2, T3, T4> <: Arbitrary<TupleWrapper2<T0, T1, T2, T3, T4>> where T0 <: Arbitrary<T0>,T1 <: Arbitrary<T1>,T2 <: Arbitrary<T2>,T3 <: Arbitrary<T3>,T4 <: Arbitrary<T4>
```

功能：为 [TupleWrapper5](#struct-tuplewrapper5t0-t1-t2-t3-t4) 扩展 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实现。

父类型：

- [Arbitrary](unittest_prop_test_package_interfaces.md#interface-arbitraryt)\<[TupleWrapper2](#struct-tuplewrapper2t0-t1)\<T0, T1, T2, T3, T4>>

#### static func arbitrary(RandomSource)

```cangjie
public static func arbitrary(random: RandomSource): Generator<TupleWrapper5<T0, T1, T2, T3, T4>>
```

功能：获取生成 [TupleWrapper5](#struct-tuplewrapper5t0-t1-t2-t3-t4)\<T0, T1, T2, T3, T4> 类型随机值生成器。

返回值：

- [Generator](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\[TupleWrapper5](#struct-tuplewrapper5t0-t1-t2-t3-t4)\<T0, T1, T2, T3, T4>> - 生成器。

### extend\<T0, T1, T2, T3, T4> TupleWrapper5\<T0, T1, T2, T3, T4> <: Shrink\<TupleWrapper5\<T0, T1, T2, T3, T4>> where T0 <: Shrink\<T0>,T1 <: Shrink\<T1>,T2 <: Shrink\<T2>, T3 <: Shrink\<T3>, T4 <: Shrink\<T4>

```cangjie
extend<T0, T1, T2, T3, T4> TupleWrapper5<T0, T1, T2, T3, T4> <: Shrink<TupleWrapper5<T0, T1, T2, T3, T4>>
        where T0 <: Shrink<T0>,
              T1 <: Shrink<T1>,
              T2 <: Shrink<T2>,
              T3 <: Shrink<T3>,
              T4 <: Shrink<T4> {
    public func shrink(): Iterable<TupleWrapper5<T0, T1, T2, T3, T4>>
}
```

### func shrink()

```cangjie
override func shrink(): Iterable<TupleWrapper5<T0, T1, T2, T3, T4>>
```

功能：缩减元组。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<TupleWrapper5<T0, T1, T2, T3, T4>> -  数据迭代器。