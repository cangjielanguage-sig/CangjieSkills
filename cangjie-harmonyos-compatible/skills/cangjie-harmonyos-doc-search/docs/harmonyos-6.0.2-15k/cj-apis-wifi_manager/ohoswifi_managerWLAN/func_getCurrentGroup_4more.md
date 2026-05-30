## func getCurrentGroup()

```cangjie
public func getCurrentGroup(): WifiP2pGroupInfo
```

**功能：** 获取P2P当前组信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WifiP2pGroupInfo](#class-wifip2pgroupinfo)|表示当前组信息。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限（仅系统应用可申请），则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|
  |2801000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let groupInfo = getCurrentGroup()
```

## func getIpInfo()

```cangjie
public func getIpInfo(): IpInfo
```

**功能：** 获取IP信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[IpInfo](#class-ipinfo)|IP信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|
  |2501000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let info = getIpInfo()
```

## func getIpv6Info()

```cangjie
public func getIpv6Info(): Ipv6Info
```

**功能：** 获取IPV6信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Ipv6Info](#class-ipv6info)|Ipv6信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|
  |2501000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let info = getIpv6Info()
```

## func getLinkedInfo()

```cangjie
public func getLinkedInfo(): WifiLinkedInfo
```

**功能：** 获取WLAN连接信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

当macType是1 - 设备MAC地址时，获取 macAddress 还需申请ohos.permission.GET_WIFI_LOCAL_MAC权限（该权限仅系统应用可申请），无该权限时，macAddress 返回空字符串。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WifiLinkedInfo](#class-wifilinkedinfo)|表示WLAN连接信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|
  |2501000|Operation failed.|
  |2501001|Wi-Fi STA disabled.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let info = getLinkedInfo()
```