### DescriptorWriteRequest(String, Int32, Int32, Bool, Bool, Array\<Byte>, String, String, String)

```cangjie
public DescriptorWriteRequest(
    public let deviceId: String,
    public let transId: Int32,
    public let offset: Int32,
    public let isPrepared: Bool,
    public let needRsp: Bool,
    public let value: Array<Byte>,
    public let descriptorUuid: String,
    public let characteristicUuid: String,
    public let serviceUuid: String
)
```

**功能：** DescriptorWriteRequest 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示发送描述符写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。|
|transId|Int32|是|表示写请求的传输ID，server端回复响应时需填写相同的传输ID。|
|offset|Int32|是|表示写描述符数据的起始位置。例如：k表示从第k个字节开始写，server端回复响应时需填写相同的offset。|
|isPrepared|Bool|是|表示写请求是否立即执行。|
|needRsp|Bool|是|表示是否要给client端回复响应。|
|value|Array\<Byte>|是|表示写入的描述符二进制数据。|
|descriptorUuid|String|是|表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。|
|characteristicUuid|String|是|特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。|
|serviceUuid|String|是|特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。|