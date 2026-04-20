### func throws(() -> Exception)

```cangjie
public func throws(exceptionFactory: () -> Exception): CardinalitySelector<GetterActionSelector<TRet>>
```

功能：指定抛出异常。

参数：

- exceptionFactory: () -> [Exception](../../core/core_package_api/core_package_exceptions.md#class-exception) - 指定的抛出的异常的生成器。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[GetterActionSelector](#class-getteractionselectortret)\<TRet>> - 预期执行次数的操作器。

### extend MethodActionSelector\<Unit>

```cangjie
extend MethodActionSelector<Unit> {}
```

功能：扩展 [MethodActionSelector](#class-methodactionselectortret) 。

#### func returns()

```cangjie
public func returns(): CardinalitySelector<MethodActionSelector<TRet>>
```

功能：指定桩函数什么都不做。

返回值：

- [CardinalitySelector](#class-cardinalityselectora)\<[MethodActionSelector](#class-methodactionselectortret)\<TRet>> - 预期执行次数的操作器。