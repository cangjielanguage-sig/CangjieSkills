# AppStorage：应用全局的UI状态存储

AppStorage是应用全局的UI状态存储，是和应用的进程绑定的，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。

和AppStorage不同的是，LocalStorage是页面级的，通常应用于页面内的数据共享。而AppStorage是应用级的全局状态共享，还相当于整个应用的“中枢”，[持久化数据PersistentStorage](./cj-persiststorage.md)和[环境变量Environment](./cj-environment.md)都是通过AppStorage中转，才可以和UI交互。

> **说明：**
>
> AppStorage仅支持纯仓颉场景，不支持用于ArkTS与仓颉混合开发场景。

本文仅介绍AppStorage使用场景和相关的宏：@StorageProp和@StorageLink。

AppStorage是应用全局的UI状态存储，不同于@State等宏仅能在组件树上传递，AppStorage的目的是为了给开发者提供更大范围的跨ability基本的数据共享。在阅读本文档前，建议开发者对状态管理框架中AppStorage的定位有一个宏观了解。建议提前阅读：[状态管理概述](cj-state-management-overview.md)。

AppStorage还提供了API接口，可以让开发者通过接口在自定义组件外手动触发AppStorage对应key的增删改查，建议配合[AppStorage API文档](../../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-appstatemanagement.md#appstorage应用全局的ui状态存储)阅读。

## 概述

AppStorage是在应用启动的时候会被创建的单例。它的目的是为了提供应用状态数据的中心存储，这些状态数据在应用级别都是可访问的。AppStorage将在应用运行过程保留其属性。属性通过唯一的键字符串值访问。

AppStorage可以和UI组件同步，且可以在应用业务逻辑中被访问。

AppStorage支持应用的[主线程](../../../Dev_Guide/application-models/cj-thread-model-stage.md)内多个UIAbility实例间的状态共享。

AppStorage中的属性可以被双向同步，数据可以是存在于本地或远程设备上，本地和远程设备具有不同的功能，比如数据持久化（详见[PersistentStorage](./cj-persiststorage.md)）。这些数据是通过业务逻辑中实现，与UI解耦，如果希望这些数据在UI中使用，需要用到[@StorageProp](#storageprop)和[@StorageLink](#storagelink)。