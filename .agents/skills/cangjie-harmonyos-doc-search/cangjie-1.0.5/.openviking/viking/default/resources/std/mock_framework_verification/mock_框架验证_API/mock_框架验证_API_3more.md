# mock 框架验证 API

验证 API 是 mock 框架的一部分，其功能如下：

* 验证是否进行了某些调用。
* 验证特定调用的次数。
* 验证是否使用特定参数进行调用。
* 验证调用是否按特定顺序进行。

验证通过检查在执行测试期间构建的调用日志来运行断言。调用日志涵盖让 **mock** 和 **spy** 对象（以及静态成员和顶层函数和顶层变量）在测试中可访问的所有调用。只能验证在 mock/spy 对象（以及静态成员和顶层函数和顶层变量）上进行的调用。

`Verify` 类是验证 API 的入口。
**@Called** 宏用于构建关于代码的断言。

<!-- 链接至验证 API 手册 中的 Verify 类介绍 （自动生成）-->

**@Called** 宏调用构造了一个 **验证语句** ，即根据调用日志检查代码的单个断言。

**Verify** 类本身是静态方法的集合。诸如 `that` 、 `ordered` 、 `unordered` 等方法可构造**验证块**。

## 示例

<!--compile.onlyformat-->
```cangjie
let foo = mock<Foo>()
// 配置 foo
@On(foo.bar()).returns()
foo.bar()
Verify.that(@Called(foo.bar())) // 验证 bar 至少被调用一次
```

## 验证语句和 `@Called` 宏

验证语句由 `VerifyStatement` 类表示。 `VerifyStatement` 实例由 `@Called` 宏创建。

`@Called` 宏调用接受[桩签名](./mock_framework_basics.md#桩签名)，类似于 `@On` 宏，并且适用[参数匹配器](./mock_framework_basics.md#参数匹配器)的规则。

示例：

<!--compile.onlyformat-->
```cangjie
@Called(foo.bar(1, _)) // 匹配 bar 方法调用的验证语句，其中第一个参数为 '1'
@Called(Foo.baz)       // 匹配 baz 静态属性 getter 调用的验证语句
```

`VerifyStatement` 类提供的 API 类似于桩配置时可用的基数说明符。

基数函数为：

* `once()`
* `atLeastOnce()`
* `times(expectedTimes: Int64)`
* `times(min!: Int64, max!: Int64)`
* `atLeastTimes(minTimesExpected: Int64)`
* `never()`

调用这些函数会返回相同的 `VerifyStatement` 实例。同一语句不能重置基数，且必须在语句传递到验证块生成器函数之前设置基数。如果没有显式设置基数，则使用默认基数。

<!--compile.onlyformat-->
```cangjie
Verify.that(@Called(foo.bar()).atLeastOnce())
Verify.that(@Called(foo.bar()).once())
```