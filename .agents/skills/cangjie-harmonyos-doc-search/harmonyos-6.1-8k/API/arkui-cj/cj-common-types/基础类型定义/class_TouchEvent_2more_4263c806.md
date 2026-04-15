## class TouchEvent

```cangjie
public class TouchEvent <: BaseEvent {
    public var eventType: TouchType
    public var touches: Array<TouchObject>
    public var changedTouches: Array<TouchObject>
}
```

**功能：** 非事件注入场景下，changedTouches是按屏幕显示刷新率重采样的点，touches是按器件刷新率报上来的点，changedTouches的数据可能会和touches里面的不相同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BaseEvent](#class-baseevent)

### var eventType

```cangjie
public var eventType: TouchType
```

**功能：** 触摸事件的类型。

**类型：** [TouchType](cj-common-types.md#enum-touchtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var touches

```cangjie
public var touches: Array<TouchObject>
```

**功能：** 全部手指信息。

**类型：** Array\<[TouchObject](#class-touchobject)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var changedTouches

```cangjie
public var changedTouches: Array<TouchObject>
```

**功能：** 当前发生变化的手指信息。

**类型：** Array\<[TouchObject](#class-touchobject)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func stopPropagation()

```cangjie
public func stopPropagation(): Unit
```

**功能：** 停止事件传播。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

## class EventTarget

```cangjie
public class EventTarget {
    public var area: Area
    public init(area: Area)
}
```

**功能：** 事件目标对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var area

```cangjie
public var area: Area
```

**功能：** 事件目标区域。

**类型：** [Area](#class-area)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Area)

```cangjie
public init(area: Area)
```

**功能：** 构造一个EventTarget对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|area|[Area](#class-area)|是|-|事件目标区域。|