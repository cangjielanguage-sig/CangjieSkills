## class HiAppEvent

```cangjie
public class HiAppEvent {}
```

**功能：** 该类提供了应用事件打点能力。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### static func addProcessor(Processor)

```cangjie
public static func addProcessor(processor: Processor): Int64
```

**功能：** 添加数据处理者配置信息，用于配置处理者接收的事件名等信息。事件发生后处理者可以接收事件。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|processor|[Processor](#class-processor)|是|-|上报事件的数据处理者。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|所添加上报事件数据处理者的ID，标识唯一数据处理者，可用于移除数据处理者。 添加失败返回-1，添加成功返回大于0的值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    var processor : Processor = Processor("test_processor")
    let processorId = HiAppEvent.addProcessor(processor)
    Hilog.info(0, "AppLogCj", "HiAppEvent::processorId is ${processorId}.", "")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```