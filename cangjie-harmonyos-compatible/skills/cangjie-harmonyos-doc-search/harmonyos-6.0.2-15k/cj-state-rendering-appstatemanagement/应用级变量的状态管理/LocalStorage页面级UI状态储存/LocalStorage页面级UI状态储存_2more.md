## LocalStorage（页面级UI状态储存）

LocalStorage是页面级的UI状态存储，通过@Entry装饰器接收的参数可以在页面内共享同一个LocalStorage实例。LocalStorage支持在同一个包内不同的页面之间共享。

### 使用说明

#### 概述

LocalStorage是仓颉为构建页面级别状态变量提供存储的内存内“数据库”。

- 应用程序可以创建多个LocalStorage实例，LocalStorage实例可以在包内共享。

- 组件树的根节点，即被@Entry装饰的@Component，可以被分配一个LocalStorage实例，此组件的所有子组件实例将自动获得对该LocalStorage实例的访问权限。

- 被@Component装饰的组件最多可以访问一个LocalStorage实例和AppStorage，未被@Entry装饰的组件不可被独立分配LocalStorage实例，只能接受父组件通过@Entry传递来的LocalStorage实例。一个LocalStorage实例在组件树上可以被分配给多个组件。

- LocalStorage中的所有属性都是可变的。

LocalStorage根据与@Component装饰的组件的同步类型不同，提供了两个装饰器：

- @LocalStorageProp：@LocalStorageProp装饰的变量与LocalStorage中给定属性建立单向同步关系。

- @LocalStorageLink：@LocalStorageLink装饰的变量与LocalStorage中给定属性建立双向同步关系。

#### 限制条件

- LocalStorage创建后，命名属性的类型不可更改。后续调用Set时必须使用相同类型的值。

- LocalStorage仅支持在同一个包内的不同页面中共享。