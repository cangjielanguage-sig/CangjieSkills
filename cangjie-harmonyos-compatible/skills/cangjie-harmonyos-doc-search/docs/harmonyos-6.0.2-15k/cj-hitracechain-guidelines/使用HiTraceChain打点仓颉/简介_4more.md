## 简介

HiTraceChain是基于云计算分布式跟踪调用链思想，在端侧业务流程（涉及跨线程、跨进程、跨设备）中的一种轻量级实现。hiTraceChain在业务控制面流程中，生成和传递唯一跟踪标识，在业务流程中输出的各类信息中（包括应用事件、系统时间、日志等）记录该跟踪标识。在调试、问题定位过程中，开发者可以通过该唯一跟踪标识将本次业务流程端到端的各类信息快速关联起来。hiTraceChain为开发者提供业务流程调用链跟踪的维测接口，帮助开发者迅速获取指定业务流程调用链的运行日志，定位跨设备/跨进程/跨线程的故障问题。

## 基本概念

**chainId：** 分布式跟踪标识，属于HiTraceId的一部分，用于标识当前跟踪的业务流程。

## 接口说明

分布式跟踪接口由hiTraceChain模块提供，详细API请参见[分布式跟踪API参考](../../API_Reference/source_zh_cn/apis/PerformanceAnalysisKit/cj-apis-hi_tracechain.md)。

**分布式跟踪接口功能介绍：**

| 接口名                                                                                | 描述       |
| ------------------------------------------------------------------------------------- | ---------- |
| HiTraceChain.begin(name: String, flag!: Int32 = HiTraceFlag.DEFAULT.value): HiTraceId | 开始跟踪。 |
| HiTraceChain.end(id: HiTraceId): Unit                                                 | 结束跟踪。 |

## 开发步骤

以构造单次[应用事件打点](../../API_Reference/source_zh_cn/apis/PerformanceAnalysisKit/cj-apis-hiappevent.md)的业务说明分布式调用链的使用方法。

1. 新建一个仓颉应用工程，编辑工程中的“entry > src > main > cangjie > index.cj” 文件，添加一个按钮，完整示例代码如下：

    ```cangjie
    import kit.BasicServicesKit.*
    import kit.PerformanceAnalysisKit.*
    import ohos.base.*

    @Entry
    @Component
    class EntryView {
        @State
        var message: String = "Start writing an app event"

        func build() {
            Row {
                Column {
                    Button(this.message).fontSize(50).fontWeight(FontWeight.Bold).onClick {
                        evt => try {
                            // 业务开始前，开启分布式跟踪。
                            let traceId = HiTraceChain.begin("Write a new app event", HiTraceFlag.INCLUDE_ASYNC)
                            // 在按钮点击函数中进行事件打点，以记录按钮点击事件
                            let eventParams: Array<Parameters> = [Parameters("click_time", INT(100))]
                            let eventInfo: AppEventInfo = AppEventInfo(
                                // 事件领域定义
                                "button",
                                // 事件名称定义
                                "click",
                                // 事件类型定义
                                EventType.BEHAVIOR,
                                // 事件参数定义
                                eventParams
                            )
                            HiAppEvent.write(eventInfo)
                            // 业务结束，关闭分布式跟踪。
                            HiTraceChain.end(traceId)
                        } catch (e: BusinessException) {
                            AppLog.error("error message is ${e}")
                        }
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

2. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击“Start writing an app event”按钮，触发业务逻辑。

3. 在Log窗口查看分布式跟踪的相关信息，使用“.*\[([0-9a-zA-Z]{15}).*].*”过滤日志，查看该业务的分布式跟踪信息。hap进程号为“21519”，点击按钮触发的系统事件打点业务涉及到“21519”与“23924”两个线程，通过值为“a92ab94c18e1341”的chainId可以有效跟踪涉及该业务的所有线程的日志信息。

    ```text
    11-02 15:13:28.922  21519-21519  C02D03/HiTraceC                  com.example.hitracechaintest     I  [a92ab94c18e1341 0 0][dict]HiTraceBegin name:Write a new app event flags:0x01.
    11-02 15:13:28.924  21519-21519  C03915/AceInputTracking          com.example.hitracechaintest     I  [a92ab94c18e1341 0 0][ace_view_ohos.cpp(operator())-(0)] touch Event markProcessed in ace_view, eventInfo: id:764
    11-02 15:13:28.926  21519-23924  C02D07/HiAppEvent_ObserverMgr    com.example.hitracechaintest     I  [a92ab94c18e1341 0 0]start to handle event
    11-02 15:13:28.930  21519-21519  A00000/testTag                   com.example.hitracechaintest     I  [a92ab94c18e1341 324c3a3 0]Succeed to write an app event
    11-02 15:13:28.930  21519-21519  C02D03/HiTraceC                  com.example.hitracechaintest     I  [a92ab94c18e1341 324c3a3 0][dict]HiTraceEnd.
   ```