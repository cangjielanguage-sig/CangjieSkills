# ForEach：循环渲染

ForEach接口基于数组类型数据来进行循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。例如，ListItem组件要求ForEach的父容器组件必须为[List组件](../../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-list.md)。详情请参见：ForEach [API参数说明](../../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-foreach.md)。

## 键值生成规则

在ForEach循环渲染过程中，系统会为每个数组元素生成一个唯一且持久的键值，用于标识对应的组件。当这个键值变化时，仓颉将视为该数组元素已被替换或修改，并会基于新的键值创建一个新的组件。

ForEach提供了一个名为keyGeneratorFunc的参数，这是一个函数，开发者可以通过它自定义键值的生成规则。如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数。

ArkUI框架对于ForEach的键值生成有一套特定的判断规则，这主要与itemGenerator函数的第二个参数index以及keyGeneratorFunc函数的第二个参数index有关。

> **说明：**
>
> ArkUI框架会对重复的键值发出警告。在UI更新的场景下，如果出现重复的键值，框架可能无法正常工作，具体请参见[渲染结果非预期](#渲染结果非预期)。

## 组件创建规则

在确定键值生成规则后，ForEach的第二个参数itemGeneratorFunc函数会根据键值生成规则为数据源的每个数组项创建组件。组件的创建包括两种情况：[ForEach首次渲染](#首次渲染)和[ForEach非首次渲染](#非首次渲染)。