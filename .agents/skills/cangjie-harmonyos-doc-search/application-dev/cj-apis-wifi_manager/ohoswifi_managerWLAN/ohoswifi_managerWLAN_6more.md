# ohos.wifi_manager（WLAN）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

wifi_manager模块主要提供WLAN基础功能、P2P（peer-to-peer）功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。

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
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md)。

## func getScanInfoList()

```cangjie
public func getScanInfoList(): Array<WifiScanInfo>
```

**功能：** 获取扫描结果。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[WifiScanInfo](#class-wifiscaninfo)>|返回扫描到的热点列表。如果应用申请了ohos.permission.GET_WIFI_PEERS_MAC权限（仅系统应用可申请），则返回结果中的bssid为真实设备地址，否则为随机设备地址。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[WIFI错误码](./cj-errorcode-wifi-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2501000 | Operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let scanInfoList = getScanInfoList()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func isWifiActive()

```cangjie
public func isWifiActive(): Bool
```

**功能：** 查询WLAN是否已使能。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true:已使能，false:未使能。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[WIFI错误码](./cj-errorcode-wifi-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |
  | 2501000 | Operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let isWifiActive = isWifiActive()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```