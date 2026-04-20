# ohos.multimodalInput.inputEvent（输入事件）

设备上报的基本事件。

## 导入模块

```cangjie
import kit.InputKit.*
```

## class InputEvent

```cangjie
public open class InputEvent {
    public InputEvent(
        public var id: Int32,
        public var deviceId: Int32,
        public var actionTime: Int64,
        public var screenId: Int32,
        public var windowId: Int32
    )
}
```

**功能：** 输入事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

### var id

```cangjie
public var id: Int32
```

**功能：** 事件id。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var deviceId

```cangjie
public var deviceId: Int32
```

**功能：** 上报输入事件的设备id。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var actionTime

```cangjie
public var actionTime: Int64
```

**功能：** 上报输入事件的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var screenId

```cangjie
public var screenId: Int32
```

**功能：** 目标屏幕id。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var windowId

```cangjie
public var windowId: Int32
```

**功能：** 目标窗口id。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### InputEvent(Int32, Int32, Int64, Int32, Int32)

```cangjie
public InputEvent(
    public var id: Int32,
    public var deviceId: Int32,
    public var actionTime: Int64,
    public var screenId: Int32,
    public var windowId: Int32
)
```

**功能：** 输入事件的构造函数。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int32|是|-|事件id。|
|deviceId|Int32|是|-|上报输入事件的设备id。|
|actionTime|Int64|是|-|上报输入事件的时间。|
|screenId|Int32|是|-|目标屏幕id。|
|windowId|Int32|是|-|目标窗口id。|
