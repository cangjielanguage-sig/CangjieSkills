## enum NetBearType

```cangjie
public enum NetBearType {
    | BEARER_CELLULAR
    | BEARER_WIFI
    | BEARER_ETHERNET
    | BEARER_BLUETOOTH
    | BEARER_VPN
    | ...
}
```

**功能：** 网络类型。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### BEARER_CELLULAR

```cangjie
BEARER_CELLULAR
```

**功能：** 蜂窝网络。

**起始版本：** 12

### BEARER_ETHERNET

```cangjie
BEARER_ETHERNET
```

**功能：** 以太网网络。

**起始版本：** 12

### BEARER_WIFI

```cangjie
BEARER_WIFI
```

**功能：** Wi-Fi网络。

**起始版本：** 12

### BEARER_BLUETOOTH

```cangjie
BEARER_BLUETOOTH
```

**功能：** 蓝牙网络。

**起始版本：** 19

### BEARER_VPN

```cangjie
BEARER_WIFI
```

**功能：** VPN网络。

**起始版本：** 19

## enum NetCap

```cangjie
public enum NetCap {
    | NET_CAPABILITY_MMS
    | NET_CAPABILITY_NOT_METERED
    | NET_CAPABILITY_INTERNET
    | NET_CAPABILITY_NOT_VPN
    | NET_CAPABILITY_VALIDATED
    | NET_CAPABILITY_PORTAL
    | NET_CAPABILITY_CHECKING_CONNECTIVITY
    | ...
}
```

**功能：** 网络具体能力。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

### NET_CAPABILITY_INTERNET

```cangjie
NET_CAPABILITY_INTERNET
```

**功能：** 表示该网络应具有访问Internet的能力，该能力由网络提供者设置。

**起始版本：** 12

### NET_CAPABILITY_MMS

```cangjie
NET_CAPABILITY_MMS
```

**功能：** 表示网络可以访问运营商的MMSC（Multimedia&nbsp;Message&nbsp;Service，多媒体短信服务）发送和接收彩信。

**起始版本：** 12

### NET_CAPABILITY_NOT_METERED

```cangjie
NET_CAPABILITY_NOT_METERED
```

**功能：** 表示网络流量未被计费。

**起始版本：** 12

### NET_CAPABILITY_NOT_VPN

```cangjie
NET_CAPABILITY_NOT_VPN
```

**功能：** 表示网络不使用VPN（Virtual&nbsp;Private&nbsp;Network，虚拟专用网络）。

**起始版本：** 12

### NET_CAPABILITY_VALIDATED

```cangjie
NET_CAPABILITY_VALIDATED
```

**功能：** 表示该网络访问Internet的能力被网络管理成功验证，该能力由网络管理模块设置。

**起始版本：** 12

### NET_CAPABILITY_PORTAL

```cangjie
NET_CAPABILITY_PORTAL
```

**功能：** 表示系统发现该网络存在强制网络门户，需要用户登陆认证，该能力由网络管理模块设置。

**起始版本：** 19

### NET_CAPABILITY_CHECKING_CONNECTIVITY

```cangjie
NET_CAPABILITY_CHECKING_CONNECTIVITY
```

**功能：** 表示网络管理正在检验当前网络的连通性，此值会在网络连接时设置，直到连通性检测结束后不再设置，当此值存在时，NET_CAPABILITY_VALIDATED的值可能不准确。

**起始版本：** 19