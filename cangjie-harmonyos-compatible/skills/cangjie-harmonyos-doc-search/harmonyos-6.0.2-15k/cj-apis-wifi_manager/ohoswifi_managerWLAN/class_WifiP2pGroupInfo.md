## class WifiP2pGroupInfo

```cangjie
public class WifiP2pGroupInfo <: ToString {
    public let isP2pGo: Bool
    public let ownerInfo: WifiP2pDevice
    public let passphrase: String
    public let interfaceName: String
    public let groupName: String
    public let networkId: Int32
    public let frequency: Int32
    public let clientDevices: Array<WifiP2pDevice>
    public let goIpAddress: String
}
```

**功能：** 表示P2P群组相关信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**父类型：**

- ToString

### let clientDevices

```cangjie
public let clientDevices: Array<WifiP2pDevice>
```

**功能：** 接入的设备列表信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**类型：** Array\<[WifiP2pDevice](#class-wifip2pdevice)>

**读写能力：** 只读

**起始版本：** 19

### let frequency

```cangjie
public let frequency: Int32
```

**功能：** 群组的频率。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let goIpAddress

```cangjie
public let goIpAddress: String
```

**功能：** 群组IP地址。

**类型：** String

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

### let interfaceName

```cangjie
public let interfaceName: String
```

**功能：** 接口名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let isP2pGo

```cangjie
public let isP2pGo: Bool
```

**功能：** 是否是群主。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let networkId

```cangjie
public let networkId: Int32
```

**功能：** 网络ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let ownerInfo

```cangjie
public let ownerInfo: WifiP2pDevice
```

**功能：** 群组的设备信息。

**类型：** [WifiP2pDevice](#class-wifip2pdevice)

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