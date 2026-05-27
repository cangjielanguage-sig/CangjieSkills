### class TouchEvent

```cangjie
public class TouchEvent {
    public var isStopPropagation: Bool = false
    public TouchEvent(
        public var eventType: TouchType,
        public var touches: ArrayList<TouchObject>,
        public var changedTouches: ArrayList<TouchObject>,
        public var timestamp: Int64,
        public var target: EventTarget,
        public var source: SourceType
    )
}
```

**功能：** 继承于[BaseEvent](./cj-universal-gesture-judge.md#class-baseevent)。非事件注入场景下，changedTouches是按屏幕显示刷新率重采样的点，touches是按器件刷新率报上来的点，changedTouches的数据可能会和touches里面的不相同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var isStopPropagation

```cangjie
public var isStopPropagation: Bool = false
```

**功能：** 控制事件的传播。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var eventType

```cangjie
public var eventType: TouchType
```

**功能：** 触摸事件的类型。

**类型：** [TouchType](cj-common-types.md#enum-touchtype)

**读写能力：** 可读写

**起始版本：** 12

#### var touches

```cangjie
public var touches: ArrayList<TouchObject>
```

**功能：** 全部手指信息。

**类型：** ArrayList\<[TouchObject](#class-touchobject)>

**读写能力：** 可读写

**起始版本：** 12

#### var changedTouches

```cangjie
public var changedTouches: ArrayList<TouchObject>
```

**功能：** 当前发生变化的手指信息。

**类型：** ArrayList\<[TouchObject](#class-touchobject)>

**读写能力：** 可读写

**起始版本：** 12

#### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 距离开机时间的时间戳，单位为毫秒。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

#### var target

```cangjie
public var target: EventTarget
```

**功能：** 被触摸元素对象。

**类型：** [EventTarget](cj-universal-gesture-bind.md#class-eventtarget)

**读写能力：** 可读写

**起始版本：** 12

#### var source

```cangjie
public var source: SourceType
```

**功能：** 事件输入设备。

**类型：** [SourceType](cj-common-types.md#enum-sourcetype)

**读写能力：** 可读写

**起始版本：** 12

#### TouchEvent(TouchType, ArrayList\<TouchObject>, ArrayList\<TouchObject>, Int64, EventTarget, SourceType)

```cangjie
public TouchEvent(
    public var eventType: TouchType,
    public var touches: ArrayList<TouchObject>,
    public var changedTouches: ArrayList<TouchObject>,
    public var timestamp: Int64,
    public var target: EventTarget,
    public var source: SourceType
)
```

**功能：** 构造触摸事件类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[TouchType](cj-common-types.md#enum-touchtype)|是|-|触摸事件的类型。|
|touches|ArrayList\<[TouchObject](#class-touchobject)>|是|-|全部手指信息。|
|changedTouches|ArrayList\<[TouchObject](#class-touchobject)>|是|-|当前发生变化的手指信息。|
|timestamp|Int64|是|-|距离开机时间的时间戳，单位为毫秒。|
|target|[EventTarget](cj-universal-gesture-bind.md#class-eventtarget)|是|-|被触摸元素对象。|
|source|[SourceType](cj-common-types.md#enum-sourcetype)|是|-|事件输入设备。|