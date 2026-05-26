## class ViewBase

```cangjie
public open class ViewBase <: InteractableView & ComponentRender {}
```

**功能：** 组件基类，更多方法详见仓颉组件的通用属性、手势处理、动画相关章节。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [InteractableView](#class-interactableview)
- [ComponentRender](#interface-componentrender)

### func initial()

```cangjie
public open func initial(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func startTrace(String, Int32)

```cangjie
public func startTrace(name: String, taskId: Int32): This
```

**功能：** 标记一个预跟踪耗时任务的开始。

> **说明：**
>
> - 如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则每次调用该方法的taskId不相同。
> - 如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[finishTrace](../apis/PerformanceAnalysisKit/cj-apis-hi_tracemeter.md#static-func-finishtracestring-int32)中的示例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|要跟踪的任务名称。|
|taskId|Int32|是|-|任务id。|

### func update()

```cangjie
public func update(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## class ViewBuilder

```cangjie
public class ViewBuilder {
    public ViewBuilder(public let build: () -> Unit)
}
```

**功能：** UI框架使用的基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let build

```cangjie
public let build:() -> Unit
```

**功能：** UI框架使用。

**类型：** ()->Unit

**读写能力：** 只读

**起始版本：** 12

### ViewBuilder(() -> Unit)

```cangjie
public ViewBuilder(public let build: () -> Unit)
```

**功能：** 创建ViewBuilder类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|build|()->Unit|是|-|自定义组件。|

## class ViewStackProcessor

```cangjie
public class ViewStackProcessor {}
```

**功能：** UI框架使用的基础类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func AllocateNewElmetIdForNextComponent()

```cangjie
public static func AllocateNewElmetIdForNextComponent(): Int64
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|组件id。|

### static func GetElmtIdToAccountFor()

```cangjie
public static func GetElmtIdToAccountFor(): Int64
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|组件id。|

### static func ImplicitPopBeforeContinue()

```cangjie
public static func ImplicitPopBeforeContinue(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func StartGetAccessRecordingFor(Int64)

```cangjie
public static func StartGetAccessRecordingFor(elmtId: Int64): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|elmtId|Int64|是|-|-|

### static func StopGetAccessRecording()

```cangjie
public static func StopGetAccessRecording(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12