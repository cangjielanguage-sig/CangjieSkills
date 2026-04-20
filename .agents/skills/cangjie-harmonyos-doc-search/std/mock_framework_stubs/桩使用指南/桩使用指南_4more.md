# 桩使用指南

mock/spy 对象和桩的使用方法多种多样。本文介绍了不同的模式和用例，便于用户编写 **mock 框架**的可维护且简洁的测试用例。

## 桩的工作原理

[桩](./mock_framework_basics.md#配置-api) 通过在测试用例内部调用 `@On` 宏来声明，该声明在特定测试用例执行完成之前有效。多个测试用例之间可以[共享桩](#共享-mock-对象和桩)。

mock 框架处理 mock/spy 对象成员（或静态成员或顶层函数或顶层变量）调用时的顺序如下：

* 查找特定声明的桩。后声明的桩优先于之前声明的桩。测试用例主体内部声明的桩优先于共享桩。
* 应用每个桩的**参数匹配器**。如果所有参数都成功匹配，则执行该桩定义的操作。
* 如果找不到桩，或者没有与实际参数匹配的桩，则应用默认行为：
    * 对于 mock 对象，上报**未打桩调用**错误；
    * 对于 spy 对象，调用被监视实例的原始成员；
    * 对于静态成员或顶层函数或顶层变量，调用原始对应声明。

无论是否为单个成员定义了多个桩，每个桩都有自己的预期，需要满足这些[预期](./mock_framework_basics.md#预期)才能通过测试。

!--compile.onlyformat-->
```cangjie
@On(foo.bar(1)).returns(1)
@On(foo.bar(2)).returns(2)

foo.bar(2)
// 第一个桩已定义但从未使用，测试失败
```

## 重新定义桩

如果希望在测试中更改桩的行为，可以重新定义桩。

<!--compile.onlyformat-->
```cangjie
@On(service.request()).returns(testData)
// 使用服务

@On(service.request()).throws(Exception())
// 测试服务开始失败时会发生什么事情
```

## 同一声明定义多个桩

根据不同参数，可以使用多个桩来定义不同的行为。

示例：

<!--compile.onlyformat-->
```cangjie
@On(storage.get(_)).returns(None) // 1
@On(storage.get(TEST_ID)).returns(Some(TEST_DATA)) // 2
```

示例中，`storage` 为除 `TEST_ID` 之外的所有参数返回 `None` 。
如果从未使用 `TEST_ID` 参数调用 `get` ，则测试失败，因为桩 **2** 未使用。如果始终使用 `TEST_ID` 参数调用 `get` ，则测试失败，因为桩 **1** 未使用。这些限制确保测试代码是纯净的，让开发人员知道桩何时变为未使用。如果用例不需要此功能，则使用 `anyTimes()` 基数说明符来提升这些预期。

<!--compile.onlyformat-->
```cangjie
// 实现经常更改，但不希望测试中断
// 使用 anyTimes 提升与测试本身无关的预期
@On(storage.get(_)).returns(None).anyTimes()
@On(storage.get(TEST_ID)).returns(Some(TEST_DATA)) // 测试必须调用正在测试的内容
```

鉴于桩优先级是**从下到上**，以下用法都不正确。

<!--compile.onlyformat-->
```cangjie
@On(storage.get(TEST_ID)).returns(Some(TEST_DATA)) // 不正确，这个桩永远不会被触发
@On(storage.get(_)).returns(None) // 在上面的桩始终会被隐藏
```

您还可以使用预期来检查调用的参数。

<!--compile.onlyformat-->
```cangjie
let renderer = spy(Renderer())

@On(renderer.render(_)).fails()
let isVisible = { c: Component => c.isVisible }
@On(renderer.render(argThat(isVisible))).callsOriginal() // 只允许可见的组件
```