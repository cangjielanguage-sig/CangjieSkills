## class ServerResponse

```cangjie
public class ServerResponse {
    public ServerResponse(
        public let deviceId: String,
        public let transId: Int32,
        public let status: Int32,
        public let offset: Int32,
        public let value: Array<Byte>
    )
}
```

**功能：** 描述server端回复client端读/写请求的响应参数类。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let offset

```cangjie
public let offset: Int32
```

**功能：** 表示请求的读/写起始位置，与订阅的读/写请求事件携带的offset保持一致。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let status

```cangjie
public let status: Int32
```

**功能：** 表示响应的状态，设置为0即可，表示正常。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let transId

```cangjie
public let transId: Int32
```

**功能：** 表示请求的传输ID，与订阅的读/写请求事件携带的ID保持一致。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let value

```cangjie
public let value: Array<Byte>
```

**功能：** 表示回复响应的二进制数据。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<Byte>

**读写能力：** 只读

**起始版本：** 19

### ServerResponse(String, Int32, Int32, Int32, Array\<Byte>)

```cangjie
public ServerResponse(
    public let deviceId: String,
    public let transId: Int32,
    public let status: Int32,
    public let offset: Int32,
    public let value: Array<Byte>
)
```

**功能：** ServerResponse 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。|
|transId|Int32|是|表示请求的传输ID，与订阅的读/写请求事件携带的ID保持一致。|
|status|Int32|是|表示响应的状态，设置为0即可，表示正常。|
|offset|Int32|是|表示请求的读/写起始位置，与订阅的读/写请求事件携带的offset保持一致。|
|value|Array\<Byte>|是|表示回复响应的二进制数据。|