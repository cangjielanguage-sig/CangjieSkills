## class GetterActionSelector\<TRet>

```cangjie
public class GetterActionSelector<TRet> <: ActionSelector {}
```

功能：此类提供了为属性 `Getter` 函数指定一个[操作 API](../unittest_mock_samples/mock_framework_basics.md#操作-api) ，并允许链式调用的方法。
入参为 `mock object` 或 `spy object` 的某个成员函数的调用表达式的 `@On` 宏调用表达式，将返回 [ActionSelector](#class-actionselector) 的实例。即，此类或其子类中的 API 可为成员函数插入桩代码。

父类型：

- [ActionSelector](#class-actionselector)

### func getsField(SyntheticField\<TRet>)

```cangjie
public func getsField(field: SyntheticField<TRet>): CardinalitySelector<GetterActionSelector<TRet>>
```

功能：读取[合成字段](../unittest_mock_samples/mock_framework_stubs.md#设置属性和字段和顶层变量)。

参数：

- field: [SyntheticField](#class-syntheticfieldt)\<TRet> - 合成字段，处理可变属性。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[GetterActionSelector](#class-getteractionselectortret)\<TRet>> - 预期执行次数的操作器。

### func getsOriginal()

```cangjie
public func getsOriginal(): CardinalitySelector<GetterActionSelector<TRet>>
```

功能：读取原始属性或获取原始实例中的字段值。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[GetterActionSelector](#class-getteractionselectortret)\<TRet>> - 预期执行次数的操作器。

### func returns(TRet)

```cangjie
public func returns(value: TRet): CardinalitySelector<GetterActionSelector<TRet>>
```

功能：指定返回值。

参数：

- value: TRet - 指定的返回的值。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[GetterActionSelector](#class-getteractionselectortret)\<TRet>> - 预期执行次数的操作器。

### func returns(() -> TRet)

```cangjie
public func returns(valueFactory: () -> TRet): CardinalitySelector<GetterActionSelector<TRet>>
```

功能：指定返回值。

参数：

- valueFactory: () -> TRet - 指定的返回的值生成器。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[GetterActionSelector](#class-getteractionselectortret)\<TRet>> - 预期执行次数的操作器。

### func returnsConsecutively(Array\<TRet>)

```cangjie
public func returnsConsecutively(values: Array<TRet>): Continuation<GetterActionSelector<TRet>>
```

功能：指定返回多个值。

参数：

- values: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<TRet> - 指定的返回的多个值。

返回值：

- [Continuation](#class-continuationa)\<[GetterActionSelector](#class-getteractionselectortret)\<TRet>> - 预期执行次数的操作器。

### func returnsConsecutively(ArrayList\<TRet>)

```cangjie
public func returnsConsecutively(values: ArrayList<TRet>): Continuation<GetterActionSelector<TRet>>
```

功能：指定返回多个值。

参数：

- values: [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<TRet> - 指定的返回的多个值。

返回值：

- [Continuation](#class-continuationa)\<[GetterActionSelector](#class-getteractionselectortret)\<TRet>> - 预期执行次数的操作器。

### func throws(Exception)

```cangjie
public func throws(exception: Exception): CardinalitySelector<GetterActionSelector<TRet>>
```

功能：指定抛出异常。

参数：

- exception: [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 指定的抛出的异常。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[GetterActionSelector](#class-getteractionselectortret)\<TRet>> - 预期执行次数的操作器。