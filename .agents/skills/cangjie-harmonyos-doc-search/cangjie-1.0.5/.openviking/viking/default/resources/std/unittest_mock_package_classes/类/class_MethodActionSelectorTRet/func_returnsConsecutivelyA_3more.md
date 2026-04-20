### func returnsConsecutively(ArrayList\<TRet>)

```cangjie
func returnsConsecutively(values: ArrayList<TRet>): Continuation<MethodActionSelector<TRet>>
```

功能：定义桩签名按列表顺序返回指定的值的行为。桩签名将被连续调用多次，次数与数组列表内值的个数相同。

参数：

- values: [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<TRet> - 桩签名的返回值列表。

返回值：

- [Continuation](#class-continuationa)\<[MethodActionSelector](#class-methodactionselectortret)\<TRet>> - 定义了桩签名按序返回指定值的 [Continuation](#class-continuationa)\<TRet> 对象实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数列表为空时，抛出异常。

### func throws(() -> Exception)

```cangjie
func throws(exceptionFactory: () -> Exception): CardinalitySelector<MethodActionSelector<TRet>>
```

功能：定义桩签名抛出异常的行为，异常由参数闭包函数生成。

> **说明：**
>
> throws vs fails
>
> throws 意味着测试桩签名抛出异常后的行为是测试的目的。例如，当某些服务不可用时，系统是否可以正确恢复等。
> fails 意味着调用桩签名将导致测试失败。即，如果系统行为正确，则永远不应调用该桩签名。

参数：

- exceptionFactory: () ->[Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 构造预期桩签名抛出的异常对象的闭包函数（生成器）。

返回值：

- [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<[MethodActionSelector](unittest_mock_package_classes.md#class-methodactionselectortret)\<TRet>> - 定义了桩签名抛出异常行为的 [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<R> 对象实例。

### func throws(Exception)

```cangjie
func throws(exception: Exception): CardinalitySelector<MethodActionSelector<TRet>>
```

功能：定义桩签名抛出异常的行为。

参数：

- exception: [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 预期桩签名抛出的异常对象。

返回值：

- [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<[MethodActionSelector](unittest_mock_package_classes.md#class-methodactionselectortret)\<TRet>>  - 定义了桩签名抛出异常的行为的 [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<R> 对象实例。