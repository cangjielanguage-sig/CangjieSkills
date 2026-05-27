## func onP2pDeviceChange(WifiCallback1\<WifiP2pDevice>)

```cangjie
public func onP2pDeviceChange(callback: WifiCallback1<WifiP2pDevice>): Unit
```

**功能：** 注册P2P设备状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|callback|[WifiCallback1](#class-wificallback1)\<[WifiP2pDevice](#class-wifip2pdevice)>|是|状态改变回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |801|Capability not supported.|
  |2801000|Operation failed.|

## func onP2pDiscoveryChange(WifiCallback1\<Int32>)

```cangjie
public func onP2pDiscoveryChange(callback: WifiCallback1<Int32>): Unit
```

**功能：** 注册发现设备状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|callback|[WifiCallback1](#class-wificallback1)\<Int32>|是|状态改变回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |801|Capability not supported.|
  |2801000|Operation failed.|

## func onP2pPeerDeviceChange(WifiCallback1\<Array\<WifiP2pDevice>>)

```cangjie
public func onP2pPeerDeviceChange(callback: WifiCallback1<Array<WifiP2pDevice>>): Unit
```

**功能：** 注册P2P对端设备状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|callback|[WifiCallback1](#class-wificallback1)\<Array\<[WifiP2pDevice](#class-wifip2pdevice)>>|是|状态改变回调函数。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限（仅系统应用可申请），则返回结果中的deviceAddress为真实设备地址，否则为随机设备地址。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |801|Capability not supported.|
  |2801000|Operation failed.|