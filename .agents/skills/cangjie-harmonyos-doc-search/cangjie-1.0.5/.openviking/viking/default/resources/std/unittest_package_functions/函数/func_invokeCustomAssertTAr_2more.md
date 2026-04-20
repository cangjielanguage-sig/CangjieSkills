## func invokeCustomAssert\<T>(Array\<String>, String, (AssertionCtx) -> T, ?AssertionCtx)

```cangjie
public func invokeCustomAssert<T>(
    passerdArgs: Array<String>,
    caller: String,
    assert: (AssertionCtx) -> T,
    optParentCtx!: ?AssertionCtx = None
): T
```

功能：运行在 [`@Test`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#test-宏), [`@TestCase`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#testcase-宏)，或 [`@CustomAssertion`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#customassertion-宏) 宏中使用的 [`@Assert\[caller\](passerArgs)`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#assert-宏) 指定的用户定义断言函数。

参数：

- passedArgs: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 未处理的已传递参数。
- caller: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 调用的自定义断言的名称。
- assert: ([AssertionCtx](./unittest_package_classes.md#class-assertionctx)) -> T - 捕获带有正确参数的断言调用。
- optParentCtx!: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[AssertionCtx](./unittest_package_classes.md#class-assertionctx)> - 存储嵌套断言失败消息的上下文。

返回值：

- T - 由用户定义的断言返回的值。

## func invokeCustomExpect(Array\<String>, String, (AssertionCtx) -> Any, ?AssertionCtx)

```cangjie
public func invokeCustomExpect(
    passerdArgs: Array<String>,
    caller: String,
    expect: (AssertionCtx) -> Any,
    optParentCtx!: ?AssertionCtx = None
): Unit
```

功能：运行在 [`@Test`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#test-宏), [`@TestCase`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#testcase-宏), 或 [`@CustomAssertion`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#customassertion-宏) 宏中使用的 [`@Expect\[caller\](passerArgs)`](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#expect-宏) 指定的用户定义断言函数。

参数：

- passedArgs: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 未处理的已传递参数。
- caller: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 调用的自定义断言的名称。
- expect: ([AssertionCtx](./unittest_package_classes.md#class-assertionctx)) -> [Any](../../core/core_package_api/core_package_interfaces.md#interface-any) - 捕获带有正确参数的断言调用。
- optParentCtx!: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[AssertionCtx](./unittest_package_classes.md#class-assertionctx)> - 存储嵌套断言失败消息的上下文。