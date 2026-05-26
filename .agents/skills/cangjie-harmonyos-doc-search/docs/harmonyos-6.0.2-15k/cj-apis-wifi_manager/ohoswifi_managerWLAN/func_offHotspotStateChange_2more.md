## func offHotspotStateChange(?WifiCallback1\<Int32>)

```cangjie
public func offHotspotStateChange(callback!: ?WifiCallback1<Int32> = None): Unit
```

**功能：** 取消注册热点状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[WifiCallback1](#class-wificallback1)\<Int32>|否|None| **命名参数。** 状态改变回调函数。如果callback没有传入参数，将取消注册该事件关联的所有回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |801|Capability not supported.|
  |2601000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let callback = WifiCallback1<Int32>() {
    i => AppLog.info("callback invoked")
}
// Register event
onHotspotStateChange(callback)
// Unregister event
offHotspotStateChange(callback: callback)
```

## func offP2pConnectionChange(?WifiCallback1\<WifiP2pLinkedInfo>)

```cangjie
public func offP2pConnectionChange(callback!: ?WifiCallback1<WifiP2pLinkedInfo> = None): Unit
```

**功能：** 取消注册P2P连接状态改变事件。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[WifiCallback1](#class-wificallback1)\<[WifiP2pLinkedInfo](#class-wifip2plinkedinfo)>|否|None| **命名参数。** 状态改变回调函数。如果callback没有传入参数，将取消注册该事件关联的所有回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |801|Capability not supported.|
  |2801000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let callback = WifiCallback1<WifiP2pLinkedInfo>() {
    i => AppLog.info("callback invoked")
}

// Register event
onP2pConnectionChange(callback)

// Unregister event
offP2pConnectionChange(callback: callback)
```