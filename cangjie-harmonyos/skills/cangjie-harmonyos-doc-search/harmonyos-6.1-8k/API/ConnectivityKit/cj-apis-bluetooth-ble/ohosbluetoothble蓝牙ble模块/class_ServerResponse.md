## class ServerResponse

```cangjie
public class ServerResponse {
    public var deviceId: String
    public var transId: Int32
    public var status: Int32
    public var offset: Int32
    public var value: Array<Byte>
    public init(
        deviceId: String,
        transId: Int32,
        status: Int32,
        offset: Int32,
        value: Array<Byte>
    )
}
```

**功能：** 描述server端回复client端读或者写请求的响应参数结构。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: String
```

**功能：** client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var offset

```cangjie
public var offset: Int32
```

**功能：** client端读或者写请求的数据偏移值，与订阅client端读或者写请求事件携带的offset保持一致。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var status

```cangjie
public var status: Int32
```

**功能：** 响应的状态，设置为0即可，表示正常。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var transId

```cangjie
public var transId: Int32
```

**功能：** 收到client端请求的标识符，与订阅client端读或者写请求事件携带的transId保持一致。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var value

```cangjie
public var value: Array<Byte>
```

**功能：** 回复的数据。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(String, Int32, Int32, Int32, Array\<Byte>)

```cangjie
public init(
    deviceId: String,
    transId: Int32,
    status: Int32,
    offset: Int32,
    value: Array<Byte>
)
```

**功能：** 描述server端回复client端读/写请求的响应参数类。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|是|-|client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。|
|transId|Int32|是|-|收到client端请求的标识符，与订阅client端读或者写请求事件携带的transId保持一致。|
|status|Int32|是|-|响应的状态，设置为0即可，表示正常。|
|offset|Int32|是|-|client端读或者写请求的数据偏移值，与订阅client端读或者写请求事件携带的offset保持一致。|
|value|Array\<Byte>|是|-|回复的数据。|