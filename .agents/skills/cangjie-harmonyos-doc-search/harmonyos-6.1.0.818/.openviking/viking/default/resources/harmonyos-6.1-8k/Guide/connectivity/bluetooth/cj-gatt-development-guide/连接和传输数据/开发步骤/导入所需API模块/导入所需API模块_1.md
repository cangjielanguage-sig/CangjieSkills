### 导入所需API模块

**1. 创建客户端实例**

客户端通过查找设备流程搜索到目标设备后，即可构造客户端实例，后续所有操作都基于该客户端实例。

- 导入模块。

<!-- compile -->

```cangjie
import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
```

- 构造客户端实例。

```cangjie
// 此处是伪代码
let device = 'XX:XX:XX:XX:XX:XX'

try {
    let device: GattClientDevice = createGattClientDevice(device)  // 请替换为您的设备地址
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

**2. 订阅连接状态变化事件**

通过订阅连接状态变化事件，可以获取实时的GATT连接状态。整个连接过程会涉及多种状态的跃迁，其中[StateConnected](../../reference/ConnectivityKit/cj-apis-bluetooth-constant.md#stateconnected)表示已连接，[StateDisconnected](../../reference/ConnectivityKit/cj-apis-bluetooth-constant.md#statedisconnected)表示已断连。

- 导入模块。

<!-- compile -->

```cangjie
import ohos.callback_invoke.*
import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
```

- 订阅连接状态变化事件。

```cangjie
// 此处是伪代码
let device = 'XX:XX:XX:XX:XX:XX'

class BLEConnectionStateChangeCallback <: Callback1Argument<BleConnectionChangeState> {
    public func invoke(err: ?BusinessException, stateInfo: BleConnectionChangeState): Unit {
        let connectState = stateInfo.state
    }
}

let bleConnectionStateChangeCallback = BLEConnectionStateChangeCallback()
try {
    let gattClient = createGattClientDevice(device)
    gattClient.on(BluetoothBleGattClientDeviceCallbackType.BleConnectionStateChange, bleConnectionStateChangeCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```

**3. 发起连接**

通过创建的客户端实例，直接发起连接即可。通过连接状态变化事件判断是否已连接成功。

- 导入模块。

<!-- compile -->

```cangjie
import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
```

- 发起连接。

```cangjie
// 此处是伪代码
let device = 'XX:XX:XX:XX:XX:XX'

try {
    let gattClient = createGattClientDevice(device)
    gattClient.connect()
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```

**4. 服务发现**

服务发现是获取服务端支持的所有服务能力集合的过程。客户端需要根据服务发现结果，判断服务端是否存在应用需要的服务能力。

- 后续的读写特征值、读写描述符等操作都需要在服务发现操作完成后进行，否则会失败。
- 后续的读写等操作中指定的特征值或描述符必须包含在服务能力集合中，否则会失败。

- 导入模块。

<!-- compile -->

```cangjie
import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
```

- 服务发现。

```cangjie
// 此处是伪代码
let device = 'XX:XX:XX:XX:XX:XX'

try {
    let gattClient = createGattClientDevice(device)
    // 此处是伪代码，需要连接上后，才可以调用
    let services = gattClient.getServices{err: ?BusinessException, c: ?Array<GattService> =>
        Hilog.info(0, "Bluetooth", "getServices successfully")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```

**5. 传输数据**

传输数据通过操作服务端的特征值或者描述符实现。

**5.1 读取或写入特征值**

读取特征值操作，可以获取服务端特征值的数据内容。

写入特征值操作，可以更新服务端特征值的数据内容。