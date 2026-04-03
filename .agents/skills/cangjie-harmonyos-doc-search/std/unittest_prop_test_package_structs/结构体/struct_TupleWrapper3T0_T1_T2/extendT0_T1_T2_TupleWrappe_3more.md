### extend\<T0, T1, T2> TupleWrapper3\<T0, T1, T2> <: Arbitrary\<TupleWrapper3\<T0, T1, T2>>  where T0 <: Arbitrary\<T0>,T1 <: Arbitrary\<T1>,T2 <: Arbitrary\<T2>

```cangjie
extend<T0, T1, T2> TupleWrapper3<T0, T1, T2> <: Arbitrary<TupleWrapper3<T0, T1, T2>>  where T0 <: Arbitrary<T0>,T1 <: Arbitrary<T1>,T2 <: Arbitrary<T2>
```

功能：为 [TupleWrapper3](#struct-tuplewrapper3t0-t1-t2) 扩展 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实现。

父类型：

- [Arbitrary](unittest_prop_test_package_interfaces.md#interface-arbitraryt)\<[TupleWrapper3](#struct-tuplewrapper3t0-t1-t2)\<T0, T1, T2>>

#### static func arbitrary(RandomSource)

```cangjie
public static func arbitrary(random: RandomSource): Generator<TupleWrapper3<T0, T1, T2>>
```

功能：获取生成 [TupleWrapper3](#struct-tuplewrapper3t0-t1-t2)\<T0, T1, T2> 类型随机值生成器。

返回值：

- [Generator](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<[TupleWrapper3](#struct-tuplewrapper3t0-t1-t2)\<T0, T1, T2>> - 生成器。

### extend\<T0, T1, T2> TupleWrapper3\<T0, T1, T2> <: Shrink\<TupleWrapper3\<T0, T1, T2>> where T0 <: Shrink\<T0>,T1 <: Shrink\<T1>,T2 <: Shrink\<T2>

```cangjie
extend<T0, T1, T2> TupleWrapper3<T0, T1, T2> <: Shrink<TupleWrapper3<T0, T1, T2>>
        where T0 <: Shrink<T0>,
              T1 <: Shrink<T1>,
              T2 <: Shrink<T2> {
    public func shrink(): Iterable<TupleWrapper3<T0, T1, T2>>
}
```

### func shrink()

```cangjie
override func shrink(): Iterable<TupleWrapper3<T0, T1, T2>>
```

功能：缩减元组。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<TupleWrapper3<T0, T1, T2> -  数据迭代器。