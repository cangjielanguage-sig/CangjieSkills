# @State宏：组件内状态

\@State装饰的变量，或称为状态变量，一旦变量拥有了状态属性，就可以触发其直接绑定UI组件的刷新。当状态改变时，UI会发生对应的渲染改变。

在状态变量相关宏中，\@State是最基础的，使变量拥有状态属性的宏，它也是大部分状态变量的数据源。

在阅读\@State文档前，建议开发者对状态管理框架有基本的了解。建议提前阅读：[状态管理概述](./cj-state-management-overview.md)。

## 概述

\@State装饰的变量，与声明式范式中的其他被装饰变量一样，是私有的，只能从组件内部访问，在声明时必须指定其类型和本地初始化。初始化也可选择使用命名参数机制从父组件完成初始化。

\@State装饰的变量具有以下特点：

- \@State装饰的变量与子组件中的\@Prop装饰变量之间建立单向数据同步,与\@Link装饰变量之间建立双向数据同步。

- \@State装饰的变量生命周期与其所属自定义组件的生命周期相同。

## 宏使用规则说明

|\@State|说明|
|:---|:---|
|非属性宏|无。|
|同步类型|不与父组件中任何类型的变量同步。|
|允许装饰的变量类型|支持基础数据类型，对于String，Int64，Float64和Bool类型的变量，可以缺省类型。其他类型的变量不可缺省类型，必须被指定。<br/>支持Enum、Option类型、struct类型，struct类型内部无法修改。<br/>支持class类型，如果要感知内部的变化，在定义的时候需要被[\@Observed](./cj-macro-observed-and-publish.md)修饰，对类内属性和嵌套属性使用[\@Publish](./cj-macro-observed-and-publish.md)装饰后，才能观察到其变化。<br/>支持数组类型，如果要感知内部的变化，需要使用[ObservedArray\<T\>](../../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-componentstatemanagement.md#class-observedarray)和[ObservedArrayList\<T\>](../../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-componentstatemanagement.md#class-observedarraylist)。数组项为自定义类型时，使用[\@Observed](./cj-macro-observed-and-publish.md)和[\@Publish](./cj-macro-observed-and-publish.md)装饰时能观察到数组项中属性赋值。其他数组类型和Collection类型，如Array、Varray、ArrayList、HashMap和HashSet，支持赋值新的数组，但是无法监听内部元素的变化。<br/>支持[Color](../../../API_Reference//source_zh_cn/arkui-cj/cj-common-types.md#class-color)类型。<br/>支持类型的场景请参见[观察变化](#观察变化)。<br/>不支持Any。|
|被装饰变量的初始值|必须本地初始化。|

## 变量的传递/访问规则说明

|传递/访问|说明|
|:---|:---|
|从父组件初始化|可选，从父组件初始化或者本地初始化。如果从父组件初始化，从父组件传入的值，将会覆盖本地初始化；<br/>支持父组件中常规变量（常规变量对@State赋值，只是数值的初始化，常规变量的变化不会触发UI刷新，只有状态变量才能触发UI刷新）、\@State、[\@Link](./cj-macro-link.md)、[\@Prop](./cj-macro-prop.md)、[\@Provide](./cj-macro-provide-and-consume.md)、[\@Consume](./cj-macro-provide-and-consume.md)、[\@StorageLink](./cj-appstorage.md#storragelink)、[\@StorageProp](./cj-appstorage.md#storrageprop)装饰的变量，初始化子组件的\@State。|
|用于初始化子组件|\@State装饰的变量支持初始化子组件的常规变量、\@State、\@Link、\@Prop、\@Provide。|
|是否支持组件外访问|不支持，只能在组件内访问。|