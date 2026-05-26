## class WifiP2PConfig

```cangjie
public class WifiP2PConfig <: ToString {
    public WifiP2PConfig(
        public let deviceAddress: String,
        public let netId: Int32,
        public let passphrase: String,
        public let groupName: String,
        public let goBand: GroupOwnerBand,
        public let deviceAddressType!: DeviceAddressType = RANDOM_DEVICE_ADDRESS
    )
}
```

**功能：** 表示P2P配置信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**父类型：**

- ToString

### let deviceAddress

```cangjie
public let deviceAddress: String
```

**功能：** 设备地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let deviceAddressType

```cangjie
public let deviceAddressType: DeviceAddressType = RANDOM_DEVICE_ADDRESS
```

**功能：** 设备地址类型。

**类型：** [DeviceAddressType](#enum-deviceaddresstype)

**读写能力：** 只读

**起始版本：** 19

### let goBand

```cangjie
public let goBand: GroupOwnerBand
```

**功能：** 群组带宽。

**类型：** [GroupOwnerBand](#enum-groupownerband)

**读写能力：** 只读

**起始版本：** 19

### let groupName

```cangjie
public let groupName: String
```

**功能：** 群组名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let netId

```cangjie
public let netId: Int32
```

**功能：** 网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let passphrase

```cangjie
public let passphrase: String
```

**功能：** 群组密钥。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### WifiP2PConfig(String, Int32, String, String, GroupOwnerBand, DeviceAddressType)

```cangjie
public WifiP2PConfig(
    public let deviceAddress: String,
    public let netId: Int32,
    public let passphrase: String,
    public let groupName: String,
    public let goBand: GroupOwnerBand,
    public let deviceAddressType!: DeviceAddressType = RANDOM_DEVICE_ADDRESS
)
```

**功能：** 构造WifiP2PConfig实例。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceAddress|String|是|-|设备地址。|
|netId|Int32|是|-|网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。|
|passphrase|String|是|-|群组密钥。|
|groupName|String|是|-|群组名称。|
|goBand|[GroupOwnerBand](#enum-groupownerband)|是|-|群组带宽。|
|deviceAddressType|[DeviceAddressType](#enum-deviceaddresstype)|否|RANDOM_DEVICE_ADDRESS| **命名参数。** 设备地址类型。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前类的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前类的字符串表示。|