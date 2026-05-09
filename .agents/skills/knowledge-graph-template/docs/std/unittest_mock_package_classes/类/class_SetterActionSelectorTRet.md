## class SetterActionSelector\<TRet>

```cangjie
public class SetterActionSelector<TRet> <: ActionSelector {}
```

功能：此类提供了为属性 `Setter` 函数指定一个[操作 API](../unittest_mock_samples/mock_framework_basics.md#操作-api) ，并允许链式调用的方法。
入参为 `mock object` 或 `spy object` 的某个成员函数的调用表达式的 `@On` 宏调用表达式，将返回 [ActionSelector](#class-actionselector) 的实例。即，此类或其子类中的 API 可为成员函数插入桩代码。

父类型：

- [ActionSelector](#class-actionselector)

### func doesNothing()

```cangjie
public func doesNothing(): CardinalitySelector<SetterActionSelector<TArg>>
```

功能：指定该属性或字段不做任何动作。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[SetterActionSelector](#class-setteractionselectortret)\<TArg>> - 预期执行次数的操作器。

### func setsOriginal()

```cangjie
public func setsOriginal(): CardinalitySelector<SetterActionSelector<TArg>>
```

功能：设置原始属性或获取原始实例中的字段值。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[SetterActionSelector](#class-setteractionselectortret)\<TArg>> - 预期执行次数的操作器。

### func setsField(SyntheticField\<TArg>)

```cangjie
public func setsField(field: SyntheticField<TArg>): CardinalitySelector<SetterActionSelector<TArg>>
```

功能：设置[合成字段](../unittest_mock_samples/mock_framework_stubs.md#设置属性和字段和顶层变量)。

参数：

- field: [SyntheticField](#class-syntheticfieldt)\<TArg> - 合成字段，处理可变属性。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[SetterActionSelector](#class-setteractionselectortret)\<TArg>> - 预期执行次数的操作器。

### func throws(Exception)

```cangjie
public func throws(exception: Exception): CardinalitySelector<SetterActionSelector<TArg>>
```

功能：指定抛出异常。

参数：

- exception: [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 指定的抛出的异常。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[SetterActionSelector](#class-setteractionselectortret)\<TArg>> - 预期执行次数的操作器。

### func throws(() -> Exception)

```cangjie
public func throws(exceptionFactory: () -> Exception): CardinalitySelector<SetterActionSelector<TArg>>
```

功能：指定抛出异常。

参数：

- exceptionFactory: () -> [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 指定的抛出的异常的生成器。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[SetterActionSelector](#class-setteractionselectortret)\<TArg>> - 预期执行次数的操作器。