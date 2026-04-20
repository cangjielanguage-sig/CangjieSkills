### static func default\<T>(T)

```cangjie
public static func default<T>(target: T): TypedMatcher<T>
```

功能：根据结构（更高优先级）或引用相等性来匹配值。如果传入的参数既不是 [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<T> 也不是引用类型，则会在运行时抛出异常（编译期不做检查）。

参数：

- target: T - 必须通过结构或引用相等来匹配的匹配对象。

返回值：

- [TypedMatcher](#class-typedmatchert)\<T> - 默认类型匹配器。

异常：

- [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) - 如果参数 target 既不是 [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<T> 类型也不是引用类型，则抛出异常。

### static func eq\<T>(T)

```cangjie
public static func eq<T>(target: T): TypedMatcher<T> where T <: Equatable<T>
```

功能：根据与提供的值的结构相等性过滤输入值。

参数：

- target: T - 匹配对象。

返回值：

- [TypedMatcher](#class-typedmatchert)\<T> - 仅允许结构上等于给定值的参数匹配器。

### static func ofType\<T>()

```cangjie
public static func ofType<T>(): TypedMatcher<T>
```

功能：根据类型过滤输入值。

返回值：

- [TypedMatcher](#class-typedmatchert)\<T> - 仅允许特定类型的类型匹配器。

### static func same\<T>(T) where T <: Object

```cangjie
public static func same<T>(target: T): TypedMatcher<T> where T <: Object
```

功能：根据与所提供对象的引用相等性来过滤输入值。

参数：

- target: T - 匹配对象。

返回值：

- [TypedMatcher](#class-typedmatchert)\<T> - 仅允许与给定对象引用相等的参数的参数匹配器。

### extend Matchers

```cangjie
extend Matchers {}
```

功能：扩展 [Matchers](#class-matchers) 。

#### static func none()

```cangjie
public static func none(): NoneMatcher
```

功能：过滤值为 `None` 的入参值。

返回值：

- [NoneMatcher](#class-nonematcher) - `None` 值匹配器。