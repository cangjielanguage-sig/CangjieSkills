# 使用HiDebug获取调试信息（仓颉）

HiDebug对外提供系统调试相关功能的接口，包括应用进程的静态堆内存（native heap）信息、应用进程内存占用PSS（Proportional Set Size）信息的获取等，也可完成虚拟机内存切片导出，虚拟机CPU Profiling采集等操作。

## 接口说明

| 接口名                          | 描述                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| getNativeHeapSize(): UInt64    | 获取内存分配器统计的进程持有的堆内存大小（含分配器元数据）。 |
| getNativeHeapAllocatedSize(): UInt64   | 获取内存分配器统计的进程业务分配的堆内存大小。               |
| getNativeHeapFreeSize(): UInt64      | 获取内存分配器持有的缓存内存大小。                           |
| getPss(): UInt64                     | 获取应用进程实际使用的物理内存大小。                         |
| getVss(): UInt64                     | 获取应用进程虚拟耗用内存大小。                               |
| getSharedDirty(): UInt64             | 获取进程的共享脏内存大小。                                   |
| getPrivateDirty(): UInt64            | 获取进程的私有脏内存大小。                                   |
| getCpuUsage(): Float64                | 获取进程的CPU使用率。                         |
| getServiceDump(serviceid: Int32, fd: Int32, args: Array\<String>): Unit      | 获取系统服务信息。                |
| getAppThreadCpuUsage(): Array\<ThreadCpuUsage>       | 获取应用线程CPU使用情况。                             |
| startAppTraceCapture(tags: Array\<UInt64>, flag: TraceFlag, limitSize: UInt32): String   | 启动应用trace采集。                |
| stopAppTraceCapture(): Unit        | 停止应用trace采集。                                          |
| getAppMemoryLimit() : MemoryLimit          | 获取应用程序进程内存限制。                                   |
| getSystemCpuUsage(): Float64          | 获取系统的CPU资源占用情况。                                  |
| setAppResourceLimit(type: String, value: Int32, enableDebugLog: Bool): Unit        | 设置应用的fd数量、线程数量、cj内存或者native内存资源限制。   |
| getAppNativeMemInfo(): NativeMemInfo        | 获取应用进程内存信息。                                       |
| getSystemMemInfo(): SystemMemInfo           | 获取系统内存信息。                                           |
| isDebugState(): Bool               | 获取应用进程被调试状态。                                     |

HiDebug的具体用法请参见[API参考文档](../../API_Reference/source_zh_cn/apis/PerformanceAnalysisKit/cj-apis-hidebug.md)。

## 开发示例

下文将展示如何在应用内增加一个按钮，并单击该按钮以调用hidebug接口。

1. 新建一个工程，选择“[Cangjie] Empty Ability”。

2. 在**Project**窗口单击entry &gt; src &gt; main &gt; cangjie，打开工程中的index.cj文件。

    新增一个方法调用hidebug接口，本文以hidebug.getSystemCpuUsage()为例，其他接口可参见[API参考文档](../../API_Reference/source_zh_cn/apis/PerformanceAnalysisKit/cj-apis-hidebug.md)。

    ```cangjie
    import kit.PerformanceAnalysisKit.*
    import kit.BasicServicesKit.*
    import ohos.base.*

    func testHidebug() {
        try {
            AppLog.info("getSystemCpuUsage: ${getSystemCpuUsage()}")
        } catch (e: BusinessException) {
            AppLog.error("error code: ${e.code}, error msg: ${e.message}");
        }
    }
    ```

    给文本Text组件添加一个点击事件，示例代码如下：

    ```cangjie
    @Entry
    @Component
    class EntryView {
        @State
        var message: String = "Hello World"

        func build() {
            Row {
                Column {
                    Text(this.message).fontSize(50).fontWeight(FontWeight.Bold).onClick {
                        evt =>
                        this.message = "Hello Cangjie"
                        testHidebug()
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

3. 在真机上运行该工程，单击应用/服务界面上的“Hello World”文本。

4. 在DevEco Studio的底部，切换到“Log”窗口，设置日志的过滤条件为“getSystemCpuUsage”。

    此时窗口将显示通过hidebug.getSystemCpuUsage()接口获取的CPU使用率的相关日志。

    ```Text

    04-24 10:09:55.004   20512-20512   A03903/m.examp...p/Cangjie-App  com.examp...n105temp  I     getSystemCpuUsage: 0.090157

    ```
