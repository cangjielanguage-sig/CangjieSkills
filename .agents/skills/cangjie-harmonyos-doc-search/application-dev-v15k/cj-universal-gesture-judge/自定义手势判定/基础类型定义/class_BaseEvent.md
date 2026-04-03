### class BaseEvent

```cangjie
public open class BaseEvent {
    public let target: EventTarget,
    public let timestamp: Int64,
    public let source: SourceType,
    public let pressure: Float64,
    public let tiltX: Int64,
    public let tiltY: Int64,
    public let sourceTool: SourceTool,
    public let axisHorizontal: Option<Float32>,
    public let axisVertical: Option<Float32>,
    public let getModifierKeyState: Option<(Array<String>) -> Bool>,
    public let deviceId: Int64
}
```

**功能：** 基础事件信息基类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let axisHorizontal

```cangjie
public let axisHorizontal: Option<Float32>
```

**功能：** 水平轴值。

**类型：** Option\<Float32>

**读写能力：** 只读

**起始版本：** 19

#### let axisVertical

```cangjie
public let axisVertical: Option<Float32>
```

**功能：** 垂直轴值。

**类型：** Option\<Float32>

**读写能力：** 只读

**起始版本：** 19

#### let deviceId

```cangjie
public let deviceId: Int64
```

**功能：** 触发当前事件的输入设备ID。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

#### let getModifierKeyState

```cangjie
public let getModifierKeyState: Option <(Array<String>) -> Bool>
```

**功能：** 获取功能键按压状态。报错信息请参考以下错误码。支持功能键 'Ctrl'|'Alt'|'Shift'|'Fn'，设备外接带Fn键的键盘不支持Fn键查询。

**类型：** Option\<(Array\<String>)->Bool>

**读写能力：** 只读

**起始版本：** 19

#### let pressure

```cangjie
public let pressure: Float64
```

**功能：** 按压的压力大小。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

#### let source

```cangjie
public let source: SourceType
```

**功能：** 事件输入设备。

**类型：** [SourceType](./cj-common-types.md#enum-sourcetype)

**读写能力：** 只读

**起始版本：** 19

#### let sourceTool

```cangjie
public let sourceTool: SourceTool
```

**功能：** 事件输入源。

**类型：** [SourceTool](./cj-common-types.md#enum-sourcetool)

**读写能力：** 只读

**起始版本：** 19

#### let target

```cangjie
public let target: EventTarget
```

**功能：** 手势标记。

**类型：** [EventTarget](./cj-universal-gesture-bind.md#class-eventtarget)

**读写能力：** 只读

**起始版本：** 19

#### let tiltX

```cangjie
public let tiltX: Int64
```

**功能：** 手写笔在设备平面上的投影与设备平面X轴的夹角。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

#### let tiltY

```cangjie
public let tiltY: Int64
```

**功能：** 手写笔在设备平面上的投影与设备平面Y轴的夹角。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

#### let timestamp

```cangjie
public let timestamp: Int64
```

**功能：** 事件时间戳。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19