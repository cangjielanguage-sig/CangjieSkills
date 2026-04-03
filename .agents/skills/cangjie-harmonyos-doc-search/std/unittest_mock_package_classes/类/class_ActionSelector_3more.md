## class ActionSelector

```cangjie
public sealed abstract class ActionSelector {}
```

功能：此抽象类提供了为成员函数指定一个[操作 API](../unittest_mock_samples/mock_framework_basics.md#操作-api) ，并允许链式调用的方法。

入参为 `mock object` 或 `spy object` 的某个成员函数的调用表达式的 `@On` 宏调用表达式，将返回 [ActionSelector](#class-actionselector) 的实例。即，此类或其子类中的 API 可为成员函数插入桩代码。

### func fails()

```cangjie
func fails(): Unit
```

功能：定义调用桩签名将导致测试失败，执行至桩签名即抛出 [AssertionException](../../unittest/unittest_package_api/unittest_package_exceptions.md#class-assertexception) 异常的行为。

## class AnyMatcher

```cangjie
public class AnyMatcher <: ArgumentMatcher {}
```

功能：任意参数匹配器，即桩签名允许任意的参数。

父类型：

- [ArgumentMatcher](#class-argumentmatcher)

### func matchesAny(Any)

```cangjie
public func matchesAny(_: Any): Bool
```

功能：匹配任意类型的任意值。

参数：

- _: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 被检查的输入参数。任意类型的任意值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 固定为 `true` 。

### extend AnyMatcher

```cangjie
extend AnyMatcher {}
```

功能：扩展 [AnyMatcher](#class-anymatcher) 。

#### func value\<T>()

```cangjie
public func value<T>(): T
```

功能：框架需要调用的参数匹配器的返回值。

返回值：

- T - 与实际入参类型匹配的值。

## class ArgumentMatcher

```cangjie
public abstract class ArgumentMatcher {}
```

功能：参数匹配器抽象类，该类与其子类可作为桩签名的入参类型。

### func withDescription(String)

```cangjie
public func withDescription(description: String): ArgumentMatcher
```

功能：配置参数匹配器抛出异常时的描述信息。

参数：

- description: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 描述信息。

返回值：

- ArgumentMatcher - 被配置的参数匹配器。

### func forParameter(String)

```cangjie
public func forParameter(name: String): ArgumentMatcher
```

功能：配置所匹配的参数名称。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 所匹配的参数名称。

返回值：

- ArgumentMatcher - 被配置的参数匹配器。

### func matchesAny(Any)

```cangjie
public func matchesAny(arg: Any)
```

功能：匹配任意类型的任意值。

参数：

- arg: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 被检查的输入参数。任意类型的任意值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 匹配结果 。