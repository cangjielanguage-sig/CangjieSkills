## class MockFramework

```cangjie
public class MockFramework {}
```

功能：提供用例执行所需的框架准备与结束回收阶段的函数。

### static func openSession(String, MockSessionKind)

```cangjie
public static func openSession(name: String, sessionKind: MockSessionKind): Unit
```

功能：打开一个新会话。会话形成一个类似堆栈的结构。
会话关闭的顺序与开始时的顺序相反。
在给定会话期间创建的 `mock object` 只能在该会话或其任何内部会话内部访问。
每个会话都保留自己的调用日志，因此对最新打开会话内进行的调用执行任何验证， 只有在会议结束时才能验证期望。

参数：

- name: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 会话的名称。
- sessionKind: [MockSessionKind](./unittest_mock_package_enums.md#enum-mocksessionkind) - 指定允许的桩类型。

### static func closeSession()

```cangjie
public static func closeSession(): Unit
```

功能：打开一个新会话。会话形成一个类似堆栈的结构。
会话关闭的顺序与开始时的顺序相反。
在给定会话期间创建的 `mock object` 只能在该会话或其任何内部会话内部访问。
每个会话都保留自己的调用日志，因此对最新打开会话内进行的调用执行任何验证， 只有在会议结束时才能验证期望。

异常：

- [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) - 检测到错误的配置信息的时候，抛出异常。
- [ExpectationFailedException](./unittest_mock_package_exceptions.md#class-expectationfailedexception) - 当预期未被满足时，抛出异常。

## class NoneMatcher

```cangjie
public class NoneMatcher <: ArgumentMatcher {}
```

功能：参数值为 `None` 的匹配器。

父类型：

- [ArgumentMatcher](#class-argumentmatcher)

### func matchesAny(Any)

```cangjie
public override func matchesAny(arg: Any): Bool
```

功能：匹配任意输入值，值为 None 时返回 `true` 。

参数：

- arg: [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 待匹配的入参值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 当输入为 None 时返回 `true` ，否则返回 `false` 。

### extend NoneMatcher

```cangjie
extend NoneMatcher {}
```

功能：扩展 [NoneMatcher](#class-nonematcher) 。

#### func value\<T>()

```cangjie
public func value<T>(): Option<T>
```

功能：框架需要调用的参数匹配器的返回值。

返回值：

- Option\<T> - 与实际入参值类型匹配的值。

## class OrderedVerifier

```cangjie
public class OrderedVerifier {}
```

功能：此类型用于收集 “验证语句”，可在 ordered 函数中动态传入验证行为。

### func checkThat(VerifyStatement)

```cangjie
public func checkThat(statement: VerifyStatement): OrderedVerifier
```

功能：添加一条 “验证语句”。

参数：

- statement: [VerifyStatement](unittest_mock_package_classes.md#class-verifystatement) - 待被添加的“验证语句”。

返回值：

- [OrderedVerifier](unittest_mock_package_classes.md#class-orderedverifier) - 返回对象自身。