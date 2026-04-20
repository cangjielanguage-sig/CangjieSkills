## func getP2pLinkedInfo()

```cangjie
public func getP2pLinkedInfo(): WifiP2pLinkedInfo
```

**功能：** 获取P2P连接信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

获取 groupOwnerAddr 还需申请ohos.permission.GET_WIFI_LOCAL_MAC权限（该权限仅系统应用可申请），无该权限时，groupOwnerAddr 返回全零地址。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WifiP2pLinkedInfo](#class-wifip2plinkedinfo)|表示P2P连接信息。|

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

let info = getP2pLinkedInfo()
```

## func getP2pLocalDevice()

```cangjie
public func getP2pLocalDevice(): WifiP2pDevice
```

**功能：** 获取P2P本端设备信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[WifiP2pDevice](#class-wifip2pdevice)|表示本端设备信息。|

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

// p2p已经建组或者连接成功，才能正常获取到本端设备信息
let device = getP2pLocalDevice()
```

## func getP2pPeerDevices()

```cangjie
public func getP2pPeerDevices(): Array<WifiP2pDevice>
```

**功能：** 获取P2P对端设备列表信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[WifiP2pDevice](#class-wifip2pdevice)>|表示对端设备列表信息。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限（仅系统应用可申请），则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。|

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

// p2p发现阶段完成，才能正常获取到对端设备列表信息
let devices = getP2pPeerDevices()
```