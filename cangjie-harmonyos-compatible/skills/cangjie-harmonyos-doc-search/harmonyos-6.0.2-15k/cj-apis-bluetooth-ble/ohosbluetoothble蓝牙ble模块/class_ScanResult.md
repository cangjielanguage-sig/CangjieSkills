## class ScanResult

```cangjie
public class ScanResult {}
```

**功能：** 扫描结果上报数据。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let connectable

```cangjie
public let connectable: Bool
```

**功能：** 表示扫描到的设备是否可连接。true表示可连接，false表示不可连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let data

```cangjie
public let data: Array<Byte>
```

**功能：** 表示扫描到的设备发送的广播包。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<Byte>

**读写能力：** 只读

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 表示扫描到的设备地址，例如："XX:XX:XX:XX:XX:XX"。基于信息安全考虑，此处获取的设备地址为随机MAC地址。配对成功后，该地址不会变更；已配对设备取消配对后重新扫描或蓝牙服务下电时，该随机地址会变更。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let deviceName

```cangjie
public let deviceName: String
```

**功能：** 表示扫描到的设备名称。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let rssi

```cangjie
public let rssi: Int32
```

**功能：** 表示扫描到的设备的rssi值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19