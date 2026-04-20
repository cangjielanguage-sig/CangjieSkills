当服务端特征值的数据内容发生变化时，客户端可以通过接收服务端的特征值变化通知或者指示来实现更新数据。该服务端特征值需包含蓝牙标准协议定义的Client Characteristic Configuration描述符UUID（00002902-0000-1000-8000-00805f9b34fb），才能支持通知或者指示能力。

客户端收到服务端通知时，不需要回复确认；客户端收到服务端指示时，需要回复确认，蓝牙子系统会实现该操作，应用无需关注。

- 先订阅服务端特征值变化事件，详情请见[on(BleCharacteristicChange)](../../reference/ConnectivityKit/cj-apis-bluetooth-ble.md#func-onbluetoothblegattclientdevicecallbacktype-callback1argumentblecharacteristic)。
- 再使能服务端特征值变化通知或者指示能力，应用根据实际场景选择一种方式即可。相关API请参考[setCharacteristicChangeNotification](../../reference/ConnectivityKit/cj-apis-bluetooth-ble.md#func-setcharacteristicchangenotificationblecharacteristic-bool-asynccallbackunit)和[setCharacteristicChangeIndication](../../reference/ConnectivityKit/cj-apis-bluetooth-ble.md#func-setcharacteristicchangeindicationblecharacteristic-bool-asynccallbackunit)。

- 导入模块。

<!-- compile -->

```cangjie
import ohos.callback_invoke.*
import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
```

- 接收服务端特征值变化通知或指示。

```cangjie
// 此处是伪代码
let device = 'XX:XX:XX:XX:XX:XX'

// 定义服务端特征值变化事件
class BLECharacteristicChangeCallback <: Callback1Argument<BleCharacteristic> {
    public func invoke(err: ?BusinessException, characteristic: BleCharacteristic): Unit {
        Hilog.info(0, "Bluetooth", "characteristic has change")
    }
}

let arrayBuffer: Array<Byte> = [11, 0]
let descriptor = BleDescriptor(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    "00002902-0000-1000-8000-00805F9B34FB",
    arrayBuffer
)
let descriptors: Array<BleDescriptor> = [descriptor]
let arrayBufferC: Array<Byte> = [0, 0]
let characteristic: BleCharacteristic = BleCharacteristic(
    "00001810-0000-1000-8000-00805F9B34FB",
    "00001820-0000-1000-8000-00805F9B34FB",
    arrayBufferC,
    descriptors
)

var gattClient: ?GattClientDevice = None
try {
    gattClient = createGattClientDevice(device)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}

// 发起订阅
let bleCharacteristicChangeCallback = BLECharacteristicChangeCallback()
try {
    gattClient?.on(BluetoothBleGattClientDeviceCallbackType.BleCharacteristicChange, bleCharacteristicChangeCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}

// 通知和指示，2选1即可
// 设置特征值变化通知能力
try {
  // enable入参: true表示启用，false表示禁用
    gattClient?.setCharacteristicChangeNotification(characteristic, true) {
        error: ?BusinessException, c: ?Unit => if (let Some(e) <- error) {
            Hilog.info(0, "Bluetooth", "setCharacteristicChangeNotification callback failed")
        } else {
            Hilog.info(0, "Bluetooth", "setCharacteristicChangeNotification callback successful")
        }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}