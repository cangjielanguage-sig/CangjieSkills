## class DescriptorReadRequest

```cangjie
public class DescriptorReadRequest {
    public DescriptorReadRequest(
        public let deviceId: String,
        public let transId: Int32,
        public let offset: Int32,
        public let descriptorUuid: String,
        public let characteristicUuid: String,
        public let serviceUuid: String
    )
}
```

**功能：** 描述server端订阅后收到的描述符读请求事件参数类。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let characteristicUuid

```cangjie
public let characteristicUuid: String
```

**功能：** 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let descriptorUuid

```cangjie
public let descriptorUuid: String
```

**功能：** 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 表示发送描述符读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let offset

```cangjie
public let offset: Int32
```

**功能：** 表示读描述符数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let serviceUuid

```cangjie
public let serviceUuid: String
```

**功能：** 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let transId

```cangjie
public let transId: Int32
```

**功能：** 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### DescriptorReadRequest(String, Int32, Int32, String, String, String)

```cangjie
public DescriptorReadRequest(
    public let deviceId: String,
    public let transId: Int32,
    public let offset: Int32,
    public let descriptorUuid: String,
    public let characteristicUuid: String,
    public let serviceUuid: String
)
```

**功能：** DescriptorReadRequest 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示发送描述符读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。|
|transId|Int32|是|表示读请求的传输ID，server端回复响应时需填写相同的传输ID。|
|offset|Int32|是|表示读描述符数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。|
|descriptorUuid|String|是|表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。|
|characteristicUuid|String|是|特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。|
|serviceUuid|String|是|特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。|