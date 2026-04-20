## interface Reporter

```cangjie
sealed interface Reporter <TReport, TReturn>
```

功能：报告器基础接口。

## interface TestClass

```cangjie
public interface TestClass {
    func asTestSuite(): TestSuite
}
```

功能：提供创建 [TestSuite](./unittest_package_classes.md#class-testsuite) 的方法。

### func asTestSuite()

```cangjie
func asTestSuite(): TestSuite
```

功能：创建 [TestSuite](./unittest_package_classes.md#class-testsuite) 的方法。

返回值：

- [TestSuite](./unittest_package_classes.md#class-testsuite) - 测试套对象。