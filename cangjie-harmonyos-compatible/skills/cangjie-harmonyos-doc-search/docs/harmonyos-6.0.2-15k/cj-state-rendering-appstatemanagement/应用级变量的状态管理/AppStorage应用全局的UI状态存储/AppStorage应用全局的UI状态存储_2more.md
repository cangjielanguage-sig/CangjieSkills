## AppStorage（应用全局的UI状态存储）

AppStorage是应用全局的UI状态存储，是和应用的进程绑定的，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。

和页面级UI状态存储LocalStorage不同，AppStorage是应用级的全局UI状态存储，相当于整个应用的“中枢”，持久化数据PersistentStorage和环境变量Environment通过AppStorage中转，才可以和UI交互。

> **说明：**
>
> AppStorage仅支持纯仓颉场景，不支持用于ArkTS与仓颉混合开发场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### 使用说明

AppStorage是在应用启动的时候会被创建的单例。它的目的是为了提供应用状态数据的中心存储，这些状态数据在应用级别都是可访问的。AppStorage将在应用运行过程保留其属性。属性通过唯一的键字符串值访问。

AppStorage可以和UI组件同步，且可以在应用业务逻辑中被访问。

AppStorage支持应用的主线程内多个UIAbility实例间的状态共享。

AppStorage中的属性可以被双向同步，数据可以是存在于本地或远程设备上，并具有不同的功能，比如数据持久化（详见[PersistentStorage](#persistentstorage持久化存储ui状态)）。这些数据是通过业务逻辑中实现，与UI解耦，如果希望这些数据在UI中使用，需要用到@StorageProp和@StorageLink。