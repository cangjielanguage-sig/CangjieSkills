# @BuilderParam宏：引用@Builder函数

当开发者创建了自定义组件，并想对该组件添加特定功能，例如想在某一个指定的自定义组件中添加一个点击跳转操作，此时若直接在组件内嵌入事件方法，将会导致所有该自定义组件的实例都增加了功能。为解决此问题，ArkUI引入了@BuilderParam宏，@BuilderParam用来修饰指向@Builder方法的变量（@BuilderParam是用来承接@Builder函数的）。开发者可以在初始化自定义组件时，使用不同的方式（如：参数修改、父组件初始化等）对@BuilderParam修饰的自定义构建函数进行传参赋值，在自定义组件内部通过调用@BuilderParam为组件增加特定的功能。该宏用于声明任意UI描述的一个元素，类似slot占位符。

在阅读本文档前，建议提前阅读：[@Builder](./cj-macro-builder.md)。

## 宏使用说明

### 初始化@BuilderParam修饰的方法

@BuilderParam修饰的方法只能被自定义构建函数（@Builder修饰的方法）初始化。

使用全局的自定义构建函数，在本地初始化@BuilderParam。

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Builder
func overBuilder() {}

@Component
class Child {
    // 使用全局自定义构建函数初始化@BuilderParam
    @BuilderParam
    var customOverBuilderParam: () -> Unit = overBuilder

    func build() {}
}
```

## 限制条件

使用@BuilderParam有如下限制：

- 所修饰的变量只能使用@Builder函数进行初始化。

- 所修饰变量的类型为函数类型，且返回值类型为Unit。

- 所修饰的变量声明中，变量的类型需要显式标注。

- 只能修饰类的成员变量声明，禁止修饰全局变量（否则将产生编译错误）。

- 所修饰的类成员变量（可见性与private修饰符一致）只允许在类内部使用。

- 所修饰变量可以是可变的，也可以是不可变的。变量的可变性遵循仓颉语法，即由let/var关键字标识的变量分别为不可变变量和可变变量。