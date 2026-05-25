## func createGroup(WifiP2PConfig)

```cangjie
public func createGroup(config: WifiP2PConfig): Unit
```

**功能：** 创建群组。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|config|[WifiP2PConfig](#class-wifip2pconfig)|是|群组配置信息。如果DeviceAddressType未指定值，则DeviceAddressType默认为随机设备地址类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2801000|Operation failed.|
  |2801001|Wi-Fi STA disabled.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let config = WifiP2PConfig("****", 0, "*****", "****", GO_BAND_AUTO)
createGroup(config)
```

## func getCandidateConfigs()

```cangjie
public func getCandidateConfigs(): Array<WifiDeviceConfig>
```

**功能：** 获取候选网络配置。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[WifiDeviceConfig](#class-wifideviceconfig)>|候选网络配置数组。|

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

let configs = getCandidateConfigs()
```

## func getCountryCode()

```cangjie
public func getCountryCode(): String
```

**功能：** 获取国家码信息。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|国家码。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|
  |2401000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let code = getCountryCode()
```