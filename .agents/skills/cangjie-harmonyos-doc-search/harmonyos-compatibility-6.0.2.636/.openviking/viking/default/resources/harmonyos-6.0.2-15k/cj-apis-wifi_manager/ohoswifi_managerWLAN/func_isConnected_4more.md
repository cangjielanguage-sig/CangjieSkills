## func isConnected()

```cangjie
public func isConnected(): Bool
```

**功能：** 查询WLAN是否已连接。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true:已连接，false:未连接。|

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

let ret = isConnected()
```

## func isFeatureSupported(Int64)

```cangjie
public func isFeatureSupported(featureId: Int64): Bool
```

**功能：** 判断设备是否支持相关WLAN特性。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|featureId|Int64|是|特性ID值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true:支持，false:不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[WIFI错误码](../../errorcodes/cj-errorcode-wifi-manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified.<br>2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2401000|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

let featureId = 0
let ret = isFeatureSupported(featureId)
```

## func isMeteredHotspot()

```cangjie
public func isMeteredHotspot(): Bool
```

**功能：** 查询设备当前连接的wifi是否是手机热点。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true:是手机热点，false:不是手机热点。|

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

let isMeteredHotspot = isMeteredHotspot()
```

## func isWifiActive()

```cangjie
public func isWifiActive(): Bool
```

**功能：** 查询WLAN是否已使能。

**需要权限：** ohos.permission.GET_WIFI_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true:已使能，false:未使能。|

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

let isWifiActive = isWifiActive()
```