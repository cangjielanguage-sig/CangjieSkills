# @Link宏：父子双向同步

子组件中被\@Link装饰的变量与其父组件中对应的数据源建立双向数据绑定。

在阅读\@Link文档前，建议开发者首先了解[\@State](./cj-macro-state.md)的基本用法。

## 概述

\@Link装饰的变量与其父组件中的数据源共享相同的值。

## 宏使用规则说明

|\@Link|说明|
|:---|:---|
|非属性宏|无。|
|同步类型|双向同步。<br/>父组件中的状态变量可以与子组件\@Link修饰的变量建立双向同步，当其中一方改变时，另外一方能够感知到变化。|
|允许装饰的变量类型|支持基础数据类型，对于String，Int64，Float64和Bool类型的变量，可以缺省类型。其他类型的变量不可缺省类型，必须被指定。<br/>支持Enum、Option类型、struct类型，struct类型内部无法修改。<br/>支持class类型，如果要感知内部的变化，在定义的时候需要被[\@Observed](./cj-macro-observed-and-publish.md)修饰，对类内属性和嵌套属性使用[\@Publish](./cj-macro-observed-and-publish.md)装饰后，才能观察到其变化。<br/>支持数组类型，如果要感知内部的变化，需要使用[ObservedArray\<T\>](../../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-componentstatemanagement.md#class-observedarray)和[ObservedArrayList\<T\>](../../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-componentstatemanagement.md#class-observedarraylist)。数组项为自定义类型时，使用[\@Observed](./cj-macro-observed-and-publish.md)和[\@Publish](./cj-macro-observed-and-publish.md)装饰时能观察到数组项中属性赋值。其他数组类型和Collection类型，如Array、Varray、ArrayList、HashMap和HashSet，支持赋值新的数组，但是无法监听内部元素的变化。<br/>支持[Color](../../../API_Reference/source_zh_cn/arkui-cj/cj-common-types.md#class-color)类型。<br/>支持类型的场景请参见[观察变化](#观察变化)。<br/>不支持Any。|
|被装饰变量的初始值|\@Link装饰的变量必须使用其父组件提供的变量进行初始化，不允许在子组件中初始化。|

## 变量的传递/访问规则说明

|传递/访问|说明|
|:---|:---|
|从父组件初始化和更新|禁止本地初始化，初始化发生在创建其所属自定义组件实例时，初值由直接父组件中的状态变量提供。允许父组件中[\@State](./cj-macro-state.md)、\@Link、[\@Prop](./cj-macro-prop.md)、[\@Provide](./cj-macro-provide-and-consume.md)、[\@Consume](./cj-macro-provide-and-consume.md)装饰变量初始化子组件\@Link。|
|用于初始化子组件|允许作为数据源初始化子组件。可用于初始化常规变量、\@State、\@Link、\@Prop、\@Provide。|
|是否支持组件外访问|私有，只能在所属组件内访问。|