# LazyForEach：数据懒加载

API参数说明见：[LazyForEach API参数说明](../../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-lazyforeach.md)。

LazyForEach从提供的数据源中按需迭代数据，并在每次迭代过程中创建相应的组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占用

## 使用限制

- LazyForEach必须在容器组件内使用，仅有[List](../../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-list.md)、[Grid](../../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-grid.md)、[Swiper](../../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-swiper.md)以及[WaterFlow](../../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-waterflow.md)组件支持数据懒加载（可配置cachedCount属性，即只加载可视部分以及其前后少量数据用于缓冲），其他组件仍然是一次性加载所有的数据。
- LazyForEach依赖生成的键值判断是否刷新子组件，若键值不发生改变，则无法触发LazyForEach刷新对应的子组件。
- 容器组件内使用LazyForEach的时候，只能包含一个LazyForEach。以List为例，同时包含ListItem、ForEach、LazyForEach的情形是不推荐的；同时包含多个LazyForEach也是不推荐的。
- LazyForEach在每次迭代中，必须创建且只允许创建一个子组件；即LazyForEach的子组件生成函数有且只有一个根组件。
- 生成的子组件必须是允许包含在LazyForEach父容器组件中的子组件。
- 允许LazyForEach包含在if/else条件渲染语句中，也允许LazyForEach中出现if/else条件渲染语句。
- 键值生成器必须针对每个数据生成唯一的值，如果键值相同，将导致键值相同的UI组件渲染出现问题。
- LazyForEach必须使用DataChangeListener对象进行更新，对第一个参数dataSource重新赋值会异常；dataSource使用状态变量时，状态变量改变不会触发LazyForEach的UI刷新。
- 为了高性能渲染，通过DataChangeListener对象的onDataChange方法来更新UI时，需要生成不同于原来的键值来触发组件刷新。
- LazyForEach必须和@Reusable装饰器一起使用才能触发节点复用。使用方法：将[@Reusable](../paradigm/cj-macro-reusable.md)装饰在LazyForEach列表的组件上，见[使用规则](../paradigm/cj-macro-reusable.md)。

## 键值生成规则

在LazyForEach循环渲染过程中，系统会为每个item生成一个唯一且持久的键值，用于标识对应的组件。当这个键值变化时，ArkUI框架将视为该数组元素已被替换或修改，并会基于新的键值创建一个新的组件。

LazyForEach提供了一个名为keyGenerator的参数，这是一个函数，开发者可以通过它自定义键值的生成规则。如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即{data: T, idx: Int64 => return "\${viewID} - \${idx} - \${uniqueKey_}"}, viewId在编译器转换过程中生成，同一个LazyForEach组件内其viewId是一致的。