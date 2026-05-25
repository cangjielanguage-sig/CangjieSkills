### func sendResponse(ServerResponse)

```cangjie
public func sendResponse(serverResponse: ServerResponse): Unit
```

**功能：** server端回复client端的读写请求。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|serverResponse|[ServerResponse](#class-serverresponse)|是|server端回复的响应数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900003|Bluetooth disabled.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

let gattServer = createGattServer()
try {
    let rspBuffer = Array<Byte>()
    let serverResponse: ServerResponse = ServerResponse(
        "XX:XX:XX:XX:XX:XX'", 0, 0, 0,
        rspBuffer
    )
    gattServer.sendResponse(serverResponse)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```