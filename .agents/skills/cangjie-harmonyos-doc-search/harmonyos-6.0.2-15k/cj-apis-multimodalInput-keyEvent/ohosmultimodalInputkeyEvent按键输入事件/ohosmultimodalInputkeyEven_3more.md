# ohos.multimodalInput.keyEvent（按键输入事件）

设备上报的按键事件，继承自[InputEvent](./cj-apis-multimodalInput-inputEvent.md#class-inputevent)。

## 导入模块

```cangjie
import kit.InputKit.*
```

## class Key

```cangjie
public class Key {
    public Key(
        public var code: KeyCode,
        public var pressedTime: Int64,
        public var deviceId: Int32
    )
}
```

**功能：** 按键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

### var code

```cangjie
public var code: KeyCode
```

**功能：** 按键码。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** [KeyCode](cj-apis-multimodalInput-keyCode.md#enum-keycode)

**读写能力：** 可读写

**起始版本：** 19

### var pressedTime

```cangjie
public var pressedTime: Int64
```

**功能：** 按键按下时间，单位为微秒（μs）。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var deviceId

```cangjie
public var deviceId: Int32
```

**功能：** 按键所属设备id。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### Key(KeyCode, Int64, Int32)

```cangjie
public Key(
    public var code: KeyCode,
    public var pressedTime: Int64,
    public var deviceId: Int32
)
```

**功能：** Key的构造函数。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|[KeyCode](cj-apis-multimodalInput-keyCode.md#enum-keycode)|是|-|按键码。|
|pressedTime|Int64|是|-|按键按下时间，单位为微秒（μs）。|
|deviceId|Int32|是|-|按键所属设备id。|