## func sppAccept(Int32, (?BusinessException, ?Int32) -> Unit)

```cangjie
public func sppAccept(serverSocket: Int32, callback: (?BusinessException, ?Int32) -> Unit): Unit
```

**功能：** 服务端监听socket等待客户端连接。使用Callback异步回调。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serverSocket|Int32|是|-|服务端socket的id。|
|callback|(?[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception), ?Int32)->Unit|是|-|表示回调函数的入参，客户端socket的id。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900003|Bluetooth disabled.|
  |2900004|Profile not supported.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

try {
    let sppOption: SppOptions = SppOptions('00001101-0000-1000-8000-00805f9b34fb', true, SPPRFCOMM)
    let serverSocket = sppListen('server1', sppOption)
    sppAccept(serverSocket, sppOption){
        error, fd =>
            if (let Some(e) <- error) {
                throw e
            }
            if (let Some(clintSocket) <- fd) {
            }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func sppCloseClientSocket(Int32)

```cangjie
public func sppCloseClientSocket(socket: Int32): Unit
```

**功能：** 关闭客户端socket，入参socket由sppAccept或sppConnect接口获取。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|socket|Int32|是|-|客户端socket的id。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |2900001|Service stopped.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

try {
    let devices = getPairedDevices()
    let deviceId = devices[0]
    let sppOption: SppOptions = SppOptions('00001101-0000-1000-8000-00805f9b34fb', true, SPPRFCOMM)
    sppConnect(deviceId, sppOption){
        error, fd =>
            if (let Some(e) <- error) {
                throw e
            }
            if (let Some(clintSocket) <- fd) {
                sppCloseClientSocket(clintSocket)
            }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```