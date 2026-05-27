## 场景介绍

当应用的代码存在规范问题或错误时，会在运行中产生异常和错误，如应用未捕获异常、应用生命周期超时等。在错误产生后，应用会异常退出。错误日志通常会保存在用户本地存储上，不方便开发者定位问题。所以，应用开发者可以使用错误管理的接口，在应用退出前，及时将相关错误及日志上报到开发者的服务平台来定位问题。

使用errormanager接口监听异常和错误后，应用不会退出，如果只是为了获取错误日志，建议使用[hiappevent](./cj-hiappevent-watcher-crash-events.md)。

## 接口说明

应用错误管理接口由[errorManager](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-errormanager)模块提供，开发者可以通过import引入，详情请参见[开发示例](#开发示例)。

**错误管理接口功能介绍：**

| 接口名称                                                       | 说明                                                 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| on(onType: String, observer: ErrorObserver): Int32       | 注册错误观测器。注册后程序如果出现crash，会触发未捕获异常机制。|
| off(offType: String, observerId: Int32): Unit | 注销错误观测器。|
| on(\`type\`: String, timeout: Int64, observer: LoopObserver): Unit| 注册主线程消息处理耗时监听器。注册后可以捕获到应用主线程处理消息的具体执行时间。|
| off(\`type\`: String, observer!:? LoopObserver = None): Unit| 注销主线程消息处理监听器。|

**错误监听(ErrorObserver)接口功能介绍：**

| 接口名称                         | 说明                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| onUnhandledException(errMsg: String): Unit | 该回调函数调用场景：在程序运行中抛出异常且该异常未被任务‘try-catch’语句成功捕获。errMsg的内容固定为Uncaught exception was found.。 |
| onException?(errObject: ErrorObject): Unit | 该回调函数调用场景：在程序运行中抛出异常且该异常未被任务‘try-catch’语句成功捕获。errObject中包含了该未被捕获的异常的异常名称、异常信息与栈追踪。|

**应用主线程监听(LoopObserver)接口功能介绍：**

| 接口名称                         | 说明                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| onLoopTimeOut?(timeout: Int64): Unit| 应用主线程处理事件超时的回调，回调函数的参数是主线程消息实际执行时间（单位：毫秒）。|