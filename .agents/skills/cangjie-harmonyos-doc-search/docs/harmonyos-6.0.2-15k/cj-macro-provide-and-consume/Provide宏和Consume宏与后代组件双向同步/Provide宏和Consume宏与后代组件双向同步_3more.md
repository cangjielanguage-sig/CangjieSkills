# @Provide宏和@Consume宏：与后代组件双向同步

`@Provide` 和 `@Consume`，应用于与后代组件的双向数据同步，应用于状态数据在多个层级之间传递的场景。不同于上文提到的父子组件之间通过命名参数机制传递，`@Provide` 和 `@Consume` 摆脱参数传递机制的束缚，实现跨层级传递。

其中`@Provide`装饰的变量是在祖先组件中，可以理解为被“提供”给后代的状态变量。`@Consume`装饰的变量是在后代组件中，去“消费（绑定）”祖先组件提供的变量。

`@Provide` / `@Consume` 是跨组件层级的双向同步。在阅读 `@Provide` 和 `@Consume` 文档前，建议开发者对UI范式基本语法和自定义组件有基本的了解。建议提前阅读：[基本语法概述](../paradigm/cj-basic-syntax-overview.md)，[声明式UI描述](../paradigm/cj-declarative-ui-description.md)，[自定义组件-创建自定义组件](../paradigm/cj-create-custom-components.md)。

## 概述

\@Provide / \@Consume装饰的状态变量有以下特性：

- \@Provide 装饰的状态变量自动对其所有后代组件可用，即该变量被“provide”给他的后代组件。由此可见，\@Provide 的方便之处在于，开发者不需要多次在组件之间传递变量。

- 后代通过使用 \@Consume 去获取 \@Provide 提供的变量，建立在 \@Provide 和 \@Consume 之间的双向数据同步，与 \@State / \@Link 不同的是，前者可以在多层级的父子组件之间传递。

- \@Provide 和 \@Consume 可以通过相同的变量名或者相同的变量别名绑定，需要类型相同，否则会发生类型隐式转换，从而导致应用行为异常。

```cangjie
// 通过相同的变量名绑定
@Provide
var age: Int64 = 0;
@Consume
var age: Int64;

// 通过相同的变量别名绑定
@Provide["a"]
var id: Float64 = 0.0;
@Consume["a"]
var age: Float64;
```

\@Provide 和 \@Consume通过相同的变量名或者相同的变量别名绑定时，\@Provide 装饰的变量和 \@Consume 装饰的变量是一对多的关系。如果在同一个自定义组件内，包括其子组件中声明多个同名或者同别名的 \@Provide 装饰的变量，\@Consume 声明的变量会向上查找匹配最近的 \@Provide 所修饰的变量。

同时，如果 \@Provide 注解中声明了别名，则需要根据对应的别名声明绑定 \@Consume 变量，根据变量名无法找到对应key的 \@Provide 变量。

## 宏说明

`@State` 的规则同样适用于 `@Provide`。不同之处在于 `@Provide` 还作为多层后代的同步源。

|\@Provide|说明|
|:---|:---|
|宏参数|别名：常量字符串，可选。如果指定了别名，则通过别名来绑定变量；如果未指定别名，则通过变量名绑定变量。|
|同步类型|双向同步。从 \@Provide 变量到所有 \@Consume 变量以及相反的方向的数据同步。双向同步的操作与 \@State 和 \@Link 的组合相同。|
|允许装饰的变量类型|仓颉内置类型包括基础数据类型（Nothing除外）和自定义类型，以及这些类型的数组。支持函数类型，支持DateTime类型。\@Provide 变量的 \@Consume 变量的类型必须相同。支持类型的场景请参考观察变化。|
|被装饰变量的初始值|必须指明类型，初始值必须指定。|
|\@Provide支持重名|允许重名，\@Consume 会向上查找匹配最近的 \@Provide。|

|\@Consume|说明|
|:---|:---|
|宏参数|别名：常量字符串，可选。如果提供了别名，则必须有 \@Provide 的变量和其有相同的别名才可以匹配成功；如果不提供别名，则需要变量名与变量类型都相同才能匹配成功。|
|同步类型|双向：从 \@Provide 变量（具体请参见 \@Provide ）到所有 \@Consume 变量，以及相反的方向。双向同步操作与 \@State 和 \@Link 的组合相同。|
|允许装饰的变量类型|仓颉内置类型包括基础数据类型（Nothing除外）和自定义类型，以及这些类型的数组。支持函数类型，支持DateTime类型。\@Provide 变量的 \@Consume 变量的类型必须相同。支持类型的场景请参考观察变化。|
|被装饰变量的初始值|必须指明类型，不能有初始值。|