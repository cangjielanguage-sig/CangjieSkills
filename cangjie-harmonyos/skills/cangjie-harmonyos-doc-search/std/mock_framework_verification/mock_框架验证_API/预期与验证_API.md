## 预期与验证 API

配置桩时，可以设置**预期**和验证 API 覆盖测试代码的一些断言。这种情况别无他法，只能选择更能反映测试意图的方法。

一般情况下，建议避免重复验证块中的配置步骤。

<!--compile.onlyformat-->
```cangjie
let foo = mock<Foo>()
@On(foo.bar(_)).returns() // 如果从未使用此桩，测试失败

foo.bar(1)
foo.bar(2)

Verify.that(
    // 不需要，自动验证
    @Called(foo.bar(_)).atLeastOnce()
)

// 但可以检查调用的数量和具体的参数
Verify.unordered(
    @Called(foo.bar(1)).once(),
    @Called(foo.bar(2)).once()
)
```

上面的示例可以使用预期重写：

<!--compile.onlyformat-->
```cangjie
let foo = mock<Foo>()
@On(foo.bar(1)).returns().once() // 预期只被调用一次，参数为`1`
@On(foo.bar(2)).returns().once() // 预期只被调用一次，参数为`2`

foo.bar(1)
foo.bar(2)

// 如果没有桩被触发，则测试失败
```