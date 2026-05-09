## func p2pCancelConnect()

```cangjie
public func p2pCancelConnect(): Unit
```

**功能：** 在P2P连接过程中，取消P2P连接。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[WIFI错误码](./cj-errorcode-wifi-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2801000 | Operation failed. |
  | 2801001 | Wi-Fi STA disabled. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    p2pCancelConnect()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func p2pConnect(WifiP2pConfig)

```cangjie
public func p2pConnect(config: WifiP2pConfig): Unit
```

**功能：** 执行P2P连接。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[WifiP2pConfig](#class-wifip2pconfig)|是|-|连接配置信息。如果DeviceAddressType未指定值，则DeviceAddressType默认为随机设备地址类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[WIFI错误码](./cj-errorcode-wifi-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2801000 | Operation failed. |
  | 2801001 | Wi-Fi STA disabled. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let config = WifiP2pConfig("xx:xx:xx:xx", -2, "", "", GroupOwnerBand.GoBandAuto)
    p2pConnect(config)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func startDiscoverDevices()

```cangjie
public func startDiscoverDevices(): Unit
```

**功能：** 开始发现设备。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[WIFI错误码](./cj-errorcode-wifi-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2801000 | Operation failed. |
  | 2801001 | Wi-Fi STA disabled. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    startDiscoverDevices()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func stopDiscoverDevices()

```cangjie
public func stopDiscoverDevices(): Unit
```

**功能：** 停止发现设备。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[WIFI错误码](./cj-errorcode-wifi-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |
  | 2801000 | Operation failed. |
  | 2801001 | Wi-Fi STA disabled. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    stopDiscoverDevices()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```