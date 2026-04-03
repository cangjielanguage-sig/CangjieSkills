## class ScanResult

```cangjie
public class ScanResult {
    public var deviceId: String
    public var rssi: Int32
    public var data: Array<Byte>
    public var deviceName: String
    public var connectable: Bool
}
```

**功能：** 扫描到符合过滤条件的广播报文后，上报的扫描数据。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var connectable

```cangjie
public var connectable: Bool
```

**功能：** 扫描到的设备是否可连接。true表示可连接，false表示不可连接。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var data

```cangjie
public var data: Array<Byte>
```

**功能：** 扫描到的设备发送的广播报文内容。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: String
```

**功能：** 扫描到的蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。

基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。

- 若和该设备地址配对成功后，该地址不会变更。

- 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。

- 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var deviceName

```cangjie
public var deviceName: String
```

**功能：** 扫描到的设备名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var rssi

```cangjie
public var rssi: Int32
```

**功能：** 扫描到的设备信号强度，单位：dBm。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22