## class ShrinkHelpers

```cangjie
public class ShrinkHelpers {}
```

功能：提供对元组实现缩减迭代器的方法。

### static func shrinkTuple\<T0, T1>((T0, T1),Iterable\<T0>,Iterable\<T1>)

```cangjie
public static func shrinkTuple<T0, T1>(
    tuple: (T0, T1),
    t0: Iterable<T0>,
    t1: Iterable<T1>
): Iterable<(T0, T1)>
```

功能：实现元组的缩减迭代器。

参数：

- tuple: (T0, T1) - 被缩减的元组。
- t0: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T0> - 第一个元组成员的缩减迭代器。
- t1: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T1> - 第二个元组成员的缩减迭代器。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<(T0, T1)> - 元组缩减迭代器。

### static func shrinkTuple\<T0, T1, T2>((T0, T1, T2),Iterable\<T0>,Iterable\<T1>,Iterable\<T2>)

```cangjie
public static func shrinkTuple<T0, T1, T2>(
    tuple: (T0, T1, T2),
    t0: Iterable<T0>,
    t1: Iterable<T1>,
    t2: Iterable<T2>
): Iterable<(T0, T1, T2)>
```

功能：实现元组的缩减迭代器。

参数：

- tuple: (T0, T1, T2) - 被缩减的元组。
- t0: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T0> - 第一个元组成员的缩减迭代器。
- t1: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T1> - 第二个元组成员的缩减迭代器。
- t2: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T2> - 第三个元组成员的缩减迭代器。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<(T0, T1, T2)> - 元组缩减迭代器。

### static func shrinkTuple\<T0, T1, T2, T3>((T0, T1, T2, T3),Iterable\<T0>,Iterable\<T1>,Iterable\<T2>,Iterable\<T3>)

```cangjie
public static func shrinkTuple<T0, T1, T2, T3>(
    tuple: (T0, T1, T2, T3),
    t0: Iterable<T0>,
    t1: Iterable<T1>,
    t2: Iterable<T2>,
    t3: Iterable<T3>
): Iterable<(T0, T1, T2, T3)>
```

功能：实现元组的缩减迭代器。

参数：

- tuple: (T0, T1, T2, T3) - 被缩减的元组。
- t0: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T0> - 第一个元组成员的缩减迭代器。
- t1: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T1> - 第二个元组成员的缩减迭代器。
- t2: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T2> - 第三个元组成员的缩减迭代器。
- t3: [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<T3> - 第四个元组成员的缩减迭代器。

返回值：

- [Iterable](../../core/core_package_api/core_package_interfaces.md#interface-iterablee)\<(T0, T1, T2,T3)> - 元组缩减迭代器。