# 状态管理概述

如果希望构建一个动态的、有交互的界面，就需要引入“状态”的概念。

**图1** 效果图

![state_manage_overview1](figures/state-mangement-overview1.gif)

上面的示例中，用户与应用程序的交互触发了文本状态变更，状态变更引起了UI渲染，UI从“Hello World”变更为“Hello Cangjie”。

在声明式UI编程框架中，UI是程序状态的运行结果，用户构建了一个UI模型，其中应用的运行时的状态是参数。当参数改变时，UI作为返回结果，也将进行对应的改变。这些运行时的状态变化所带来的UI的重新渲染，在仓颉中统称为状态管理机制。

自定义组件拥有变量，变量必须被装饰器装饰才可以成为状态变量，状态变量的改变会引起UI的渲染刷新。如果不使用状态变量，UI只能在初始化时渲染，后续将不会再刷新。 下图展示了State和View（UI）之间的关系。

![state_manage_overview2](figures/state-mangement-overview2.png)

- View(UI)：UI渲染，指将build方法内的UI描述和@Builder装饰的方法内的UI描述映射到界面。

- State：状态，指驱动UI更新的数据。用户通过触发组件的事件方法，改变状态数据。状态数据的改变，引起UI的重新渲染。

在阅读状态管理文档前，开发者需要对UI范式基本语法有基本的了解。建议提前阅读：基本语法概述，声明式UI描述，自定义组件-创建自定义组件。

## 基本概念

- 状态变量：被状态装饰器装饰的变量，状态变量值的改变会引起UI的渲染更新。示例：@State var num: Int32 = 1,其中，@State是状态装饰器，num是状态变量。
- 常规变量：没有被状态装饰器装饰的变量，通常应用于辅助计算。它的改变永远不会引起UI的刷新。以下示例中increaseBy变量为常规变量。
- 数据源/同步源：状态变量的原始来源，可以同步给不同的状态数据。通常意义为父组件传给子组件的数据。以下示例中数据源为count: 1。
- 命名参数机制：父组件通过指定参数传递给子组件的状态变量，为父子传递同步参数的主要手段。示例：CompA(aProp: this.aProp)。
- 从父组件初始化：父组件使用命名参数机制，将指定参数传递给子组件。子组件初始化的默认值在有父组件传值的情况下，会被覆盖。示例：

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Component
class MyComponent {
    @State
    var count: Int32 = 0
    private var increaseBy: Int32 = 1
    func build() {}
}

@Entry
@Component
class Parent {
    func build() {
        Column() {
            // 从父组件初始化，覆盖本地定义的默认值
            MyComponent(count: 1, increaseBy: 2)
        }
    }
}
```

- 初始化子组件：父组件中状态变量可以传递给子组件，初始化子组件对应的状态变量。示例同上。
- 本地初始化：在变量声明的时候赋值，作为变量的默认值。示例：@State count: Int32 = 0。

> **说明：**
>
> 当前状态管理的功能仅支持在UI主线程使用，不能在子线程、worker、taskpool中使用。