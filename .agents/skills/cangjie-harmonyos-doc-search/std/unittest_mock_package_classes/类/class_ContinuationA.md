## class Continuation\<A>

```cangjie
public class Continuation<A> where A <: ActionSelector {}
```

功能：此类提供了可继续定义桩签名的行为的 API 。
此类提供的方法能力如下：

- 允许当先前的操作得到满足时，桩签名将执行额外的操作。仅当后面跟着一个行为定义时，`Continuation` 实例才有意义。
- 当先前的操作未得到满足时，将抛出 [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) 异常。并不保证抛出此异常的确切位置。

### func then()

```cangjie
func then(): A
```

功能：当链中的先前操作完成时，返回 [ActionSelector](unittest_mock_package_classes.md#class-actionselector) 的子类对象。

返回值：

- A - [ActionSelector](unittest_mock_package_classes.md#class-actionselector)的子类对象实例。

异常：

- [MockFrameworkException](./unittest_mock_package_exceptions.md#class-mockframeworkexception) - 当先前的操作未得到满足时，将抛出异常。