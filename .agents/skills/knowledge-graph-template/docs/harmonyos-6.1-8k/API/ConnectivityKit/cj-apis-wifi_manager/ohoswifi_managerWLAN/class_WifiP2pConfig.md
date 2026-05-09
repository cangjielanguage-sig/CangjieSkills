## class WifiP2pConfig

```cangjie
public class WifiP2pConfig {
    public var deviceAddress: String
    public var netId: Int32
    public var passphrase: String
    public var groupName: String
    public var goBand: GroupOwnerBand
    public var deviceAddressType: DeviceAddressType
    public init(
        deviceAddress: String,
        netId: Int32,
        passphrase: String,
        groupName: String,
        goBand: GroupOwnerBand,
        deviceAddressType!: DeviceAddressType = RandomDeviceAddress
    )
}
```

**功能：** 表示P2P配置信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### var deviceAddress

```cangjie
public var deviceAddress: String
```

**功能：** 设备地址。

**类型：** String

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### var deviceAddressType

```cangjie
public var deviceAddressType: DeviceAddressType
```

**功能：** 设备地址类型。

**类型：** [DeviceAddressType](#enum-deviceaddresstype)

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### var goBand

```cangjie
public var goBand: GroupOwnerBand
```

**功能：** 群组带宽。

**类型：** [GroupOwnerBand](#enum-groupownerband)

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### var groupName

```cangjie
public var groupName: String
```

**功能：** 群组名称。

**类型：** String

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### var netId

```cangjie
public var netId: Int32
```

**功能：** 网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。

**类型：** Int32

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### var passphrase

```cangjie
public var passphrase: String
```

**功能：** 群组密钥。

**类型：** String

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### init(String, Int32, String, String, GroupOwnerBand, DeviceAddressType)

```cangjie
public init(
    deviceAddress: String,
    netId: Int32,
    passphrase: String,
    groupName: String,
    goBand: GroupOwnerBand,
    deviceAddressType!: DeviceAddressType = RandomDeviceAddress
)
```

**功能：** 构造WifiP2PConfig实例。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceAddress|String|是|-|设备地址。|
|netId|Int32|是|-|网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。|
|passphrase|String|是|-|群组密钥。|
|groupName|String|是|-|群组名称。|
|goBand|[GroupOwnerBand](#enum-groupownerband)|是|-|群组带宽。|
|deviceAddressType|[DeviceAddressType](#enum-deviceaddresstype)|否|RandomDeviceAddress| **命名参数。** 设备地址类型。|