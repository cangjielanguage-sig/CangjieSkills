### static func shrinkTuple\<T0, T1, T2, T3, T4>((T0, T1, T2, T3, T4),Iterable\<T0>,Iterable\<T1>,Iterable\<T2>,Iterable\<T3>,Iterable\<T4>)

```cangjie
public static func shrinkTuple<T0, T1, T2, T3, T4>(
    tuple: (T0, T1, T2, T3, T4),
    t0: Iterable<T0>,
    t1: Iterable<T1>,
    t2: Iterable<T2>,
    t3: Iterable<T3>,
    t4: Iterable<T4>
): Iterable<(T0, T1, T2, T3, T4)>
```

功能：实现元组的缩减迭代器。

参数：

- tuple: (T0, T1, T2, T3, T4) - 被缩减的元组。
- t0: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T0> - 第一个元组成员的缩减迭代器。
- t1: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T1> - 第二个元组成员的缩减迭代器。
- t2: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T2> - 第三个元组成员的缩减迭代器。
- t3: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T3> - 第四个元组成员的缩减迭代器。
- t4: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T4> - 第五个元组成员的缩减迭代器。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<(T0, T1, T2,T3,T4)> - 元组缩减迭代器。

### static func mix\<T>(Array<Iterable\<T>>)

```cangjie
public static func mix<T>(iterables: Array<Iterable<T>>): Iterable<T>
```

功能：将迭代器列表混合为一个迭代器。

参数：

- iterables: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T>> - 待混合的列表。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T> - 混合后的迭代器。