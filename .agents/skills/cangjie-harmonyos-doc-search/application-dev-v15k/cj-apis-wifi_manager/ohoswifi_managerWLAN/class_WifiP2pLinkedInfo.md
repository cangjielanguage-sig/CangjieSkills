## class WifiP2pLinkedInfo

```cangjie
public class WifiP2pLinkedInfo <: ToString {
    public let connectState: P2pConnectState
    public let isGroupOwner: Bool
    public let groupOwnerAddr: String
}
```

**功能：** 提供WLAN连接的相关信息。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**父类型：**

- ToString

### let connectState

```cangjie
public let connectState: P2pConnectState
```

**功能：** P2P连接状态。

**类型：** [P2pConnectState](#enum-p2pconnectstate)

**读写能力：** 只读

**起始版本：** 19

### let groupOwnerAddr

```cangjie
public let groupOwnerAddr: String
```

**功能：** 群组IP地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let isGroupOwner

```cangjie
public let isGroupOwner: Bool
```

**功能：** 是否是群主。

**类型：** Bool

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