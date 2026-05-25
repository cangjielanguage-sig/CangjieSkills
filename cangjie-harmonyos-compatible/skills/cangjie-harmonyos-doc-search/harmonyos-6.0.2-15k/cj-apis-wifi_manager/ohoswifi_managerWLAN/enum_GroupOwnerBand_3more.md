## enum GroupOwnerBand

```cangjie
public enum GroupOwnerBand <: ToString {
    | GO_BAND_AUTO
    | GO_BAND_2GHZ
    | GO_BAND_5GHZ
    | ...
}
```

**功能：** 表示群组带宽。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**父类型：**

- ToString

### GO_BAND_2GHZ

```cangjie
GO_BAND_2GHZ
```

**功能：** 2.4GHZ。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### GO_BAND_5GHZ

```cangjie
GO_BAND_5GHZ
```

**功能：** 5GHZ。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### GO_BAND_AUTO

```cangjie
GO_BAND_AUTO
```

**功能：** 自动模式。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|

## enum P2pConnectState

```cangjie
public enum P2pConnectState <: ToString {
    | DISCONNECTED
    | CONNECTED
    | ...
}
```

**功能：** 表示P2P连接状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**父类型：**

- ToString

### CONNECTED

```cangjie
CONNECTED
```

**功能：** 连接状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### DISCONNECTED

```cangjie
DISCONNECTED
```

**功能：** 断开状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|

## enum P2pDeviceStatus

```cangjie
public enum P2pDeviceStatus <: ToString {
    | CONNECTED
    | INVITED
    | FAILED
    | AVAILABLE
    | UNAVAILABLE
    | ...
}
```

**功能：** 表示设备状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**父类型：**

- ToString

### AVAILABLE

```cangjie
AVAILABLE
```

**功能：** 可用状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### CONNECTED

```cangjie
CONNECTED
```

**功能：** 连接状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### FAILED

```cangjie
FAILED
```

**功能：** 失败状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### INVITED

```cangjie
INVITED
```

**功能：** 邀请状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### UNAVAILABLE

```cangjie
UNAVAILABLE
```

**功能：** 不可用状态。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|