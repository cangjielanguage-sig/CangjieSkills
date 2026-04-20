## 定位步骤与思路

定位应用无响应问题，首先需要开发者获取相关日志，再通过日志记录的问题基本信息，结合hilog日志和trace来定位出无响应问题的发生的具体位置。

### 获取日志

应用无响应日志是一种故障日志，与Native进程崩溃、cj应用崩溃、系统进程异常等都由FaultLog模块管理，可通过以下方式获取日志：

- 方式一：通过DevEco Studio获取日志。

    DevEco Studio会收集设备的故障日志并归档到FaultLog下。

- 方式二：通过hiAppEvent接口订阅。

    hiAppEvent 提供了故障订阅接口，可以订阅各类故障打点，详情请参见[HiAppEvent介绍](./cj-hiappevent-intro.md)。