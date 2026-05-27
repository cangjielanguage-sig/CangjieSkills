# @Watch宏：状态变量更改通知

@Watch应用于对状态变量的监听。如果开发者需要关注某个状态变量的值是否改变，可以使用@Watch为状态变量设置回调函数。

@Watch提供了状态变量的监听能力，@Watch仅能监听到可以观察到的变化。

在阅读本文档前，建议开发者对状态管理基本观察能力有基本的了解。建议提前阅读：[@State](./cj-macro-state.md)。

## 概述

@Watch用于监听状态变量的变化，当状态变量变化时，@Watch的回调方法将被调用。@Watch在ArkUI框架内部判断数值有无更新使用的是严格相等（==），遵循严格相等规范。当严格相等判断的结果是false（即不相等）的情况下，就会触发@Watch的回调。

## 宏说明

| @Watch补充变量宏 | 说明 |
| :-------------------|:-----|
| 宏参数 |必填。回调方法名。|
| 宏的顺序 |宏顺序不影响实际功能，开发者可以根据自己的需要决定宏顺序的先后。建议[@State](./cj-macro-state.md)、[@Prop](./cj-macro-prop.md)、[@Link](./cj-macro-link.md)等宏在@Watch宏之前，以保持整体风格的一致。|
|@Watch触发时机|使用@Watch来监听状态变量变化时，回调触发时间是变量真正变化、被赋值的时间。|

## 观察变化和行为表现

1. 当观察到状态变量的变化（包括双向绑定的[AppStorage](./cj-appstorage.md)和[LocalStorage](./cj-localstorage.md)中对应的key发生的变化）的时候，对应的@Watch的回调方法将被触发；
2. @Watch方法在自定义组件的属性变更之后同步执行；
3. 如果在@Watch的方法里改变了其他的状态变量，也会引起状态变更和@Watch的执行；
4. 在第一次初始化的时候，@Watch装饰的方法不会被调用，即认为初始化不是状态变量的改变。只有在后续状态改变时，才会调用@Watch回调方法。

## 限制条件

- 建议开发者避免无限循环。循环可能是因为在@Watch的回调方法里直接或者间接地修改了同一个状态变量引起的。为了避免循环的产生，建议不要在@Watch的回调方法里修改当前装饰的状态变量；
- 开发者应关注性能，属性值更新函数会延迟组件的重新渲染（具体请见上面的行为表现），因此，回调函数应仅执行快速运算；
- 不建议在@Watch函数中调用异步操作，因为@Watch设计的用途是为了快速的计算，异步行为可能会导致重新渲染速度的性能问题。
- @Watch参数为必选，且参数必须是声明的方法名，否则编译期会报错。

  ```cangjie
  @State
  @Watch[]
  var count: Int64 = 10

  @State
  @Watch["onChanged"]
  var count: Int64 = 10
  // 正确写法
  @State
  @Watch[onChanged]
  var count: Int64 = 0

  func onChanged() {
      Hilog.info(0, "xxx", "xxx")
  }
  ```

- @Watch内的参数必须是声明的方法名，否则编译期会报错。

  ```cangjie
  // 错误写法，没有对应名称的函数，编译报错
  @State
  @Watch[change]
  var count: Int64 = 0

  func onChanged() {
      Hilog.info(0, "xxx", "xxx")
  }

  // 正确写法
  @State
  @Watch[change]
  var count: Int64 = 0

  func change() {
      Hilog.info(0, "xxx", "xxx")
  }
  ```

- 常规变量不能被@Watch装饰，否则编译期会报错。

  ```cangjie
  // 错误写法
  @Watch[change]
  var count: Int64 = 0

  func change() {
      Hilog.info(0, "xxx", "xxx")
  }

  // 正确写法
  @State
  @Watch[change]
  var count: Int64 = 0

  func change() {
      Hilog.info(0, "xxx", "xxx")
  }
  ```