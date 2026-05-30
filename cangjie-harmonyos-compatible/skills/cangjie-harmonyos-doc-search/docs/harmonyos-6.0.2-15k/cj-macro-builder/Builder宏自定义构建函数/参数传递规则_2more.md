## 参数传递规则

自定义构建函数的参数传递有[按值传递](#按值传递参数)和[按引用传递](#按引用传递参数)两种，均需遵守以下规则：

- 参数的类型必须与参数声明的类型一致。

- 在@Builder修饰的函数内部，不允许改变参数值。

- @Builder内UI语法遵循[UI语法规则](./cj-create-custom-components.md)。

- 只有传入一个参数，且参数需要直接传入对象字面量才会按引用传递该参数，其余传递方式均为按值传递。

### 按值传递参数

调用@Builder修饰的函数默认按值传递。当传递的参数为状态变量时，状态变量的改变不会引起@Builder方法内的UI刷新。所以当使用状态变量的时候，推荐使用[按引用传递](#按引用传递参数)。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Builder
func overBuilder(paramA1: String) {
    Row {
        Text("UseStateVarByValue: ${paramA1}")
    }
}

@Entry
@Component
class EntryView {
    @State
    var label: String = "Hello"

    func build() {
        Column {
            overBuilder(label)
        }
    }
}
```

### 按引用传递参数

按引用传递参数时，传递的参数可为状态变量，且状态变量的改变会引起@Builder方法内的UI刷新。

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Tmp {
    @Publish
    var paramA1: String = ""
}

@Builder
func overBuilder(params: Tmp) {
    Row {
        Text("UseStateVarByReference: ${params.paramA1}")
    }
}

@Entry
@Component
class EntryView {
    @State
    var tmp: Tmp = Tmp(paramA1: "Hello")

    func build() {
        Column {
            // 在父组件中调用overBuilder组件时，
            // 把参数通过引用传递的方式传给overBuilder组件。
            overBuilder(tmp)
            Button("Click me").onClick({
                _ =>
                // 单击Click me后，UI文本更改为ArkUI。
                this.tmp.paramA1 = "ArkUI"
            })
        }
    }
}
```

## 限制条件

@Builder通过按引用传递的方式传入参数，才会触发动态渲染UI。请参考[按引用传递参数](#按引用传递参数)。