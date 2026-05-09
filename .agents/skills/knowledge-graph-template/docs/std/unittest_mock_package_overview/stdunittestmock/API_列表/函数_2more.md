### 函数

|              函数名          |           功能           |
| --------------------------- | ------------------------ |
| [mock\<T>()](./unittest_mock_package_api/unittest_mock_package_functions.md#func-mockt) | 创建类型 T 的 [`mock object`](./unittest_mock_samples/mock_framework_basics.md#创建-mock-对象)， 这个对象默认情况下，所有的成员函数、属性或运算符重载函数没有任何具体实现。 |
| [mock\<T>(Array\<StubMode>)](./unittest_mock_package_api/unittest_mock_package_functions.md#func-mocktarraystubmode) | 创建类型 T 的 [`mock object`](../unittest_mock/unittest_mock_samples/mock_framework_basics.md#创建-mock-对象) ， 参数指定了[桩的模式](../unittest_mock/unittest_mock_samples/mock_framework_stubs.md#桩的模式)。 |
| [spy\<T>(T)](./unittest_mock_package_api/unittest_mock_package_functions.md#func-spytt) | 创建类型 T 的 `spy object` ( `mock object` 的扩展，对象的成员拥有默认实现的“骨架”对象)。 这个对象包装了所传入的对象，并且默认情况下成员函数、属性或运算符重载函数实现为对这个传入的实例对象的对应成员函数、属性或运算符重载函数的调用。 |

### 接口

|              接口名          |           功能           |
| --------------------------- | ------------------------ |
| [ValueListener\<T>](./unittest_mock_package_api/unittest_mock_package_interfaces.md#interface-valuelistenert) | 此接口提供了多个成员函数以支持“监听”传入给桩签名的参数。 |