## 其他 API

另外，`Verify` 类还提供了以下工具。

* that(statement: VerifyStatement) 为 Verify.unordered(Paritial, statement) 的别名，用于检查单个语句，不需要列出对应 mock/spy 对象的所有调用。
* noInteractions(mocks: Array\<Object>) 用于检查没有进行调用的 mock/spy 对象。
* `clearInvocationLog()` 将日志重置为空状态。这会影响后面的所有验证块，但并不影响桩预期。

示例：

<!--compile.onlyformat-->
```cangjie
foo.bar()
Verify.that(@Called(foo.bar())) // OK
Verify.noInteractions(foo)      // 失败，foo.bar() 调用在日志中
Verify.clearInvocationLog()     // 清除日志
Verify.noInteractions(foo)      // 从日志中清除所有与 foo 的交互
Verify.that(@Called(foo.bar())) // 失败
```

## `Verify` 类 API

<!--compile.onlyformat-->
```cangjie
public class Verify {
    public static func that(statement: VerifyStatement): Unit

    public static func unordered(
        exhaustive: Exhaustiveness,
        collectStatements: (UnorderedVerifier) -> Unit
    ): Unit

    public static func unordered(
        collectStatements: (UnorderedVerifier) -> Unit
    ): Unit

    public static func unordered(statements: Array<VerifyStatement>): Unit

    public static func unordered(
        exhaustive: Exhaustiveness,
        statements: Array<VerifyStatement>
    ): Unit

    public static func ordered(
        collectStatements: (OrderedVerifier) -> Unit
    ): Unit

    public static func ordered(statements: Array<VerifyStatement>): Unit

    public static func clearInvocationLog(): Unit

    public static func noInteractions(mocks: Array<Object>): Unit
}
```

## 验证错误

验证失败时，会抛出 `VerificationFailedException` ，mock 框架会给出报告。不要捕获该异常。

失败类型如下：

* **调用次数太少**或**调用次数太多**：调用次数与块中的语句不匹配。
* **语句不匹配**：块中存在与日志中的调用不匹配的语句。
* **调用不匹配**：日志中存在与块中的语句不匹配的调用。
* **意外调用**：**有序**验证块需要的是其他的调用。
* **无用交互**： **noInteractions** 检测到意外调用。

还有另一种失败类型**不相交的语句**，不一定是测试代码本身有问题。调用匹配到多个语句时，就会上报这种失败类型。在单个验证块中使用具有不相交参数匹配器的语句可能会导致此错误。不允许在语句和调用之间进行模糊匹配。