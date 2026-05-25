## class KeyEvent

```cangjie
public class KeyEvent {
    public var keyType: KeyType
    public var keyCode: Int32
    public var keyText: String
    public var keySource: KeySource
    public var deviceId: Int64
    public var metaKey: Int32
    public var timestamp: Int64
    public init(keyText: String, keyType: KeyType, keyCode: Int32, keySource: KeySource, metaKey: Int32,
        deviceId: Int64, timestamp: Int64)
}
```

**功能：** 按键事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var keyText

```cangjie
public var keyText: String
```

**功能：** 按键的键值。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var keyType

```cangjie
public var keyType: KeyType
```

**功能：** 按键的类型。

**类型：** [KeyType](./cj-common-types.md#enum-keytype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var keyCode

```cangjie
public var keyCode: Int32
```

**功能：** 按键的键值。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var keySource

```cangjie
public var keySource: KeySource
```

**功能：** 触发当前按键的输入设备类型。

**类型：** [KeySource](./cj-common-types.md#enum-keysource)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var metaKey

```cangjie
public var metaKey: Int32
```

**功能：** 按键发生时元键的状态，1表示按压态，0表示未按压态。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: Int64
```

**功能：** 触发当前按键的输入设备ID。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 按键发生时的时间戳。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(String, KeyType, Int32, KeySource, Int32, Int64, Int64)

```cangjie
public init(keyText: String, keyType: KeyType, keyCode: Int32, keySource: KeySource, metaKey: Int32,
        deviceId: Int64, timestamp: Int64)
```

**功能：** 构造按键事件类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|keyText|String|是|-|按键的键值。|
|keyType|[KeyType](./cj-common-types.md#enum-keytype)|是|-|按键的类型。|
|keyCode|Int32|是|-|按键的键值。|
|keySource|[KeySource](./cj-common-types.md#enum-keysource)|是|-|触发当前按键的输入设备类型。|
|metaKey|Int32|是|-|按键发生时元键的状态，1表示按压态，0表示未按压态。|
|deviceId|Int64|是|-|触发当前按键的输入设备ID。|
|timestamp|Int64|是|-|按键发生时的时间戳。|

### func stopPropagation()

```cangjie
public func stopPropagation(): Unit
```

**功能：** 阻塞事件冒泡传递。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22