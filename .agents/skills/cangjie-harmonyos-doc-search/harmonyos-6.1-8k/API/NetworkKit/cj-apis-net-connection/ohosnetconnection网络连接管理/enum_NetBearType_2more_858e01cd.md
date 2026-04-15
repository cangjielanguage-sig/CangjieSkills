## enum NetBearType

```cangjie
public enum NetBearType {
    | BearerCellular
    | BearerWifi
    | BearerEthernet
    | ...
}
```

**功能：** 网络类型。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### BearerCellular

```cangjie
BearerCellular
```

**功能：** 蜂窝网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### BearerEthernet

```cangjie
BearerEthernet
```

**功能：** 以太网网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### BearerWifi

```cangjie
BearerWifi
```

**功能：** Wi-Fi网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

## enum NetCap

```cangjie
public enum NetCap {
    | NetCapabilityMms
    | NetCapabilityNotMetered
    | NetCapabilityInternet
    | NetCapabilityNotVpn
    | NetCapabilityValidated
    | ...
}
```

**功能：** 网络具体能力。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetCapabilityInternet

```cangjie
NetCapabilityInternet
```

**功能：** 表示该网络应具有访问Internet的能力，此能力由网络提供者设置，但该网络访问Internet的连通性并未被网络管理成功验证。网络连通性可以通过NetCapabilityValidated判断。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetCapabilityMms

```cangjie
NetCapabilityMms
```

**功能：** 表示网络可以访问运营商的MMSC（Multimedia&nbsp;Message&nbsp;Service，多媒体短信服务）发送和接收彩信。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetCapabilityNotMetered

```cangjie
NetCapabilityNotMetered
```

**功能：** 表示网络流量未被计费。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetCapabilityNotVpn

```cangjie
NetCapabilityNotVpn
```

**功能：** 表示网络不使用VPN（Virtual&nbsp;Private&nbsp;Network，虚拟专用网络）。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### NetCapabilityValidated

```cangjie
NetCapabilityValidated
```

**功能：** 表示网络管理通过该网络与华为云地址成功建立连接，此能力由网络管理模块设置。

注意： 网络管理可能会与华为云地址建立连接失败，导致网络能力不具备此标记位，但不完全代表该网络无法访问互联网。另外，对于新完成连接的网络，由于网络正在进行连通性验证，此值可能无法反映真实的验证结果。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22