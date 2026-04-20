## enum NetConnectionEvent

```cangjie
public enum NetConnectionEvent <: Equatable<NetConnectionEvent> {
    | NetAvailable
    | NetBlockStatusChange
    | NetCapabilitiesChange
    | NetConnectionPropertiesChange
    | NetLost
    | NetUnavailable
    | ...
}
```

**功能：** 网络连接事件类型。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<NetConnectionEvent>

### NetAvailable

```cangjie
NetAvailable
```

**功能：** 网络可用事件。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetBlockStatusChange

```cangjie
NetBlockStatusChange
```

**功能：** 网络阻塞状态变化事件。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetCapabilitiesChange

```cangjie
NetCapabilitiesChange
```

**功能：** 网络能力变化事件。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetConnectionPropertiesChange

```cangjie
NetConnectionPropertiesChange
```

**功能：** 网络连接信息变化事件。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetLost

```cangjie
NetLost
```

**功能：** 网络丢失事件。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetUnavailable

```cangjie
NetUnavailable
```

**功能：** 网络不可用事件。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### func !=(NetConnectionEvent)

```cangjie
public operator func !=(other: NetConnectionEvent): Bool
```

**功能：** 判断两个事件是否不相等。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NetConnectionEvent](#enum-netconnectionevent)|是|-|另一个事件枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当两个事件不相等时返回true，否则返回false。|

### func ==(NetConnectionEvent)

```cangjie
public operator func ==(other: NetConnectionEvent): Bool
```

**功能：** 判断两个事件是否相等。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NetConnectionEvent](#enum-netconnectionevent)|是|-|另一个事件枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当两个事件相等时返回true，否则返回false。|