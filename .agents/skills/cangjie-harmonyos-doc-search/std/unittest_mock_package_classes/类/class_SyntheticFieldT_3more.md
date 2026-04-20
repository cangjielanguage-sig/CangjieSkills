## class SyntheticField\<T>

```cangjie
public class SyntheticField<T> {}
```

功能：合成字段。用于处理可变属性和字段。

### static func create(T)

```cangjie
public static func create(initialValue!: T): SyntheticField<T>
```

功能：创建合成字段。

参数：

- initialValue!: T - 初始值。

返回值：

- [SyntheticField](#class-syntheticfieldt)\<T> - 合成字段。

## class TypedMatcher\<T>

```cangjie
public abstract class TypedMatcher<T> <: ArgumentMatcher {}
```

功能：参数类型匹配器。

父类型：

- [ArgumentMatcher](#class-argumentmatcher)

### func matches(T)

```cangjie
public func matches(arg: T): Bool
```

功能：检查入参类型是否与预期相符。

参数：

- arg: T - 待检查的入参。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 若类型匹配则返回 `true` ，否则返回 `false` 。

### func matchesAny(Any)

```cangjie
public func matchesAny(arg: Any): Bool
```

功能：检查入参类型是否与预期相符。

参数：

- arg: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 待检查的入参。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 若类型匹配则返回 `true` ，否则返回 `false` 。

### extend\<T> TypedMatcher\<T>

```cangjie
extend<T> TypedMatcher<T> {}
```

功能：扩展 [TypedMatcher](#class-typedmatchert) 。

#### func value\<T>()

```cangjie
public func value<T>(): T
```

功能：框架需要调用的参数匹配器的返回值。

返回值：

- T - 与实际入参值类型匹配的值。

## class UnorderedVerifier

```cangjie
public class UnorderedVerifier{}
```

功能：此类型用于收集 “验证语句”， 可在 unordered 函数中动态传入验证行为。

### func checkThat(VerifyStatement)

```cangjie
public func checkThat(statement: VerifyStatement):UnorderedVerifier
```

功能：添加一条 “验证语句”。

参数：

- statement: [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 待被添加的“验证语句”。

返回值：

- [UnorderedVerifier](unittest_mock_package_classes.md#class-unorderedverifier) - 返回对象自身。