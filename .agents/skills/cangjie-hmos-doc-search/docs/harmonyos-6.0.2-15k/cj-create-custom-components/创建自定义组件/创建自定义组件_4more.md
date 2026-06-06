# 创建自定义组件

在ArkUI中，UI显示的内容均为组件，由框架直接提供的称为系统组件，由开发者定义的称为自定义组件。在进行 UI 界面开发时，通常不是简单的将系统组件进行组合使用，而是需要考虑代码可复用性、业务逻辑与UI分离，后续版本演进等因素。因此，将UI和部分业务逻辑封装成自定义组件是不可或缺的能力。

自定义组件具有以下特点：

- 可组合：允许开发者组合使用系统组件、及其属性和方法。
- 可重用：自定义组件可以被其他组件重用，并作为不同的实例在不同的父组件或容器中使用。
- 数据驱动UI更新：通过状态变量的改变，来驱动UI的刷新。

## 自定义组件的基本用法

以下示例展示了自定义组件的基本用法。

```cangjie
@Component
class HelloComponent {
    @State
    var message: String = "Hello, World!"
    func build() {
        // HelloComponent自定义组件组合系统组件Row和Text
        Row() {
            Text(this.message)
                // 状态变量message的改变驱动UI刷新，UI从"Hello, World!"刷新为"Hello, Cangjie!"
                .onClick({etv => this.message = "Hello, Cangjie!"})
        }
    }
}
```

HelloComponent可以在其他自定义组件中的build()函数中多次创建，实现自定义组件的重用。

```cangjie
@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Text("ArkUI message")
            HelloComponent(message: "Hello, World!")
            Divider()
            HelloComponent(message: "你好，世界!")
        }
    }
}
```

要完全理解上面的示例，需要了解自定义组件的以下概念定义，本文将在后面的小节中介绍。

## 自定义组件的基本结构

### class

自定义组件基于class实现，class + 自定义组件名 + {...}的组合构成自定义组件，不能有继承关系。

> **说明：**
>
> 自定义组件名、类名、函数名不能和系统组件名相同。

### @Component

@Component宏仅能装饰class关键字声明的数据结构。class被@Component装饰后具备组件化的能力，需要实现build方法描述UI，一个class只能被一个@Component装饰。

```cangjie
@Component
class MyComponent {}
```

使用限制：

一个被@Component修饰的class类型(自定义组件)的成员变量（包括普通成员变量、状态变量）总数不能超过128个。

### build()函数

build()函数用于定义自定义组件的声明式UI描述，自定义组件必须定义build()函数。

```cangjie
@Component
class MyComponent {
    func build() {
    }
}
```

### @Entry

@Entry装饰的自定义组件将作为UI页面的入口。在单个UI页面中，最多可以使用@Entry装饰一个自定义组件。@Entry可以接受一个可选的[LocalStorage](../state_management/cj-localstorage.md)的参数。

```cangjie
@Entry
@Component
class MyComponent {}
```

#### EntryOptions

|名称|类型|必填|说明|
|:---|:---|:---|:---|
|storage|[LocalStorage](../state_management/cj-localstorage.md)|否|页面级的UI状态存储。|

### @Reusable

@Reusable装饰的自定义组件具备可复用能力。详细请参见：[@Reusable宏：组件复用](./cj-macro-reusable.md#使用场景)。

```cangjie
@Reusable
@Component
class MyComponent {}
```

## 成员函数/变量

自定义组件除了必须要实现build()函数外，还可以实现其他成员函数，成员函数具有以下约束：

- 自定义组件的成员函数为私有的，且不建议声明成静态函数。

自定义组件可以包含成员变量，成员变量具有以下约束：

- 自定义组件的成员变量为私有的，且不建议声明成静态变量。
- 自定义组件的成员变量本地初始化有些是可选的，有些是必选的。具体是否需要本地初始化，是否需要从父组件通过参数传递初始化子组件的成员变量，请参见[状态管理](../state_management/cj-state-management-overview.md)。