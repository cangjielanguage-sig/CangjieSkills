## class HiAppEvent

```cangjie
public class HiAppEvent {}
```

**功能：** 该类提供了应用事件打点能力。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### static func addProcessor(Processor)

```cangjie
public static func addProcessor(processor: Processor): Int64
```

**功能：** 开发者可添加数据处理者，该数据处理者用于提供事件上云功能，数据处理者的实现可预置在设备中，开发者可根据数据处理者的约束设置属性。

Processor的配置信息需要由数据处理者提供，目前设备内暂未预置可供交互的数据处理者，因此当前事件上云功能不可用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|processor|[Processor](#class-processor)|是|-|上报事件的数据处理者。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|所添加上报事件数据处理者的ID。添加失败返回-1，添加成功返回大于0的值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*

var processor : Processor = Processor("test_processor")
let processorId = HiAppEvent.addProcessor(processor)
Hilog.info(0, "HiAppEvent", "HiAppEvent::processorId is ${processorId}.")
```