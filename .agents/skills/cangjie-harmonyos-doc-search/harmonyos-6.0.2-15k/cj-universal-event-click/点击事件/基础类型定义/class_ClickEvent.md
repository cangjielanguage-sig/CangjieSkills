### class ClickEvent

```cangjie
public class ClickEvent {
    public ClickEvent(
        public var x: Float64,
        public var y: Float64,
        public var timestamp: Int64,
        public var source: SourceType,
        public var target: EventTarget,
        public var windowX: Float64,
        public var windowY: Float64,
        public var displayX: Float64,
        public var displayY: Float64
    )
}
```

**功能：** 描述点击事件的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var displayX

```cangjie
public var displayX: Float64
```

**功能：** 标记点击点在屏幕左上角的横向绝对坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var displayY

```cangjie
public var displayY: Float64
```

**功能：** 标记点击点在屏幕左上角的纵向绝对坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var source

```cangjie
public var source: SourceType
```

**功能：** 标识触发点击的设备类型。

**类型：** [SourceType](./cj-common-types.md#enum-sourcetype)

**读写能力：** 可读写

**起始版本：** 12

#### var target

```cangjie
public var target: EventTarget
```

**功能：** 触发事件的元素对象显示区域。

**类型：** [EventTarget](#class-eventtarget)

**读写能力：** 可读写

**起始版本：** 12

#### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 记录事件发生与系统启动之间的时间间隔。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

#### var windowX

```cangjie
public var windowX: Float64
```

**功能：** 定位点击点在应用窗口左上角的横向坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var windowY

```cangjie
public var windowY: Float64
```

**功能：** 定位点击点在应用窗口左上角的纵向坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var x

```cangjie
public var x: Float64
```

**功能：** 记录点击点在元素内部的横向位置坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var y

```cangjie
public var y: Float64
```

**功能：** 记录点击点在元素内部的纵向位置坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### ClickEvent(Float64, Float64, Int64, SourceType, EventTarget, Float64, Float64, Float64, Float64)

```cangjie
public ClickEvent(
    public var x: Float64,
    public var y: Float64,
    public var timestamp: Int64,
    public var source: SourceType,
    public var target: EventTarget,
    public var windowX: Float64,
    public var windowY: Float64,
    public var displayX: Float64,
    public var displayY: Float64
)
```

**功能：** 构造一个ClickEvent类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|点击位置相对于被点击元素左边缘的X坐标。|
|y|Float64|是|-|点击位置相对于被点击元素原始区域左上角的Y坐标。|
|timestamp|Int64|是|-|事件时间戳。触发事件时距离系统启动的时间间隔。|
|source|[SourceType](./cj-common-types.md#enum-sourcetype)|是|-|事件输入设备。|
|target|[EventTarget](#class-eventtarget)|是|-|触发事件的元素对象显示区域。|
|windowX|Float64|是|-|点击位置相对于应用窗口左上角的X坐标。|
|windowY|Float64|是|-|点击位置相对于应用窗口左上角的Y坐标。|
|displayX|Float64|是|-|点击位置相对于应用屏幕左上角的X坐标。|
|displayY|Float64|是|-|点击位置相对于应用屏幕左上角的Y坐标。|