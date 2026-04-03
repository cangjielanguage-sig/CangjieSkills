## class BaseEvent

```cangjie
abstract sealed class BaseEvent {
    public var target: ?EventTarget
    public var timestamp: Int64
    public var source: ?SourceType
    public var deviceId: ?Int64
}
```

**功能：** 基础事件类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var target

```cangjie
public var target: ?EventTarget
```

**功能：** 触发事件的元素对象。

**类型：** ?[EventTarget](#class-eventtarget)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 事件时间戳，触发事件时距离系统启动的时间间隔。单位：ns

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var source

```cangjie
public var source: ?SourceType
```

**功能：** 事件输入设备的类型。

**类型：** ?[SourceType](#enum-sourcetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: ?Int64
```

**功能：** 触发当前事件的输入设备ID。初始值：0，取值范围：[0, +∞)。

**类型：** ?Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

## class ClickEvent

```cangjie
public class ClickEvent <: BaseEvent {
    public var displayX: Float64
    public var displayY: Float64
    public var windowX: Float64
    public var windowY: Float64
    public var x: Float64
    public var y: Float64
}
```

**功能：** 描述点击事件的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [BaseEvent](#class-baseevent)

### var displayX

```cangjie
public var displayX: Float64
```

**功能：** 标记点击点在屏幕左上角的横向绝对坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var displayY

```cangjie
public var displayY: Float64
```

**功能：** 标记点击点在屏幕左上角的纵向绝对坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var windowX

```cangjie
public var windowX: Float64
```

**功能：** 定位点击点在应用窗口左上角的横向坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var windowY

```cangjie
public var windowY: Float64
```

**功能：** 定位点击点在应用窗口左上角的纵向坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: Float64
```

**功能：** 记录点击点在元素内部的横向位置坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: Float64
```

**功能：** 记录点击点在元素内部的纵向位置坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22