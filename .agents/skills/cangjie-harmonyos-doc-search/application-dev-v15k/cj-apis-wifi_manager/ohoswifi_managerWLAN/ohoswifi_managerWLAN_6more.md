# ohos.wifi_manager（WLAN）

该模块主要提供WLAN基础功能、P2P（peer-to-peer）功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。

## 导入模块

```cangjie
import kit.ConnectivityKit.*
```

## 权限列表

ohos.permission.GET_WIFI_INFO

ohos.permission.SET_WIFI_INFO

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func addCandidateConfig(WifiDeviceConfig)

```cangjie
public func addCandidateConfig(config: WifiDeviceConfig): Int32
```

**功能：** 添加候选网络配置。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|config|[WifiDeviceConfig](#class-wifideviceconfig)|是|WLAN配置信息。如果bssidType未指定值，则bssidType默认为随机设备地址类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|表示网络配置ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2501000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let cfg = WifiDeviceConfig("****", "****", WifiSecurityType.WIFI_SEC_TYPE_INVALID)
let id = addCandidateConfig(cfg)
```

## func connectToCandidateConfig(Int32)

```cangjie
public func connectToCandidateConfig(networkId: Int32): Unit
```

**功能：** 应用使用该接口连接到自己添加的候选网络（如果当前已经连接到热点，需要先断开连接）。

**需要权限：** ohos.permission.SET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|networkId|Int32|是|候选网络配置的ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2501000|Operation failed.|
  |2501001|Wi-Fi STA disabled.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let networkId: Int32 = 0 // 实际的候选网络ID，在添加候选网络时生成，取自WifiDeviceConfig.netId
connectToCandidateConfig(networkId)
```