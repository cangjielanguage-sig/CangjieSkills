## func p2pConnect(WifiP2PConfig)

```cangjie
public func p2pConnect(config: WifiP2PConfig): Unit
```

**功能：** 执行P2P连接。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|config|[WifiP2PConfig](#class-wifip2pconfig)|是|连接配置信息。如果DeviceAddressType未指定值，则DeviceAddressType默认为随机设备地址类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2801000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import std.sync.Timer
import ohos.base.*
import kit.ConnectivityKit.*

let recvP2pConnectionChangeFunc = WifiCallback1<WifiP2pLinkedInfo>({ result =>
    AppLog.info("p2p connection change receive event: ${result}")
    let info = getP2pLinkedInfo()
    AppLog.info(info.toString())
})

onP2pConnectionChange(recvP2pConnectionChangeFunc)

let recvP2pDeviceChangeFunc = WifiCallback1<WifiP2pDevice>({ result =>
    AppLog.info("p2p device change receive event: ${result}")
})
onP2pDeviceChange(recvP2pDeviceChangeFunc)

let recvP2pPeerDeviceChangeFunc = WifiCallback1<Array<WifiP2pDevice>>({ result =>
    AppLog.info("p2p peer device change receive event: ${result}")
    let devices = getP2pPeerDevices()
    AppLog.info("get peer devices: ${devices}")
    for(device in devices) {
        if (device.deviceName == "my_test_device") {
            AppLog.info("p2p connect to test device: ${device.deviceAddress}")
            let config = WifiP2PConfig(device.deviceAddress, -2, "", "", GroupOwnerBand.GO_BAND_AUTO)
            p2pConnect(config)
        }
    }
})
onP2pPeerDeviceChange(recvP2pPeerDeviceChangeFunc)

let recvP2pPersistentGroupChangeFunc = WifiCallback0({ =>
    AppLog.info("p2p persistent group change receive event")
    let group = getCurrentGroup()
    AppLog.info("get current group: ${group}")
})
onP2pPersistentGroupChange(recvP2pPersistentGroupChangeFunc)

Timer.once(Duration.second * 125, { => offP2pConnectionChange(callback: recvP2pConnectionChangeFunc) })
Timer.once(Duration.second * 125, { => offP2pDeviceChange(callback: recvP2pDeviceChangeFunc) })
Timer.once(Duration.second * 125, { => offP2pPeerDeviceChange(callback: recvP2pPeerDeviceChangeFunc) })
Timer.once(Duration.second * 125, { => offP2pPersistentGroupChange(callback: recvP2pPersistentGroupChangeFunc) })

AppLog.info("start discover devices")
startDiscoverDevices()
```