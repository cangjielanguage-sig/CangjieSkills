# @Builder宏：自定义构建函数

仓颉UI提供了一种轻量的UI元素复用机制@Builder，其内部UI结构固定，仅与使用方进行数据传递，开发者可以将重复使用的UI元素抽象成一个方法，在build方法里调用。

为了简化语言，我们将@Builder修饰的函数也称为“自定义构建函数”。

在阅读本文档前，建议提前阅读：[基本语法概述](./cj-basic-syntax-overview.md)，[声明式UI描述](./cj-declarative-ui-description.md)，[自定义组件-创建自定义组件](./cj-create-custom-components.md)。

## 宏使用说明

@Builder宏有两种使用方式，分别是定义在自定义组件内部的私有自定义构建函数和定义在全局的全局自定义构建函数。

### 私有自定义构建函数

定义的语法：

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @Builder
    func showTextBuilder() {
        Text("Hello World").fontSize(30).fontWeight(FontWeight.Bold)
    }

    @Builder
    func showTextValueBuilder(param: String) {
        Text(param).fontSize(30).fontWeight(FontWeight.Bold)
    }

    func build() {
        Column {
            // 无参数
            this.showTextBuilder()
            // 有参数
            this.showTextValueBuilder("Hello @Builder")
        }
    }
}
```

使用方法：

```cangjie
this.showTextBuilder()
```

- 允许在自定义组件内定义一个或多个@Builder方法，该方法被认为是该组件的私有、特殊类型的成员函数。

- 私有自定义构建函数允许在自定义组件内、build方法和其他自定义构建函数中调用。

- 在自定义函数体中，this指代当前所属组件，组件的状态变量可以在自定义构建函数内访问。建议通过this访问自定义组件的状态变量而不是参数传递。

### 全局自定义构建函数

定义的语法：

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Builder
func showTextBuilder() {
    Text("Hello World").fontSize(30).fontWeight(FontWeight.Bold)
}

@Entry
@Component
class EntryView {
    func build() {
        Column {
            showTextBuilder()
        }
    }
}
```

使用方法：

```cangjie
showTextBuilder()
```

- 如果不涉及组件状态变化，建议使用全局的自定义构建方法。

- 全局自定义构建函数允许在build方法和其他自定义构建函数中调用。