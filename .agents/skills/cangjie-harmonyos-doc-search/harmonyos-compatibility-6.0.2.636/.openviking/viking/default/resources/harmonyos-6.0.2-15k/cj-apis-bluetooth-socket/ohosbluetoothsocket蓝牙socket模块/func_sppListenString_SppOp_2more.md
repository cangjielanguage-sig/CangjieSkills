## func sppListen(String, SppOptions)

```cangjie
public func sppListen(name: String, options: SppOptions): Int32
```

**功能：** 创建一个服务端监听Socket。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|服务的名称。|
|options|[SppOptions](#class-sppoptions)|是|-|spp监听配置参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|服务端Socket的id。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
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
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func sppWrite(Int32, Array\<UInt8>)

```cangjie
public func sppWrite(clientSocket: Int32, data: Array<UInt8>): Unit
```

**功能：** 通过socket向远端发送数据，入参clientSocket由sppAccept或sppConnect接口获取 。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clientSocket|Int32|是|-|客户端socket的id。|
|data|Array\<UInt8>|是|-|写入的数据。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |2901054|IO error.|
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
                sppWrite(clintSocket, "test".toArray())
            }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```