# ohos.emitter（事件处理调度）

本模块提供了在同一进程不同线程间、或同一进程同一线程内，发送和处理事件的能力，包括持续订阅事件、单次订阅事件、取消订阅事件，以及发送事件到事件队列的能力。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class InnerEvent

```cangjie
public class InnerEvent {
    public InnerEvent(
        public var eventId: UInt32,
        public var priority!: EventPriority = LOW
    )
}
```

**功能：** 订阅或发送的事件。单次订阅事件时EventPriority无需指定，也不生效。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### var eventId

```cangjie
public var eventId: UInt32
```

**功能：** 事件ID，由开发者定义用来辨别事件。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 12

### var priority

```cangjie
public var priority: EventPriority = LOW
```

**功能：** 事件被投递的优先级。

**类型：** [EventPriority](#enum-eventpriority)

**读写能力：** 可读写

**起始版本：** 12

### InnerEvent(UInt32, EventPriority)

```cangjie
public InnerEvent(
    public var eventId: UInt32,
    public var priority!: EventPriority = LOW
)
```

**功能：** InnerEvent的构造函数。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventId|UInt32|是|-|事件ID，由开发者定义用来辨别事件。|
|priority|[EventPriority](#enum-eventpriority)|否|LOW| **命名参数。** 事件被投递的优先级。|