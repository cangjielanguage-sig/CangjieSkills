# LocalStorage：页面级UI状态存储

LocalStorage是页面级的UI状态存储，通过@Entry宏接收的参数可以在页面内共享同一个LocalStorage实例。LocalStorage支持UIAbility实例内多个页面间状态共享。

在阅读本文档前，建议开发者对状态管理框架有基本的了解。建议提前阅读：[状态管理概述](cj-state-management-overview.md)。

LocalStorage还提供了API接口，可以让开发者通过接口在自定义组件外手动触发Storage对应key的增删改查，建议配合[LocalStorage API文档](../../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-appstatemanagement.md#localstorage页面级ui状态储存)阅读。

## 概述

LocalStorage是Cangjie为构建页面级别状态变量提供存储的内存内的“数据库”。

- 应用程序可以创建多个LocalStorage实例，LocalStorage实例可以在页面内共享，也可以实现跨页面、UIAbility实例内共享。
- 组件树的根节点，即被@Entry装饰的@Component，可以被分配一个LocalStorage实例，此组件的所有子组件实例将自动获得对该LocalStorage实例的访问权限。
- 被@Component装饰的组件最多可以访问一个LocalStorage实例和AppStorage，未被@Entry装饰的组件不可被独立分配LocalStorage实例，只能接受父组件通过@Entry传递来的LocalStorage实例。一个LocalStorage实例在组件树上可以被分配给多个组件。
- LocalStorage中的所有属性都是可变的。

应用程序决定LocalStorage对象的生命周期。当应用释放最后一个指向LocalStorage的引用时，比如销毁最后一个自定义组件，LocalStorage将被垃圾回收。

LocalStorage根据与@Component装饰的组件的同步类型不同，提供了两个宏：

- [@LocalStorageProp](#localstorageprop)：@LocalStorageProp装饰的变量与LocalStorage中给定属性建立单向同步关系。
- [@LocalStorageLink](#localstoragelink)：@LocalStorageLink装饰的变量与LocalStorage中给定属性建立双向同步关系。