## 导入模块

```cangjie
import kit.UIKit.*
```

## class LazyForEach

LazyForEach调用形式如下：

```cangjie
LazyForEach(dataSource: IDataSource<T>, itemGeneratorFunc: ItemGenFuncType<T>, keyGeneratorFunc: KeyGenFuncType<T>)
```

**功能：** 构建一个LazyForEach对象，LazyForEach从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占用。

> **说明：**
>
> - 数据懒加载必须在容器组件内使用，且仅有List、Grid以及Swiper组件支持数据的懒加载（即只加载可视部分以及其前后少量数据用于缓冲），其他组件仍然是一次加载所有的数据。
> - LazyForEach在每次迭代中，必须且只允许创建一个子组件。
> - 生成的子组件必须允许在LazyForEach的父容器组件中。
> - 允许LazyForEach包含在if/else条件渲染语句中，也允许LazyForEach中出现if/else条件渲染语句。
> - 键值生成器必须针对每个数据生成唯一的值，如果键值相同，将导致键值相同的UI组件渲染出现问题。
> - LazyForEach必须使用DataChangeListener对象来进行更新，第一个参数dataSource使用状态变量时，状态变量改变不会触发LazyForEach的UI刷新。
> - 为了高性能渲染，通过DataChangeListener对象的onDataChange方法来更新UI时，需要生成不同于原来的键值来触发组件刷新。
> - List使用LazyForEach加载子组件时，没有设置List的宽高，会加载所有子组件，设置了List的宽高，会加载List显示区域内的子组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [ComponentRender](./cj-ui-framework.md#interface-componentrender)

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataSource|ArrayList\<T>|是|-|LazyForEach数据源，需要开发者实现相关接口。|
|itemGeneratorFunc|(T,Int64)->Unit|是|-|子组件生成函数，为数组中的每一个数据项创建一个子组件。lambda函数的第一个泛型参数为数据类型，必须为FFIData的子类；第二个参数为当前列表项的索引值。|
|keyGeneratorFunc|(T,Int64)->String|是|-|匿名函数，用于键值生成，为给定数组项生成唯一且稳定的键值。当子项在数组中的位置更改时，子项的键值不得更改，当数组中的子项被新项替换时，被替换项的键值和新项的键值必须不同。键值生成器的功能是可选的，但是，为了使开发框架能够更好地识别数组更改，提高性能，建议提供。如将数组反向时，如果没有提供键值生成器，则LazyForEach中的所有节点都将重建。|