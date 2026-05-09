## class Matchers

```cangjie
public class Matchers {}
```

功能：该类提供生成[匹配器](../unittest_mock_samples/mock_framework_basics.md#参数匹配器)的静态函数。匹配器对象仅可通过此处的静态函数生成。匹配器可在[桩链](../unittest_mock_samples/mock_framework_basics.md#桩链)中使用。

例如：`@On(foo.bar(ofType<Int64>())).returns(1)`

参数匹配器可以在 `@On` 宏调用表达式入参处使用，来描述期望将哪些参数传递到[桩签名](../unittest_mock_samples/mock_framework_basics.md#桩签名)中。参数匹配器有两个最常见的用途：

- 为不同的参数指定不同的行为。例如：

    ```cangjie
    // 当 bar 的入参为 5 时，返回某个值
    @On(foo.bar(eq(5))).returns(...)
    // 当 bar 的入参为 6 时，抛出异常
    @On(foo.bar(eq(6))).throws(...)
    ```

- 确保只有某些参数被传递到某些桩签名中。

    ```cangjie
    let foo = mock<Foo>()
    // bar 的入参只能为正数，否则将抛出 UnhandledCallException 异常
    @On(foo.bar(argThat<Int64> { arg => arg > 0 })).returns(...)
    ```

    > **注意：**
    >
    > 上例仅适用于 `mock object` 。`spy object` 的行为不同。

    ```cangjie
    let foo = spy(Foo())
    // 当 bar 的入参不为正数时，将调用 Foo() 对象的成员函数。
    @On(foo.bar(argThat<Int64> { arg => arg <= 0 })).fails()
    ```

### static func any()

```cangjie
public static func any(): AnyMatcher
```

功能：允许将任何值作为参数。

返回值：

- [AnyMatcher](#class-anymatcher) - 允许任意值的参数匹配器。

### static func argThat\<T>(ValueListener\<T>, (T) -> Bool)

```cangjie
public static func argThat<T>(listener: ValueListener<T>, predicate: (T) -> Bool): TypedMatcher<T>
```

功能：通过传入的 predicate 闭包函数过滤传入的参数值，允许 listener 值监听器对满足条件的传入参数值进行处理。

参数：

- listener: [ValueListener](unittest_mock_package_interfaces.md#interface-valuelistenert)\<T> - 值监听器。
- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 过滤器，可通过此函数定义过滤参数值的匹配条件。

返回值：

- [TypedMatcher](#class-typedmatchert)\<T> - 拥有值监听器和过滤器的类型匹配器。

### static func argThat\<T>((T) -> Bool)

```cangjie
public static func argThat<T>(predicate: (T) -> Bool): TypedMatcher<T>
```

功能：根据提供的过滤器闭包过滤输入值。

参数：

- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 过滤器。

返回值：

- [TypedMatcher](#class-typedmatchert)\<T> - 参数过滤类型匹配器实例。

### static func argThatNot\<T>((T) -> Bool)

```cangjie
public static func argThatNot<T>(predicate: (T) -> Bool): TypedMatcher<T>
```

功能：根据提供的过滤器闭包过滤输入值。

参数：

- predicate: (T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 过滤器。

返回值：

- [TypedMatcher](#class-typedmatchert)\<T> - 参数过滤类型匹配器实例。

### static func capture\<T>(ValueListener\<T>)

```cangjie
public static func capture<T>(listener: ValueListener<T>): TypedMatcher<T>
```

功能：允许 listener 值监听器对类型为 T 的传入参数值进行处理。当 capture 的类型参数未指定时，将使用值监听器的类型参数值。

参数：

- listener: [ValueListener](unittest_mock_package_interfaces.md#interface-valuelistenert)\<T> - 值监听器。

返回值：

- [TypedMatcher](#class-typedmatchert)\<T> - 拥有值监听器的类型匹配器。

注意：值监听器不允许在 @Called 的参数范围内使用。