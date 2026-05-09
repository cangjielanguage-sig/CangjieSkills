# 页面和自定义组件生命周期

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

在开始之前，需要先明确自定义组件和页面的关系：

- 自定义组件：[@Component](./cj-create-custom-components.md#component)修饰的UI单元，可以组合多个系统组件实现UI的复用，可以调用组件的生命周期。

- 页面：即应用的UI页面。可以由一个或者多个自定义组件组成，[@Entry](./cj-create-custom-components.md#entry)修饰的自定义组件为页面的入口组件，即页面的根节点，一个页面有且仅能有一个@Entry。只有被@Entry修饰的组件才可以调用页面的生命周期。

页面生命周期，即被@Entry修饰的组件生命周期，提供以下生命周期接口：

组件生命周期，即一般用@Component修饰的自定义组件的生命周期，提供以下生命周期接口：

生命周期流程如下图所示，下图展示的是被@Entry修饰的组件（页面）生命周期。

![lifecycle](./figures/lifecycle.png)

根据上面的流程图，本文从自定义组件的初始创建、重新渲染和删除来详细解释。

## 自定义组件的创建和渲染流程

1. 自定义组件的创建：自定义组件的实例由ArkUI框架创建。

2. 初始化自定义组件的成员变量：通过本地默认值或者构造方法传递参数来初始化自定义组件的成员变量，初始化顺序为成员变量的定义顺序。

3. 如果开发者定义了[aboutToAppear](../../reference/arkui-cj/cj-custom-component-lifecycle.md#func-abouttoappear)，则执行[aboutToAppear](../../reference/arkui-cj/cj-custom-component-lifecycle.md#func-abouttoappear)方法。

4. 在首次渲染的时候，执行build方法渲染系统组件，如果子组件为自定义组件，则创建自定义组件的实例。在首次渲染的过程中，框架会记录状态变量和组件的映射关系，当状态变量改变时，驱动其相关的组件刷新。

5. 如果开发者定义了onDidBuild，则执行onDidBuild方法。

## 自定义组件重新渲染

当事件句柄被触发（比如设置了点击事件，即触发点击事件）改变了状态变量时，或者LocalStorage / AppStorage中的属性更改，并导致绑定的状态变量更改其值时：

1. 框架观察到了变化，将启动重新渲染。

2. 根据框架持有的两个map（[自定义组件的创建和渲染流程](#自定义组件的创建和渲染流程)中第4步），框架可以知道该状态变量管理了哪些UI组件，以及这些UI组件对应的更新函数。执行这些UI组件的更新函数，实现最小化更新。