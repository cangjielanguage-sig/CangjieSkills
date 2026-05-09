### extend\<T0, T1> TupleWrapper2\<T0, T1> <: Arbitrary\<TupleWrapper2\<T0, T1>> where T0 <: Arbitrary\<T0>,T1 <: Arbitrary\<T1>

```cangjie
extend<T0, T1> TupleWrapper2<T0, T1> <: Arbitrary<TupleWrapper2<T0, T1>> where T0 <: Arbitrary<T0>,T1 <: Arbitrary<T1>
```

功能：为 [TupleWrapper2](#struct-tuplewrapper2t0-t1) 扩展 [Arbitrary](./unittest_prop_test_package_interfaces.md#interface-arbitraryt) 实现。

父类型：

- [Arbitrary](unittest_prop_test_package_interfaces.md#interface-arbitraryt)\<[TupleWrapper2](#struct-tuplewrapper2t0-t1)\<T0, T1>>

#### static func arbitrary(RandomSource)

```cangjie
public static func arbitrary(random: RandomSource): Generator<TupleWrapper2<T0, T1>>
```

功能：获取生成 [TupleWrapper2](#struct-tuplewrapper2t0-t1)\<T0, T1> 类型随机值生成器。

返回值：

- [Generator](../unittest_prop_test_package_api/unittest_prop_test_package_interfaces.md#interface-generatort)\<[TupleWrapper2](#struct-tuplewrapper2t0-t1)\<T0, T1>> - 生成器。

### extend\<T0, T1> TupleWrapper2\<T0, T1> <: Shrink\<TupleWrapper2\<T0, T1>> where T0 <: Shrink\<T0>,T1 <: Shrink\<T1>

```cangjie
extend<T0, T1> TupleWrapper2<T0, T1> <: Shrink<TupleWrapper2<T0, T1>>
        where T0 <: Shrink<T0>,
              T1 <: Shrink<T1> {
    public func shrink(): Iterable<TupleWrapper2<T0, T1>>
}
```

#### func shrink()

```cangjie
override func shrink(): Iterable<TupleWrapper2<T0, T1>>
```

功能：缩减元组。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<TupleWrapper2<T0, T1> - 数据迭代器。