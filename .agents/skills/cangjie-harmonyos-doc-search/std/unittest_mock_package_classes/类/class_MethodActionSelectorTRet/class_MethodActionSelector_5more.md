## class MethodActionSelector\<TRet>

```cangjie
public class MethodActionSelector<TRet> <: ActionSelector {}
```

功能：此类提供了为成员函数指定一个[操作 API](../unittest_mock_samples/mock_framework_basics.md#操作-api) ，并允许链式调用。
入参为 `mock object` 或 `spy object` 的某个成员函数的调用表达式的 `@On` 宏调用表达式，将返回 [ActionSelector](#class-actionselector)\<TRet> 的实例（其中 `TRet` 代表正在配置的函数成员的返回值类型）。
即，此类中的 API 可为成员函数插入桩代码。

父类型：

- [ActionSelector](#class-actionselector)

### func callsOriginal()

```cangjie
func callsOriginal(): CardinalitySelector<MethodActionSelector<TRet>>
```

功能：定义桩签名执行原始代码逻辑的行为。

返回值：

- [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<[MethodActionSelector](#class-methodactionselectortret)\<TRet>> - 定义了桩签名执行原始代码逻辑的 [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<TRet> 对象实例。

### func returns(() -> TRet)

```cangjie
func returns(valueFactory: () -> TRet): CardinalitySelector<MethodActionSelector<TRet>>
```

功能：定义桩签名返回指定的值的行为，该值由传入的闭包生成。

参数：

- valueFactory: () -> TRet - 生成预期返回值的闭包函数（生成器）。

返回值：

- [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<[MethodActionSelector](#class-methodactionselectortret)\<TRet>> - 定义了桩签名返回指定值的行为的 [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<TRet> 对象实例。

### func returns(TRet)

```cangjie
func returns(value: TRet): CardinalitySelector<MethodActionSelector<TRet>>
```

功能：定义[桩签名](../unittest_mock_samples/mock_framework_basics.md#桩签名)返回指定值的行为。

参数：

- value: TRet - 预期桩签名的返回值。

返回值：

- [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<[MethodActionSelector](#class-methodactionselectortret)\<TRet>> - 定义了桩签名返回行为的 [CardinalitySelector](unittest_mock_package_classes.md#class-cardinalityselectora)\<TRet> 对象实例。

### func returnsConsecutively(Array\<TRet>)

```cangjie
func returnsConsecutively(values: Array<TRet>): Continuation<MethodActionSelector<TRet>>
```

功能：定义桩签名按列表顺序返回指定的值的行为。桩签名将被调用多次，次数与数组内值的个数相同。

参数：

- values: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<TRet> - 桩签名的返回值列表。

返回值：

- [Continuation](#class-continuationa)\<[MethodActionSelector](#class-methodactionselectortret)\<TRet>> - 定义了桩签名按序返回指定值的行为的 [Continuation](#class-continuationa)\<TRet>  对象实例。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当参数列表为空时，抛出异常。